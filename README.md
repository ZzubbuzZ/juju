# Juju

Suivi des travaux de Juju, voilier Gib'Sea 31 de 1984.

| Chantier | État |
|---|---|
| [Électricité](Electricité/README.md) | Relevé de l'existant en cours ; sécurisation, chauffe-eau, shunt et batterie décidés ; solaire à l'étude |

## Mise en route après un clone

```sh
python -m pip install -r Electricité/outils/requirements.txt
git config core.hooksPath .githooks      # active le contrôle avant commit
```

Dans VS Code, installer les extensions recommandées (YAML de Red Hat pour la validation en direct des fichiers de données).
