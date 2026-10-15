# 3.1 · Odeur de brûlé, fumée

*Fiche réflexe. La lire en entier une fois, au calme. En situation, suivre le recto dans l'ordre, sans sauter d'étape.*

Une odeur de plastique chaud ou de vernis, une fumée, un câble ou un appareil brûlant au toucher : **on coupe d'abord, on cherche ensuite.**

## Recto : couper

### 1. Des flammes ?

- Faire monter tout l'équipage sur le pont, gilets de sauvetage.
- Extincteur : *emplacements à relever (Q66)*. Viser la base des flammes. **Pas d'eau** sur un tableau ou un appareil électrique.
- Feu non maîtrisé en une minute : **MAYDAY** à la VHF, canal 16, ou **196** (CROSS) depuis un téléphone. Fermer la descente pour étouffer le feu, ne plus l'ouvrir.
- Ne faire les étapes 2 à 5 que si on peut atteindre les organes sans danger.

### 2. Arrêter le moteur

Clé du tableau moteur sur arrêt. *Le coupe-circuit moteur ne s'ouvre pas moteur tournant : cela abîme l'alternateur.*

### 3. Couper le 230 V

- Au quai : débrancher le câble **côté borne du ponton**.
- Sinon : ouvrir le **différentiel 30 mA**, dans le boîtier d'arrivée 230 V (coffre de cockpit tribord).

Cela coupe les deux chargeurs de quai, le ballon, les prises, l'éclairage 230 V et le frigo s'il est sur sa prise.

### 4. Arrêter l'Orion XS

**Interrupteur à voyant de l'Orion XS**, dans la descente, près du tableau Scheiber : voyant éteint. La batterie moteur ne recharge plus la batterie de servitude.

### 5. Ouvrir la platine des coupe-circuits

Platine sur la contremarche de la descente :

| Organe | Position sur la platine | Mettre sur |
|---|---|---|
| Coupe-circuit **servitude** | en bas à droite | OFF |
| Coupe-circuit **moteur** | en haut à droite | OFF |
| Coupe-circuit des **négatifs** | en haut à gauche | OFF |
| Sélecteur du **guindeau** (1 / OFF / 2) | en bas à gauche | OFF |

Cela coupe tout le 12 V du bord : tableau de la table à carte, tableau Scheiber (frigo, **pompe de cale**), ballon sur batterie, guindeau, démarreur. Surveiller les fonds : la pompe de cale électrique ne marche plus.

## Verso : comprendre et chercher

### Ce qui reste sous tension après l'étape 5

Les coupe-circuits isolent les circuits du bord, **pas les batteries ni leurs chargeurs**. Restent alimentés en permanence :

| Depuis | Par | Jusqu'à |
|---|---|---|
| Batterie de servitude (coffre sous la couchette de la cabine de poupe) | fusible MEGA de 300 A, câble de 35 mm² (wire009, wire008) | borne côté batterie du coupe-circuit servitude, puis dans la niche derrière la platine : shunt (fusible de 1 A), **sortie de l'Orion XS** (fusible de 70 A), **câble du Blue Smart** jusqu'au coffre de cockpit (fusible de 25 A, 10 mm², environ 5 m) |
| Batterie moteur (coffre de cockpit tribord) | fusible MEGA de 400 A, câble de 35 mm² (wire002, wire001) | borne côté batterie du coupe-circuit moteur ; entrée auxiliaire du shunt (fusible de 1 A) ; sortie du chargeur Dolphin (fusible de 30 A) |

Les négatifs des deux batteries, de l'Orion XS et du Blue Smart arrivent sur la borne côté batteries du coupe-circuit des négatifs : l'ouvrir ne les isole pas.

**Si la fumée vient de ces parties** (niche derrière la platine, coffre d'une batterie, coffre de cockpit, câbles de 35 mm²), la seule coupure est le **fusible MEGA de la batterie concernée**, vissé à côté d'elle. Le retirer seulement après les étapes 2 à 5 (plus aucun courant ne le traverse), avec des gants et un outil isolé, et seulement si on l'atteint sans danger. *Pour la batterie de servitude, l'application de la batterie permet peut-être de couper son BMS à distance (Q67).*

### Où chercher

Suivre l'odeur, puis toucher du dos de la main les appareils et les câbles, sans saisir.

| Endroit | Ce qui peut chauffer |
|---|---|
| Descente, niche derrière la platine (accès par l'ouverture côté cabine de poupe) | Orion XS, shunt, porte-fusibles MIDI, bornes des coupe-circuits |
| Cabine de poupe | batterie de servitude et son fusible MEGA (coffre sous la couchette) ; disjoncteurs du guindeau (70 A) et du ballon (30 A), sous l'ouverture d'accès aux coupe-circuits |
| Coffre de cockpit tribord | batterie moteur, chargeurs Dolphin et Blue Smart, boîtier d'arrivée 230 V, prise de quai |
| Compartiment moteur | démarreur, alternateur, faisceau du tableau moteur |
| Table à carte | tableau de servitude, ballon (12 V et 230 V), prise du ballon |
| Cuisine, meuble sous l'évier | EPS 100 et groupe froid du frigo |
| Cabinet de toilette | boîtier de distribution 230 V |
| Cabine de proue | boîtier relais du guindeau |

### Avant de remettre sous tension

- Trouver la cause. Un câble noirci, une gaine fondue ou une cosse bleuie se **remplace** ; changer le fusible ne suffit pas.
- Ne jamais remplacer un fusible par un calibre plus fort.
- Remettre un organe à la fois, dans l'ordre inverse : coupe-circuit des négatifs, coupe-circuit servitude, coupe-circuit moteur, sélecteur du guindeau sur 1, Orion XS, puis le 230 V. Rester devant quelques minutes à chaque étape, nez et main aux aguets.
- Un circuit en défaut reste coupé jusqu'à la réparation (fiche 3.6 pour les fusibles du tableau).
