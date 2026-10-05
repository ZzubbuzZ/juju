# Étude E · Batterie de servitude

**Objectif** : supprimer le risque d'accumulation d'hydrogène dans la cabine de poupe (anomalie A11). La batterie de servitude, au plomb, est dans un coffre peu aéré sous le matelas de la cabine de poupe : en fin de charge, elle dégage de l'hydrogène, qui peut s'accumuler là où l'on dort et exploser au moindre arc.

Deux voies : **remplacer la batterie par une LiFePO4**, qui ne dégage pas de gaz en fonctionnement normal, ou **garder le plomb et traiter le gaz**, en ventilant le coffre ou en déplaçant la batterie.

**Base** : le programme retenu de l'étude A (A-H4, qui cumule A-H2), comme l'étude D. Les fusibles de 400 A près des batteries et les fusibles des départs du coupleur et du chargeur (folio 2c) sont donc supposés posés.

## Ce que le relevé dit déjà

- Batterie de servitude : 110 Ah, plomb « sans entretien », dans un coffre sous le matelas de la cabine de poupe, contre le coffre moteur. Type exact (ouverte ou AGM) et dimensions non relevés ; le coffre a de la place pour une batterie de taille voisine (Q45, 03/10).
- Batterie moteur : Varta 110 Ah, plomb, dans le coffre de cockpit tribord. Elle n'est pas concernée par l'étude.
- Coupleur Scheiber 38.14700 à relais, prévu pour le plomb uniquement. Le coupe-circuit de couplage (node011, node012) met les deux batteries en parallèle à la main.
- Chargeur de quai Dolphin 12 V 20 A, trois sorties, prévu pour le plomb uniquement. Sa notice ne prévoit pas de mélanger les technologies.
- Alternateur d'environ 20 A (spécification d'origine, Q14).
- Bilan énergétique (estimations) : environ 60 Ah par jour au mouillage et 87 Ah par jour en navigation.

## Hypothèses

| | Principe | Hydrogène | Coût estimé | État |
|---|---|---|---|---|
| [H1](H1-lifepo4/proposition.md) | Batterie LiFePO4 (200 Ah commandée le 05/10) à la place du plomb, chargeur DC/DC à la place du coupleur Scheiber, coupe-circuit de couplage déposé, chargeur de quai dédié à la LiFePO4 | Supprimé à la source | environ 900 € | **Retenue** le 02/10 |
| [H2](H2-plomb-ventile/proposition.md) | Plomb conservé en place, coffre ventilé vers l'extérieur | Évacué | environ 90 € | Écartée le 02/10 |
| [H3](H3-plomb-deplace/proposition.md) | Plomb déplacé dans un coffre ventilé hors des cabines | Évacué hors des cabines | environ 190 € | Écartée le 02/10 |
| [H4](H4-chargeur-coffre/proposition.md) | Variante de H1 : Orion XS, chargeur de quai et shunt dans le coffre de la batterie au lieu de la contremarche | Supprimé à la source | comme H1, à quelques mètres de câble près | À choisir sur place face à H1 |

Les coûts sont les totaux des nomenclatures : prix relevés par recherche web le 01/10/2026 pour la batterie et les chargeurs, estimations pour le reste. Toutes les questions de l'étude sont répondues (Q45 à Q53). **Câblage écrit le 05/10** : [H1](H1-lifepo4/cablage.yaml) (base : D-H1, Orion XS, chargeur de quai et shunt dans la contremarche) et sa variante [H4](H4-chargeur-coffre/cablage.yaml) (dans le coffre de la batterie). Folios cibles, chacun avec un circuit moteur et un circuit servitude : H1, [2h](H1-lifepo4/folio-2h-circuit-moteur.svg) et [2i](H1-lifepo4/folio-2i-circuit-servitude.svg) ; H4, [2j](H4-chargeur-coffre/folio-2j-circuit-moteur.svg) et [2k](H4-chargeur-coffre/folio-2k-circuit-servitude.svg). Nouveaux numéros : node360 à node379, wire200 à wire217 ; node074 (fusible de 30 A du Dolphin) est remonté sur le goujon du fusible de 400 A. Le guindeau passe sur le circuit moteur (wire217 remplace wire017).

## Critères de comparaison

