# État des lieux de Juju

## Qui est Juju?

Juju est un bateau Gib'Sea 31 de 1984. Il a été entierement rénové en 2020 (grément, peinture, vaigrage) et équipé d'une batterie de servitude, et d'un circuit 220v utilisable à quai.

## Si Juju est tout beau, tout retapé, pourquoi monter un dossier "électricité"?

### Circuit 12v

Les points suivants sont à revoir sur le circuit 12v :

- Pas de cosses sertie au bout des câbles de la batteries moteur, ils sont très abimés par le connecteur actuel. Il faut prévoir la pose de cosses.
- Pas de fusible en sortie de batterie (ni sur la batterie moteur, ni sur la batterie servitude )
- Le guindau est positionné sur la batterie de servitude (bien que celle-ci puisse être couplée à la batterie moteur)
- un coupleur à relai permet la charge de la batterie de servitude lorsque le moteur thermique tourne, mais ne permet pas un changement de technologie de batterie, comme la mise en place d'une batterie LiFePO4.
- Les poles 12vs du coupleur sont directement connectés aux connecteurs positifs des batteries. Le pole négatif est connecté au coupe circuit commun des masses des batteries (coté charge, pas coté batteries !). Je ne vois pas bien pourquoi ce choix a été fait
- Un chargeur de quai prenant en charge jusqu'à 3 batteries Pb est en place et est connecté en permanence aux batteries (sans passer par les coupes-circuits). Il ne permet pas non plus l'usage de batteires de technomogies différentes.
- C'est le basard derriere le panneau de servitude (plat de spaghettis de câbles)
- Pas de shunt pour controler le niveau de charge de la batterie de servitude.
- Pas de compte tour moteur.
- Pas de prises USB-C à bord 12v, et pas de 220v en navigation.
- Pas de haut parleur dans le cockpit.
- Les 2 circuits 12v ne sont pas du tout séparés (masses communes, 1 coupleur mécanique, un coupleur à relai).

### Circuit 220v

- Il faudrait ajouter un petit chauffe eau 10-15l
- La terre n'est présente que sur les PE. Quelles sont les bonnes pratiques à bord d'un bateau sur ce point, sachant que la coque est en plastique est qu'elle ne conduit pas l'electricité?
  - Réponse et pistes : étude A (sécurisation), section « Terre 230 V ». Points à relever : Q31.

## Equipements

