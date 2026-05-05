#!/usr/bin/env python3
"""
OPTCGSim iOS — French patch builder.

Takes an OPTCGSim .ipa, the FR community repo (Sparklight-TL/OPTCGSim_FR),
and produces a patched .ipa with French card images and UI translation.

The patcher injects:
  - Card image overrides at Payload/OPTCGSim.app/Data/Raw/Cards/<set>/<card>_OVERRIDE.png
    (mirrors the PC patcher's behaviour, which writes to the same Unity StreamingAssets path)
  - Replaces Payload/OPTCGSim.app/Data/Raw/TRANSLATION.txt with the FR version

The output .ipa must be re-signed and installed via Sideloadly (or AltStore).
This script does NOT redistribute any copyrighted binary or artwork — you supply
your own .ipa and it pulls translations from the public Sparklight-TL/OPTCGSim_FR
GitHub repo.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

FR_REPO_URL = "https://github.com/Sparklight-TL/OPTCGSim_FR.git"
APP_BUNDLE_PREFIX = "Payload/OPTCGSim.app"
CARDS_PREFIX = f"{APP_BUNDLE_PREFIX}/Data/Raw/Cards"
TRANSLATION_ARCNAME = f"{APP_BUNDLE_PREFIX}/Data/Raw/TRANSLATION.txt"

# Default art-style priority (high -> low). Higher in this list wins on overlap.
# Anything not listed here is applied with lower priority, alphabetically.
DEFAULT_PRIORITY = [
    "Manga",
    "Red Manga",
    "Event Manga",
    "SP Cards",
    "TR Cards",
    "Full Art",
    "Old Full Art",
]


def ensure_fr_repo(path: Path) -> Path:
    """Clone the FR repo if missing; return its path."""
    if (path / "FR_classique").is_dir() and (path / "TRANSLATION.txt").is_file():
        return path
    print(f"Cloning {FR_REPO_URL} into {path} (this is ~2 GB) ...")
    path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.check_call(["git", "clone", "--depth", "1", FR_REPO_URL, str(path)])
    return path


def resolve_fr_files(fr_repo: Path, priority_high_to_low: list[str]) -> dict[tuple[str, str], Path]:
    """Build {(set, filename): source_path}. Higher-priority sources overwrite earlier ones."""
    classique_root = fr_repo / "FR_classique"
    fa_root = fr_repo / "FR_full_art"

    all_styles = sorted(d.name for d in fa_root.iterdir() if d.is_dir()) if fa_root.is_dir() else []
    rest = [s for s in all_styles if s not in priority_high_to_low]
    # Application order from low to high priority (last write wins).
    layers: list[tuple[str, Path]] = [("FR_classique", classique_root)]
    layers += [(s, fa_root / s) for s in rest]
    layers += [(s, fa_root / s) for s in reversed(priority_high_to_low) if s in all_styles]

    fr_map: dict[tuple[str, str], Path] = {}
    label_of: dict[tuple[str, str], str] = {}
    layer_total: dict[str, int] = {}

    for label, src in layers:
        if not src.is_dir():
            continue
        n = 0
        for f in src.glob("*/*_OVERRIDE.png"):
            fr_map[(f.parent.name, f.name)] = f
            label_of[(f.parent.name, f.name)] = label
            n += 1
        layer_total[label] = n

    winners: dict[str, int] = {}
    for k, lbl in label_of.items():
        winners[lbl] = winners.get(lbl, 0) + 1

    print(f"\nResolved {len(fr_map)} unique cards.")
    print("Source layers (last applied wins on overlap):")
    for label, _ in layers:
        if layer_total.get(label):
            display = "FR_classique (base)" if label == "FR_classique" else f"FR_full_art/{label}"
            print(f"  {display:45s} {layer_total[label]:5d} files -> {winners.get(label,0):5d} winning")
    return fr_map


def build_ipa(src_ipa: Path, dst_ipa: Path, fr_repo: Path,
              priority_high_to_low: list[str], compresslevel: int = 1) -> None:
    fr_map = resolve_fr_files(fr_repo, priority_high_to_low)
    translation_fr = fr_repo / "TRANSLATION.txt"
    if not translation_fr.is_file():
        sys.exit(f"Missing {translation_fr}")

    with zipfile.ZipFile(src_ipa, "r") as zin:
        ipa_names = set(zin.namelist())
    ipa_sets = {n.split("/")[5] for n in ipa_names
                if n.startswith(CARDS_PREFIX + "/") and n.count("/") >= 6}
    if not ipa_sets:
        sys.exit("No card sets found in IPA — wrong path or unexpected IPA structure.")
    print(f"\nIPA contains {len(ipa_sets)} card sets.")

    has_translation = TRANSLATION_ARCNAME in ipa_names
    if has_translation:
        print(f"Will replace {TRANSLATION_ARCNAME}.")
    else:
        print(f"Note: {TRANSLATION_ARCNAME} not found in IPA — UI translation skipped.")

    print(f"\nBuilding {dst_ipa} ...")
    dst_ipa.parent.mkdir(parents=True, exist_ok=True)
    injected = 0
    skipped_set = 0
    with zipfile.ZipFile(src_ipa, "r") as zin, \
         zipfile.ZipFile(dst_ipa, "w", zipfile.ZIP_DEFLATED,
                         compresslevel=compresslevel, allowZip64=True) as zout:
        for item in zin.infolist():
            if has_translation and item.filename == TRANSLATION_ARCNAME:
                zout.writestr(item, translation_fr.read_bytes())
            else:
                zout.writestr(item, zin.read(item.filename))

        for (set_name, fname), fr_file in fr_map.items():
            if set_name not in ipa_sets:
                skipped_set += 1
                continue
            arc = f"{CARDS_PREFIX}/{set_name}/{fname}"
            zout.write(fr_file, arc)
            injected += 1
            if injected % 300 == 0:
                print(f"  injected {injected}/{len(fr_map)}")

    size_mb = dst_ipa.stat().st_size / 1024 / 1024
    print(f"\nDone. Injected {injected} card overrides "
          f"({skipped_set} skipped: set not in IPA).")
    print(f"Output: {dst_ipa}  ({size_mb:.1f} MB)")
    print("\nNext: open Sideloadly, drag the .ipa, sign with your Apple ID, install.")


def parse_priority(arg: str | None) -> list[str]:
    if not arg:
        return DEFAULT_PRIORITY
    return [s.strip() for s in arg.split(",") if s.strip()]


def main() -> None:
    p = argparse.ArgumentParser(
        description="Build a French-patched OPTCGSim iOS IPA.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Priority list (high -> low) controls which alt-art style wins when a card has\n"
            "several variants in FR_full_art. Default: " + ",".join(DEFAULT_PRIORITY) + "\n"
        ),
    )
    p.add_argument("--ipa", required=True, type=Path, help="Path to the source .ipa")
    p.add_argument("--output", "-o", type=Path,
                   help="Output .ipa path (default: <input>_FR.ipa next to source)")
    p.add_argument("--fr-repo", type=Path, default=Path("./fr_repo"),
                   help="Path to a clone of Sparklight-TL/OPTCGSim_FR; will be cloned if missing")
    p.add_argument("--priority", type=str, default=None,
                   help="Comma-separated art-style priority (high to low). "
                        "Pass an empty string with --priority='' to disable all alt art.")
    p.add_argument("--compresslevel", type=int, default=1,
                   help="Zip compression level (0=store, 1=fast, 9=max). Default 1.")
    args = p.parse_args()

    if not args.ipa.is_file():
        sys.exit(f"IPA not found: {args.ipa}")

    output = args.output or args.ipa.with_name(args.ipa.stem + "_FR.ipa")
    priority = parse_priority(args.priority) if args.priority is not None else DEFAULT_PRIORITY

    fr_repo = ensure_fr_repo(args.fr_repo.resolve())
    build_ipa(args.ipa.resolve(), output.resolve(), fr_repo, priority, args.compresslevel)


if __name__ == "__main__":
    main()
