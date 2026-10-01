---
hypothese: E-H1
titre: Batterie LiFePO4, chargeur DC/DC et chargeur de quai dédié
etat: recommandee
resume: Une batterie LiFePO4 de 100 Ah, avec BMS intégré, remplace le plomb dans le même coffre. Un chargeur DC/DC la charge depuis la batterie moteur, à la place du coupleur Scheiber, et le coupe-circuit de couplage est déposé. Au quai, un chargeur dédié la charge ; le Dolphin ne charge plus que la batterie moteur.
points_forts:
  - Plus d'hydrogène dans la cabine de poupe (A11 traitée à la source).
  - 80 à 90 Ah utiles au lieu d'environ 55, plus qu'une journée au mouillage.
  - Environ 10 kg au lieu de 25 à 30 kg ; plusieurs milliers de cycles.
  - Chaque batterie a son chargeur et son profil (DC/DC au moteur, chargeur dédié au quai pour la LiFePO4, Dolphin pour la batterie moteur seule). L'alternateur est protégé et la batterie moteur reste indépendante pour le démarrage.
points_faibles:
  - Environ 860 €, dont 185 € pour le chargeur de quai dédié.
  - Pas de charge en dessous de 0 °C ; le BMS coupe la charge, ce qui est sans danger mais à savoir l'hiver (Q47).
  - Le BMS peut couper toute la servitude en cas de surintensité ou de batterie vide, sans prévenir ; une alarme de charge basse (étude D) devient indispensable.
  - Le guindeau, environ 50 à 60 A, ne peut plus être secouru par la batterie moteur ; son pic de courant doit rester sous la limite du BMS.
  - Dimensions de la batterie et du coffre à vérifier (Q45) ; place du second chargeur de quai (Q49) et + après contact pour commander le DC/DC (Q48).
---

# E-H1 · Batterie LiFePO4, chargeur DC/DC et chargeur de quai dédié

Hypothèse de l'étude E. Base : **A-H4** (programme retenu de l'étude A, avec les fusibles de A-H2).

Nomenclature : [nomenclature.yaml](nomenclature.yaml), environ **860 €**. Le câblage (`cablage.yaml`, folio) sera écrit si l'hypothèse est retenue, après les réponses à Q45 à Q49.

## Principe

Une batterie LiFePO4 (lithium fer phosphate) ne dégage pas d'hydrogène en fonctionnement normal : la chimie ne produit pas de gaz à la charge, et le BMS (carte électronique intégrée) coupe la charge avant toute surtension. Elle peut donc rester dans le coffre de la cabine de poupe.

Elle impose en revanche une charge adaptée : tension d'absorption d'environ 14,2 à 14,6 V, pas de charge d'entretien prolongée (« floating ») au-dessus d'environ 13,5 V, pas de charge sous 0 °C. Elle ne doit pas non plus être mise en parallèle directe avec une batterie au plomb. D'où les trois modifications ci-dessous.

### 1. Déposer le coupe-circuit de couplage

Le coupe-circuit de couplage (node011, node012) met la batterie de servitude en parallèle avec la batterie moteur. Avec une LiFePO4, ce parallèle ferait passer un fort courant de l'une à l'autre (les tensions de repos diffèrent : environ 13,3 V pour la LiFePO4 et 12,7 V pour le plomb), et la LiFePO4 serait chargée par l'alternateur sans contrôle.

Il est donc déposé avec ses deux câbles de 35 mm² (wire010, wire011). Conséquence : on ne peut plus démarrer sur la batterie de servitude, ni faire tourner le guindeau sur la batterie moteur. La batterie moteur, au plomb, reste dédiée au démarrage.

### 2. Remplacer le coupleur Scheiber par un chargeur DC/DC

Le coupleur à relais relie les deux batteries dès que la tension monte : même problème que le couplage manuel. Il est déposé, avec ses fils (wire002, wire007, wire014) et les fusibles de 40 A que A-H2 avait mis sur ses départs (wire164, wire165).

