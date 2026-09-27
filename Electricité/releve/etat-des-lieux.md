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

## Equipements

### Moteur
Moteur Yanmar 3GM30
Batterie Varta 110Ah au Plomb sans entretien
Coupe circuit dédié sur pole 12v

### Equipements de servitudes

- Batterie 12v 110Ah au Plomb sans entretien
- Lampes 12v x 5 ou 6
- Panneau de controle des equipements de bord (coté moteur) :
  - Interrupteur réfrigérateur + fusible 15A
  - Interrupteur Pompe de cale moteur + fusible 10A
- Panneau de controle des equipements de bord (coté table à carte) :
  - 12 Interrupteurs + 12 fusibles de différents calibres
    - feu route fusible 10A
    - feu moteur fusible 10A
    - pompe à eau potable fusible 15A
    - radio fusible 10A
    - prises 12v fusible 10A
    - éclairage 12v fusible 10A
    - projecteur fusible 10A
    - mouillage fusible 10A
    - compas fusible 5A
    - pilote fusible 10A
    - VHF fusible 10A
    - GPS Loch fusible 10A
  - Pompe à eau
  - Pompe de cale
  - sondeur
  - GPS Garmin Map 7407 xsv ou xdv
  - Répéteur GPS MLR fx312 dans le cockpit
  - 2 x prises 12v allume cigare
  - VHF Standar horizon Matrix GX 2200 AIS
  - autoradio
  - Radar
  - Anémomètre / girouette Advensea
  - Loch

### Guindeau

Lewmar Pro-Series 1000 700W
Relai de commande à proximité du guindeau
Disjoncteur thermique proche du sectionneur
Cablage en 50mm2
Telecommande

### Refrigerateur

WAECO ColdMachine CU-55 12/24V 40W
Dometic EPS 100 pour permettre un fonctionnement en 12/220v

### Pompe à eau

Seaflow SFDP1-045-040-... 12v, 6-15A

### Coupleur

Scheiber 38.14700.00

### Chargeur de quai

Dolphin 12v 20A

### Coupes circuits 12v

Les 4 coupes circuits sont disposés en carré, à chaque coin
- 1 coupe circuit sur pole + batterie moteur en haut à droite
- 1 coupe circuit sur pole + batterie servitude en bas à droite
- 1 coupe circuit sur pole - des 2 batteries en haut à gauche
- 1 coupe circuit de couplage des 2 batteries en bas à gauche (couple la batterie de servitude à l'alternateur/démarreur du moteur).

### Distribution 220v

- 2 boitiers électriques (un par bord) avec différentiel et 2 discjonteurs (1 pour PE, l'autre pour le reste)
- Une PE pour alimentation groupe froid Dometic EPS 100
- 4 autres PE
- 6 points lumineux (LED)

## Câblage

La netlist et la wirelist sont désormais tenues dans des fichiers structurés, contrôlés par `outils/verifier.py` :

- [equipements.yaml](equipements.yaml) : les équipements ;
- [netlist.yaml](netlist.yaml) : les nœuds (une borne d'équipement = un nœud) ;
- [wirelist.yaml](wirelist.yaml) : les fils relevés ;
- [anomalies.md](anomalies.md) : les défauts constatés (A1…) ;
- [questions.md](questions.md) : ce qu'il reste à relever à bord (Q1…).

Le schéma correspondant est [le folio 1](../schemas/folio-1-actuel.svg).
