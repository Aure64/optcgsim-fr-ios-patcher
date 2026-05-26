# OPTCGSim iOS — French patch builder

A small Python script that patches an OPTCGSim `.ipa` (iOS) with the
community French translation maintained at
[Sparklight-TL/OPTCGSim_FR](https://github.com/Sparklight-TL/OPTCGSim_FR).

It mirrors what the official Windows `OPTCGSim_FR_Patcher.exe` does on PC,
but for iOS: it injects French card image overrides into the app's Unity
StreamingAssets path inside the `.ipa`, and replaces the bundled
`TRANSLATION.txt` (used for menus / UI strings).

The output is an unsigned `.ipa` that you re-install via
[Sideloadly](https://sideloadly.io/) (or AltStore) with your own Apple ID.

> **You bring your own `.ipa`.** This repository contains no game binary,
> no card artwork, and no copyrighted material. It is just a build script
> that orchestrates files between an `.ipa` you already have and the public
> [Sparklight-TL/OPTCGSim_FR](https://github.com/Sparklight-TL/OPTCGSim_FR)
> translation repo.

## Tested versions

| OPTCGSim iOS | Patched on | Cards injected | Notes                                              |
|--------------|------------|----------------|----------------------------------------------------|
| 1.39a        | 2026-05-26 | 1530           | OP16 / ST30 not yet translated upstream (English). |

## What it patches

- **Card images** — adds `<card>_OVERRIDE.png` next to each original card
  inside `Payload/OPTCGSim.app/Data/Raw/Cards/<set>/`. The game already
  contains the override-loading logic (visible as `_OVERRIDE.png` /
  `_OVERRIDE.jpg` / `image_overrides` strings in the iOS binary).
- **UI / menu translation** — replaces
  `Payload/OPTCGSim.app/Data/Raw/TRANSLATION.txt` with the FR version.

## Requirements

- Python 3.9+
- `git` on your PATH (used to clone the FR repo on first run)
- ~5 GB free disk space (the FR repo is ~2 GB; the patched IPA is ~2 GB)
- A non-jailbroken iPhone + Sideloadly (or AltStore) and an Apple ID

## Usage

```bash
# 1. Clone this repo
git clone https://github.com/Aure64/optcgsim-fr-ios-patcher.git
cd optcgsim-fr-ios-patcher

# 2. Run the patcher (the FR repo is auto-cloned into ./fr_repo on first run)
python3 build_patched_ipa.py --ipa /path/to/OPTCGSim.ipa
```

Output: `OPTCGSim_FR.ipa` next to the input. Open Sideloadly, drag the
`.ipa`, sign with your Apple ID, install.

### Options

```
--ipa PATH            Source .ipa (required)
-o, --output PATH     Output .ipa (default: <input>_FR.ipa)
--fr-repo PATH        Path to a local clone of OPTCGSim_FR
                      (default: ./fr_repo, auto-cloned if missing)
--priority "A,B,..."  Comma-separated alt-art style priority, high -> low.
                      Default:  Manga, Red Manga, Event Manga,
                                SP Cards, TR Cards, Full Art, Old Full Art
                      Pass --priority="" to disable all alt art and use
                      only FR_classique.
--compresslevel N     Zip compression level 0-9 (default 1, fast).
```

When two art styles cover the same card, the **higher-priority** style
wins. Anything not listed in `--priority` falls below the listed styles
(applied alphabetically, lowest priority).

### Examples

```bash
# Plain classique-only translation, no alt artworks
python3 build_patched_ipa.py --ipa OPTCGSim.ipa --priority=""

# Custom priority: Full Art > Manga > Foil > rest
python3 build_patched_ipa.py --ipa OPTCGSim.ipa \
    --priority="Full Art,Manga,Foil"
```

## Installing the patched IPA

1. Open Sideloadly on your computer
2. Drag the patched `.ipa` into Sideloadly
3. Plug in your iPhone, enter your Apple ID, click *Start*
4. On the iPhone: *Settings → General → VPN & Device Management* — trust
   the developer profile
5. Launch OPTCGSim

Same Apple ID = direct replacement of the previous install (you don't
need to delete the existing app first). With a free Apple ID, the
signature lasts 7 days; just re-sideload the same `.ipa` to renew.

## Troubleshooting

- **Cards still in English after install** — possible only for sets that
  ship as `.jpg` in the bundle (PRB01, OP09–16, ST21+, …) if the iOS
  override path differs from PC. Open an issue with details.
- **Sideloadly fails to install due to size** — the patched IPA is ~2 GB.
  Free up space on the iPhone, or use a paid developer account (no size
  limit on free accounts in practice, but Sideloadly may time out).
- **TRANSLATION.txt not in IPA** — the script will warn and skip the
  step. Newer game builds may move the file; open an issue.

## Credits

- [Sparklight-TL](https://github.com/Sparklight-TL) — French translation
  and the original Windows / Android patcher
- Batsu — OPTCGSim
- Bandai / Toei / Shueisha — One Piece IP

## License

The script in this repository is released under the MIT License (see
`LICENSE`). The translation files and card images are governed by their
own respective licenses on the upstream
[Sparklight-TL/OPTCGSim_FR](https://github.com/Sparklight-TL/OPTCGSim_FR)
repository.
