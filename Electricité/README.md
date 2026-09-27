# Électricité de Juju

## Où en est-on

| Axe | Branche | État |
|---|---|---|
| Relevé de l'existant | `main` | 21 fils relevés, 20 questions ouvertes ([questions.md](releve/questions.md)), 5 anomalies ([anomalies.md](releve/anomalies.md)) |
| A · Sécurisation de l'existant | `etude/securisation` | H1 (distribution de servitude) rédigée, à valider |
| B · Chauffe-eau | `etude/chauffe-eau` | Cadrage |
| C · Panneaux solaires | `etude/solaire` | Cadrage |

Schéma de l'existant : [folio 1](schemas/folio-1-actuel.svg).

## Organisation

```
releve/      ce qui a été constaté à bord, et rien d'autre
schemas/     folios SVG de l'existant
etudes/      une hypothèse = un dossier H<n>-<nom> (sur la branche de son axe)
commun/      bilan énergétique partagé par les études
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

1. Emporter [questions.md](releve/questions.md).
2. Au retour, noter les réponses (section « Réponses », avec la date) et corriger les YAML : retirer `statut: estime` des valeurs mesurées, ajouter les fils relevés.
3. Mettre à jour le folio 1, lancer le vérificateur, commiter sur `main`.
4. Rebaser les branches d'étude sur `main`.

## Déroulé d'une hypothèse

1. Sur la branche de l'axe, créer `etudes/<axe>/H<n>-<nom>/`.
2. Y écrire `proposition.md` (quoi, pourquoi, conséquences), `cablage.yaml` (ajouts et suppressions par rapport à la base) et les folios SVG.
3. Vérifier, commiter. Comparer les hypothèses dans le README de l'axe.
4. Une fois l'hypothèse retenue : `decision.md` dans le dossier de l'axe, puis fusion dans `main`.
