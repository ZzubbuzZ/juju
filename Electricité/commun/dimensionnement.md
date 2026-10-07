# Dimensionnement de l'installation cible

Vérification des sections, des protections et des chutes de tension de l'installation telle qu'elle sera après les études décidées. Note commune à toutes les études, comme le [bilan énergétique](bilan-energetique.yaml) : elle se met à jour sur `main` à chaque étude fusionnée.

**Revue du 08/10/2026.** Installation cible : le relevé, plus le programme retenu de l'étude A (A-H2 et A-H4), le shunt (D-H1), la batterie LiFePO4 (E-H1) et le chauffe-eau (B-H1, B-H3). Le recâblage du tableau de la table à carte (A-H1, différé) est vérifié à part, en fin de note. Schéma de l'installation cible : [folio 4](../cible/folio-4-cible-12v.svg).

## Méthode

- Chute de tension : ΔU = Σ (L × I × 0,0175 / S) sur chaque fil du trajet, aller et retour, avec les longueurs et les sections des `cablage.yaml` et du relevé. Pourcentage rapporté à 12 V.
- Chute admise (CLAUDE.md) : **3 %** pour les feux, l'électronique, le pilote, la pompe de cale et le frigo ; **10 %** pour le confort. Pour un moteur (guindeau, démarreur), 10 % sont couramment admis.
- Protection : le fusible protège le câble, il est placé à sa source et son calibre ne dépasse pas le courant admissible du câble. Pour les câbles de batterie, la règle de l'ABYC (E-11) admet jusqu'à 150 % du courant admissible.
- Les longueurs marquées « est. » sont des estimations des études, pas des mesures.

## Circuits 12 V de puissance

| Circuit | Fils | Section, longueur | Courant | Protection | ΔU | Verdict |
|---|---|---|---|---|---|---|
| Batterie de servitude → coupe-circuit | wire161, wire006 ; retour wire009, wire180 | 35 mm², 1,2 m + 1,2 m | 100 A (pointe des départs) ; BMS 250 A | MEGA 300 A (E-H1) | 1,0 % à 100 A | Conforme si l'isolant est à 105 °C (Q58) |
| Batterie moteur → coupe-circuit | wire160, wire001 | 35 mm², 2,2 m | démarreur 200 à 275 A | MEGA 400 A (A-H2) | sans objet | Écart accepté le 30/09 (démarreur) ; isolant : Q58 |
| Guindeau (sur le circuit moteur, E-H1) | wire217, wire018, wire020, wire021, wire015, wire004 | 35, 50 et 10 mm², environ 26 m de trajet | 50 A normal, 60 A en charge | disjoncteur 70 A (notice Lewmar) | **4,6 %** à 50 A, **5,6 %** à 60 A | Acceptable pour un moteur (< 10 %) |
| Dolphin → batterie moteur | wire200, wire201 | 6 mm², 0,5 + 0,5 m | 20 A | 30 A à la batterie | 0,5 % | Conforme |
| Orion XS, entrée et sortie | wire202 à wire206 | 16 mm², 0,65 + 0,5 m | réglé vers 15 A ; 50 A au plus | 70 A aux deux bouts (notice) | 0,2 % à 15 A ; 0,5 % à 50 A | Conforme |
| Blue Smart IP67 12/17 → servitude | wire210 à wire212 | 4 mm², 0,65 + 0,5 m | 17 A | 25 A à la source | 0,7 % | Conforme |
| Ballon, entrée 12 V (B-H3) | wire306 à wire308 | 6 mm², 3,5 + 3 m (est., Q57) | 17 A | 30 A à la platine (notice) | 2,8 % | Conforme (confort, 10 %) |
| Frigo : batterie → tableau Scheiber → EPS 100 → groupe froid | wire022 à wire025, wire027, wire028 | 6 puis 3,5 mm², environ 6,5 m (est.) | 3,5 A ; 5 A au démarrage | 30 A (A-H2), puis 15 A (tableau Scheiber) | 1,8 % ; **2,6 %** au démarrage | Conforme ; longueurs de wire022 à wire025 non relevées |
| Pompe de cale | wire026, wire036 | 2,5 mm², 3 m (est.) | 3 A | 10 A (tableau Scheiber) | 1,1 % | Section conforme ; fusible : anomalie A10 (3 A demandés) |

Les fils de mesure et de commande (shunt, Orion XS, relais du ballon) sont en 0,75 mm² avec un fusible de 1 A à leur source : conforme.

## Alimentation du tableau de la table à carte

wire166 et wire019 (+), wire016 (−) : 6 mm², environ 3 m chacun, fusible de 50 A à la source (A-H2).

| Courant du tableau | ΔU sur l'alimentation |
|---|---|
| 10 A (navigation de nuit : feux, pilote, VHF, GPS, éclairage) | 1,5 % |
| 15 A | 2,2 % |
| 25 A | 3,7 % |

