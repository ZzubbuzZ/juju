---
hypothese: E-H1
titre: Batterie LiFePO4 et chargeur DC/DC
etat: recommandee
resume: Une batterie LiFePO4 de 100 Ah, avec BMS intégré, remplace le plomb dans le même coffre. Un chargeur DC/DC la charge depuis la batterie moteur, à la place du coupleur Scheiber, et le coupe-circuit de couplage est déposé.
points_forts:
  - Plus d'hydrogène dans la cabine de poupe (A11 traitée à la source).
  - 80 à 90 Ah utiles au lieu d'environ 55, plus qu'une journée au mouillage.
  - Environ 10 kg au lieu de 25 à 30 kg ; plusieurs milliers de cycles.
  - Le chargeur DC/DC protège l'alternateur et charge la LiFePO4 avec le bon profil, au moteur comme au quai à travers le chargeur Dolphin ; la batterie moteur reste indépendante pour le démarrage.
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

**Conclusion** : le Dolphin pourrait charger la LiFePO4 en dépannage, sur « Norm », mais pas dans de bonnes conditions au quai, à cause du floating permanent. **La sortie 2 (wire008, avec son fusible wire163 de A-H2) est donc débranchée**, comme prévu, et la LiFePO4 est chargée par le DC/DC, qui applique son propre profil.

**Le DC/DC chargera-t-il la LiFePO4 quand le Dolphin charge la batterie moteur ?** Oui pendant l'absorption, pas de façon sûre pendant le floating, avec les réglages d'usine. L'Orion XS n'a pas de fil « moteur en marche » : il déduit que l'alternateur tourne de la tension de la batterie moteur. Réglages d'usine pour un alternateur classique (notice Victron) :

| Seuil | Valeur | Avec le Dolphin |
|---|---|---|
| Démarrage immédiat | 14,0 V | Atteint pendant l'absorption (14,4 V) : le DC/DC démarre |
| Démarrage différé | 13,8 V pendant 120 s | Jamais atteint en floating (13,6 V) |
| Arrêt | 13,5 V | Le floating, 13,6 V à ± 2 %, n'est qu'à 0,1 V au-dessus |

- Pendant l'**absorption** du Dolphin, le DC/DC démarre et charge la LiFePO4. Le Dolphin fournit 20 A au plus : réglé à 15 A, le DC/DC lui laisse de quoi tenir la batterie moteur.
- Au passage en **floating**, la tension tombe à 13,6 V, trop près du seuil d'arrêt : la chute dans les câbles ou la tolérance du chargeur peuvent arrêter le DC/DC, qui ne redémarrera pas à 13,6 V. La LiFePO4 resterait alors partiellement chargée jusqu'à la prochaine absorption du Dolphin.

Deux façons de le rendre fiable :

1. **Abaisser les seuils** dans l'application VictronConnect, par exemple démarrage différé à 13,4 V et arrêt à 13,2 V. Le floating du Dolphin (13,6 V) reste alors au-dessus, tandis qu'une batterie au plomb au repos, sans charge, retombe vers 12,7 à 12,9 V et arrête le DC/DC. À valider sur place, avec la tension mesurée à l'entrée du DC/DC.
2. **Commander le DC/DC par son entrée « remote »** plutôt que par la tension : un relais l'active quand le moteur tourne (contact) ou quand le 230 V du quai est présent. Plus sûr, mais un relais et des fils de plus.

La première solution est retenue : elle ne demande aucun matériel. Le courant de sortie du DC/DC se règle de 1 à 50 A ; 15 A ménagent à la fois l'alternateur et le Dolphin.

**Plus tard** : remplacer le Dolphin par un chargeur à plusieurs sorties avec un profil LiFePO4 (environ 250 €) chargerait la LiFePO4 directement et plus vite, avec le 16 A du ponton.

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
