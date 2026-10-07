# Électricité de Juju

## Où en est-on

| Axe | Branche | État détaillé |
|---|---|---|
| Relevé de l'existant | `main` | 67 fils relevés (12 V et 230 V), 14 questions ouvertes ([questions.md](releve/questions.md)), 10 anomalies en cours et 1 levée ([anomalies.md](releve/anomalies.md)) |
| A · Sécurisation de l'existant | `main` (fusionnée) | Programme retenu le 30/09 : fusibles de batterie et de départs, cosses, terre 230 V, passages de cloison ; [README de l'étude](etudes/A-securisation/README.md) |
| B · Chauffe-eau | `main` (fusionnée le 07/10) | CozyWater 10C, 230 V sur prise dédiée (H1) et 12 V par relais (H3, retenue le 08/10) ; [README de l'étude](etudes/B-chauffe-eau/README.md) |
| C · Panneaux solaires | `etude/solaire` | En cadrage ; [README de l'étude](https://github.com/ZzubbuzZ/juju/blob/etude/solaire/Electricit%C3%A9/etudes/C-solaire/README.md) |
| D · Shunt et suivi des batteries | `main` | Shunt avec le chargeur de quai ; lecture sur téléphone (H1) ou afficheur (H2) à choisir ; [README de l'étude](etudes/D-shunt/README.md) |
| E · Batterie de servitude | `main` (fusionnée le 08/10) | LiFePO4 200 Ah, Orion XS, Blue Smart ; emplacement à choisir à bord (H1 ou H4) ; [décision](etudes/E-batterie/decision.md) |

Schémas de l'existant : [folio 0 · implantation](schemas/folio-0-implantation.svg), [folio 1 · 12 V](schemas/folio-1-actuel.svg), [folio 3 · 230 V](schemas/folio-3-230v.svg). L'état de chaque étude est tenu dans son propre README (sur sa branche tant qu'elle n'est pas fusionnée) : ce fichier-ci n'est modifié que sur `main`, pour éviter les conflits de rebase. Manuel du bord en préparation : [documentation-technique/](documentation-technique/README.md).

## Organisation

```
releve/      ce qui a été constaté à bord, et rien d'autre
schemas/     folios SVG de l'existant
etudes/      une hypothèse = un dossier H<n>-<nom> (sur la branche de son axe)
commun/      bilan énergétique partagé par les études
documentation-technique/  manuel du bord (installation, réglages, entretien)
outils/      vérificateur, générateur de page, schémas JSON
build/       page HTML générée (non versionnée)
```

## Contrôler les données

```sh
python Electricité/outils/verifier.py
```

Le vérificateur contrôle la syntaxe YAML (clés en double comprises), le schéma JSON, les références entre fichiers, la polarité et la couleur des fils, la présence de chaque fil sur les schémas, et applique les hypothèses sur leur base. Il donne aussi le bilan en Ah par jour. Le hook `pre-commit` refuse un commit qui contient une erreur.

Dans VS Code, l'extension YAML de Red Hat valide les fichiers en direct grâce à la ligne `# yaml-language-server: $schema=…` en tête de chaque fichier. La tâche « Vérifier les données » (Ctrl+Maj+P, puis « Run Test Task ») lance le vérificateur.

## Déroulé d'une visite à bord

1. Emporter [questions.md](releve/questions.md), sur papier ou sur téléphone.
2. Noter les réponses sous chaque question, précédées de `→` et de la date. Déposer les photos dans `releve/photos/`.
3. Demander à Claude d'« intégrer les réponses ». Il met à jour les YAML (en retirant `statut: estime` des valeurs mesurées), le folio 1, l'état des lieux et la liste des questions, lance le vérificateur, commite sur `main`, rebase les branches d'étude et republie la page. Il signale aussi les conséquences sur les études en cours.
4. Relire le commit, puis pousser.

## Déroulé d'une hypothèse

1. Sur la branche de l'axe, créer `etudes/<axe>/H<n>-<nom>/`.
2. Y écrire `proposition.md` (en-tête YAML, puis quoi, pourquoi, conséquences), `nomenclature.yaml` (matériel chiffré, liens produits), `cablage.yaml` (ajouts et suppressions par rapport à la base) et les folios SVG. La page de consultation compare les hypothèses de chaque étude à partir de ces en-têtes et nomenclatures.
3. Vérifier, commiter. Comparer les hypothèses dans le README de l'axe.
4. Une fois l'hypothèse retenue : `decision.md` dans le dossier de l'axe, puis fusion dans `main`.