### Moteur
Moteur Yanmar 3GMD, d'après la plaque signalétique (d'abord noté 3GM30). Refroidissement direct à l'eau de mer.
Alternateur d'environ 20 A (spécification d'origine ; celui de Juju semble plus récent mais semblable, plaque à relever : Q14).
Démarreur : 60 A à vide, 460 A rotor bloqué (couple maximal, vitesse nulle), puissance maximale entre 200 et 275 A ([manuel d'atelier Yanmar](documentation/YANMAR-WORKSHOP-MANUAL-1GM-2GM-3GM-3HM.pdf)).
Batterie Varta 110Ah au Plomb sans entretien
Coupe circuit dédié sur pole 12v

### Equipements de servitudes

- Batterie 12v 110Ah au Plomb sans entretien
- 6 points lumineux (LED) 12v
- Panneau de controle des equipements de bord (coté moteur) :
  - Interrupteur réfrigérateur + fusible 15A
  - Interrupteur Pompe de cale moteur + fusible 10A (Attwood Tsunami T500, sans flotteur, mise en route manuelle ; le fabricant demande un fusible de 3 A : anomalie A10)
  - Alimenté par les coupe-circuits voisins en 6 mm² ; départ frigo et retour de l'EPS 100 (sur la barrette de masse du tableau) en 3,5 mm²
- Panneau de controle des equipements de bord (coté table à carte) :
  - 12 Interrupteurs + 12 fusibles de différents calibres
    - feu route fusible 10A (feux de navigation à incandescence)
    - feu moteur fusible 10A
    - pompe à eau potable fusible 15A
    - radio fusible 10A
    - prises 12v fusible 10A
    - éclairage 12v fusible 10A
    - projecteur fusible 10A (incandescent)
    - mouillage fusible 10A (feu à LED)
    - compas fusible 5A
    - pilote fusible 10A (Raymarine ST2000+, barre franche)
    - VHF fusible 10A
    - GPS Loch fusible 10A
  - Pompe à eau
  - Pompe de cale
  - sondeur
  - GPS Garmin Map 7407 xsv ou xdv
  - Répéteur GPS MLR fx312 : unité principale à la table à carte, écran déporté au-dessus de la descente, côté cockpit
  - 2 x prises 12v allume cigare
  - VHF Standar horizon Matrix GX 2200 AIS
  - autoradio
  - Radar
  - Anémomètre / girouette Advensea
  - Loch

### Guindeau

Lewmar Pro-Series 1000 700W
Relai de commande à proximité du guindeau
Disjoncteur thermique de 70 A, proche du sectionneur, conforme à la notice.
Notice Lewmar (tableau 7.5, [documentation](documentation/OSCULATI-Notice-LEWMAR-Guindeau-Pro-Série.pdf)) : courant normal 50 A.
Cablage en 50mm2
Télécommande alimentée par le + d'entrée du relais, à travers un fusible de 5 A

### Refrigerateur

WAECO ColdMachine CU-55 12/24V 40W
Dometic EPS 100 pour permettre un fonctionnement en 12/220v. Bornes pour cosses à fourche SV 2-4 (1,5 à 2,5 mm²).
Liaison EPS 100 → groupe froid : 3,5 mm², environ 3 m.

### Pompe à eau

Seaflow SFDP1-045-040-... 12v, 6-15A

### Coupleur

Scheiber 38.14700.00

### Chargeur de quai

Dolphin 12v 20A
Alimenté en 230 V par un boîtier de distribution voisin (différentiel 30 mA / 25 A, disjoncteur 10 A dédié au chargeur), lui-même alimenté par la prise de quai EU placée sous le banc tribord du cockpit. Schéma : [folio 3](../schemas/folio-3-230v.svg).

### Coupes circuits 12v

Les 4 coupes circuits sont disposés en carré, à chaque coin
- 1 coupe circuit sur pole + batterie moteur en haut à droite
- 1 coupe circuit sur pole + batterie servitude en bas à droite
- 1 coupe circuit sur pole - des 2 batteries en haut à gauche
- 1 coupe circuit de couplage des 2 batteries en bas à gauche (couple la batterie de servitude à l'alternateur/démarreur du moteur).

### Distribution 230v

3 boitiers électriques : 
- Boitier d'arrivée dans le coffre cockpit tribord avec dicjoncteur différentiel 30mA/25A protégeant tout le circuit + 1 disjoncteur 10A pour le chargeur de quai, et 1 disjonteur 16A pour le reste.
- Boîtier de distribution tribord, dans le cabinet de toilette, avec 4 disjoncteurs Legrand DNX3 : deux 10A (dont l'éclairage) et deux 16A (PE, un par bord) ; le circuit du second 10A est à identifier (Q42). Correction du 01/10, photo Boitier-230v-cabinet-toilette.jpg.
- Boîte de dérivation bâbord, sans disjoncteur, à l'arrière gauche de la table à carte : les PE bâbord ne sont protégées que par le 16A du boîtier d'arrivée.
- Une PE pour alimentation groupe froid Dometic EPS 100 sur boitier tribord
- Une PE pour la cuisine sur boitier tribord
- Un plafonnier d'éclairage sur boitier tribord
- Une PE pour la table à carte sur la boîte de dérivation bâbord
- Une PE pour le carré sur la boîte de dérivation bâbord
- Boîtier tribord dans le cabinet de toilette (correction du 01/10 : il était noté sur la cloison entre le cabinet de toilette et le coffre de cockpit).
- La terre 230 V n'est reliée ni à la masse 12 V ni à un isolateur galvanique (anomalie A8).
- Au ponton de Saint-Chamas, la prise de quai ne fournit que **6 A, soit environ 1 400 W** pour tout le bord (12 A à quai).
- Prises en 3 × 2,5 mm², éclairage en 3 × 1,5 mm², arrivée et chargeur en 3 × 2,5 mm².
- Schéma : [folio 3](../schemas/folio-3-230v.svg), d'après la description ci-dessus et le [plan manuscrit](photos/Circuit-electrique-230v.jpeg).

## Implantation

Les zones de l'aménagement sont décrites dans [amenagement.yaml](amenagement.yaml), et la position de chaque équipement dans [equipements.yaml](equipements.yaml) (champs `zone` et `emplacement`).

- **Batterie moteur** : coffre de cockpit tribord, contre la paroi du cabinet de toilette.
- **Chargeur de quai** : au-dessus de la batterie moteur, avec son boîtier 230 V à côté. La prise de quai est sous le banc tribord du cockpit.
- **Batterie de servitude** : cabine de poupe bâbord, dans un coffre, au sol, contre le coffre moteur.
- **Coupe-circuits** : sur une contremarche de l'escalier de descente. Le coupleur est derrière. On accède au coupleur et à la connectique des coupe-circuits par une ouverture qui donne sur la cabine de poupe.
- **Tableau Scheiber 2 voies** : sur une contremarche de la descente, près de l'appareillage moteur.
- **Moteur** : derrière l'escalier de descente, dans l'axe, entre le cabinet de toilette et la cabine de poupe. La pompe de cale est dans la cale moteur.
- **Disjoncteur du guindeau** : cabine de poupe, sous l'ouverture d'accès aux coupe-circuits.
- **Relais du guindeau** : dans un boîtier de type boîte de dérivation près du guindeau, accessible depuis la cabine de proue.
- **Guindeau** : à la proue, posé sur le pont au-dessus du puits de chaîne.
- **Groupe froid et EPS 100** : cuisine (tribord), entre le puits de dérive et la glacière, dans la partie droite du meuble bas sous l'évier.
- **Puits de dérive** : entre la table à carte et la cuisine. La quille est en deux parties : un aileron lesté en polyester et une dérive relevable en fonte, qui remonte dans ce puits.
- **Tableau de servitude** : table à carte (bâbord), avec la boîte de dérivation 230 V bâbord à l'arrière gauche et l'unité principale du répétiteur GPS. L'écran déporté du répétiteur est au-dessus de la descente, côté cockpit.

Plan : [folio 0](../schemas/folio-0-implantation.svg), d'après le [plan de brochure](photos/gibsea-31-drawing.jpg).

## Câblage

La netlist et la wirelist sont désormais tenues dans des fichiers structurés, contrôlés par `outils/verifier.py` :

- [equipements.yaml](equipements.yaml) : les équipements ;
- [netlist.yaml](netlist.yaml) : les nœuds (une borne d'équipement = un nœud) ;
- [wirelist.yaml](wirelist.yaml) : les fils relevés ;
- [anomalies.md](anomalies.md) : les défauts constatés (A1…) ;
- [questions.md](questions.md) : ce qu'il reste à relever à bord (Q1…).

Schémas : [folio 1](../schemas/folio-1-actuel.svg) pour le 12 V, [folio 3](../schemas/folio-3-230v.svg) pour le 230 V.

## Documentation et photos

- [documentation/](documentation/) : fiche du Gib'Sea 31, notice Lewmar du guindeau, manuel d'atelier Yanmar (1GM, 2GM, 3GM, 3HM), abaque de sections 12 V.
- [photos/](photos/) : platine des coupe-circuits, tableaux de la descente et de la table à carte, moteur, instruments, plans manuscrits 230 V et 12 V. Le plan manuscrit 12 V (`Circuit-electrique-12v-faux.jpeg`) est faux, comme son nom l'indique : il ne sert pas de source.
