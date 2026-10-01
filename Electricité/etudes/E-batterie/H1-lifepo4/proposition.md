---
hypothese: E-H1
titre: Batterie LiFePO4 et chargeur DC/DC
etat: recommandee
resume: Une batterie LiFePO4 de 100 Ah, avec BMS intégré, remplace le plomb dans le même coffre. Un chargeur DC/DC la charge depuis la batterie moteur, à la place du coupleur Scheiber, et le coupe-circuit de couplage est déposé.
points_forts:
  - Plus d'hydrogène dans la cabine de poupe (A11 traitée à la source).
  - 80 à 90 Ah utiles au lieu d'environ 55, plus qu'une journée au mouillage.
  - Environ 10 kg au lieu de 25 à 30 kg ; plusieurs milliers de cycles.
  - Le chargeur DC/DC protège l'alternateur et charge la LiFePO4 avec le bon profil ; la batterie moteur reste indépendante pour le démarrage.
points_faibles:
  - Environ 660 €.
  - Pas de charge en dessous de 0 °C ; le BMS coupe la charge, ce qui est sans danger mais à savoir l'hiver (Q47).
  - Le BMS peut couper toute la servitude en cas de surintensité ou de batterie vide, sans prévenir ; une alarme de charge basse (étude D) devient indispensable.
  - Le guindeau, environ 50 à 60 A, ne peut plus être secouru par la batterie moteur ; son pic de courant doit rester sous la limite du BMS.
  - Dimensions de la batterie et du coffre à vérifier (Q45).
---

# E-H1 · Batterie LiFePO4 et chargeur DC/DC

Hypothèse de l'étude E. Base : **A-H4** (programme retenu de l'étude A, avec les fusibles de A-H2).

Nomenclature : [nomenclature.yaml](nomenclature.yaml), environ **660 €**. Le câblage (`cablage.yaml`, folio) sera écrit si l'hypothèse est retenue, après les réponses à Q45 et Q47.

## Principe

Une batterie LiFePO4 (lithium fer phosphate) ne dégage pas d'hydrogène en fonctionnement normal : la chimie ne produit pas de gaz à la charge, et le BMS (carte électronique intégrée) coupe la charge avant toute surtension. Elle peut donc rester dans le coffre de la cabine de poupe.

Elle impose en revanche une charge adaptée : tension d'absorption d'environ 14,2 à 14,6 V, pas de charge d'entretien prolongée (« floating ») au-dessus d'environ 13,5 V, pas de charge sous 0 °C. Elle ne doit pas non plus être mise en parallèle directe avec une batterie au plomb. D'où les trois modifications demandées.

### 1. Déposer le coupe-circuit de couplage

Le coupe-circuit de couplage (node011, node012) met la batterie de servitude en parallèle avec la batterie moteur. Avec une LiFePO4, ce parallèle ferait passer un fort courant de l'une à l'autre (les tensions de repos diffèrent : environ 13,3 V pour la LiFePO4 et 12,7 V pour le plomb), et la LiFePO4 serait chargée par l'alternateur sans contrôle.

Il est donc déposé avec ses deux câbles de 35 mm² (wire010, wire011). Conséquence : on ne peut plus démarrer sur la batterie de servitude, ni faire tourner le guindeau sur la batterie moteur. La batterie moteur, au plomb, reste dédiée au démarrage.

### 2. Remplacer le coupleur Scheiber par un chargeur DC/DC

Le coupleur à relais relie les deux batteries dès que la tension monte : même problème que le couplage manuel. Il est déposé, avec ses fils (wire002, wire007, wire014) et les fusibles de 40 A que A-H2 avait mis sur ses départs (wire164, wire165).

Un **chargeur DC/DC** (type Victron Orion XS 12/12-50A) le remplace. Il prend le courant sur la batterie moteur et charge la LiFePO4 avec son propre profil :

- **L'alternateur ne voit que la batterie au plomb**, qu'il sait charger. Si le BMS de la LiFePO4 coupe, l'alternateur n'est pas exposé à la surtension d'une coupure brutale de charge.
- **Courant réglable** : l'alternateur de Juju ne donne qu'environ 20 A (Q14). Le courant du DC/DC doit être réglé en dessous, vers 15 A, pour ne pas vider la batterie moteur. Le modèle de 50 A est choisi pour son prix et sa disponibilité, pas pour sa puissance ; un modèle de 18 ou 30 A conviendrait aussi.
- **Démarrage automatique** : le DC/DC se met en route quand la tension de la batterie moteur indique que l'alternateur charge, et s'arrête moteur arrêté.
- **Fusibles** : un à chaque extrémité de ses câbles d'entrée et de sortie, puisque chacune aboutit à une batterie. Calibre et section selon la notice et la longueur, au moment du câblage.

