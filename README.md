# OPTCGSim iOS — French patch

A pre-built French translation of [OPTCGSim](https://www.optcgsim.com/) for
iOS, based on the community translation maintained at
[Sparklight-TL/OPTCGSim_FR](https://github.com/Sparklight-TL/OPTCGSim_FR).

Just download the patched `.ipa` from the
[**Releases**](https://github.com/Aure64/optcgsim-fr-ios-patcher/releases)
page and sideload it on your iPhone.

## What's translated

- **Card images** — French versions of the cards, with alt-art styles
  (Manga, Full Art, SP Cards, Tampon Foil, etc.) applied where available.
- **UI / menus** — buttons, dialogs, deck editor, and all text strings
  shown by the app.

A few sets stay in English until Sparklight-TL ships their translation
(typically the latest OP set and the latest ST deck right after a game
update). See the release notes for which sets are covered.

## Installation

### What you need

- An iPhone (no jailbreak required)
- A computer with [Sideloadly](https://sideloadly.io/) installed
- Your Apple ID (a free one works; you'll need to re-sideload every 7 days)

### Steps

1. Download the latest `OPTCGSim_FR.ipa` from the
   [Releases page](https://github.com/Aure64/optcgsim-fr-ios-patcher/releases).
2. Open Sideloadly and drag the `.ipa` into it.
3. Plug in your iPhone, enter your Apple ID, click **Start**.
4. On the iPhone: *Settings → General → VPN & Device Management* — trust
   the developer profile.
5. Launch OPTCGSim.

If you've already installed an English OPTCGSim with the same Apple ID,
the French one replaces it directly — you don't need to delete the old
app first.

### Re-signing every 7 days (free Apple ID)

A free Apple ID signature expires after 7 days. Just open Sideloadly,
re-drop the same `.ipa`, and start again — your decks and settings are
preserved.

## Troubleshooting

- **Sideloadly fails to install** — the `.ipa` is ~2 GB. Free up space on
  the iPhone, or split the install over Wi-Fi rather than USB if it times
  out.
- **Some cards still in English** — expected for the newest sets that
  haven't been translated upstream yet. Check the release notes for the
  list of covered sets.
- **App crashes on launch** — make sure your iOS version is supported by
  the OPTCGSim release this IPA was built from (see release notes).

## Credits

- [Sparklight-TL](https://github.com/Sparklight-TL) — French translation
  (card images and UI strings)
- Batsu — OPTCGSim
- Bandai / Toei / Shueisha — One Piece IP

## License

This distribution combines third-party assets governed by their own
licenses:

- The OPTCGSim binary is the work of Batsu; see the original app for its
  terms.
- The French card images and `TRANSLATION.txt` are governed by the
  licenses on [Sparklight-TL/OPTCGSim_FR](https://github.com/Sparklight-TL/OPTCGSim_FR).
- One Piece artwork and trademarks belong to Bandai, Toei Animation, and
  Shueisha.

This repository is a fan distribution channel for the iOS port of the
above translation. No commercial use.
