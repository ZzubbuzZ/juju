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
| Batterie de servitude → coupe-circuit | wire009, wire008 ; retour wire010, wire011 | 35 mm², 1,2 m + 1,2 m | 100 A (pointe des départs) ; BMS 250 A | MEGA 300 A (E-H1) | 1,0 % à 100 A | Conforme si l'isolant est à 105 °C (Q58) |
| Batterie moteur → coupe-circuit | wire002, wire001 | 35 mm², 2,2 m | démarreur 200 à 275 A | MEGA 400 A (A-H2) | sans objet | Écart accepté le 30/09 (démarreur) ; isolant : Q58 |
| Guindeau (sur le circuit moteur, E-H1) | wire101, wire109, wire111, wire112, wire105, wire003 | 35, 50 et 10 mm², environ 26 m de trajet | 50 A normal, 60 A en charge | disjoncteur 70 A (notice Lewmar) | **4,6 %** à 50 A, **5,6 %** à 60 A | Acceptable pour un moteur (< 10 %) |
| Guindeau en secours sur la LiFePO4 (sélecteur en position 2, 13/10) | wire103, wire108, wire109, wire111, wire112, wire105 | 35, 50 et 10 mm², trajet voisin du circuit moteur | 50 A normal, 60 A en charge | MEGA 300 A, puis disjoncteur 70 A | voisine du circuit moteur | Acceptable en secours ; 50 à 60 A sous les 250 A du BMS |
| Dolphin → batterie moteur | wire063, wire050 | 6 mm², 0,5 + 0,5 m | 20 A | 30 A à la batterie | 0,5 % | Conforme |
| Orion XS, entrée et sortie | wire053, wire058, wire062, wire065, wire066 | 16 mm², 0,65 + 0,5 m | réglé vers 15 A ; 50 A au plus | 70 A aux deux bouts (notice) | 0,2 % à 15 A ; 0,5 % à 50 A | Conforme |
| Blue Smart IP67 12/17 (coffre de cockpit, E-H5) → servitude | wire056, wire059, wire064 | pont de 4 mm² 0,1 m depuis le fusible de sortie de l'Orion XS (15/10), puis 10 mm² 2 × 5 m (Q64) | 17 A | 25 A à la source | 2,6 % | Conforme sous 3 % ; fin de charge corrigée par la tension du shunt (VE.Smart) |
| Ballon, entrée 12 V (B-H3) | wire154, wire161, wire173 | 6 mm², 3,5 + 3 m (est. : trajet de wire200, ballon sous la table à carte, Q57) | 17 A | disjoncteur 12 V CC de 30 A à la platine (notice : 30 A ; 12/10) | 2,8 % | Conforme (confort, 10 %) |
| Frigo : batterie → tableau Scheiber → EPS 100 → groupe froid | wire158, wire162, wire165, wire166, wire171, wire172 | 6 puis 3,5 mm², environ 6,5 m (est.) | 3,5 A ; 5 A au démarrage | 30 A (A-H2), puis 15 A (tableau Scheiber) | 1,8 % ; **2,6 %** au démarrage | Conforme ; longueurs de wire158, wire162, wire165, wire166 non relevées |
| Pompe de cale | wire167, wire168 | 2,5 mm², 3 m (est.) | 3 A | 10 A (tableau Scheiber) | 1,1 % | Section conforme ; fusible : anomalie A10 (3 A demandés) |

Les fils de mesure et de commande (shunt, Orion XS) sont en 0,75 mm² avec un fusible de 1 A à leur source : conforme.

## Ponts entre porte-fusibles (15/10)

Les porte-fusibles MIDI de la niche sont reliés par des ponts, un par potentiel, au lieu d'un câble chacun depuis les coupe-circuits (proposition de l'utilisateur) :

| Pont | Câble d'alimentation (non protégé) | Pont | Somme des fusibles |
|---|---|---|---|
| Côté batterie de servitude (node020) : sortie de l'Orion XS, Blue Smart | wire058, 16 mm², 0,25 m | wire056, 4 mm², vers le fusible de 25 A | 70 + 25 A (au plus 50 + 17 A de charge) |
| Côté charges (node021) : table à carte, Scheiber | wire157, 16 mm², 0,25 m | wire156, 6 mm², vers le fusible de 30 A | 50 + 30 A |

