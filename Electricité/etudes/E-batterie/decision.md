# Étude E · Décision

**02/10/2026** : Julie retient **H1**, une batterie de servitude LiFePO4 ([proposition](H1-lifepo4/proposition.md)). H2 (plomb ventilé) et H3 (plomb déplacé) sont écartées.

## Ce qui est décidé

- Batterie LiFePO4 à BMS intégré, dans le coffre actuel de la cabine de poupe : plus d'hydrogène dans la cabine (anomalie A11).
- Coupleur Scheiber déposé, remplacé par un chargeur DC/DC (type Victron Orion XS), commandé par un + après contact pour ne tourner qu'au moteur.
- Chargeur de quai dédié à la LiFePO4 ; le Dolphin ne charge plus que la batterie moteur (sa sortie 2 est débranchée).

## Ce qui reste à décider

- **Démarrage de secours** : niveau 1 seul (recharge de secours de la batterie moteur par le DC/DC, sans matériel), ou niveau 2 en plus (démarrage direct sur la LiFePO4 : batterie capable de démarrer, coupe-circuit de couplage conservé, protecteur d'alternateur, environ 150 à 200 € de plus). Voir la proposition, section « Démarrage de secours ».
- **Capacité** : 100 Ah, ou davantage selon l'objectif d'autonomie, à fixer avec l'étude C (solaire).
- **Modèle** de batterie et de chargeur de quai, d'après les fiches techniques.

## Avant le câblage et la fusion dans `main`

Réponses à Q45 (batterie et coffre), Q47 (hivernage), Q48 (+ après contact), Q49 (place du second chargeur). Puis `cablage.yaml` et folio de H1, et vérification du pouvoir de coupure du fusible de 400 A de A-H2 face à une LiFePO4.