### 3. Chargeur de quai

Le chargeur Dolphin est prévu pour le plomb. Deux solutions :

| | Solution | Pour | Contre |
|---|---|---|---|
| a | **Garder le Dolphin sur la batterie moteur seule** : sa sortie 2 (wire008, et son fusible wire163) est débranchée. Au quai, le Dolphin charge la batterie moteur et le DC/DC transfère vers la LiFePO4. | Aucun achat ; le DC/DC applique le bon profil | La LiFePO4 n'est chargée au quai qu'à travers le DC/DC, à environ 15 A ; le DC/DC doit reconnaître la tension du chargeur comme « moteur en marche » (tension de démarrage réglable, à vérifier) |
| b | **Remplacer le Dolphin** par un chargeur à plusieurs sorties avec profil LiFePO4 | Charge directe et rapide | Environ 250 € de plus |

La solution **a** est retenue dans la nomenclature. La b peut venir plus tard, avec un 230 V plus puissant au ponton (16 A depuis le 01/10).

## Choix de la batterie

- **Capacité 100 Ah** : même encombrement environ que le plomb actuel (à vérifier, Q45), pour 80 à 90 Ah utiles. Une 150 ou 200 Ah se justifierait avec le solaire (étude C).
- **BMS intégré de 100 A au moins en continu**, avec un pic plus élevé pendant quelques secondes : le guindeau consomme 50 A en régime normal d'après sa notice, davantage en tirant fort sur la chaîne. Un BMS trop juste couperait tout le bord pendant la manœuvre de mouillage. À vérifier sur la fiche du modèle choisi, ou prendre une batterie de 150 A.
- **Protection basse température** (coupure de la charge sous 0 °C) et, si possible, **application Bluetooth** pour lire l'état des cellules.
- Les batteries Victron « NG » demandent un BMS externe (Lynx Smart BMS), ce qui double le prix : écartées pour un bord de cette taille.

## Changements de câblage (à écrire dans `cablage.yaml`)

| Action | Éléments |
|---|---|
| Dépose | Coupe-circuit de couplage (node011, node012) ; wire010, wire011 |
| Dépose | Coupleur Scheiber (node013 à node015) ; wire002, wire007, wire014 ; wire164, wire165 et leurs fusibles de 40 A (A-H2) |
| Débranchement | Sortie 2 du chargeur de quai : wire008, wire163 et son fusible de 30 A (A-H2) |
| Remplacement | Batterie de servitude : mêmes bornes (node007, node008), wire161 et wire009 repris |
| Ajout | Chargeur DC/DC : entrée sur la batterie moteur (côté batterie du coupe-circuit moteur, node003), sortie sur la batterie de servitude (node009), masse côté charges du shunt ; un fusible à chaque extrémité |

## Conséquences

- **Fusible de batterie (A-H2)** : une LiFePO4 peut débiter plusieurs milliers d'ampères en court-circuit. Le fusible MEGA de 400 A prévu par A-H2 doit avoir un pouvoir de coupure suffisant ; sinon, prendre un fusible de classe T ou un MRBF de pouvoir de coupure adapté. À vérifier sur la fiche du fusible et de la batterie.
- **Étude D** : le SmartShunt se règle sur la chimie LiFePO4 ; l'alarme de charge basse prévient avant la coupure du BMS. Sans couplage, le démarreur ne traverse plus le shunt.
- **Bilan énergétique** : la capacité utile passe d'environ 55 Ah à 80-90 Ah. Le DC/DC consomme quelques milliampères en veille.
- **Coffre** : la LiFePO4 doit être solidement fixée (sangle, cales) et ses bornes protégées par un capot. Le coffre n'a plus besoin d'être ventilé pour le gaz, mais une LiFePO4 n'aime pas la chaleur : le coffre est contre le coffre moteur, température à surveiller.
- **Ancienne batterie** : à déposer en déchetterie ou chez un revendeur (reprise obligatoire).