Cette chute s'ajoute à celle de chaque départ. Pour le pilote (pointe de 5 A, 4 mm² sur 5 m, 1,8 %), le total atteint environ **3,3 % en pointe** de nuit, juste au-dessus des 3 %. C'est sans conséquence pratique avec la LiFePO4, dont la tension reste vers 13,2 V : le pilote reçoit encore plus de 12,7 V. L'alimentation en 10 mm² prévue par A-H1 (différée) diviserait cette chute par 1,7.

## Courant admissible et calibres : Q58

Le courant qu'un câble supporte dépend de la température admise par son isolant, jamais relevée sur les câbles existants. Ordres de grandeur, d'après les tables de l'ABYC E-11 et de l'ISO 13297, à confirmer sur la norme et sur le marquage du câble :

| Section | Isolant 60 °C | Isolant 105 °C |
|---|---|---|
| 6 mm² | environ 40 A | environ 70 A |
| 35 mm² | environ 140 A | environ 210 A |

| Calibre retenu | Câble | Condition |
|---|---|---|
| 50 A (A-H2) | wire019, 6 mm² | isolant de 75 °C au moins ; sinon **40 A** suffisent au tableau |
| 30 A (A-H2) | wire022, 6 mm² | conforme dans tous les cas |
| 300 A (E-H1) | wire006, 35 mm² | isolant à 105 °C (règle des 150 %) |
| 400 A (A-H2) | wire001, 35 mm² | écart accepté le 30/09, câble du démarreur |

## 230 V

| Point | Valeur | Verdict |
|---|---|---|
| Borne de Saint-Chamas | 16 A, environ 3 700 W | |
| Consommation à bord, ballon compris | environ 1 450 W, soit 6,5 A | Sans contrainte ; en escale à 6 A, couper un chargeur pendant la chauffe |
| Disjoncteur du chargeur (C10) : Dolphin et Blue Smart | environ 2,7 A | Conforme ; wire213 à wire215 en 1,5 mm² sur un C10 |
| Second C10 du boîtier tribord : prise du ballon | 3,5 A ; wire300 à wire302 en 1,5 mm² | Conforme, si le C10 est libre (Q42) |
| Différentiel d'arrivée | 30 mA type A, 40 A (A-H4) | Calibre supérieur à la borne : conforme |

## Tableau de la table à carte (A-H1, différé)

Section requise S = 2 × L × I × 0,0175 / ΔU, pour chaque départ, comparée à la section prévue au [folio 2b](../etudes/A-securisation/H1-distribution-servitude/folio-2b-tableau-servitude.svg). Longueurs estimées dans A-H1 (mesures : Q12).

| Départ | Courant | L aller | ΔU admise | Section requise | Section prévue |
|---|---|---|---|---|---|
| Feu bicolore | 2,1 A | 8 m | 3 % | 1,63 mm² | 2,5 mm² |
| Feu de poupe | 0,8 A | 5 m | 3 % | 0,39 mm² | 1,5 mm² |
| Feu de tête de mât | 2,1 A | 10 m | 3 % | 2,04 mm² | 2,5 mm² |
| Feu de mouillage | 0,2 A | 15 m | 3 % | 0,29 mm² | 2,5 mm² |
| Projecteur | 2,9 A | 9 m | 10 % | 0,76 mm² | 2,5 mm² |
| Pompe à eau | 15 A | 3 m | 10 % | 1,31 mm² | 2,5 mm² |
| Autoradio | 5 A | 1,5 m | 10 % | 0,22 mm² | 1,5 mm² |
| Prises 12 V | 10 A | 4 m | 10 % | 1,17 mm² | 2,5 mm² |
| Éclairage | 5 A | 8 m | 10 % | 1,17 mm² | 2,5 mm² |
| Compas | 0,1 A | 3 m | 3 % | 0,03 mm² | 1,5 mm² |
| Pilote | 5 A | 5 m | 3 % | 2,43 mm² | 4 mm² |
| VHF | 6 A | 1 m | 3 % | 0,58 mm² | 2,5 mm² |
| GPS et instruments | 3 A | 1 m | 3 % | 0,29 mm² | 2,5 mm² |

Toutes les sections prévues conviennent. **Pompe à eau** : sa notice demande un fusible de 30 A, que 2,5 mm² ne supportent pas. Le fusible de 15 A est conservé pour protéger le câble ; s'il fond au démarrage, passer à 20 A.

## Points ouverts

- **Q58** : isolant des câbles de 6 et 35 mm² ; conditionne les calibres de 50 A et 300 A.
- **Q57** : longueur du câble 12 V du ballon (3 m estimés ; jusqu'à 12 m, le 6 mm² reste sous 10 %).
- **Q12** : longueurs réelles des départs du tableau de la table à carte.
- Longueurs de wire022 à wire026 (tableau Scheiber, frigo, pompe de cale) : non relevées, estimées ici.
- **Q14** : courant de l'alternateur, qui fixe le réglage de l'Orion XS (15 A pour un alternateur de 20 A).
