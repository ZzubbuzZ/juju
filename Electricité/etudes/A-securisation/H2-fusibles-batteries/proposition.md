# A-H2 · Fusibles de batterie

Hypothèse de l'étude A. Base : le relevé, ou A-H1 si elle est retenue. Anomalies traitées : **A2** (aucun fusible en sortie des batteries), **A4** (fils du coupleur et du chargeur sans fusible), et depuis le 01/10 **A1** et **A6** (câbles des tableaux de la table à carte et Scheiber sans fusible).

- Données : [cablage.yaml](cablage.yaml) (base : le relevé).
- Schéma : [folio 2c](folio-2c-fusibles.svg).
- Nomenclature : [nomenclature.yaml](nomenclature.yaml).

Les câbles existants gardent leur numéro : seule leur extrémité côté source est reprise sur le porte-fusible.

## Décision du 30/09

- **Option A, avec un calibre de 400 A** sur les deux batteries (au lieu des 300 A étudiés d'abord) : même fusible des deux côtés, démarrage de secours couplé possible. **wire006 est conservé en 35 mm²** (décision du 30/09), comme wire001 : voir l'écart accepté plus bas.
- **Départs** : 30 A pour le chargeur, **40 A pour le coupleur**, dont le relais est donné pour 40 A.
- **Tableau de la table à carte (A1)** : fusible de 50 A à la source de wire019, repris de A-H1 le 01/10 (voir plus bas).
- **Tableau Scheiber (A6)** : fusible de 30 A à la source de wire022, ajouté le 01/10 (voir plus bas).

Le choix de 400 A et ses conséquences sont détaillés dans [Calibre retenu : 400 A](#calibre-retenu--400-a).

## Principe

Un fusible protège le câble qui part de lui, et se place à sa source. Aujourd'hui, un court-circuit sur n'importe quel câble branché sur une batterie n'est coupé par rien.

### Ce que dit le démarreur

D'après le manuel d'atelier Yanmar : **60 A à vide, 200 à 275 A en démarrage normal** (zone de puissance maximale), et **460 A rotor bloqué**, pendant une fraction de seconde au lancement. Un fusible supporte largement plus que son calibre pendant quelques secondes. Un calibre de 300 A laisse donc passer un démarrage, y compris la pointe à 460 A, mais fond en quelques millisecondes sur un court-circuit franc, qui fait plusieurs milliers d'ampères. La courbe temps-courant du fusible choisi est à vérifier au moment de l'achat.

### Batterie moteur

Les normes nautiques dispensent le circuit du démarreur de fusible. Mais wire001 fait 2 m, et s'il frotte contre une masse, rien ne coupe. **Fusible sur la borne +**, de 300 A dans l'étude initiale, **400 A retenus** (voir plus bas). Il ne gêne pas le démarrage et coupe un court-circuit franc.

C'est d'ailleurs la pratique de l'automobile récente : sur un Ford Transit Custom, le démarreur et l'alternateur sont raccordés à la batterie à travers un fusible de 470 A, pour un démarreur de diesel plus puissant que celui du 3GMD. À bord, l'alternateur est lui aussi derrière ce fusible, puisqu'il charge la batterie moteur par le même câble que le démarreur (node031) : ses 20 A environ ne sollicitent pas un calibre de 300 A.

### Batterie de servitude

En temps normal, le circuit de servitude tire au plus 160 A environ : guindeau (50 A en courant normal), tableau de la table à carte (50 A), tableau Scheiber (30 A), pompe de cale. Mais il y a le **démarrage de secours** : on ferme le coupe-circuit de couplage parce que la batterie moteur est à plat, et c'est alors la batterie de servitude qui fournit seule les 200 à 275 A du démarreur, à travers son fusible.

| | Option A (retenue le 30/09) | Option B |
|---|---|---|
| Fusible de la batterie de servitude | 300 A étudiés, 400 A retenus | 200 A |
| Démarrage de secours couplé | possible | le fusible risque de fondre |
| wire006 (batterie → coupe-circuit, 1 m) | 50 mm² proposés pour que le câble tienne le calibre du fusible ; **conservé en 35 mm²** (30/09) | conservé en 35 mm² |
| Coût supplémentaire | 0 € depuis la décision du 30/09 (30 € avec wire006 en 50 mm²) | 0 € |

Un fusible doit rester adapté à la tenue du câble qu'il protège. Avec 300 A, le 35 mm² actuel est trop juste, d'où son remplacement dans l'option A ; il ne fait qu'un mètre. Les valeurs de tenue sont à confirmer dans les tables de la norme ISO 13297:2020 (qui a remplacé l'ISO 10133 pour le courant continu) au moment de l'achat. Avec l'option A, les deux batteries ont le même fusible : une seule référence de rechange à bord.

### Calibre retenu : 400 A

**Au démarrage**, un fusible de 300 A ne fondrait pas : la pointe de 460 A ne dure qu'une fraction de seconde, bien moins que ce qu'un fusible de ce calibre supporte à 150 % de son courant, et le lancement à 200-275 A reste sous le calibre. 400 A donnent une marge supplémentaire, pour des démarrages longs ou répétés par temps froid.

**Ce que 400 A changent** :

- **Type de fusible** : la gamme MRBF, qui se fixe directement sur la borne, s'arrête à 300 A. À 400 A, il faut un fusible MEGA (ou ANL) dans un porte-fusible vissé à côté de la batterie, relié à la borne par un câble aussi court que possible (une vingtaine de centimètres au plus) : ce tronçon n'est protégé par rien.
- **Tenue des câbles** : la règle usuelle limite le fusible à environ 150 % de la tenue du câble (ABYC E-11, à vérifier sur le texte). **wire001 et wire006 (35 mm², un par batterie) la dépassent** : un 35 mm² supporte environ 210 A en continu, soit un fusible de 300 A au plus. 400 A coupent un court-circuit franc, de plusieurs milliers d'ampères, en quelques millisecondes, mais un court-circuit partiel de 300 à 400 A chaufferait le câble sans faire fondre le fusible. **Écart accepté le 30/09** pour les deux câbles : la chute de tension est négligeable sur ces longueurs, et le courant de service reste loin de 400 A. Pour le supprimer, il faudrait les refaire en 50 mm². En compensation : protéger soigneusement leurs passages de cloison (A-H5), les fixer pour qu'ils ne frottent nulle part, et vérifier que leurs cosses ne chauffent pas après un démarrage de secours couplé.
- **Détection du court-circuit résistif** : un défaut de ce type ne se déclare pas d'un coup ; il commence par une fuite de courant, qui grandit avec l'usure. Il doit être repéré avant de devenir dangereux par l'**historique des consommations** : un courant débité alors que tout est éteint, ou une consommation qui dérive sans raison. C'est le rôle du moniteur de batterie de l'étude D (shunt), pour la batterie de servitude.
- **Correction à long terme : wire006 en 50 mm²**, peu prioritaire mais à ne pas oublier. Le risque de court-circuit partiel croît avec l'usure de l'installation (isolants, cosses, passages de cloison) : ce qui est acceptable sur une installation remise en état l'est de moins en moins avec les années. Lot « long terme » de la nomenclature, environ 30 €.
- **Abaque de chute de tension** ([documentation](../../../releve/documentation/tabla-calcular-seccion-cable-12V.png)) : il donne 1,25 m pour 35 mm² sous 400 A. C'est la longueur qui garde la chute de tension sous 0,5 V, aller et retour compris ; ses cases « NA » signalent une longueur inférieure à 1 m, pas une limite d'échauffement. Il ne dit donc rien de la tenue thermique, qui est la limite déterminante sur un câble court.
- **Batterie lithium** : si la batterie de servitude passe un jour en LiFePO4, son courant de court-circuit dépasse le pouvoir de coupure d'un MEGA ou d'un ANL. Il faudra alors un **fusible de classe T** de 400 A, qui existe à ce calibre.
- **Disjoncteur 12 V à la place du fusible** : il en existe de ce calibre, réarmables et utilisables comme interrupteur, mais plus chers et plus encombrants, avec la même logique de courbe. Pas d'intérêt ici, les coupe-circuits jouant déjà le rôle d'interrupteur.

### Départs du coupleur et du chargeur (A4)

Quatre fils de 6 mm² partent directement des bornes côté batterie des coupe-circuits (node003 et node009) :

| Fil | Départ | Fusible proposé | Pourquoi |
|---|---|---|---|
| wire003 | chargeur, sortie batterie moteur | 30 A | le chargeur débite 20 A au plus |
| wire008 | chargeur, sortie batterie servitude | 30 A | idem |
| wire002 | coupleur, côté batterie moteur | 40 A | le relais du coupleur est donné pour 40 A. Il transmet le courant de l'alternateur (environ 20 A), mais, à sa fermeture, deux batteries très inégales peuvent échanger davantage : le fusible protège alors le câble et le relais |
| wire007 | coupleur, côté batterie servitude | 40 A | idem |

Les porte-fusibles se fixent près de la platine des coupe-circuits, dans la zone accessible par l'ouverture côté cabine de poupe.

#### Le fusible de 25 A de la notice du chargeur

La notice du Dolphin indique un « fusible de sortie F25A » : c'est le fusible **interne** du chargeur, côté batteries (rapide, 32 V), à remplacer à l'identique. Il protège le chargeur, notamment en cas d'inversion de polarité, mais pas les câbles : un court-circuit sur wire003 ou wire008 est alimenté par la batterie, de l'autre côté, et ce fusible interne ne le voit pas. D'où le fusible externe, à la batterie.

Son calibre doit rester au-dessus du courant du chargeur (20 A ± 5 %, pendant des heures) et en dessous de la tenue du 6 mm². **30 A** laisse une marge pour un fusible qui travaille en continu dans un coffre chaud ; 25 A conviendrait aussi, mais tournerait à plus de 80 % de son calibre en début de charge.

La notice préconise aussi des câbles batterie de 6 mm² sur **1,5 m au plus**. wire003 et wire008 font 2 m : la chute de tension, un peu plus forte que prévu, abaisse légèrement la tension de charge. Ce n'est pas un problème de sécurité ; à reprendre si ces fils sont refaits pour la pose des porte-fusibles.

### Tableau de la table à carte (A1)

wire019 (6 mm², 3 m) part de la sortie du coupe-circuit de servitude (node010, relevé corrigé le 01/10) sans aucune protection. Un **fusible MIDI de 50 A** se place à sa source, près de la platine des coupe-circuits, avec les fusibles des départs : un tronçon court (wire166) va de node010 au porte-fusible, et wire019 est repris sur sa sortie. 50 A reste dans la tenue du 6 mm² et laisse passer la consommation du tableau (Q12 pour les longueurs exactes). C'est la seule partie de A-H1 retenue le 30/09.

### Tableau Scheiber (A6)

wire022 (6 mm²) part lui aussi de node010, sans fusible, vers le tableau Scheiber 2 voies (frigo 15 A, pompe de cale). Même traitement que wire019 : un **fusible MIDI de 30 A** à côté du premier, près de la platine ; un tronçon court (wire167) va de node010 au porte-fusible, et wire022 est repris sur sa sortie. 30 A couvre les deux voies du tableau et reste dans la tenue du 6 mm². C'était le lot « distribution » de A-H1 ; la barrette de A-H1 reste différée.

### Numéros

| Fusible | Calibre | Tronçon court (nouveau) | Câble existant repris |
|---|---|---|---|
| batterie moteur | 400 A | wire160 (35 mm²) | wire001 |
| batterie de servitude | 400 A | wire161 (35 mm²) | wire006 |
| chargeur, sortie moteur | 30 A | wire162 (6 mm²) | wire003 |
| chargeur, sortie servitude | 30 A | wire163 (6 mm²) | wire008 |
| coupleur, côté moteur | 40 A | wire164 (6 mm²) | wire002 |
| coupleur, côté servitude | 40 A | wire165 (6 mm²) | wire007 |
| tableau de la table à carte | 50 A | wire166 (6 mm²) | wire019 |
| tableau Scheiber | 30 A | wire167 (6 mm²) | wire022 |

## Questions liées

Aucune : le calibre du coupleur (40 A) et le choix de l'option A sont tranchés depuis le 30/09.