- **Sécurité** : hydrogène dans la cabine, et pour la LiFePO4, tenue en court-circuit (pouvoir de coupure du fusible de batterie) et coupure par le BMS.
- **Énergie utile** : une batterie au plomb ne doit pas descendre sous 50 % de charge, soit environ 55 Ah utiles sur 110 Ah, moins que la consommation d'une journée au mouillage. Une LiFePO4 de 100 Ah en donne 80 à 90.
- **Charge** : compatibilité avec l'alternateur, le chargeur de quai, le futur régulateur solaire (étude C).
- **Poids et place** : environ 25 à 30 kg pour le plomb de 110 Ah, environ 10 kg pour une LiFePO4 de 100 Ah.
- **Hiver** : une LiFePO4 ne se charge pas en dessous de 0 °C ; sans conséquence en Méditerranée, batterie à l'intérieur du bateau (Q47, 03/10).
- **Coût et travaux**.

## Ce que l'étude change chez les autres

- **Étude A** : H1 dépose le coupleur et le coupe-circuit de couplage, donc les fusibles de leurs départs (wire164, wire165) et le fusible de la sortie 2 du chargeur (wire163) deviennent inutiles. Le fusible de 400 A de la batterie de servitude doit avoir un pouvoir de coupure suffisant pour une LiFePO4.
- **Étude D** : le shunt de 500 A était justifié par le démarrage avec les batteries couplées. Sans couplage, et avec le guindeau sur la batterie moteur (05/10), ni le démarreur ni le guindeau ne le traversent ; le plus fort courant est celui des départs de la servitude. Le SmartShunt de 500 A reste le plus petit modèle, il est conservé ; sa chimie se règle sur LiFePO4.
- **Étude C** : le régulateur solaire devra avoir un profil LiFePO4.
- **Réseau 230 V (folio 3)** : H1 ajoute un second chargeur de quai, sur le disjoncteur de 10 A du chargeur.
- **Bilan énergétique** : avec H1, la capacité utile passe d'environ 55 Ah à 160-180 Ah.

## Décision

**02/10/2026 : H1 retenue par Julie**, batterie de servitude LiFePO4. Voir [decision.md](decision.md). H2 et H3 sont écartées.

**05/10/2026 : matériel commandé** : batterie Humsienk 12 V 200 Ah Plus (BMS 250 A), Victron Orion XS 12/12-50A, Victron Blue Smart IP67 12/17 ; fusible MEGA pour la batterie de servitude, sans classe T. Détail et conséquences dans [decision.md](decision.md) et [H1](H1-lifepo4/proposition.md#batterie-commandée-0510). La batterie fait 52 cm et 26 kg ; sa place dans le coffre n'est pas un problème (Q51).

**Réponses du 05/10** : commande manuelle de l'Orion XS par un interrupteur près du tableau Scheiber (Q48) ; place de la batterie sans problème (Q51) ; Blue Smart BPC121713006 à 118 € (Q52) ; 230 V du Blue Smart par un câble dédié depuis le disjoncteur du chargeur (Q53). Orion XS acheté 259 €.

**Remarques du 05/10 (suite)** : coupe-circuit de couplage déposé sans exception (les deux batteries n'ont pas la même tension) et démarrage direct sur la LiFePO4 abandonné ; commande de l'Orion XS par un + commuté sur la broche H (option b de la notice, cavalier H-L retiré), avec un interrupteur à voyant dont le voyant va à la masse ; fusibles de 70 A et câbles de 16 mm² pour l'Orion XS (notice) ; recharge de secours inversée de 25 A au plus ; **guindeau sur le circuit moteur**.

**Réponses du 03/10** : place suffisante dans le coffre (Q45), second chargeur à côté du Dolphin (Q49), pas de gel en Méditerranée (Q47). Restent à préciser avant le câblage : la commande du DC/DC, après contact ou interrupteur à la table à carte (Q48, voir H1), la longueur du câble 12 V du second chargeur (Q50), et le pic de courant du BMS face au guindeau, au choix de la batterie.

Proposition initiale de Claude (01/10), qui a conduit à ce choix : H1 est la seule hypothèse qui supprime le gaz au lieu de l'évacuer, et elle répond aussi au manque d'énergie au mouillage (55 Ah utiles avec le plomb, pour environ 60 Ah consommés par jour). Chaque batterie a son propre chargeur : le DC/DC au moteur et un chargeur dédié au quai pour la LiFePO4, le Dolphin pour la seule batterie moteur.

En attendant la pose, une mesure immédiate et gratuite : soulever le matelas et ouvrir le coffre pour l'aérer quand le chargeur de quai tourne.
