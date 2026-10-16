# 2.1 · Mise sous tension, à l'arrivée à bord

*Fiche de fonctionnement normal. Elle suppose les travaux terminés (installation cible).*

En arrivant, on met le bord sous tension dans un ordre fixe, puis on lit l'état des deux batteries avant de consommer.

## Recto : dans l'ordre

### 1. Avant de toucher à quoi que ce soit

- Ouvrir la descente, **sentir** : une odeur de brûlé ou de plastique chaud, c'est la fiche **3.1**.
- Jeter un œil dans les fonds : de l'eau au-dessus du plancher, c'est la fiche **3.10**.

### 2. Platine des coupe-circuits (contremarche de la descente)

Tourner les coupe-circuits **dans cet ordre**, un par un :

| Ordre | Organe | Position sur la platine | Mettre sur |
|---|---|---|---|
| 1 | Coupe-circuit des **négatifs** | en haut à gauche | ON |
| 2 | Coupe-circuit **servitude** | en bas à droite | ON |
| 3 | Coupe-circuit **moteur** | en haut à droite | ON |
| 4 | Sélecteur du **guindeau** | en bas à gauche | **1** (batterie moteur) |

La position **2** du sélecteur est un secours (batterie moteur hors service) : voir la fiche 2.3, verso.

### 3. Lire l'état des batteries (téléphone, application VictronConnect, SmartShunt)

| Lecture | Attendu | Sinon |
|---|---|---|
| État de charge de la servitude (%) | plus de 50 % pour partir la journée | moins de 20 % : recharger d'abord (quai ou moteur) |
| Tension de la servitude | 13,0 à 13,4 V au repos | moins de 12,4 V : batterie presque vide (fiche 3.2) |
| Tension du démarreur (« Starter ») | 12,4 V ou plus, moteur arrêté | moins de 12,2 V : batterie moteur faible (fiche 2.3, verso) |
| Courant, tout éteint | quelques dixièmes d'ampère au plus | noter la valeur : une hausse d'une visite à l'autre signale une fuite |

Le pourcentage affiché n'est juste que si le shunt s'est recalé à 100 % lors de la dernière charge complète (voir 2.5).

### 4. Au quai : le 230 V

- Brancher le câble de quai **côté bateau d'abord** (prise de quai sous le banc tribord du cockpit), **puis côté borne** du ponton.
- Boîtier d'arrivée 230 V (coffre de cockpit tribord) : **différentiel 30 mA** sur ON, puis les deux **C10** des chargeurs (Dolphin, Blue Smart).
- Boîtier de distribution du cabinet de toilette : disjoncteurs des prises, de l'éclairage et du ballon selon les besoins.
- Vérifier dans VictronConnect que le Blue Smart charge (courant positif sur le shunt).

### 5. Mettre en service ce dont on a besoin

- **Tableau de la table à carte** : un interrupteur par circuit (feux, pompe à eau, éclairage, instruments…).
- **Tableau Scheiber** (descente, à côté de la platine) : frigo ; pompe de cale seulement au besoin (mise en route manuelle).
- L'**Orion XS** reste coupé tant que le moteur ne tourne pas (fiche 2.3).

## Verso : pourquoi cet ordre

- **Les négatifs d'abord** : les autres coupe-circuits n'alimentent rien tant que le retour n'est pas fermé, et l'on ne coupe ni ne rétablit un courant franc sur un coupe-circuit +.
- **Ce que les coupe-circuits ne coupent pas** : le SmartShunt, la sortie de l'Orion XS et le Blue Smart sont branchés du côté batterie (voir fiche 3.1, verso). Le shunt mesure donc même tout coupé : sa lecture est valable dès l'arrivée.
- **Pas de position commune** sur le sélecteur du guindeau : les deux batteries ne sont jamais reliées. Le tourner **guindeau à l'arrêt**.
- **Le câble de quai** se branche côté bateau d'abord et se débranche côté borne d'abord : on ne manipule jamais une fiche sous tension.
- **Repères de tension** : une LiFePO4 garde presque la même tension de 90 à 20 % de charge ; on lit donc son état en %, pas en volts. La batterie moteur, au plomb, se lit en volts, au repos depuis au moins une heure : 12,6 V pleine, 12,4 V aux trois quarts, 12,2 V à moitié, moins de 12,0 V déchargée.
- **Alarmes du shunt** (réglées le 16/10, [manuel du bord](../../documentation-technique/reglages-charge-et-shunt.md)) : état de charge sous 20 %, servitude sous 12,4 V, au-dessus de 14,6 V, démarreur sous 12,0 V. Elles s'affichent sur le téléphone seulement.
