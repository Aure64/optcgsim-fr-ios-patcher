# OPTCGSim iOS — Patch français

Une version pré-traduite d'[OPTCGSim](https://www.optcgsim.com/) pour
iOS, basée sur la traduction communautaire maintenue par
[Sparklight-TL/OPTCGSim_FR](https://github.com/Sparklight-TL/OPTCGSim_FR).

Télécharge simplement le `.ipa` patché depuis la page
[**Releases**](https://github.com/Aure64/optcgsim-fr-ios-patcher/releases),
puis sideload-le sur ton iPhone.

## Ce qui est traduit

- **Images des cartes** — versions françaises de toutes les cartes, avec
  les styles alt-art (Manga, Full Art, SP Cards, Tampon Foil, etc.)
  appliqués quand ils existent.
- **Interface / menus** — boutons, dialogues, éditeur de deck, et tous
  les textes affichés par l'application.

Quelques sets restent en anglais tant que Sparklight-TL ne publie pas
leur traduction (typiquement le dernier OP et le dernier ST juste après
une mise à jour du jeu). Voir les notes de release pour la liste précise
des sets couverts.

## Installation

### Ce qu'il te faut

- Un iPhone (pas besoin de jailbreak)
- Un PC ou Mac avec [Sideloadly](https://sideloadly.io/) installé
- Ton Apple ID (un compte gratuit suffit ; il faudra re-sideloader tous
  les 7 jours)

### Étapes

1. Télécharge le dernier `OPTCGSim_FR.ipa` depuis la
   [page Releases](https://github.com/Aure64/optcgsim-fr-ios-patcher/releases).
2. Ouvre Sideloadly et glisse le `.ipa` dedans.
3. Branche ton iPhone, entre ton Apple ID, clique sur **Start**.
4. Sur l'iPhone : *Réglages → Général → VPN et gestion de l'appareil* —
   fais confiance au profil développeur.
5. Lance OPTCGSim.

Si tu avais déjà installé OPTCGSim en anglais avec le même Apple ID, la
version française remplace directement l'ancienne — pas besoin de
désinstaller avant.

### Re-signer tous les 7 jours (Apple ID gratuit)

Avec un Apple ID gratuit, la signature expire au bout de 7 jours. Il
suffit de rouvrir Sideloadly, re-déposer le même `.ipa`, et relancer
l'install — tes decks et tes paramètres sont conservés.

## En cas de problème

- **Sideloadly n'arrive pas à installer** — le `.ipa` fait ~2 GB. Libère
  de l'espace sur l'iPhone, ou passe l'install en Wi-Fi si le câble USB
  timeout.
- **Certaines cartes restent en anglais** — c'est normal pour les sets
  les plus récents qui n'ont pas encore été traduits côté Sparklight-TL.
  Voir les notes de release pour la liste des sets couverts.
- **L'appli crash au lancement** — vérifie que ta version d'iOS est bien
  supportée par la version d'OPTCGSim sur laquelle l'IPA a été construit
  (indiqué dans les notes de release).

## Crédits

- [Sparklight-TL](https://github.com/Sparklight-TL) — traduction
  française (images des cartes et textes de l'interface)
- Batsu — OPTCGSim
- Bandai / Toei / Shueisha — propriété intellectuelle One Piece

## Licence

Cette distribution combine des contenus tiers régis par leurs propres
licences :

- Le binaire OPTCGSim est l'œuvre de Batsu ; voir l'application
  d'origine pour ses conditions d'utilisation.
- Les images de cartes françaises et le fichier `TRANSLATION.txt` sont
  régis par les licences du dépôt
  [Sparklight-TL/OPTCGSim_FR](https://github.com/Sparklight-TL/OPTCGSim_FR).
- Les artworks et marques One Piece appartiennent à Bandai, Toei
  Animation et Shueisha.

Ce dépôt est un canal de distribution communautaire pour le portage iOS
de la traduction ci-dessus. Aucun usage commercial.
