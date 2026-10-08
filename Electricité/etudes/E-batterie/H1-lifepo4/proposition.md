---
hypothese: E-H1
titre: Batterie LiFePO4, chargeur DC/DC et chargeur de quai dédié
etat: retenue
resume: Une batterie LiFePO4 de 200 Ah (Humsienk, BMS 250 A) remplace le plomb dans le même coffre. Un Orion XS, commandé par un interrupteur, la charge depuis la batterie moteur à la place du coupleur Scheiber, et le coupe-circuit de couplage est déposé. Au quai, un Blue Smart IP67 12/17 la charge ; le Dolphin ne charge plus que la batterie moteur, raccordé au plus près d'elle. Chargeur de quai et shunt dans la contremarche (variante dans le coffre de la batterie, E-H4).
points_forts:
  - Plus d'hydrogène dans la cabine de poupe (A11 traitée à la source).
  - Environ 160 à 180 Ah utiles au lieu d'environ 55, près de trois jours au mouillage.
  - BMS de 250 A ; plusieurs milliers de cycles.
  - Guindeau sur la batterie moteur (décision du 05/10) ; il tire sur l'alternateur moteur tournant, ne sollicite plus le BMS et ne fausse plus le bilan du shunt.
  - Chaque batterie a son chargeur et son profil (Orion XS au moteur, Blue Smart au quai pour la LiFePO4, Dolphin pour la batterie moteur seule). L'alternateur est protégé et la batterie moteur reste indépendante pour le démarrage.
points_faibles:
  - 26,4 kg, autant que le plomb ; 52 cm de long.
  - Pas de charge en dessous de 0 °C (le BMS coupe la charge) ; sans conséquence en Méditerranée (Q47).
  - Le BMS peut couper toute la servitude sans prévenir, batterie vide ; une alarme de charge basse (étude D) devient indispensable.
  - Plus de démarrage direct sur la LiFePO4 ; le couplage est déposé (tensions différentes, courant de pointe du BMS non spécifié). La recharge de secours par l'Orion XS (25 A, 15 min) le remplace.
  - Guindeau utilisé moteur arrêté ; il entame la batterie de démarrage (environ 2 à 3 Ah par mouillage).
  - Commande manuelle du DC/DC (Q48) ; un oubli au port le laisse démarrer sur la charge du Dolphin.
  - Fusible MEGA (décision du 05/10) ; un MRBF aurait un meilleur pouvoir de coupure, pour le même prix.
decision: "02/10/2026 : retenue par Julie (batterie de servitude LiFePO4). 05/10 : batterie Humsienk 12 V 200 Ah Plus (BMS 250 A), Orion XS 12/12-50A (259 €) et Blue Smart IP67 12/17 (BPC121713006, 118 €) achetés ; fusible MEGA de 300 A ; commande manuelle de l'Orion XS (Q48). Câblage écrit ; emplacement de l'Orion XS, du chargeur de quai et du shunt à choisir sur place (E-H1 ou E-H4). 05/10, suite : guindeau sur le circuit moteur, couplage déposé sans retour (démarrage direct abandonné), fusibles de 70 A et câbles de 16 mm² pour l'Orion XS, commande sur la broche H avec interrupteur à voyant ; folios cibles 2h et 2i. 08/10 : calibre du MEGA confirmé à 300 A ; étude fusionnée dans main. 08/10, suite : entrée et commande de l'Orion XS côté charges du coupe-circuit moteur (node004), masse du voyant sur node005."
---

# E-H1 · Batterie LiFePO4, chargeur DC/DC et chargeur de quai dédié

Hypothèse de l'étude E. Base : **A-H4** (programme retenu de l'étude A, avec les fusibles de A-H2).

