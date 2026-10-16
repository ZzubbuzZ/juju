# 3.2 · Plus rien sur la servitude

*Fiche réflexe. Elle suppose les travaux terminés (installation cible).*

Tout le 12 V du bord s'éteint d'un coup ou presque : tableau de la table à carte (feux, VHF, pilote, instruments), frigo, **pompe de cale**. Le moteur et le guindeau, eux, marchent encore : ils sont sur la batterie moteur.

## Recto : retrouver le 12 V

### 1. Sécurité d'abord

- De nuit en navigation : plus de feux de navigation. Lampe de poche, feux de secours, veille renforcée.
- VHF fixe coupée : prendre la VHF portable.
- Surveiller les fonds : la pompe de cale électrique ne marche plus ; pomper à la main.
- *Matériel de secours à bord et emplacement (feux, VHF portable, pompe de cale manuelle) : Q73.*
- Pilote coupé : barrer à la main.

### 2. Les coupe-circuits (platine, contremarche de la descente)

**Négatifs** (en haut à gauche) et **servitude** (en bas à droite) sur ON ? Un coupe-circuit ouvert par mégarde suffit à tout éteindre.

### 3. Le SmartShunt répond-il ? (téléphone, VictronConnect)

| Le shunt… | Ce que cela veut dire | Suite |
|---|---|---|
| répond, servitude au-dessus de 12 V | la batterie va bien : la coupure est en aval | étape 4 |
| répond, servitude sous 11 V ou à 0 V | la batterie ne débite plus : **BMS coupé** ou **fusible MEGA fondu** | étape 5 |
| ne répond plus | le shunt est alimenté par la batterie : même diagnostic | étape 5 |

### 4. Coupure en aval de la batterie

- Seul le tableau de la table à carte est éteint : fusible de 50 A de son départ (porte-fusibles MIDI, niche derrière la platine).
- Seul le tableau Scheiber : fusible de 30 A, même endroit.
- Accès à la niche : par l'ouverture côté cabine de poupe. **Ne pas remplacer un fusible fondu sans avoir trouvé pourquoi** (fiche 3.6) ; jamais de calibre plus fort.

### 5. BMS coupé ou MEGA fondu

Ouvrir l'**application de la batterie** (Humsienk, Bluetooth, téléphone près de la cabine de poupe) :

| L'application… | Cause probable | Que faire |
|---|---|---|
| indique une protection **décharge** (sous-tension) | batterie vide | **recharger**, étape 6 |
| indique une protection **surintensité** ou **court-circuit** | un appareil ou un câble en défaut | ouvrir le coupe-circuit servitude, chercher la cause (odeur, chaleur : fiche 3.1), puis réarmer le BMS *(procédure : Q72)* |
| indique une protection **température** | batterie trop chaude ou sous 0 °C | laisser revenir à température ; aérer le coffre |
| répond, sans protection, batterie pleine | le courant ne sort pas : **fusible MEGA de 300 A** | étape 7 |
| ne répond pas | BMS éteint (batterie très vide) ou application hors de portée | se rapprocher du coffre ; sinon étape 6 |

### 6. Recharger une batterie vidée

- **Au moteur** : démarrer (fiche 2.3), allumer l'**Orion XS** (interrupteur à voyant dans la descente). Sur le shunt, le courant doit entrer dans la servitude. *Reprise de la charge par l'Orion XS sur une batterie coupée par son BMS : à vérifier (Q72).*
- **Au quai** : 230 V et C10 du Blue Smart (coffre de cockpit tribord). Le Blue Smart sait reprendre la charge d'une batterie lithium coupée par son BMS (fiche Victron).
- Ne rallumer les circuits qu'une fois la batterie au-dessus de 20 % ; d'abord feux et VHF.

### 7. Fusible MEGA de 300 A fondu

Il est vissé à côté de la batterie de servitude, dans le coffre sous la couchette de la cabine de poupe. Un MEGA de 300 A ne fond que sur un **court-circuit franc** : avant tout remplacement, ouvrir tous les coupe-circuits, chercher le câble ou l'appareil brûlé (fiche 3.1, verso), et ne remplacer le fusible qu'après réparation. *Fusible de rechange à bord : voir la fiche 4.2.*

## Verso : comprendre

- **Le BMS** est la carte électronique intégrée à la batterie. Il coupe tout, sans prévenir, si la batterie est vide, si le courant dépasse 250 A, ou si la température sort des limites. C'est une protection de la batterie, pas des câbles : le fusible MEGA reste indispensable.
- **Prévenir plutôt que subir** : l'alarme du shunt sonne sur le téléphone à 20 % de charge (fiche 2.1). À ce seuil, démarrer le moteur avec l'Orion XS, ou délester : ballon sur batterie coupé (disjoncteur de 30 A, cabine de poupe), frigo coupé (tableau Scheiber).
- **Ce qui marche encore** : le moteur, son alternateur, le guindeau (sélecteur sur 1), le Dolphin au quai. La batterie moteur ne peut pas alimenter la servitude : les deux batteries ne sont jamais reliées, volontairement.
- **Une batterie vidée jusqu'à la coupure** se recharge sans dommage si l'on ne tarde pas ; la laisser des semaines vide l'abîme.
