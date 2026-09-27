# Juju : contexte pour Claude

Juju est un voilier Gib'Sea 31 de 1984, moteur Yanmar 3GMD (plaque signalétique). Ce dépôt suit sa rénovation. Le seul chantier en cours est l'électricité (dossier `Electricité/`). Tout est rédigé en français, y compris les messages de commit.

## Organisation de `Electricité/`

| Dossier | Contenu | Règle |
|---|---|---|
| `releve/` | L'existant : état des lieux, `amenagement.yaml` (zones du bateau), `equipements.yaml`, `netlist.yaml`, `wirelist.yaml`, `anomalies.md`, `questions.md`, `photos/` | **Uniquement des faits constatés à bord.** Une valeur supposée porte `statut: estime`. Ne modifier ce dossier que sur une information donnée par l'utilisateur, et le signaler. |
| `schemas/` | Folios SVG de l'existant | Doivent refléter `releve/` exactement. |
| `etudes/<X-axe>/H<n>-<nom>/` | Une hypothèse : `proposition.md`, `cablage.yaml` (delta), folios SVG | Le `cablage.yaml` décrit uniquement les différences avec sa `base` (le relevé ou une autre hypothèse). |
| `commun/` | `bilan-energetique.yaml`, partagé par les études | |
| `outils/` | `verifier.py`, `page.py`, schémas JSON | |

## Règles de travail

- **Lancer `python Electricité/outils/verifier.py` après toute modification de données ou de SVG.** Zéro erreur exigé ; le hook `pre-commit` bloque sinon. Les avertissements sont à lire, pas forcément à corriger.
- **Ne jamais renuméroter un identifiant existant** : les fils seront étiquetés à bord avec leur numéro. Un fil modifié garde son id ; un fil remplacé est supprimé (`supprime.fils`) et le nouveau porte `remplace:`.
- **Plages de numéros.** Nœuds : 001-019 batteries et charge, 020-039 guindeau et moteur, 040-049 frigo, 050-059 tableau Scheiber et pompe de cale, 060-099 propositions, 100-199 tableau de servitude, 200-299 réseau 230 V (exception historique : node046-048 de l'EPS 100). Fils : wire001-099 relevé, wire100 et suivants propositions.
- **Ne pas supposer, demander.** Une information manquante devient une question `Qn` dans `releve/questions.md` et une pastille bleue sur le schéma concerné.
- **Calcul des sections** : S = 2 × L × I × 0,0175 / ΔU. ΔU = 3 % pour les feux, l'électronique, le pilote, la pompe de cale et le frigo ; 10 % pour le confort. Sections normalisées uniquement. Le fusible protège le câble et se place à sa source.
- **Couleurs** : + rouge, − noir ; en 230 V, phase marron, neutre bleu, terre vert-jaune.
- **Section ou couleur inconnue** : ne pas l'inventer, omettre le champ et poser une question.

## Conventions des SVG

- Même bloc `<style>` autonome dans chaque folio (variables de couleur clair et sombre). `page.py` le retire quand il assemble la page.
- `<title>` au format « Folio N · Nom », `<desc>` = légende d'une ou deux phrases.
- Classes : `p` / `n` (fil + / −), `w1`…`w5` (épaisseur selon la section), `u` (zone d'ombre en pointillés bleus), `box`, `box-new` (nouveau, en vert), `box-unk`, `fuse`, `fuse-new`, `flag` (renvoi vers un nœud), `mk-a` / `mk-q` (pastilles d'anomalie et de question).
- Écrire les identifiants en entier dans les étiquettes (`wire020 / wire021`, jamais `wire020/021`) : le vérificateur les recherche dans le texte.
- Dans une hypothèse, ce qui est nouveau est en vert (`box-new`, `fuse-new`, `idn`, `tn`).
- 230 V : `ph` (phase), `ne` (neutre), `pe` + `pey` superposés (terre vert-jaune).
- Folios : 0 implantation, 1 câblage 12 V actuel, 3 réseau 230 V ; les hypothèses ont leurs propres folios (2a, 2b…).
- Plan d'implantation (`folio-0-implantation.svg`) : chaque zone porte `data-zone="id"`, chaque équipement placé `data-equipement="id"` (un `<tspan>` vide suffit pour un équipement regroupé avec un autre). Classes `hull`, `zone`, `zone-pont`, `callout`, `leader`. Le vérificateur exige que tout équipement ayant une `zone` y figure.
- Le bloc `<style>` évolue : quand une classe est ajoutée, la reporter dans tous les folios et dans le gabarit de `outils/page.py`.

## Git

- `main` : le relevé et les décisions validées.
- `etude/securisation`, `etude/chauffe-eau`, `etude/solaire` : une branche par axe. Les hypothèses sont des dossiers dans la branche, pas des branches, pour pouvoir les comparer côte à côte.
- Ordre de fusion prévu : la sécurisation d'abord (prérequis), puis rebase des autres branches.
- **Une branche d'étude ne modifie que son dossier `etudes/<X-axe>/`.** Le relevé, `commun/`, `outils/`, les README généraux et CLAUDE.md se modifient sur `main`, puis les branches sont rebasées. Sinon, chaque rebase produit des conflits.
- Un commit = un sujet. Tag `rev-X` quand une révision des schémas est publiée.
- Push : remote SSH `origin`, poussé par l'utilisateur (pas de clé GitHub configurée pour Claude).

## Page de consultation

`python Electricité/outils/page.py` produit `Electricité/build/schemas.html` (non versionné). Cette page est publiée en artifact privé : https://claude.ai/artifact/Vj1VV9bWUtJjnwGRuP5a36 (republier sur la même URL).

Python 3.12 est installé pour l'utilisateur. S'il n'est pas dans le PATH : `%LOCALAPPDATA%\Programs\Python\Python312\python.exe`. Dépendances : `Electricité/outils/requirements.txt`.
