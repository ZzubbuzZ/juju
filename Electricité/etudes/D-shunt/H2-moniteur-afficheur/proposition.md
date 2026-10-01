---
hypothese: D-H2
titre: Moniteur avec afficheur à la table à carte
etat: recommandee
resume: Même shunt et même pose que H1, avec un afficheur rond à la place de l'indicateur de charge à aiguille, relié par un câble de données.
points_forts:
  - Lecture et alarme sans téléphone, à la table à carte.
  - Prend la place de l'indicateur à aiguille, sans découpe nouvelle si le trou fait 52 mm (Q41).
  - Shunt de 500 A, câble de 10 m et Bluetooth fournis.
points_faibles:
  - Câble de données à tirer de la descente à la table à carte.
  - Branchement et diamètre du trou de l'indicateur à relever (Q41).
---

# D-H2 · Moniteur avec afficheur à la table à carte

Hypothèse de l'étude D. Base : **D-H1** (même shunt, même position, mêmes fils de mesure, sur le programme retenu de l'étude A).

Câblage : [cablage.yaml](cablage.yaml), [folio 2f](folio-2f-afficheur.svg) ; les fils de mesure sont sur le [folio 2e](../H1-shunt-connecte/folio-2e-shunt.svg). Nomenclature : [nomenclature.yaml](nomenclature.yaml), environ **165 €**, plus une éventuelle adaptation de la découpe (Q41).

## Principe

Un moniteur de batterie à afficheur (type Victron BMV-712 Smart) : shunt de 500 A, afficheur rond de 52 mm et Bluetooth. Le shunt se pose exactement comme dans D-H1. Un câble de données (RJ12, fourni en 10 m) le relie à l'afficheur, qui prend la place de l'indicateur de charge à aiguille du tableau de servitude (Q28). L'afficheur est alimenté par ce câble : aucun fil + ni fusible à ajouter au tableau.

## Câblage

Tout ce que décrit [D-H1](../H1-shunt-connecte/proposition.md#câblage), plus :

| Fil | De → vers | Rôle |
|---|---|---|
| wire185 | shunt (node094) → afficheur (node095), environ 4 m | Câble de données, qui alimente aussi l'afficheur |

Le câble de données suit le trajet de wire019, de la descente à la table à carte, avec des colliers et un passe-fil à chaque cloison (voir A-H5). Le câble fourni fait 10 m : la longueur en trop se love derrière le tableau.

L'indicateur à aiguille est déposé. Son branchement n'est pas relevé (**Q41**) : ses fils seront retirés jusqu'à leur source, ou isolés et étiquetés s'ils sont inaccessibles. Q41 demande aussi le diamètre du trou et la profondeur libre derrière le tableau : si le trou ne fait pas 52 mm, il faut une platine ou une collerette d'adaptation (article à chiffrer).

## Différences avec D-H1

| | D-H1 | D-H2 |
|---|---|---|
| Lecture | Smartphone seulement | Afficheur fixe et smartphone |
| Alarme de tension basse | Sur le téléphone | Sur l'afficheur (et relais d'alarme disponible) |
| Travaux en plus | aucun | Câble de données à tirer, découpe du tableau (Q41) |
| Coût estimé | environ 160 € | environ 165 € |

## Conséquences

- **Consommation propre** : un peu plus que D-H1 à cause de l'afficheur, toujours de l'ordre du milliampère (à vérifier sur la fiche). Négligeable.
- **Lecture sans téléphone** : l'état de charge et la tension de la batterie moteur sont visibles en passant devant la table à carte, ce qui sert directement l'objectif de surveillance.
- **LiFePO4 et solaire** : comme D-H1.
