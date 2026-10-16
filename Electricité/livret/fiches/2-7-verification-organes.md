# 2.7 · Vérifier le fonctionnement des organes

*Tour de contrôle complet : au premier embarquement de la saison, après une intervention sur l'électricité, ou avant une navigation de plusieurs jours. Compter une heure, à deux (une personne dehors pour les feux). Elle suppose les travaux terminés (installation cible).*

Principe : **un circuit à la fois**, en regardant le courant sur le SmartShunt (téléphone, VictronConnect). Chaque appareil qui marche fait monter le courant d'une valeur à peu près constante d'une fois à l'autre : la noter dans la colonne de droite. Un écart net d'une saison à l'autre signale un appareil qui faiblit, ou une fuite.

## Recto : le tour

### 1. Au repos (fiche 2.1 faite, tout éteint)

| Organe | Où | Vérifier | Noté |
|---|---|---|---|
| Platine des coupe-circuits | contremarche de la descente | chaque coupe-circuit et le sélecteur tournent franchement, sans point dur | |
| SmartShunt | téléphone | il répond ; tension de la servitude, % de charge, tension du démarreur | ___ V · ___ % · ___ V |
| Courant de veille | téléphone | tout éteint, coupe-circuits fermés | ___ A |
| BMS de la batterie | téléphone, application Humsienk | aucune alarme ; écart entre cellules (seuils : Q68) | ___ mV |

### 2. Tableau de la table à carte, circuit par circuit

| Circuit | Vérifier | Courant noté |
|---|---|---|
| Feu route | feux bicolore (proue) et de poupe allumés, vus de dehors | ___ A |
| Feu moteur | feu de tête de mât allumé | ___ A |
| Mouillage | feu de mouillage en tête de mât | ___ A |
| Projecteur | projecteur de pont | ___ A |
| Pompe à eau | ouvrir un robinet : l'eau coule ; robinet fermé, la pompe s'arrête et ne redémarre pas seule | ___ A |
| Radio | l'autoradio s'allume et garde ses stations | ___ A |
| Prises 12 V | un chargeur de téléphone dans chacune des deux prises | ___ A |
| Éclairage | chaque luminaire, par son propre interrupteur | ___ A |
| Compas | éclairage du compas | ___ A |
| Pilote | le pilote s'allume (pas de mise en route en charge au port) | ___ A |
| VHF | s'allume ; essai radio sur un canal de travail | ___ A |
| GPS loch | traceur, répétiteur, loch, anémomètre s'allument | ___ A |

### 3. Tableau Scheiber (descente, à côté de la platine)

| Circuit | Vérifier | Courant noté |
|---|---|---|
| Frigo | le compresseur démarre (EPS 100, sous l'évier) | ___ A |
| Pompe de cale | interrupteur sur marche quelques secondes : elle tourne (pas à sec longtemps) | ___ A |

### 4. Disjoncteurs de la cabine de poupe (sous l'ouverture d'accès aux coupe-circuits)

| Organe | Vérifier | Courant noté |
|---|---|---|
| Disjoncteur du **ballon** (30 A) | fermé quelques minutes, câble de quai débranché : le ballon chauffe ; puis le rouvrir | ___ A (environ 17 A) |
| Disjoncteur du **guindeau** (70 A) | armé ; voir l'étape 5 | |

### 5. Moteur tournant (fiche 2.3)

| Organe | Vérifier | Noté |
|---|---|---|
| Alternateur | la tension du démarreur monte vers 13,8 à 14,4 V | ___ V |
| Orion XS | interrupteur sur marche, voyant allumé, courant de la servitude vers +15 A | ___ A |
| Guindeau | sélecteur sur **1**, télécommande : un bref essai de montée et de descente, chaîne au repos | |

### 6. Au quai (230 V)

| Organe | Où | Vérifier |
|---|---|---|
| Différentiel 30 mA | boîtier d'arrivée, coffre de cockpit tribord | le bouton **test** le fait déclencher ; le réarmer |
| Blue Smart | téléphone, VictronConnect | il charge ; le shunt voit le courant entrer dans la servitude (17 A au plus) |
| Dolphin | coffre de cockpit tribord | la tension du démarreur sur le shunt monte au-dessus de 13 V |
| Prises 230 V | toutes les prises du bord | un appareil s'allume dans chacune |
| Ballon sur le 230 V | prise dédiée sous la table à carte | il chauffe, disjoncteur 12 V ouvert |
| Frigo sur le 230 V | prise du frigo | l'EPS 100 passe sur le 230 V |

### 7. Pour finir

Remettre chaque organe dans sa position normale (fiche 2.1), sélecteur du guindeau sur **1**, disjoncteur du ballon ouvert hors usage, Orion XS coupé moteur arrêté.

## Verso : en cas d'anomalie

| Constat | Fiche |
|---|---|
| Un circuit du tableau ne marche pas, ou son fusible a fondu | 3.6 |
| Le guindeau ne répond pas | 3.5 |
| Le Blue Smart ou l'Orion XS ne charge pas | 3.4 |
| Le différentiel ne déclenche pas au test | ne pas rester branché au quai ; le faire remplacer (étude A, H4) |
| Le différentiel déclenche seul | 3.7 |
| Le frigo ne refroidit pas | 3.8 |
| Courant de veille plus élevé que la dernière fois | chercher en ouvrant les circuits un à un ; une fuite qui grandit peut chauffer un câble (fiche 3.1) |
| Odeur de chaud pendant un essai | couper le circuit, fiche 3.1 |

**Garder les relevés** d'une saison à l'autre, au dos de cette fiche ou dans le journal de bord : ils remplacent aussi les estimations du bilan énergétique (étude D, protocole de mesure).
