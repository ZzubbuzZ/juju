# Juju : contexte pour Claude

Juju est un voilier Gib'Sea 31 de 1984, moteur Yanmar 3GMD (plaque signalétique). Ce dépôt suit sa rénovation. Le seul chantier en cours est l'électricité (dossier `Electricité/`). Tout est rédigé en français, y compris les messages de commit.

## Organisation de `Electricité/`

| Dossier | Contenu | Règle |
|---|---|---|
| `releve/` | L'existant : état des lieux, `amenagement.yaml` (zones du bateau), `equipements.yaml`, `netlist.yaml`, `wirelist.yaml`, `anomalies.md`, `questions.md`, `photos/`, `documentation/` (notices, fiches) | **Uniquement des faits constatés à bord.** Une valeur supposée porte `statut: estime`. Ne modifier ce dossier que sur une information donnée par l'utilisateur, et le signaler. |
| `schemas/` | Folios SVG de l'existant | Doivent refléter `releve/` exactement. |
| `etudes/<X-axe>/H<n>-<nom>/` | Une hypothèse : `proposition.md` (avec en-tête YAML), `nomenclature.yaml`, `cablage.yaml` (delta), folios SVG | Le `cablage.yaml` décrit uniquement les différences avec sa `base` (le relevé ou une autre hypothèse). Une hypothèse écartée sans câblage peut n'avoir que `proposition.md` et `nomenclature.yaml`. |
| `commun/` | `bilan-energetique.yaml`, partagé par les études | |
| `documentation-technique/` | Manuel du bord : installation, réglages et entretien de ce qui est installé ou décidé. Pour l'instant une liste de sections à écrire (`README.md`) | Se modifie sur `main`. Ne décrit pas les hypothèses à l'étude. |
| `outils/` | `verifier.py`, `page.py`, schémas JSON | |

## Règles de travail