Le câble d'alimentation porte la somme des fusibles qu'il dessert, d'où le 16 mm². Il n'est protégé que par le MEGA de 300 A, comme l'étaient les câbles qu'il remplace : longueur courte, porte-fusibles capotés. Un 35 mm², calibré pour le MEGA, ne se réalise pas en pont et n'apporterait rien de plus (décision de l'utilisateur, 15/10). Chaque pont ne porte que le courant du fusible qu'il alimente. Ponts en câble isolé, cosses serties sous gaine thermorétractable.

## Alimentation du tableau de la table à carte

wire200 (+) et wire201 (−) : 6 mm², environ 3 m chacun, fusible de 50 A à la source (A-H2). En amont du fusible, wire157 (16 mm², 0,25 m) alimente aussi, par le pont wire156, le fusible du Scheiber (15/10).

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
| 50 A (A-H2) | wire200, 6 mm² | isolant de 75 °C au moins ; sinon **40 A** suffisent au tableau |
| 30 A (A-H2) | wire158, 6 mm² | conforme dans tous les cas |
| 300 A (E-H1) | wire008, 35 mm² | isolant à 105 °C (règle des 150 %) |
| 400 A (A-H2) | wire001, 35 mm² | écart accepté le 30/09, câble du démarreur |

## 230 V

| Point | Valeur | Verdict |
|---|---|---|
| Borne de Saint-Chamas | 16 A, environ 3 700 W | |
| Consommation à bord, ballon compris | environ 1 450 W, soit 6,5 A | Sans contrainte ; en escale à 6 A, couper un chargeur pendant la chauffe |
| Disjoncteurs des chargeurs : un C10 pour le Dolphin, un C10 pour le Blue Smart (12/10) | 2,5 A et 1,5 A environ | Conforme ; wire311 à wire313 en 1,5 mm² sur le C10 du Blue Smart (node316) |
| C10 libéré du boîtier tribord : prise du ballon, sous la table à carte | 3,5 A ; wire334 à wire336 en 1,5 mm², environ 5 m (est.), par une boîte de dérivation ; ΔU 0,2 % | Conforme ; câbles des deux C10 regroupés sur l'autre C10 (décision du 12/10, voir ci-dessous) |
| Différentiel d'arrivée | 30 mA type A, 40 A (A-H4) | Calibre supérieur à la borne : conforme |

### Les deux C10 du boîtier tribord (Q42)

**15/10** : affectation supposée par l'utilisateur, C10 n°1 éclairage tribord, C10 n°2 éclairage bâbord (hypothèse 1 ci-dessous). Le câble bâbord (wire331) passe sur le C10 n°1, le C10 n°2 alimente le ballon (B-H1). Le câble d'alimentation du boîtier tribord (wire308 à wire310, 2,5 mm²) n'a pas de disjoncteur à l'arrivée (A12) : il n'est protégé que par la borne du port.

Le 12/10, les deux C10 sont trouvés occupés, chacun par un seul câble de 1,5 mm², sans que leurs circuits aient été vérifiés. Deux hypothèses sont à vérifier à bord. Dans les deux cas, la question est de savoir si l'on peut regrouper ces circuits sur un seul C10 pour libérer l'autre au profit du ballon. Puissances estimées, à confirmer sur les appareils :

| Charge | Puissance | Courant à 230 V | Base de l'estimation |
|---|---|---|---|
| Éclairage 230 V : 4 spots GU10 et 2 barrettes de 2 spots, soit 8 lampes à LED | environ 50 W | 0,2 A ; 0,4 A au plus avec un mauvais facteur de puissance | 4 à 7 W par lampe GU10 à LED (valeur courante) |
| Frigo : EPS 100 (prise du frigo) | environ 70 W ; 100 W au plus | 0,3 A ; 0,5 A au plus | groupe froid 3,5 A sous 12 V, 5 A au démarrage, rendement d'environ 85 % ; l'EPS 100 est donné pour 100 W |
| Ballon (prise dédiée, B-H1) | 800 W (notice) | 3,5 A | |

| Répartition | C10 n° a | C10 n° b | Verdict |
|---|---|---|---|
| **Hypothèse 1 : éclairage réparti sur les deux C10** (état probable) | un câble d'éclairage : 0,2 A | l'autre câble d'éclairage : 0,2 A | Regroupement possible : 0,4 A au plus sur un C10, soit 4 % de son calibre. L'autre C10 est libéré pour le ballon. |
| **Hypothèse 2 : le frigo sur un C10** (et non sur le C16 des prises tribord, comme noté au relevé) | câble de l'éclairage : 0,4 A | câble du frigo : 0,5 A | Regroupement possible : 0,9 A au plus sur un C10, soit environ 200 W. L'autre C10 est libéré pour le ballon. |
| Avec le ballon, après regroupement | éclairage et frigo éventuel : 0,9 A au plus | ballon seul : 3,5 A | Conforme. Même tout sur un seul C10, on ne ferait que 4,4 A, mais la notice du ballon et Q56 demandent un disjoncteur pour lui seul. |