Un **chargeur DC/DC** (type Victron Orion XS 12/12-50A) le remplace. Il prend le courant sur la batterie moteur et charge la LiFePO4 avec son propre profil :

- **L'alternateur ne voit que la batterie au plomb**, qu'il sait charger. Si le BMS de la LiFePO4 coupe, l'alternateur n'est pas exposé à la surtension d'une coupure brutale de charge.
- **Courant réglable** : l'alternateur de Juju ne donne qu'environ 20 A (Q14). Le courant du DC/DC doit être réglé en dessous, vers 15 A, pour ne pas vider la batterie moteur. Le modèle de 50 A est choisi pour son prix et sa disponibilité, pas pour sa puissance ; un modèle de 18 ou 30 A conviendrait aussi.
- **Démarrage au moteur seulement** : le DC/DC est autorisé par son entrée « remote », reliée à un + après contact (Q48), puis se met en route quand la tension de la batterie moteur indique que l'alternateur charge. Sans cette entrée, la charge de quai du Dolphin le ferait démarrer (voir 3).
- **Fusibles** : un à chaque extrémité de ses câbles d'entrée et de sortie, puisque chacune aboutit à une batterie. Calibre et section selon la notice et la longueur, au moment du câblage.

### 3. Chargeur de quai

**Le Dolphin est-il vraiment inadapté au LiFePO4 ?** Pas tout à fait. Sa notice (relevé, `documentation/MANUAL-DOLBB-1210-1220-299519-299520.pdf`) donne deux profils, choisis par un sélecteur :

| Position | Absorption | Floating |
|---|---|---|
| « Norm » | 14,4 V | 13,6 V |
| « Pb-Ca » | 15,0 V | 13,6 V |

Elle ne parle pas du lithium ; elle renvoie aux préconisations du fabricant de la batterie. Face au profil d'une LiFePO4 :

- **En position « Norm », 14,4 V est dans la plage de charge** d'une LiFePO4 (14,2 à 14,6 V environ) : le Dolphin la chargerait à peu près complètement.
- **Le floating permanent à 13,6 V est le vrai défaut.** Au quai, le chargeur reste branché des semaines : la LiFePO4 resterait à 100 % de charge en continu, ce qui accélère son vieillissement. Beaucoup de fabricants demandent pas de floating, ou un floating plus bas (Victron : 13,5 V). À comparer avec la fiche de la batterie choisie.
- **La position « Pb-Ca » (15,0 V) est à proscrire** : au-dessus de la tension maximale d'une LiFePO4, le BMS couperait la charge. Ce n'est pas dangereux, mais c'est un mauvais usage. Un sélecteur basculé par erreur suffit.
- **Pas de coupure de charge par temps froid** : seul le BMS protège la batterie sous 0 °C.
- **Ses trois sorties partagent la même régulation** (« tolérance tensions ± 2 % ») : les deux batteries reçoivent le même profil. C'est la vraie raison pour laquelle il ne permet pas de traiter différemment deux technologies : sur « Norm », un plomb ouvert et une LiFePO4 se partageraient un profil acceptable pour les deux, mais optimal pour aucune.

**Conclusion** : le Dolphin pourrait charger la LiFePO4 en dépannage, sur « Norm », mais pas dans de bonnes conditions au quai, à cause du floating permanent. **Sa sortie 2 (wire008, avec son fusible wire163 de A-H2) est donc débranchée** : il ne charge plus que la batterie moteur.

**Pourquoi un chargeur dédié, et pas le DC/DC derrière le Dolphin.** Une première version de cette hypothèse faisait charger la LiFePO4, au quai, par le DC/DC branché sur la batterie moteur, elle-même chargée par le Dolphin. C'est une erreur (remarque de l'utilisateur, 01/10) :