Nomenclature : [nomenclature.yaml](nomenclature.yaml), environ **900 €**. Câblage : [cablage.yaml](cablage.yaml) (base : **D-H1**, le shunt de l'étude D), avec l'Orion XS, le chargeur de quai et le shunt dans la contremarche : [folio 2h](folio-2h-circuit-moteur.svg) (circuit moteur cible) et [folio 2i](folio-2i-circuit-servitude.svg) (circuit servitude cible). Variante dans le coffre de la batterie : [E-H4](../H4-chargeur-coffre/proposition.md), folios [2j](../H4-chargeur-coffre/folio-2j-circuit-moteur.svg) et [2k](../H4-chargeur-coffre/folio-2k-circuit-servitude.svg). Choix sur place (Q53). Réponses du 03/10 : place suffisante dans le coffre (Q45), pas de gel (Q47), second chargeur à côté du Dolphin (Q49).

## Principe

Une batterie LiFePO4 (lithium fer phosphate) ne dégage pas d'hydrogène en fonctionnement normal : la chimie ne produit pas de gaz à la charge, et le BMS (carte électronique intégrée) coupe la charge avant toute surtension. Elle peut donc rester dans le coffre de la cabine de poupe.

Elle impose en revanche une charge adaptée : tension d'absorption d'environ 14,2 à 14,6 V, pas de charge d'entretien prolongée (« floating ») au-dessus d'environ 13,5 V, pas de charge sous 0 °C. Elle ne doit pas non plus être mise en parallèle directe avec une batterie au plomb. D'où les trois modifications ci-dessous.

### 1. Déposer le coupe-circuit de couplage

Le coupe-circuit de couplage (node011, node012) met la batterie de servitude en parallèle avec la batterie moteur. Avec une LiFePO4, ce parallèle ferait passer un fort courant de l'une à l'autre (les tensions de repos diffèrent : environ 13,3 V pour la LiFePO4 et 12,7 V pour le plomb), et la LiFePO4 serait chargée par l'alternateur sans contrôle.

Il est donc **déposé avec ses deux câbles de 35 mm²** (wire010, wire011), **sans exception** (05/10, remarque de l'utilisateur). Les deux batteries n'ont pas la même tension : fermé par erreur avec le coupe-circuit moteur, il les mettrait en parallèle, et l'une se viderait dans l'autre à un courant limité seulement par la résistance des câbles et des batteries, plusieurs centaines d'ampères, sans fusible adapté sur ce chemin. Le démarrage direct sur la LiFePO4, qui le conservait comme interrupteur de secours, est abandonné (voir « Démarrage de secours »). La batterie moteur, au plomb, reste dédiée au démarrage et au guindeau.

### 1 bis. Guindeau sur le circuit moteur (décision du 05/10)

Le guindeau était alimenté par la servitude : wire017, de node010 (côté charges du coupe-circuit de servitude) à son disjoncteur de 70 A (node020). **Il passe sur la batterie moteur** : wire017 est remplacé par **wire217**, 35 mm², de node004 (côté charges du coupe-circuit moteur, la borne du démarreur) au disjoncteur. Le disjoncteur, le relais et wire018 ne changent pas.

- **Manœuvre moteur tournant** : c'est le cas normal au mouillage. L'alternateur (20 A) et la batterie moteur fournissent les 50 à 60 A du guindeau directement, sans passer par l'Orion XS.
- **La LiFePO4 et son BMS ne voient plus le guindeau** : plus de pointe de courant à surveiller sur le BMS. Le départ le plus chargé de la servitude devient celui du tableau de la table à carte.
- **Le shunt de l'étude D ne compte plus le guindeau** : son bilan ne mesure que la vie à bord.
- **Protection** : wire217 est protégé, comme wire012, par le fusible de 400 A de la batterie moteur (A-H2) ; le disjoncteur de 70 A protège ensuite wire018. Ouvrir le coupe-circuit moteur coupe aussi le guindeau.
- **Revers** : guindeau utilisé moteur arrêté, il entame la batterie de démarrage, environ 2 à 3 Ah par mouillage (50 A pendant 2 à 3 minutes), sur 110 Ah. Sans conséquence pour le démarrage, mais la règle reste de relever l'ancre moteur tournant.

### 2. Remplacer le coupleur Scheiber par un chargeur DC/DC

Le coupleur à relais relie les deux batteries dès que la tension monte : même problème que le couplage manuel. Il est déposé, avec ses fils (wire002, wire007, wire014) et les fusibles de 40 A que A-H2 avait mis sur ses départs (wire164, wire165).

Un **chargeur DC/DC** (type Victron Orion XS 12/12-50A) le remplace. Il prend le courant sur la batterie moteur et charge la LiFePO4 avec son propre profil :

- **L'alternateur ne voit que la batterie au plomb**, qu'il sait charger. Si le BMS de la LiFePO4 coupe, l'alternateur n'est pas exposé à la surtension d'une coupure brutale de charge.
- **Courant réglable** : l'alternateur de Juju ne donne qu'environ 20 A (Q14). Le courant du DC/DC doit être réglé en dessous, vers 15 A, pour ne pas vider la batterie moteur. Le modèle de 50 A est choisi pour son prix et sa disponibilité, pas pour sa puissance ; un modèle de 18 ou 30 A conviendrait aussi.
- **Démarrage au moteur seulement** : le DC/DC est autorisé par son entrée « remote », commandée par un interrupteur (Q48, voir « Commande du DC/DC »), puis se met en route quand la tension de la batterie moteur indique que l'alternateur charge. Sans cette entrée, la charge de quai du Dolphin le ferait démarrer (voir 3).
- **Fusibles et câbles (notice Victron, § 3.3)** : un fusible à chaque extrémité, puisque chacune aboutit à une batterie, de **60 à 70 A** pour le modèle de 50 A, avec du **16 mm²** jusqu'à 5 m (21 mm² de 5 à 10 m). Choix : **fusibles MIDI de 70 A** et câble de 16 mm². Le calibre est celui de l'appareil, pas du courant réglé : l'Orion XS peut débiter 50 A si son réglage change, et le fusible doit tenir ce courant avec une marge. Le 16 mm² tient bien plus de 70 A ; c'est la chute de tension qui fixe sa section.
- **Recharge de secours inversée** : 25 A au plus, la moitié du courant nominal (notice), donc sous les 50 A de l'appareil et les 70 A des fusibles. Elle reste possible interrupteur ouvert, coupe-circuit moteur fermé (voir « Démarrage de secours »).
- **Raccordement des deux côtés (08/10)** : l'entrée est prise **côté charges du coupe-circuit moteur** (node004), la sortie **côté batterie du coupe-circuit de servitude** (node009).
  - **Entrée côté charges.** L'Orion XS ne charge que moteur tournant, donc coupe-circuit moteur fermé : ce raccordement ne retire rien à la charge. Coupe-circuit moteur ouvert, l'Orion XS est isolé de la batterie de démarrage : plus de consommation de veille sur elle (moins de 1,5 mA d'après les fiches, relevé par recherche, environ 1 Ah par mois), ni de consommation à vide si l'interrupteur est oublié fermé (moins de 100 mA, jusqu'à 2,4 Ah par jour). La recharge de secours inversée demande seulement de fermer le coupe-circuit moteur, ce qu'on fait de toute façon pour démarrer.
  - **Sortie côté batterie.** Côté charges (node010), coupe-circuit de servitude ouvert moteur tournant, l'Orion XS alimenterait le réseau de bord sans batterie derrière lui, et la LiFePO4 ne serait pas chargée.

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
- **230 V** : le chargeur consomme environ 1,5 A ; avec le Dolphin (2,5 A au plus), un départ de 10 A suffit. Avec 16 A aux bornes du port, la puissance de quai n'est pas une contrainte.
- **Emplacement** : **avec le shunt de l'étude D**, dans la contremarche de la descente (H1) ou dans le coffre de la batterie (H4), à décider sur place (05/10), et non dans le coffre de cockpit tribord envisagé avec Q49. Voir « Chargeur de quai : Blue Smart IP67 12/17 » ci-dessous.

**Le DC/DC ne doit alors tourner qu'au moteur.** Sinon, l'absorption du Dolphin à 14,4 V le ferait démarrer (seuil d'usine 14,0 V) et l'on retrouverait le problème ci-dessus. La tension seule ne permet pas de distinguer l'alternateur (environ 14,2 à 14,4 V) du Dolphin (14,4 V). On commande donc le DC/DC par son **entrée « remote »**, par un fil fin protégé à sa source (Q48, ci-dessous). Sa détection de tension reste active avec les réglages d'usine : clé tournée mais moteur arrêté, il ne tire rien sur la batterie moteur.

**Commande du DC/DC (Q48, 03/10).** Le + après contact du tableau moteur est pris sur la batterie moteur. Ce n'est pas un obstacle : les deux batteries ont leur négatif en commun (coupe-circuit des négatifs, node005), et l'entrée « remote » de l'Orion XS ne demande qu'une tension positive par rapport à ce négatif commun. L'écart de tension entre les deux batteries, quelques dixièmes de volt, est sans effet. Deux câblages possibles :

| | Commande | Fil à tirer | Inconvénient |
|---|---|---|---|
| a | Automatique : + après contact du tableau moteur | Un fil fin du tableau moteur à l'Orion XS, près de la platine des coupe-circuits, avec un fusible de 1 A à sa source | Trajet du tableau moteur à la platine à relever |
| b | Manuelle : interrupteur à la table à carte | Un départ du tableau de servitude vers l'Orion XS, environ 3 m ; l'interrupteur peut être alimenté par le + de la servitude, sans fil + moteur | Un oubli au port laisse l'Orion XS démarrer sur la charge du Dolphin et maintenir la batterie moteur en absorption |

Proposition : **a**, qui ne demande aucune manœuvre et ne dépend pas d'un oubli.

**Choix du 05/10 : b, commande manuelle**, par un interrupteur près du tableau Scheiber 2 voies, dans la contremarche de la descente, à côté de la platine où se trouve l'Orion XS : le fil de commande est court. L'interrupteur est alimenté par le + de l'entrée de l'Orion XS, côté charges du coupe-circuit moteur (node004), à travers un fusible de 1 A à sa source : c'est ce que demande la notice (remarque de l'utilisateur, 08/10 ; il était d'abord pris sur la servitude, node010). Coupe-circuit moteur ouvert, la commande est coupée en même temps que l'entrée. Le risque de l'oubli au port demeure : interrupteur fermé, l'absorption du Dolphin (14,4 V) fait démarrer l'Orion XS et maintient la batterie moteur en absorption. Parades : un interrupteur à voyant, une étiquette « Orion XS : ouvrir au port », et l'arrêt de l'Orion XS dans la check-list d'amarrage.

**Câblage de l'entrée « remote » (notice Victron).** Ce n'est pas une sortie à drain ou à source ouverts, mais une **entrée à deux broches, H et L**, livrée avec un cavalier entre elles (l'Orion XS démarre alors dès qu'il est alimenté). La notice donne quatre façons de la commander :

| | Commande | Condition |
|---|---|---|
| a | Contact sec entre H et L | Résistance de moins de 30 kΩ |
| b | + de la batterie sur H, par un interrupteur | Actif au-dessus d'environ 4 V ; H tolère ± 70 V |
| c | L mis à la masse | Actif sous environ 6 V |
| d | Sortie d'un BMS sur H | Variante de b |

**Option b retenue** : le **cavalier H-L est retiré**, L reste libre, et l'interrupteur relie le + de l'entrée (node004, fusible de 1 A à la source, wire207 et wire208) à la broche H (wire209). **Un interrupteur à voyant convient** : son voyant est branché entre sa borne de sortie et la masse (wire216, sur le coupe-circuit des négatifs côté batteries, node005, 08/10 ; d'abord prévu sur la barrette de masse du tableau Scheiber, node051), et l'entrée H ne demande qu'une tension, pas un courant. En option a, au contraire, le voyant n'aurait pas de masse et laisserait passer un courant de fuite entre H et L : un interrupteur à voyant serait à proscrire.

## Démarrage de secours sur la LiFePO4

Question de l'utilisateur (02/10) : peut-on démarrer le moteur sur la LiFePO4 si la batterie moteur est en panne ? Oui, à deux niveaux.

### Niveau 1 : recharge de secours de la batterie moteur par le DC/DC (sans matériel)

L'Orion XS a une fonction **« emergency reverse charge »** : lancée depuis l'application VictronConnect, elle fait passer le courant **dans l'autre sens**, de la LiFePO4 vers la batterie moteur, pendant 15 minutes, puis annonce « Battery ready » après 5 minutes de repos (notice Victron). Le courant est la moitié du courant nominal, soit **25 A pour le modèle de 50 A**, environ 6 Ah transférés. La batterie de servitude n'est pas descendue sous 12 V.

- Un démarrage de diesel consomme peu d'énergie (quelques secondes à 200-300 A, moins de 1 Ah) : 6 Ah suffisent à une batterie moteur **déchargée** (feux oubliés, longue immobilisation).
- La LiFePO4 ne fournit que 25 A : **aucune exigence de courant de pointe** sur son BMS.
- Limite, écrite dans la notice : « Battery ready » ne garantit pas que la batterie lance le moteur. Une batterie moteur **défectueuse** (élément en court-circuit, sulfatée) ne reprendra pas.

Ce niveau est acquis avec H1 telle qu'elle est chiffrée : il suffit de connaître la manœuvre, coupe-circuit moteur fermé (l'entrée de l'Orion XS est de son côté charges).

### Niveau 2 : démarrage direct sur la LiFePO4 (abandonné le 05/10)

Il consistait à conserver le coupe-circuit de couplage (node009 → wire011 → couplage → wire010 → node004) pour alimenter le démarreur par la LiFePO4, coupe-circuit moteur ouvert. Il est abandonné :

- **Tensions différentes** : une erreur de manœuvre (couplage et coupe-circuit moteur fermés ensemble) mettrait les deux batteries en parallèle, avec un courant de plusieurs centaines d'ampères de l'une vers l'autre (remarque de l'utilisateur, 05/10).
- **BMS** : le démarreur consomme 200 à 275 A au lancement et 460 A rotor bloqué (manuel d'atelier Yanmar) ; la batterie achetée tient 250 A en continu et sa fiche ne donne aucun courant de pointe. Le démarrage direct n'est pas garanti.
- **Alternateur** : moteur démarré, il chargerait la LiFePO4 sans contrôle jusqu'à l'ouverture du couplage, au risque d'une surtension si le BMS coupe.
- **Guindeau** : le couplage servait aussi à faire tourner le guindeau sur la batterie moteur ; il y est maintenant raccordé directement (1 bis).

### Recommandation

**Niveau 1 seul.** Il couvre le cas le plus fréquent, la batterie moteur déchargée, sans matériel ni autre manœuvre que la fermeture habituelle du coupe-circuit moteur. Une batterie moteur défectueuse loin d'un port reste un cas non couvert : la parade est son remplacement préventif.

## Choix de la batterie

- **Capacité 100 Ah** : même encombrement environ que le plomb actuel ; le coffre a de la place (Q45), pour 80 à 90 Ah utiles. Une 150 ou 200 Ah se justifierait avec le solaire (étude C).
- **BMS intégré de 100 A au moins en continu** (150 à 200 A, avec un courant de pointe de démarrage, si le niveau 2 du démarrage de secours est retenu), avec un pic plus élevé pendant quelques secondes : le guindeau consomme 50 A en régime normal d'après sa notice, davantage en tirant fort sur la chaîne. Un BMS trop juste couperait tout le bord pendant la manœuvre de mouillage. À vérifier sur la fiche du modèle choisi, ou prendre une batterie de 150 A.
- **Protection basse température** (coupure de la charge sous 0 °C) et, si possible, **application Bluetooth** pour lire l'état des cellules.
- Les batteries Victron « NG » demandent un BMS externe (Lynx Smart BMS), ce qui double le prix : écartées pour un bord de cette taille.

## Batterie commandée (05/10)

**Humsienk 12 V 200 Ah Plus** (fiche du site du fabricant, relevée le 05/10) : 12,8 V, 200 Ah (2 560 Wh), BMS de **250 A en continu**, en décharge comme en charge ; charge recommandée 40 A, tension de charge 14,4 V ± 0,2 V ; charge entre 0 et 55 °C ; **521 × 238 × 221 mm, 26,4 kg**, bornes M8, IP65 ; Bluetooth et application ; 6 000 cycles à 80 % de profondeur. La fiche ne donne **ni courant de pointe ni courant de court-circuit**.

Ce que ce choix change par rapport à la batterie de 100 Ah étudiée :

- **Énergie** : environ 160 à 180 Ah utiles, soit **près de trois jours au mouillage** sans recharge (environ 60 Ah par jour d'après le bilan, à remplacer par des mesures avec le shunt de l'étude D). Le solaire (étude C) n'est plus indispensable pour tenir un week-end.
- **Encombrement et poids** : 52 cm de long et 26 kg, le poids du plomb actuel. Le gain de poids disparaît, et la place dans le coffre n'est pas un problème (Q51, 05/10).
- **Guindeau** : il passe de toute façon sur la batterie moteur (05/10) ; le BMS ne le voit plus.
- **Démarrage de secours, niveau 2** : le lancement (200 à 275 A pendant quelques secondes) est à la limite du courant continu du BMS, et l'appel de 460 A à rotor bloqué dépend d'un courant de pointe que la fiche ne donne pas. Le démarrage direct n'est donc **pas garanti** ; il est abandonné, et le niveau 1 (recharge de secours par l'Orion XS) reste la solution.
- **Charge** : 14,4 V ± 0,2 V convient au Blue Smart (profil lithium) et à l'Orion XS. Les courants de charge (15 A au moteur, 17 A au quai) sont bien en dessous des 40 A recommandés.
- **Bluetooth** : le BMS donne déjà un état de charge sur son application. Ce que le SmartShunt de l'étude D apporte en plus est détaillé dans l'étude D.

### Chargeur de quai : Blue Smart IP67 12/17

À la place du Blue Smart IP65 12/15 prévu : 17 A au lieu de 15, et un boîtier étanche (IP67) aux câbles sortants. Référence BPC121713006, achetée 118 € (Q52, 05/10).

**Emplacement : avec le shunt, pas à côté du Dolphin (05/10).** Placé à côté du Dolphin, il aurait fallu 5 m de câble 12 V jusqu'à la batterie (Q50) : environ 10 mm² pour rester sous 3 % de chute à 17 A, soit deux câbles épais à faire passer à travers les cloisons. Placé avec le shunt, dans la contremarche (H1) ou dans le coffre de la batterie (H4) :

- **Côté 12 V**, le câble ne fait que quelques dizaines de centimètres : la chute de tension devient négligeable, la section est celle de la notice, et un **fusible de 25 A à sa source** le protège. Le + rejoint le côté batterie du coupe-circuit de servitude (node009) dans la contremarche, ou la borne + de la batterie, avant le fusible de 300 A, dans le coffre (H4) : dans les deux cas, la charge reste possible coupe-circuit ouvert.
- **Le négatif doit revenir du côté « bord » du shunt** de l'étude D, sinon la charge n'est pas comptée. Le chargeur et le shunt étant posés ensemble, ce fil reste court dans les deux variantes.
- **Côté 230 V**, c'est l'alimentation qui fait le trajet d'environ 5 m, mais elle ne transporte qu'environ 1,5 A : un câble 3 × 1,5 mm² (H07RN-F) suffit largement. **Choix du 05/10 (Q53)** : un câble dédié depuis le disjoncteur du chargeur de quai (C10), dans le boîtier d'arrivée, jusqu'à une prise dédiée ou un boîtier de raccordement à bornes Wago près du chargeur. Le chargeur reste derrière le différentiel de 30 mA.
- **Emplacement définitif** (05/10) : l'Orion XS, le chargeur et le shunt de l'étude D vont ensemble, soit dans la contremarche de la descente, près de la platine, soit dans le coffre de la batterie ; à décider sur place selon la place dans la contremarche. Dans la contremarche, le + du chargeur rejoint le côté batterie du coupe-circuit de servitude (node009) avec son fusible à la source, et le câble 230 V est un peu plus court.
- **Chaleur** : environ 40 W perdus en pleine charge. Le boîtier IP67 supporte l'humidité du coffre, mais il lui faut un peu d'air autour ; à fixer sur une paroi, pas contre la batterie.

### Dolphin : sortie moteur au plus près de la batterie moteur (décision du 05/10)

Le Dolphin ne charge plus que la batterie moteur, et il est fixé juste au-dessus d'elle. Sa sortie 1 passe aujourd'hui par la platine des coupe-circuits : wire003 (2 m) jusqu'à son fusible de 30 A (A-H2, wire162 sur node003). Elle est raccordée **directement à la batterie moteur** :

- **+** : un câble court de la sortie 1 jusqu'à un **fusible de 30 A à la batterie**, monté sur le même goujon d'entrée que le fusible de 400 A (ou dans un bloc qui porte les deux), pour ne pas empiler les cosses sur la borne. wire003 et wire162, avec le fusible de 30 A de la platine, sont déposés.
- **−** : le négatif du Dolphin (wire005, 35 mm², 2 m jusqu'au coupe-circuit des négatifs) peut lui aussi aller au plus court, sur la borne − de la batterie moteur (node002). Il ne charge plus la servitude : son retour n'a pas à passer près du shunt.
- **Gains** : câble sous les 1,5 m demandés par la notice du Dolphin, deux câbles et un passage de cloison en moins, tension de charge mesurée au plus près de la batterie.
- **Revers** : le chargeur charge la batterie moteur même coupe-circuit moteur ouvert, ce qui est voulu au quai.

### Fusible de batterie : décision du 05/10

**Décision de l'utilisateur : un fusible MEGA, pas de classe T.** Argument : le BMS limite le courant à 250 A ; sauf défaillance du BMS au même moment, un MEGA suffit.

Réserve, consignée pour mémoire (voir « Conséquences » ci-dessous) : la panne la plus courante d'un BMS est un transistor en court-circuit, qui ne se voit pas tant que tout va bien. Un court-circuit franc sur une batterie dont le BMS est déjà défaillant est donc moins improbable qu'une coïncidence de deux pannes. Une LiFePO4 de 200 Ah peut alors débiter plusieurs milliers d'ampères, au-delà du pouvoir de coupure d'un MEGA (environ 2 000 A sous 32 V). Un **fusible MRBF** vissé sur la borne (environ 10 000 A sous 14 V, bornes 5/16" ou 3/8", compatibilité avec les bornes M8 à vérifier) coûte à peu près le même prix qu'un MEGA avec son support et lève cette réserve sans classe T.

**Calibre : 300 A au lieu de 400 A** (proposé le 05/10, confirmé par l'utilisateur le 08/10). Le BMS coupe à 250 A : un fusible de 400 A ne servirait qu'en court-circuit. 300 A laisse passer tout ce que le BMS autorise, et respecte la règle des 150 % pour wire006 en 35 mm² (environ 210 A en continu) : l'écart accepté dans A-H2 pour wire006 disparaît, et wire006 en 50 mm² n'est plus nécessaire, même à long terme.

## Changements de câblage (à écrire dans `cablage.yaml`)

| Action | Éléments |
|---|---|
| Dépose | Coupe-circuit de couplage (node011, node012) ; wire010, wire011 |
| Remplacement | Guindeau : wire017 (node010, servitude) remplacé par wire217 (node004, côté charges du coupe-circuit moteur), 35 mm² |
| Dépose | Coupleur Scheiber (node013 à node015) ; wire002, wire007, wire014 ; wire164, wire165 et leurs fusibles de 40 A (A-H2) |
| Débranchement | Sortie 2 du chargeur de quai : wire008, wire163 et son fusible de 30 A (A-H2) |
| Remplacement | Sortie 1 du Dolphin : wire003, wire162 et leur fusible de 30 A (A-H2) déposés ; câble court jusqu'à un fusible de 30 A à la batterie moteur (node001). Négatif du Dolphin (wire005) ramené sur la borne − de la batterie moteur (node002) |
| Remplacement | Batterie de servitude : mêmes bornes (node007, node008), wire161 et wire009 repris |
| Ajout | Orion XS : entrée côté charges du coupe-circuit moteur (node004, 08/10), sortie sur la batterie de servitude (node009, ou node007 dans le coffre), masse côté « bord » du shunt ; fusibles MIDI de 70 A aux deux extrémités, câbles de 16 mm² (wire202 à wire206). Commande : interrupteur à voyant entre le + de l'entrée (fusible de 1 A sur node004) et la broche H, voyant au coupe-circuit des négatifs (node005) (wire207 à wire209, wire216) ; cavalier H-L retiré |
| Ajout | Chargeur de quai LiFePO4, avec le shunt (contremarche ou coffre de la batterie, sur place) : 230 V par un câble dédié depuis le disjoncteur du chargeur (C10) jusqu'à une prise ou un boîtier à bornes Wago (Q53), sortie 12 V courte avec fusible à sa source (node007 dans le coffre, node009 dans la contremarche), négatif côté « bord » du shunt |

## Conséquences

- **Fusible de batterie : il reste indispensable, BMS ou non** (question de l'utilisateur, 03/10).
  - **Le BMS n'est pas une protection de câble fiable.** Il coupe par des transistors (MOSFET), dont la panne la plus courante est le court-circuit : le BMS reste alors fermé et ne protège plus rien. C'est précisément dans ce cas, et sur un court-circuit franc, qu'il faut une coupure qui ne dépende pas d'une électronique. Les règles nautiques (ABYC E-11, et E-13 pour le lithium) demandent un fusible près de la batterie quel que soit le BMS.
  - **Pouvoir de coupure.** Si le BMS est en panne, une LiFePO4 de 100 Ah peut débiter plusieurs milliers d'ampères en court-circuit (environ 13 V sur quelques milliohms de résistance interne). Le fusible doit couper ce courant sans arc soutenu. Ordres de grandeur, à confirmer sur les fiches : MEGA environ 2 000 A sous 32 V, MRBF (fusible sur borne de batterie) 10 000 A sous 14 V, classe T 20 000 A. **Le MEGA prévu par A-H2 pour le plomb ne suffit pas** ; le MRBF ou la classe T conviennent. Le courant de court-circuit de la batterie choisie, s'il est donné sur sa fiche, tranche.
  - **Proposition du 03/10, non retenue (MEGA décidé le 05/10, voir ci-dessus) : un fusible MRBF vissé sur la borne + de la batterie.** Il remplace le fusible MEGA de A-H2 côté servitude (et son tronçon non protégé wire161), coûte bien moins cher qu'une classe T avec son support, et se place au plus près de la batterie, dans le coffre. La classe T reste la solution si la fiche de la batterie l'exige, ou pour une batterie de plus de 200 Ah.
  - **Calibre** : il protège le câble de 35 mm² (wire006) tout en laissant passer le guindeau et les pointes de consommation. Retenu : 300 A (voir « Fusible de batterie : décision du 05/10 »).
- **Étude D** : le SmartShunt se règle sur la chimie LiFePO4 ; l'alarme de charge basse prévient avant la coupure du BMS. Sans couplage et avec le guindeau sur la batterie moteur, ni le démarreur ni le guindeau ne traversent plus le shunt.
- **Bilan énergétique** : la capacité utile passe d'environ 55 Ah à 160-180 Ah. Le DC/DC consomme quelques milliampères en veille, sur la batterie moteur, et rien coupe-circuit moteur ouvert. Avec la masse de ses chargeurs côté charges du shunt, toute la charge de la LiFePO4 est comptée.
- **Coffre** : la LiFePO4 doit être solidement fixée (sangle, cales) et ses bornes protégées par un capot. Le coffre n'a plus besoin d'être ventilé pour le gaz, mais une LiFePO4 n'aime pas la chaleur : le coffre est contre le coffre moteur, température à surveiller.
- **Ancienne batterie** : à déposer en déchetterie ou chez un revendeur (reprise obligatoire).