**Câbles en 1,5 mm².** Un câble de 1,5 mm² admet environ 16 A : un C10 le protège, quel que soit le nombre de départs. La chute de tension est négligeable à ces courants : 0,9 A sur 10 m aller donnent 2 × 10 × 0,9 × 0,0175 / 1,5 = 0,21 V, soit 0,1 % de 230 V. Un circuit de prise en 1,5 mm² sur un C10 (le frigo dans l'hypothèse 2) est aussi conforme.

**Raccordement des départs.** Chaque C10 n'a qu'un câble de 1,5 mm² (12/10). Regrouper revient donc à mettre deux câbles de 1,5 mm² sur un même disjoncteur : deux conducteurs de même section sous une même vis sont en général admis (capacité exacte des bornes : notice du DNX3). Si la borne ne les accepte pas, il faut un répartiteur ou deux bornes à levier (Wago 221) dans le boîtier, avec une seule liaison en 1,5 mm² vers le disjoncteur. Le neutre et la terre de chaque câble restent sur les barrettes.

**Décision du 12/10** : l'utilisateur regroupe les deux câbles sur un seul C10 et tire un câble neuf du C10 libéré vers le ballon, par une boîte de dérivation (B-H1). Le 12 V du ballon (B-H3) va dans une autre boîte, ou dans un compartiment séparé par une cloison.

**Conséquences.** Le frigo sur le même C10 que l'éclairage serait coupé par un défaut d'éclairage, et inversement. C'est acceptable à quai, où ces circuits servent, mais ce n'est pas conseillé si le frigo doit rester en route en l'absence de l'équipage. Si l'on veut garder le frigo seul, le mettre sur le C16 des prises tribord (environ 0,5 A de plus), comme le relevé le suppose déjà. À vérifier à bord : quels câbles partent de chaque C10, et où ils vont (Q42, Q60).

### Second C10 pour le chargeur de la LiFePO4 (retenu le 12/10)

Aujourd'hui, l'étude E prévoit les deux chargeurs de quai sur le même C10 du boîtier d'arrivée : le Dolphin (2,5 A au plus) et le Blue Smart IP67 12/17 (environ 1,5 A), soit environ 4 A pour 10 A. Un C10 de plus, pour le Blue Smart seul :

| | Un C10 pour les deux (prévu) | Un C10 par chargeur (option) |
|---|---|---|
| Charge | environ 4 A sur 10 A | 2,5 A et 1,5 A |
| Défaut sur un chargeur | coupe les deux | coupe celui-là seul : l'autre batterie continue de charger |
| Couper un chargeur à la main (borne de 6 A pendant la chauffe du ballon, B-H1 ; hivernage ; intervention) | débrancher sa fiche, si Q53 retient une prise ; sinon impossible sans couper l'autre | au disjoncteur |
| Coût et travaux | rien | disjoncteur 1P+N C10 (Merlin Gerin DT40 ou équivalent, environ 20 à 30 €) ; le câble wire311 à wire313 part de ce disjoncteur au lieu de node311 |
| Condition | | une place libre sur le rail du boîtier d'arrivée : il y en a une (Q63, 12/10) |

Le câble 3 × 1,5 mm² du Blue Smart reste protégé : un C10 le protège comme aujourd'hui. **Verdict** : utile, pas nécessaire. **Retenu le 12/10** (disjoncteur à 9 €, place libre confirmée) : câblé dans E-H1 (node315, node316, wire315, folio 2i). La place existe (Q63, 12/10) : l'option est réalisable. Elle vaut surtout si le Blue Smart est raccordé par un boîtier à bornes (sans fiche à débrancher, Q53). Sinon, une prise dédiée au Blue Smart (Q53) donne déjà le moyen de le couper seul.

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
- **Q57** : longueur du câble 12 V du ballon (3 m estimés, trajet de wire200 ; jusqu'à 12 m, le 6 mm² reste sous 10 %).
- **Q12** : longueurs réelles des départs du tableau de la table à carte.
- Longueurs de wire158, wire162, wire165, wire166, wire167 (tableau Scheiber, frigo, pompe de cale) : non relevées, estimées ici.
- Alternateur de 20 A, sans borne W (Q14, 13/10) : réglage de l'Orion XS à 15 A confirmé.
