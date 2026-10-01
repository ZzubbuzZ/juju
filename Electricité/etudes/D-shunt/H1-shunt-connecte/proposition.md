---
hypothese: D-H1
titre: Shunt connecté, lecture sur smartphone
etat: proposee
resume: Shunt Bluetooth de 500 A sur le négatif de la batterie de servitude ; état de charge, historique et tension de la batterie moteur dans l'application.
points_forts:
  - Le plus simple à poser, rien à percer au tableau.
  - Historique des consommations dans l'application.
  - Aucun câble à tirer jusqu'à la table à carte.
points_faibles:
  - Lecture et alarme de tension basse sur le téléphone seulement.
  - Pas d'afficheur dédié possible ; une lecture fixe ne peut s'ajouter que par l'écran d'un Cerbo GX (H5), bien plus cher.
---

# D-H1 · Shunt connecté, lecture sur smartphone

Hypothèse de l'étude D. Base : **A-H4**, c'est-à-dire le programme retenu de l'étude A (fusibles de 400 A près des batteries compris). Aucune anomalie traitée : l'étude D ajoute une mesure, elle ne corrige pas un défaut.

Câblage : [cablage.yaml](cablage.yaml), [folio 2e](folio-2e-shunt.svg). Nomenclature : [nomenclature.yaml](nomenclature.yaml), environ **160 €**.

## Principe

Un shunt connecté de 500 A (type Victron SmartShunt) est inséré sur le négatif de la batterie de servitude. Il compte les ampères-heures entrés et sortis, en déduit l'état de charge et transmet le tout par Bluetooth à une application sur smartphone, qui garde aussi l'historique. Son entrée auxiliaire mesure la tension de la batterie moteur.

## Câblage

Emplacement **b** du [README de l'étude](../README.md#deux-emplacements-possibles) : derrière la descente, près du coupe-circuit des négatifs, accessible par l'ouverture côté cabine de poupe.

| Fil | De → vers | Section | Rôle |
|---|---|---|---|
| wire009 (repris) | − batterie de servitude (node008) → shunt, côté batterie (node086) | 35 mm², 1 m | Câble existant : seule son extrémité côté coupe-circuit change |
| wire180 | shunt, côté système (node087) → coupe-circuit des négatifs (node005) | 35 mm², 0,2 m | Tout le reste du bord revient par ce fil |
| wire181 → wire182 | côté batterie du coupe-circuit de servitude (node009) → fusible 1 A → shunt Vbatt+ (node088) | 0,75 mm² | Alimentation du shunt et mesure de la tension de servitude |
| wire183 → wire184 | côté batterie du coupe-circuit moteur (node003) → fusible 1 A → entrée auxiliaire (node089) | 0,75 mm² | Tension de la batterie moteur |

Points de câblage :

- **Rien d'autre que wire009 sur la borne côté batterie du shunt.** C'est la condition d'une mesure juste : la batterie moteur (wire004) et le chargeur (wire005) restent sur node005, de l'autre côté.
- **Fils de mesure pris en aval des fusibles de 400 A**, sur la borne côté batterie des coupe-circuits : ils sont protégés en amont, et le moniteur reste alimenté coupe-circuits ouverts. Il mesure donc la consommation résiduelle et la charge au quai, bateau coupé.
- **Fusible de 1 A à la source de chaque fil de mesure**, contre la borne, comme pour les autres départs (règle du dépôt). Le 0,75 mm² est largement protégé par 1 A.
- Les deux coupe-circuits étant sur la même platine, les fils de mesure ne font que quelques dizaines de centimètres.
- **Variante, emplacement a** (shunt dans le coffre de la batterie) : mêmes fils, mêmes numéros ; wire009 devient le court tronçon et wire180 le fil de 1 m, et le fil d'alimentation du shunt doit alors venir de node009, à travers la cloison. Rien ne la justifie depuis que wire009 est confirmé à 1 m (Q30).

## Ce que la mesure couvre

Tout courant qui entre dans la batterie de servitude ou qui en sort : les charges, le chargeur de quai, l'alternateur par le coupleur, et le démarreur quand le coupe-circuit de couplage est fermé. Ce dernier cas explique le calibre de 500 A ; un shunt de 300 A risquerait d'être saturé au démarrage couplé.

La batterie moteur n'est suivie qu'en tension, par l'entrée auxiliaire. L'objectif fixé ne demande pas plus (voir le README de l'étude).

## Mise en service

1. Régler la chimie (plomb), la capacité (110 Ah) et la tension de pleine charge sur l'application ; régler l'entrée auxiliaire sur « batterie de démarrage ».
2. Faire une pleine charge au quai pour synchroniser l'état de charge à 100 %.
3. Appliquer le protocole du README : allumer les circuits un par un, noter le courant, et remplacer les estimations de [bilan-energetique.yaml](../../../commun/bilan-energetique.yaml) (modification à faire sur `main`).

## Conséquences

- **Consommation propre** : de l'ordre du milliampère d'après les fiches des modèles de ce type (à vérifier), soit quelques centièmes d'ampère-heure par jour. Négligeable devant les 60 Ah par jour du bilan au mouillage.
- **Lecture** : il faut un smartphone à portée Bluetooth pour voir l'état de charge, et l'alarme de tension basse n'est visible que sur le téléphone. C'est la limite de cette hypothèse.
- **Évolution** : un shunt connecté n'accepte pas d'afficheur dédié. Une lecture fixe ne pourra s'ajouter que par une centrale Cerbo GX et son écran (D-H5), qui reprend le SmartShunt sans le racheter. Si un simple afficheur est souhaité, autant partir sur D-H2.
- **LiFePO4** : la chimie se règle dans l'application, sans changer de matériel.
- **Solaire (étude C)** : les régulateurs de la même famille peuvent recevoir la tension et le courant du shunt par Bluetooth, pour une charge plus juste. À vérifier sur les fiches au moment du choix du régulateur.
