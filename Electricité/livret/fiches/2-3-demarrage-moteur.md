# 2.3 · Démarrer le moteur, partir au moteur

*Fiche de fonctionnement normal, avec au verso la conduite si la batterie moteur est faible. Elle suppose les travaux terminés (installation cible).*

Le moteur démarre sur sa propre batterie, au plomb, dans le coffre de cockpit tribord. La batterie de servitude (LiFePO4) ne peut pas le démarrer : les deux batteries ne sont jamais reliées.

## Recto : démarrer

### 1. Avant de lancer

- **Vannes d'eau de mer et de gasoil ouvertes** *(emplacements : Q70)*.
- Platine des coupe-circuits (contremarche de la descente) : **négatifs** (en haut à gauche) et **moteur** (en haut à droite) sur ON.
- **Étouffoir** poussé à fond : tirette marquée d'un **S rouge**.
- Téléphone, VictronConnect, SmartShunt : **tension du démarreur** (« Starter ») 12,2 V au moins. En dessous, passer directement au verso.
- **Orion XS coupé** : interrupteur à voyant dans la descente, près du tableau Scheiber, voyant éteint.

### 2. Lancer

Au **tableau moteur**, sur la contremarche de la descente, à gauche de la platine des coupe-circuits :

1. Insérer la clé dans le commutateur et la tourner dans le **sens horaire** jusqu'à entendre le **buzzer**.
2. Enfoncer le **poussoir de démarrage** jusqu'à ce que le moteur parte, **moins de 10 secondes**.

- S'il ne part pas, attendre 30 secondes avant de recommencer.
- Après trois essais sans succès, ne pas insister : batterie qui s'épuise, démarreur qui chauffe. Voir le verso.
- *Manette des gaz au lancement, buzzer et voyants une fois le moteur parti : Q70.*

### 3. Moteur tourné

- **Charge de l'alternateur** : la tension du démarreur sur le shunt monte vers 13,8 à 14,4 V dans la minute. Si elle reste vers 12,5 V, l'alternateur ne charge pas (courroie, câblage) : la batterie moteur se vide en route.
- **Orion XS** : interrupteur à voyant sur marche, voyant allumé. Sur le shunt, le courant de la servitude devient positif, environ **+15 A**, moins la consommation du bord.
- **Feux de navigation** au tableau de la table à carte, si besoin : « feu moteur » (tête de mât) en plus des feux de route.

### 4. Arrêter

- **Orion XS d'abord** : interrupteur sur arrêt.
- Puis arrêter le moteur *(étouffoir, clé : procédure à confirmer, Q70)*.
- Le coupe-circuit moteur ne s'ouvre **jamais moteur tournant** : cela abîme l'alternateur. Au port, on l'ouvre après l'arrêt du moteur.

## Verso : batterie moteur faible

### Les signes

Démarreur qui tourne lentement, claquements du relais sans rotation, voyants du tableau moteur qui faiblissent au lancement ; sur le shunt, tension du démarreur sous 12,2 V au repos, ou qui tombe sous 10 V au lancement.

### Niveau 1 : recharge de secours depuis la batterie de servitude (sans matériel)

L'Orion XS sait faire passer le courant **à l'envers**, de la LiFePO4 vers la batterie moteur.

1. Coupe-circuit **moteur** et **négatifs** sur ON, moteur arrêté. L'interrupteur de l'Orion XS peut rester coupé : la recharge de secours marche aussi quand il est désactivé à distance.
2. Vérifier sur le shunt que la servitude a de la réserve (plus de 30 %), et couper ce qui consomme sur la servitude (frigo, chauffe-eau, prises 12 V) : l'Orion XS ne descend pas la servitude sous 12 V et réduit le courant en approchant de ce seuil.
3. Ouvrir **VictronConnect** et se connecter à l'**Orion XS**. Sur l'écran **État**, toucher l'**icône du moteur**, en haut à gauche.
4. La fenêtre « Démarrer la charge inverse d'urgence » indique la tension visée (14,4 V au plus) et le courant (25 A au plus). Cocher **« J'ai compris cette fonctionnalité »**, puis **DÉMARRER**.
5. L'application affiche « Charge inverse d'urgence » et le temps restant : **15 minutes**, environ 6 Ah. Le courant s'affiche en négatif, c'est normal. Inutile de rester connecté.
6. Au bout des 15 minutes, l'application affiche **« Batterie prête »** pendant **5 minutes** : **démarrer à ce moment-là** (recto, étape 2). Ensuite, l'Orion XS reprend son fonctionnement normal.

Si l'icône du moteur est grisée : l'Orion XS est en train de charger (le laisser constater que le moteur est arrêté, ou mettre son interrupteur sur arrêt) ou il est réglé en mode alimentation au lieu du mode chargeur. Si elle n'apparaît pas : le micrologiciel de l'Orion XS (v1.15 au moins) ou VictronConnect (v6.43 au moins) est à mettre à jour, à faire au port, pas en mer sans réseau.

Cela suffit pour une batterie **déchargée** (feux oubliés, longue absence, guindeau utilisé moteur arrêté). Une batterie **défectueuse** (élément en court-circuit, batterie chaude, tension qui s'effondre aussitôt) ne reprendra pas : passer au niveau 2.

### Niveau 2 : booster de démarrage

**Pas de booster à bord pour l'instant (17/10).** S'il est acheté : booster lithium autonome, rangé à bord et tenu chargé ; noter ici son emplacement et sa recharge.

- **Batterie déchargée** : coupe-circuit moteur sur ON ; pince rouge sur la borne + de la batterie moteur (coffre de cockpit tribord), pince noire sur sa borne −, ou suivre la notice du booster. Démarrer, puis retirer les pinces, noire d'abord. L'alternateur recharge ensuite la batterie.
- **Batterie défectueuse** : la procédure prévue au 13/10 (coupe-circuit moteur ouvert, pinces côté charges du coupe-circuit moteur et sur la masse moteur) fait tourner l'alternateur sans batterie dès que l'on retire le booster, ce qui peut l'abîmer. *Procédure à arrêter avant de l'écrire ici (voir plan, points à trancher).*

### Le guindeau si la batterie moteur est hors service

Le guindeau tire sur la batterie moteur (sélecteur sur **1**). Batterie moteur hors service : guindeau **à l'arrêt**, coupe-circuit moteur sur OFF, puis sélecteur du guindeau (platine, en bas à gauche) sur **2** : le guindeau tire alors sur la batterie de servitude. Revenir sur **1** dès que possible. Ne jamais tourner le sélecteur pendant que le guindeau tourne.

### Pourquoi l'Orion XS reste coupé moteur arrêté

Il tire son courant de la batterie moteur. Allumé au port, il continuerait de charger la servitude sur le Dolphin, qui maintiendrait alors la batterie moteur en charge forte pendant des heures, ou, sans chargeur, tirerait sur la batterie moteur jusqu'à son seuil de coupure.