- **Lancer `python Electricité/outils/verifier.py` après toute modification de données ou de SVG.** Zéro erreur exigé ; le hook `pre-commit` bloque sinon. Les avertissements sont à lire, pas forcément à corriger.
- **Ne jamais renuméroter un identifiant existant** : les fils seront étiquetés à bord avec leur numéro. Un fil modifié garde son id ; un fil remplacé est supprimé (`supprime.fils`) et le nouveau porte `remplace:`.
- **Plages de numéros.** Nœuds : 001-019 batteries et charge, 020-039 guindeau et moteur, 040-049 frigo, 050-059 tableau Scheiber et pompe de cale, 060-099 propositions (plage pleine), 100-199 tableau de servitude, 200-299 réseau 230 V (exception historique : node046-048 de l'EPS 100), 300-399 propositions, par étude : 300-319 B, 320-339 C, 340-359 D, 360-379 E, 380-399 en réserve. Fils : wire001-099 relevé, wire100 et suivants propositions.
- **Ne pas supposer, demander.** Une information manquante devient une question `Qn` dans `releve/questions.md` et une pastille bleue sur le schéma concerné.
- **Calcul des sections** : S = 2 × L × I × 0,0175 / ΔU. ΔU = 3 % pour les feux, l'électronique, le pilote, la pompe de cale et le frigo ; 10 % pour le confort. Sections normalisées uniquement. Le fusible protège le câble et se place à sa source.
- **Couleurs** : + rouge, − noir ; en 230 V, phase marron, neutre bleu, terre vert-jaune.
- **Section ou couleur inconnue** : ne pas l'inventer, omettre le champ et poser une question. Une section relevée approximativement (AWG, câble non normalisé) porte `section_indicative: true`.
- **Propositions** : `proposition.md` commence par un en-tête YAML entre deux lignes `---` (`hypothese`, `titre`, `etat`, `resume`, `points_forts`, `points_faibles`, `decision` ; schéma `outils/schema/proposition.schema.json`). `page.py` en tire la comparaison des hypothèses de chaque étude, avec le total de la nomenclature. Mettre `etat` à jour à chaque décision.
- **Liens produits** : dans `nomenclature.yaml`, sur l'article concerné : `source` (URL), `date_prix`, `statut: catalogue`. Un lien doit avoir été vérifié (page ouverte) ou, à défaut, être signalé comme relevé par recherche. Préférer la page du fabricant ou d'un revendeur français à un lien de place de marché, qui expire.
- **Anomalies** : une anomalie infondée passe dans « Levées » d'`anomalies.md`, avec sa justification, et garde son numéro.

## Conventions des SVG

- Même bloc `<style>` autonome dans chaque folio (variables de couleur clair et sombre). `page.py` le retire quand il assemble la page.
- `<title>` au format « Folio N · Nom », `<desc>` = légende d'une ou deux phrases.
- Classes : `p` / `n` (fil + / −), `w1`…`w5` (épaisseur selon la section), `u` (zone d'ombre en pointillés bleus), `box`, `box-new` (nouveau, en vert), `box-unk`, `fuse`, `fuse-new`, `flag` (renvoi vers un nœud), `mk-a` / `mk-q` (pastilles d'anomalie et de question).
- Écrire les identifiants en entier dans les étiquettes (`wire020 / wire021`, jamais `wire020/021`) : le vérificateur les recherche dans le texte.
- Dans une hypothèse, ce qui est nouveau est en vert (`box-new`, `fuse-new`, `idn`, `tn`).
- 230 V : le folio 3 est unifilaire (un trait par câble, barres obliques = nombre de conducteurs) ; les trois fils du câble sont cités dans l'étiquette. Classes `ph`, `ne`, `pe` + `pey` réservées au multifilaire.
- Folios : 0 implantation, 1 câblage 12 V actuel, 3 réseau 230 V ; les hypothèses ont leurs propres folios (2a, 2b…).
- Plan d'implantation (`folio-0-implantation.svg`) : chaque zone porte `data-zone="id"`, chaque équipement placé `data-equipement="id"` (un `<tspan>` vide suffit pour un équipement regroupé avec un autre). Classes `hull`, `zone`, `zone-pont`, `callout`, `leader`. Le vérificateur exige que tout équipement ayant une `zone` y figure.
- Le bloc `<style>` évolue : quand une classe est ajoutée, la reporter dans tous les folios et dans le gabarit de `outils/page.py`.

## Git

- `main` : le relevé et les décisions validées.
- `etude/securisation`, `etude/chauffe-eau`, `etude/solaire`, `etude/shunt`, `etude/batterie` : une branche par axe. Les hypothèses sont des dossiers dans la branche, pas des branches, pour pouvoir les comparer côte à côte.
- Ordre de fusion prévu : la sécurisation d'abord (prérequis), puis rebase des autres branches.
- **Une branche d'étude ne modifie que son dossier `etudes/<X-axe>/`.** Le relevé, `commun/`, `documentation-technique/`, `outils/`, les README généraux et CLAUDE.md se modifient sur `main`, puis les branches sont rebasées. Sinon, chaque rebase produit des conflits.
- Un commit = un sujet. Tag `rev-X` quand une révision des schémas est publiée.
- Push : remote SSH `origin`, poussé par l'utilisateur (pas de clé GitHub configurée pour Claude).

## Page de consultation

`python Electricité/outils/page.py` produit `Electricité/build/juju.html` (non versionné) : une seule page, avec un menu qui choisit la vue « Relevé » (branche `main` : folios de l'existant et des études fusionnées, anomalies, questions) ou une vue par branche d'étude (README de l'étude, folios et comparaison de ses hypothèses). Les branches sont lues par `git archive`, sans changer de branche ; la branche courante est lue sur le disque. Une étude fusionnée dans `main` n'a pas de vue propre.

La page est publiée en artifact : https://claude.ai/artifact/Vj1VV9bWUtJjnwGRuP5a36 (republier sur la même URL après tout changement, sur n'importe quelle branche). Chaque vue a son ancre (`#releve`, `#etude-D`…).

Python 3.12 est installé pour l'utilisateur. S'il n'est pas dans le PATH : `%LOCALAPPDATA%\Programs\Python\Python312\python.exe`. Dépendances : `Electricité/outils/requirements.txt`.
