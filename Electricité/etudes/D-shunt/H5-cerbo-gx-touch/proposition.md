---
hypothese: D-H5
titre: SmartShunt, Cerbo GX et écran GX Touch 50
etat: proposee
resume: Le SmartShunt de D-H1, lu par une centrale Victron Cerbo GX qui affiche tout le bord sur un écran tactile de 5 pouces à la table à carte, et peut fédérer plus tard le régulateur solaire et le chargeur.
points_forts:
  - Écran tactile lisible, alarmes visibles sans téléphone, historique détaillé.
  - Centralise les futurs appareils Victron (régulateur solaire de l'étude C, chargeur, batterie LiFePO4).
  - Suivi à distance par le portail VRM, si le bord dispose d'une connexion Internet.
points_faibles:
  - Environ quatre fois le prix de H2.
  - Consommation d'environ 0,3 A (3,8 W) tant que le Cerbo GX est allumé, soit environ 7 Ah par jour au mouillage, 12 % du bilan.
  - Écran rectangulaire qui n'entre pas dans le trou de l'indicateur à aiguille ; place à trouver pour l'écran et le Cerbo GX (Q43).
---

# D-H5 · SmartShunt, Cerbo GX et écran GX Touch 50

Hypothèse de l'étude D. Base : **D-H1** (même SmartShunt, même position, mêmes fils de mesure, sur le programme retenu de l'étude A).

Câblage : [cablage.yaml](cablage.yaml), [folio 2g](folio-2g-cerbo.svg) ; les fils de mesure sont sur le [folio 2e](../H1-shunt-connecte/folio-2e-shunt.svg). Nomenclature : [nomenclature.yaml](nomenclature.yaml), environ **675 €**.

## Principe

Le GX Touch 50 n'est qu'un écran : il a besoin d'une centrale **Cerbo GX**, qui lit les appareils Victron et les affiche. Ici, le Cerbo GX lit le SmartShunt de D-H1 par un câble VE.Direct. L'écran affiche l'état de charge, les courants, la tension de la batterie moteur et l'historique ; il déclenche les alarmes de tension basse.

L'intérêt de cette architecture dépasse le shunt : le régulateur solaire de l'étude C, un futur chargeur Victron ou une batterie LiFePO4 avec son BMS se branchent sur le même Cerbo GX et s'affichent sur le même écran.

## Câblage

Tout ce que décrit [D-H1](../H1-shunt-connecte/proposition.md#câblage), plus :

| Fil | De → vers | Rôle |
|---|---|---|
| wire186 → wire187 | côté charges du coupe-circuit de servitude (node010) → fusible 3 A → Cerbo GX + (node342) | Alimentation du Cerbo GX, 0,75 mm² |
| wire188 | Cerbo GX − (node343) → coupe-circuit des négatifs, côté charges (node006) | Masse du Cerbo GX, comptée par le shunt |
| wire189 | port VE.Direct du SmartShunt (node094) → Cerbo GX (node344) | Câble VE.Direct de 1,8 m |
| wire190 | Cerbo GX (node345) → GX Touch 50 (node346) | Câble de l'écran (2 m fourni, plus une rallonge de 2 m), sur le trajet de wire019 |

Points de câblage :

- **Cerbo GX alimenté après le coupe-circuit de servitude** : il s'éteint quand on coupe le bateau, ce qui supprime sa consommation au port. Le SmartShunt, alimenté avant le coupe-circuit (node009), continue de compter : l'historique reste complet.
- **Fusible de 3 A à la source**, contre la borne, comme les autres départs. Le Cerbo GX consomme environ 0,3 A.
- **Cerbo GX près de la platine des coupe-circuits** : câble VE.Direct court jusqu'au shunt, et place pour les futurs appareils (régulateur solaire, chargeur). Si la place manque, il peut aller à la table à carte, avec un câble VE.Direct de 5 m et sans rallonge d'écran (Q43).

## Conséquences

- **Bilan énergétique** : 2,8 W pour le Cerbo GX seul, 3,8 W avec l'écran rétroéclairage éteint, 4,8 W au maximum (fiche Victron). Allumé 24 h au mouillage, il consomme environ 7 Ah, à ajouter aux 60 Ah par jour du bilan (modification à faire sur `main` si H5 est retenue).
- **Écran** : rectangulaire (environ 13 × 9 cm), il ne prend pas la place de l'indicateur à aiguille comme l'afficheur de D-H2. Il se monte en saillie ou encastré, selon la place à la table à carte (Q43).
- **Solaire (étude C)** : un régulateur MPPT Victron se raccorde au Cerbo GX par VE.Direct ; le Cerbo GX partage alors la tension et le courant mesurés par le shunt avec le régulateur, pour une charge plus juste.
- **LiFePO4** : la chimie se règle dans le SmartShunt, et le BMS d'une batterie lithium compatible peut se raccorder au Cerbo GX.
- **Indicateur à aiguille** : il peut rester en place, ou être déposé (Q41).
