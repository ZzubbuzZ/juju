# Étude E · Décision

**02/10/2026** : Julie retient **H1**, une batterie de servitude LiFePO4 ([proposition](H1-lifepo4/proposition.md)). H2 (plomb ventilé) et H3 (plomb déplacé) sont écartées.

## Ce qui est décidé

- Batterie LiFePO4 à BMS intégré, dans le coffre actuel de la cabine de poupe : plus d'hydrogène dans la cabine (anomalie A11).
- Coupleur Scheiber déposé, remplacé par un chargeur DC/DC (Victron Orion XS), commandé manuellement par un interrupteur à voyant (Q48, 05/10).
- Coupe-circuit de couplage déposé avec wire010 et wire011, sans exception : les deux batteries n'ont pas la même tension (05/10).
- **Guindeau sur le circuit moteur** (05/10) : wire217, depuis node004, remplace wire017.
- Chargeur de quai dédié à la LiFePO4 ; le Dolphin ne charge plus que la batterie moteur (sa sortie 2 est débranchée).

## Matériel commandé (05/10/2026)

| Élément | Modèle | Remarque |
|---|---|---|
| Batterie de servitude | **Humsienk 12 V 200 Ah Plus**, LiFePO4, BMS 250 A, Bluetooth | 259,99 € (prix remisé, fiche du site Humsienk). 521 × 238 × 221 mm, 26,4 kg, bornes M8, IP65 |
| Chargeur DC/DC | **Victron Orion XS 12/12-50A** | Acheté 259 € ; courant à régler vers 15 A (alternateur de 20 A) ; commande manuelle (Q48) |
| Chargeur de quai LiFePO4 | **Victron Blue Smart IP67 12/17** | À la place du Blue Smart IP65 12/15 prévu ; référence BPC121713006, 118 € (Q52) |
| Fusible de la batterie de servitude | **MEGA 300 A** (décision de l'utilisateur ; calibre confirmé le 08/10), pas de classe T | Voir « Fusible de batterie » dans [H1](H1-lifepo4/proposition.md#fusible-de-batterie--décision-du-0510) |

Le SmartShunt (étude D) n'est pas encore commandé.

**Emplacements des chargeurs (05/10)** : le Blue Smart se place **avec le shunt de l'étude D**, soit dans la contremarche de la descente, près de la platine, soit dans le coffre de la batterie de servitude : à décider sur place selon la place dans la contremarche (Q53). Son alimentation 230 V vient du disjoncteur du chargeur de quai (C10) par un câble dédié, jusqu'à une prise dédiée ou un boîtier de raccordement à bornes Wago (Q53). Dans les deux cas, son câble 12 V reste court. Le Dolphin, qui ne charge plus que la batterie moteur, est raccordé **au plus près d'elle** (fusible de 30 A à la batterie, négatif sur sa borne −), au lieu de passer par la platine.

## Ce qui reste à décider (mis à jour le 08/10)

- **Emplacement de l'Orion XS, du chargeur de quai et du shunt** : contremarche de la descente (H1, folios 2h et 2i) ou coffre de la batterie (H4, folios 2j et 2k), sur place. Les deux variantes sont fusionnées dans `main` ; celle qui n'est pas retenue sera marquée écartée.

Tranché le 08/10 : calibre du fusible MEGA de la servitude, **300 A**.

Tranchés le 05/10 : place de la batterie (Q51, pas un problème), commande manuelle de l'Orion XS (Q48), version du Blue Smart (Q52), alimentation 230 V du Blue Smart (Q53), démarrage de secours (niveau 1 seul, recharge inversée de 25 A par l'Orion XS ; démarrage direct abandonné), fusibles de l'Orion XS (70 A aux deux extrémités, 16 mm², d'après la notice), guindeau sur le circuit moteur.

## Ancienne liste (02/10)

- **Démarrage de secours** : niveau 1 seul (recharge de secours de la batterie moteur par le DC/DC, sans matériel), ou niveau 2 en plus (démarrage direct sur la LiFePO4 : batterie capable de démarrer, coupe-circuit de couplage conservé, protecteur d'alternateur, environ 150 à 200 € de plus). Voir la proposition, section « Démarrage de secours ».
- **Capacité** : 100 Ah, ou davantage selon l'objectif d'autonomie, à fixer avec l'étude C (solaire). → 05/10 : 200 Ah.
- **Modèle** de batterie et de chargeur de quai, d'après les fiches techniques. → 05/10 : commandés (ci-dessus).

## Fusion dans `main` (08/10)

Toutes les questions de l'étude sont répondues (Q45 à Q53). Le câblage de H1 et de sa variante H4 est écrit, avec leurs folios cibles (2h et 2i, 2j et 2k). Le fusible de la batterie de servitude est un MEGA de 300 A, par décision de l'utilisateur (la réserve sur son pouvoir de coupure est consignée dans H1). L'étude est fusionnée avec ses deux variantes d'emplacement, à départager à bord.