- Le Dolphin décide de passer de l'absorption (14,4 V) au floating (13,6 V) d'après ce qu'il voit sur sa sortie. Si le DC/DC tire 15 A sur la batterie moteur, le Dolphin croit que celle-ci accepte encore du courant et la maintient en absorption tant que la LiFePO4 n'est pas pleine : plusieurs heures à 14,4 V pour une batterie au plomb déjà chargée, donc perte d'eau, dégagement gazeux et corrosion des grilles, à chaque passage au quai.
- Le DC/DC, lui, démarre sur la tension d'absorption du Dolphin, mais risque de s'arrêter en floating (13,6 V, à 0,1 V de son seuil d'arrêt de 13,5 V) : la LiFePO4 serait mal chargée.

**Solution retenue : un chargeur de quai dédié à la LiFePO4**, à une sortie, avec profil LiFePO4 réglable (type Victron Blue Smart IP65 12/15) :

- Profil adapté : absorption vers 14,2 V, puis floating bas ou mode stockage ; coupure de la charge par temps froid si le modèle a une sonde.
- 15 A suffisent pour recharger 100 Ah en une nuit de quai ; le Dolphin reste à 20 A pour la seule batterie moteur.
- **230 V** : sur le disjoncteur de 10 A du chargeur, dans le boîtier d'arrivée (folio 3). Le Dolphin consomme au plus 2,5 A et le nouveau chargeur environ 1,5 A : le 10 A suffit. Avec 16 A aux bornes du port, la puissance de quai n'est pas une contrainte.
- **Emplacement** (Q49) : près du Dolphin dans le coffre de cockpit tribord si la place le permet, avec un câble 12 V jusqu'à la batterie de servitude, fusible à la batterie ; sinon dans une place sèche près de la batterie, avec un câble 230 V jusque-là.

**Le DC/DC ne doit alors tourner qu'au moteur.** Sinon, l'absorption du Dolphin à 14,4 V le ferait démarrer (seuil d'usine 14,0 V) et l'on retrouverait le problème ci-dessus. La tension seule ne permet pas de distinguer l'alternateur (environ 14,2 à 14,4 V) du Dolphin (14,4 V). On commande donc le DC/DC par son **entrée « remote »**, reliée par un fil fin, protégé à sa source, à un + 12 V présent seulement clé de contact tournée (Q48). Sa détection de tension reste active avec les réglages d'usine : clé tournée mais moteur arrêté, il ne tire rien sur la batterie moteur.

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
| Ajout | Chargeur DC/DC : entrée sur la batterie moteur (côté batterie du coupe-circuit moteur, node003), sortie sur la batterie de servitude (node009), masse côté charges du shunt ; un fusible à chaque extrémité. Fil de commande « remote » depuis un + après contact, fusible à sa source |
| Ajout | Chargeur de quai LiFePO4 : 230 V sur le disjoncteur de 10 A du chargeur (folio 3), sortie 12 V sur la batterie de servitude (node009) avec fusible à la batterie, masse côté charges du shunt |

## Conséquences

- **Fusible de batterie (A-H2)** : une LiFePO4 peut débiter plusieurs milliers d'ampères en court-circuit. Le fusible MEGA de 400 A prévu par A-H2 doit avoir un pouvoir de coupure suffisant ; sinon, prendre un fusible de classe T ou un MRBF de pouvoir de coupure adapté. À vérifier sur la fiche du fusible et de la batterie.
- **Étude D** : le SmartShunt se règle sur la chimie LiFePO4 ; l'alarme de charge basse prévient avant la coupure du BMS. Sans couplage, le démarreur ne traverse plus le shunt.
- **Bilan énergétique** : la capacité utile passe d'environ 55 Ah à 80-90 Ah. Le DC/DC consomme quelques milliampères en veille. Avec la masse de ses chargeurs côté charges du shunt, toute la charge de la LiFePO4 est comptée.
- **Coffre** : la LiFePO4 doit être solidement fixée (sangle, cales) et ses bornes protégées par un capot. Le coffre n'a plus besoin d'être ventilé pour le gaz, mais une LiFePO4 n'aime pas la chaleur : le coffre est contre le coffre moteur, température à surveiller.
- **Ancienne batterie** : à déposer en déchetterie ou chez un revendeur (reprise obligatoire).
