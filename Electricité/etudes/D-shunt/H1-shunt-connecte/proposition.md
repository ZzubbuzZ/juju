---
hypothese: D-H1
titre: Shunt connecté, lecture sur smartphone
etat: retenue
resume: Shunt Bluetooth de 500 A sur le négatif de la batterie de servitude ; état de charge, historique et tension de la batterie moteur dans l'application.
points_forts:
  - Le plus simple à poser, rien à percer au tableau.
  - Historique des consommations dans l'application.
  - Aucun câble à tirer jusqu'à la table à carte.
points_faibles:
  - Lecture et alarme de tension basse sur le téléphone seulement.
  - Pas d'afficheur dédié possible ; une lecture fixe ne peut s'ajouter que par l'écran d'un Cerbo GX (H5), bien plus cher.
decision: "14/10/2026 : retenue par l'utilisateur, lecture et alarme sur smartphone (application VictronConnect). Emplacement : niche de la contremarche (emplacement b), avec l'Orion XS ; chargeur de quai au coffre de cockpit (E-H5 retenue, E-H4 écartée le 14/10). Un Cerbo GX (H6) reste possible plus tard par le port VE.Direct, sans rien racheter."
---

# D-H1 · Shunt connecté, lecture sur smartphone

Hypothèse de l'étude D. Base : **A-H4**, c'est-à-dire le programme retenu de l'étude A (fusibles de 400 A près des batteries compris). Aucune anomalie traitée : l'étude D ajoute une mesure, elle ne corrige pas un défaut.

Câblage : [cablage.yaml](cablage.yaml), [folio 2e](folio-2e-shunt.svg). Nomenclature : [nomenclature.yaml](nomenclature.yaml), environ **120 €** (SmartShunt IP65 à 86 €, 05/10).

## Principe

Un shunt connecté de 500 A (type Victron SmartShunt) est inséré sur le négatif de la batterie de servitude. Il compte les ampères-heures entrés et sortis, en déduit l'état de charge et transmet le tout par Bluetooth à une application sur smartphone, qui garde aussi l'historique. Son entrée auxiliaire mesure la tension de la batterie moteur.

## Câblage

Emplacement **b** du [README de l'étude](../README.md#deux-emplacements-possibles) : derrière la descente, près du coupe-circuit des négatifs, accessible par l'ouverture côté cabine de poupe.

| Fil | De → vers | Section | Rôle |
|---|---|---|---|
| wire010 (repris) | − batterie de servitude (node008) → shunt, côté batterie (node011) | 35 mm², 1 m | Câble existant : seule son extrémité côté coupe-circuit change |
| wire003 (repris) | − batterie moteur (node002) → coupe-circuit des négatifs (node022) | 35 mm², longueur à relever (Q62) | Relevé sur le − de la batterie de servitude (node008) : son extrémité est reprise sur node022 pour ne pas passer par le shunt |
| wire011 | shunt, côté système (node012) → coupe-circuit des négatifs (node022) | 35 mm², 0,2 m | Tout le reste du bord revient par ce fil |
| wire014 → wire012 | côté batterie du coupe-circuit de servitude (node020) → fusible 1 A → shunt Vbatt+ (node013) | 0,75 mm² | Alimentation du shunt et mesure de la tension de servitude |
| wire006 → wire013 | côté batterie du coupe-circuit moteur (node005) → fusible 1 A → entrée auxiliaire (node014) | 0,75 mm² | Tension de la batterie moteur |

Points de câblage :

- **Rien d'autre que wire010 sur la borne côté batterie du shunt.** C'est la condition d'une mesure juste : le chargeur (wire060) reste sur node022, de l'autre côté, et la batterie moteur (wire003), relevée sur le − de la batterie de servitude, y est ramenée.
- **Fils de mesure pris en aval des fusibles de 400 A**, sur la borne côté batterie des coupe-circuits : ils sont protégés en amont, et le moniteur reste alimenté coupe-circuits ouverts. Il mesure donc la consommation résiduelle et la charge au quai, bateau coupé.
- **Fusible de 1 A à la source de chaque fil de mesure**, contre la borne, comme pour les autres départs (règle du dépôt). Le 0,75 mm² est largement protégé par 1 A.
- Les deux coupe-circuits étant sur la même platine, les fils de mesure ne font que quelques dizaines de centimètres.
- **Variante, emplacement a** (shunt dans le coffre de la batterie) : mêmes fils, mêmes numéros ; wire010 devient le court tronçon et wire011 le fil de 1 m, et le fil d'alimentation du shunt doit alors venir de node020, à travers la cloison. Rien ne la justifie depuis que wire010 est confirmé à 1 m (Q30).

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
