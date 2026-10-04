---
hypothese: E-H1
titre: Batterie LiFePO4, chargeur DC/DC et chargeur de quai dédié
etat: retenue
resume: Une batterie LiFePO4 de 100 Ah, avec BMS intégré, remplace le plomb dans le même coffre. Un chargeur DC/DC la charge depuis la batterie moteur, à la place du coupleur Scheiber, et le coupe-circuit de couplage est déposé. Au quai, un chargeur dédié la charge ; le Dolphin ne charge plus que la batterie moteur.
points_forts:
  - Plus d'hydrogène dans la cabine de poupe (A11 traitée à la source).
  - 80 à 90 Ah utiles au lieu d'environ 55, plus qu'une journée au mouillage.
  - Environ 10 kg au lieu de 25 à 30 kg ; plusieurs milliers de cycles.
  - Chaque batterie a son chargeur et son profil (DC/DC au moteur, chargeur dédié au quai pour la LiFePO4, Dolphin pour la batterie moteur seule). L'alternateur est protégé et la batterie moteur reste indépendante pour le démarrage.
points_faibles:
  - Environ 900 €, dont 185 € pour le chargeur de quai dédié.
  - Pas de charge en dessous de 0 °C (le BMS coupe la charge) ; sans conséquence en Méditerranée (Q47).
  - Le BMS peut couper toute la servitude en cas de surintensité ou de batterie vide, sans prévenir ; une alarme de charge basse (étude D) devient indispensable.
  - Le guindeau, environ 50 à 60 A, ne peut plus être secouru par la batterie moteur ; son pic de courant doit rester sous la limite du BMS.
  - Commande du DC/DC à choisir, après contact ou interrupteur (Q48) ; longueur du câble 12 V du second chargeur à relever (Q50).
decision: "02/10/2026 : retenue par Julie (batterie de servitude LiFePO4). 05/10 : batterie Humsienk 12 V 200 Ah Plus (BMS 250 A), Orion XS 12/12-50A et Blue Smart IP67 12/17 commandés ; fusible MEGA. Place de la batterie à vérifier (Q51). Reste à choisir le niveau de secours au démarrage (recharge de secours par le DC/DC seule, ou démarrage direct sur la LiFePO4), puis à écrire le câblage après le choix de la commande du DC/DC (Q48) et la longueur du câble du second chargeur (Q50) ; Q45, Q47 et Q49 répondues le 03/10."
---

# E-H1 · Batterie LiFePO4, chargeur DC/DC et chargeur de quai dédié

Hypothèse de l'étude E. Base : **A-H4** (programme retenu de l'étude A, avec les fusibles de A-H2).

Nomenclature : [nomenclature.yaml](nomenclature.yaml), environ **900 €**. Le câblage (`cablage.yaml`, folio) sera écrit si l'hypothèse est retenue, après le choix de la commande du DC/DC (Q48) et la longueur du câble du second chargeur (Q50). Réponses du 03/10 : place suffisante dans le coffre (Q45), pas de gel (Q47), second chargeur à côté du Dolphin (Q49).

## Principe

Une batterie LiFePO4 (lithium fer phosphate) ne dégage pas d'hydrogène en fonctionnement normal : la chimie ne produit pas de gaz à la charge, et le BMS (carte électronique intégrée) coupe la charge avant toute surtension. Elle peut donc rester dans le coffre de la cabine de poupe.

Elle impose en revanche une charge adaptée : tension d'absorption d'environ 14,2 à 14,6 V, pas de charge d'entretien prolongée (« floating ») au-dessus d'environ 13,5 V, pas de charge sous 0 °C. Elle ne doit pas non plus être mise en parallèle directe avec une batterie au plomb. D'où les trois modifications ci-dessous.

### 1. Déposer le coupe-circuit de couplage

Le coupe-circuit de couplage (node011, node012) met la batterie de servitude en parallèle avec la batterie moteur. Avec une LiFePO4, ce parallèle ferait passer un fort courant de l'une à l'autre (les tensions de repos diffèrent : environ 13,3 V pour la LiFePO4 et 12,7 V pour le plomb), et la LiFePO4 serait chargée par l'alternateur sans contrôle.

Il est donc déposé avec ses deux câbles de 35 mm² (wire010, wire011), **sauf si le démarrage direct sur la LiFePO4 est retenu** (voir « Démarrage de secours », niveau 2) : il devient alors un interrupteur de secours, à n'utiliser que coupe-circuit moteur ouvert. Sans lui, on ne peut plus démarrer sur la batterie de servitude, ni faire tourner le guindeau sur la batterie moteur. La batterie moteur, au plomb, reste dédiée au démarrage.

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
- **230 V** : le chargeur consomme environ 1,5 A ; avec le Dolphin (2,5 A au plus), un départ de 10 A suffit. Avec 16 A aux bornes du port, la puissance de quai n'est pas une contrainte.
- **Emplacement** : **près de la batterie de servitude, dans la cabine de poupe** (décision du 05/10, à la place du coffre de cockpit tribord envisagé avec Q49). C'est le 230 V qui fait le trajet d'environ 5 m (Q50), et non plus le 12 V. Voir « Chargeur de quai : Blue Smart IP67 12/17 » ci-dessous.

**Le DC/DC ne doit alors tourner qu'au moteur.** Sinon, l'absorption du Dolphin à 14,4 V le ferait démarrer (seuil d'usine 14,0 V) et l'on retrouverait le problème ci-dessus. La tension seule ne permet pas de distinguer l'alternateur (environ 14,2 à 14,4 V) du Dolphin (14,4 V). On commande donc le DC/DC par son **entrée « remote »**, reliée par un fil fin, protégé à sa source, à un + 12 V présent seulement clé de contact tournée (Q48). Sa détection de tension reste active avec les réglages d'usine : clé tournée mais moteur arrêté, il ne tire rien sur la batterie moteur.

**Commande du DC/DC (Q48, 03/10).** Le + après contact du tableau moteur est pris sur la batterie moteur. Ce n'est pas un obstacle : les deux batteries ont leur négatif en commun (coupe-circuit des négatifs, node005), et l'entrée « remote » de l'Orion XS ne demande qu'une tension positive par rapport à ce négatif commun. L'écart de tension entre les deux batteries, quelques dixièmes de volt, est sans effet. Deux câblages possibles :

| | Commande | Fil à tirer | Inconvénient |
|---|---|---|---|
| a | Automatique : + après contact du tableau moteur | Un fil fin du tableau moteur à l'Orion XS, près de la platine des coupe-circuits, avec un fusible de 1 A à sa source | Trajet du tableau moteur à la platine à relever |
| b | Manuelle : interrupteur à la table à carte | Un départ du tableau de servitude vers l'Orion XS, environ 3 m ; l'interrupteur peut être alimenté par le + de la servitude, sans fil + moteur | Un oubli au port laisse l'Orion XS démarrer sur la charge du Dolphin et maintenir la batterie moteur en absorption |

Proposition : **a**, qui ne demande aucune manœuvre et ne dépend pas d'un oubli.

## Démarrage de secours sur la LiFePO4

Question de l'utilisateur (02/10) : peut-on démarrer le moteur sur la LiFePO4 si la batterie moteur est en panne ? Oui, à deux niveaux.

### Niveau 1 : recharge de secours de la batterie moteur par le DC/DC (sans matériel)

L'Orion XS a une fonction **« emergency reverse charge »** : lancée depuis l'application VictronConnect, elle fait passer le courant **dans l'autre sens**, de la LiFePO4 vers la batterie moteur, pendant 15 minutes, puis annonce « Battery ready » après 5 minutes de repos (notice Victron). Le courant est la moitié du courant nominal, soit **25 A pour le modèle de 50 A**, environ 6 Ah transférés. La batterie de servitude n'est pas descendue sous 12 V.

- Un démarrage de diesel consomme peu d'énergie (quelques secondes à 200-300 A, moins de 1 Ah) : 6 Ah suffisent à une batterie moteur **déchargée** (feux oubliés, longue immobilisation).
- La LiFePO4 ne fournit que 25 A : **aucune exigence de courant de pointe** sur son BMS.
- Limite, écrite dans la notice : « Battery ready » ne garantit pas que la batterie lance le moteur. Une batterie moteur **défectueuse** (élément en court-circuit, sulfatée) ne reprendra pas.

Ce niveau est acquis avec H1 telle qu'elle est chiffrée : il suffit de connaître la manœuvre.

### Niveau 2 : démarrage direct sur la LiFePO4 (option)

Pour couvrir aussi une batterie moteur défectueuse, le démarreur doit pouvoir être alimenté par la LiFePO4 seule.

**Le chemin existe déjà.** Le coupe-circuit de couplage ne relie pas la batterie de servitude à la batterie moteur, mais au côté démarreur du coupe-circuit moteur : node009 → wire011 → couplage → wire010 → node004, d'où partent le câble du démarreur (wire012) et celui de l'alternateur (même borne, node031). Coupe-circuit moteur **ouvert**, fermer le couplage alimente le démarreur par la LiFePO4 **sans** la mettre en parallèle avec le plomb. Il suffit donc de le **conserver** au lieu de le déposer.

**Exigences sur la batterie.** D'après le manuel d'atelier Yanmar (relevé, fiche du moteur), le démarreur consomme 60 A à vide, **200 à 275 A** à sa puissance maximale et **460 A rotor bloqué**, c'est-à-dire à l'instant du démarrage, pendant quelques centièmes de seconde. Il faut donc une batterie dont la fiche technique indique :

| Grandeur | Valeur minimale | Pourquoi |
|---|---|---|
| Courant de décharge de pointe du BMS | 300 A pendant au moins 5 s | lancement du moteur, quelques secondes à 200-275 A, avec une marge |
| Courant d'appel toléré | environ 500 A pendant moins de 0,5 s, sans déclencher la protection court-circuit | appel du démarreur à rotor bloqué |
| Courant continu du BMS | 150 à 200 A | le guindeau (50 à 60 A, davantage en tirant fort) et une marge |

Les batteries « de servitude » courantes à BMS de 100 A ne conviennent pas : leur protection coupe au-delà de 150 à 200 A en quelques secondes. Il faut un modèle annoncé pour le démarrage (courant de démarrage ou « CCA » donné par le fabricant) ou un BMS de 200 A, environ 100 à 150 € de plus que la batterie chiffrée (estimation, à vérifier sur les fiches). Le fusible de 400 A de A-H2 sur la batterie de servitude tient ces courants brefs ; son pouvoir de coupure reste à vérifier pour une LiFePO4 (voir « Conséquences »).

**Procédure** (à afficher près de la platine des coupe-circuits) :

1. Ouvrir le coupe-circuit **moteur** : la batterie moteur défaillante est isolée.
2. Fermer le coupe-circuit de **couplage** : la LiFePO4 alimente le démarreur.
3. Démarrer.
4. **Moteur tournant, ouvrir le couplage sans attendre.** Sinon l'alternateur charge la LiFePO4 sans contrôle, et si le BMS coupe pendant la charge, la surtension (« load dump ») peut détruire les diodes de l'alternateur.
5. Laisser le coupe-circuit moteur ouvert seulement si la batterie moteur est hors service ; sinon le refermer pour que l'alternateur la recharge.

**Risques et parades.**

- **Alternateur sans batterie** : entre les étapes 4 et 5, ou si la batterie moteur est hors service, l'alternateur tourne sans batterie, ce qu'il supporte mal. Parade : un **protecteur d'alternateur** (« alternator protection device », diode de suppression branchée sur sa sortie), environ 30 à 50 €.
- **Erreur de manœuvre** : couplage et coupe-circuit moteur fermés ensemble remettent les deux batteries en parallèle, ce que H1 voulait éviter. Parade : étiquette sur le couplage (« secours démarrage : coupe-circuit moteur ouvert »), et un coupe-circuit de couplage qui reste normalement ouvert.
- **Batterie de servitude vidée** : un lancement prolongé consomme peu, mais la servitude reste le seul secours ; ne pas insister au-delà de quelques essais.

**Coût du niveau 2** : environ 150 à 200 € de plus (batterie capable de démarrer, protecteur d'alternateur, étiquette), et le coupe-circuit de couplage conservé. Non compté dans la nomenclature tant que ce niveau n'est pas retenu.

### Recommandation

Le niveau 1 couvre le cas le plus fréquent, la batterie moteur déchargée, sans rien ajouter. Le niveau 2 ne se justifie que si l'on veut aussi parer à une batterie moteur défectueuse loin d'un port ; il impose une batterie plus chère, une procédure et une protection de l'alternateur. Choix à faire par Julie et l'utilisateur.

## Choix de la batterie

- **Capacité 100 Ah** : même encombrement environ que le plomb actuel ; le coffre a de la place (Q45), pour 80 à 90 Ah utiles. Une 150 ou 200 Ah se justifierait avec le solaire (étude C).
- **BMS intégré de 100 A au moins en continu** (150 à 200 A, avec un courant de pointe de démarrage, si le niveau 2 du démarrage de secours est retenu), avec un pic plus élevé pendant quelques secondes : le guindeau consomme 50 A en régime normal d'après sa notice, davantage en tirant fort sur la chaîne. Un BMS trop juste couperait tout le bord pendant la manœuvre de mouillage. À vérifier sur la fiche du modèle choisi, ou prendre une batterie de 150 A.
- **Protection basse température** (coupure de la charge sous 0 °C) et, si possible, **application Bluetooth** pour lire l'état des cellules.
- Les batteries Victron « NG » demandent un BMS externe (Lynx Smart BMS), ce qui double le prix : écartées pour un bord de cette taille.

## Batterie commandée (05/10)

**Humsienk 12 V 200 Ah Plus** (fiche du site du fabricant, relevée le 05/10) : 12,8 V, 200 Ah (2 560 Wh), BMS de **250 A en continu**, en décharge comme en charge ; charge recommandée 40 A, tension de charge 14,4 V ± 0,2 V ; charge entre 0 et 55 °C ; **521 × 238 × 221 mm, 26,4 kg**, bornes M8, IP65 ; Bluetooth et application ; 6 000 cycles à 80 % de profondeur. La fiche ne donne **ni courant de pointe ni courant de court-circuit**.

Ce que ce choix change par rapport à la batterie de 100 Ah étudiée :

- **Énergie** : environ 160 à 180 Ah utiles, soit **près de trois jours au mouillage** sans recharge (environ 60 Ah par jour d'après le bilan, à remplacer par des mesures avec le shunt de l'étude D). Le solaire (étude C) n'est plus indispensable pour tenir un week-end.
- **Encombrement et poids** : 52 cm de long et 26 kg, le poids du plomb actuel. Le gain de poids disparaît, et la place dans le coffre est **à vérifier avant la livraison** (Q51) : Q45 supposait une batterie de la taille du plomb de 110 Ah.
- **Guindeau** : 50 à 60 A, davantage en tirant fort, très en dessous des 250 A du BMS : plus de risque de coupure en pleine manœuvre.
- **Démarrage de secours, niveau 2** : le lancement (200 à 275 A pendant quelques secondes) est à la limite du courant continu du BMS, et l'appel de 460 A à rotor bloqué dépend d'un courant de pointe que la fiche ne donne pas. Le démarrage direct n'est donc **pas garanti** ; le niveau 1 (recharge de secours par l'Orion XS) reste la solution. Demander au fabricant le courant de pointe et sa durée avant de retenir le niveau 2.
- **Charge** : 14,4 V ± 0,2 V convient au Blue Smart (profil lithium) et à l'Orion XS. Les courants de charge (15 A au moteur, 17 A au quai) sont bien en dessous des 40 A recommandés.
- **Bluetooth** : le BMS donne déjà un état de charge sur son application. Ce que le SmartShunt de l'étude D apporte en plus est détaillé dans l'étude D.

### Chargeur de quai : Blue Smart IP67 12/17

À la place du Blue Smart IP65 12/15 prévu : 17 A au lieu de 15, et un boîtier étanche (IP67) aux câbles sortants. La version (1) ou (1+Si) se lit sur l'étiquette (Q52) : la sortie de maintien « Si » pourrait entretenir la batterie moteur, mais le Dolphin le fait déjà.

**Emplacement : près de la batterie (décision du 05/10).** Placé à côté du Dolphin, il aurait fallu 5 m de câble 12 V jusqu'à la batterie (Q50) : environ 10 mm² pour rester sous 3 % de chute à 17 A, soit deux câbles épais à faire passer à travers les cloisons. Placé près de la batterie, dans la cabine de poupe :

- **Côté 12 V**, le câble ne fait que quelques dizaines de centimètres : la chute de tension devient négligeable, la section est celle de la notice, et un **fusible à la batterie** (environ 25 A, selon la notice) le protège. Le + rejoint la borne + de la batterie, du côté batterie de son fusible de 300 A, pour que la charge reste possible coupe-circuit ouvert.
- **Le négatif doit revenir du côté « bord » du shunt** de l'étude D, sinon la charge n'est pas comptée. Avec le shunt à la platine (emplacement b de l'étude D), ce négatif remonte jusqu'à la platine, environ 1 m. Avec le shunt dans le coffre de la batterie (emplacement a), tout reste dans le coffre : ce choix fait pencher l'étude D vers l'emplacement a.
- **Côté 230 V**, c'est l'alimentation qui fait le trajet d'environ 5 m, mais elle ne transporte qu'environ 1,5 A : un câble 3 × 1,5 mm² (H07RN-F) suffit largement. Deux façons de l'alimenter (Q53) : un câble depuis le disjoncteur de 10 A du chargeur, dans le boîtier d'arrivée, à travers les cloisons jusqu'à la cabine de poupe ; ou une prise 230 V proche, si le Blue Smart est livré avec une fiche (prises de la table à carte et de l'armoire, à bâbord, sur le 16 A bâbord). Dans les deux cas, le chargeur reste derrière le différentiel de 30 mA.
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

**Calibre proposé : 300 A au lieu de 400 A.** Le BMS coupe à 250 A : un fusible de 400 A ne servirait qu'en court-circuit. 300 A laisse passer tout ce que le BMS autorise, et respecte la règle des 150 % pour wire006 en 35 mm² (environ 210 A en continu) : l'écart accepté dans A-H2 pour wire006 disparaît, et wire006 en 50 mm² n'est plus nécessaire, même à long terme.

## Changements de câblage (à écrire dans `cablage.yaml`)

| Action | Éléments |
|---|---|
| Dépose | Coupe-circuit de couplage (node011, node012) ; wire010, wire011. Conservés si le démarrage direct sur la LiFePO4 (niveau 2) est retenu |
| Dépose | Coupleur Scheiber (node013 à node015) ; wire002, wire007, wire014 ; wire164, wire165 et leurs fusibles de 40 A (A-H2) |
| Débranchement | Sortie 2 du chargeur de quai : wire008, wire163 et son fusible de 30 A (A-H2) |
| Remplacement | Sortie 1 du Dolphin : wire003, wire162 et leur fusible de 30 A (A-H2) déposés ; câble court jusqu'à un fusible de 30 A à la batterie moteur (node001). Négatif du Dolphin (wire005) ramené sur la borne − de la batterie moteur (node002) |
| Remplacement | Batterie de servitude : mêmes bornes (node007, node008), wire161 et wire009 repris |
| Ajout | Chargeur DC/DC : entrée sur la batterie moteur (côté batterie du coupe-circuit moteur, node003), sortie sur la batterie de servitude (node009), masse côté charges du shunt ; un fusible à chaque extrémité. Fil de commande « remote » depuis un + après contact, fusible à sa source |
| Ajout | Chargeur de quai LiFePO4, dans la cabine de poupe près de la batterie : 230 V depuis le disjoncteur de 10 A du chargeur ou une prise proche (Q53), sortie 12 V courte sur la borne + de la batterie de servitude (node007) avec fusible à la batterie, négatif côté « bord » du shunt |

## Conséquences

- **Fusible de batterie : il reste indispensable, BMS ou non** (question de l'utilisateur, 03/10).
  - **Le BMS n'est pas une protection de câble fiable.** Il coupe par des transistors (MOSFET), dont la panne la plus courante est le court-circuit : le BMS reste alors fermé et ne protège plus rien. C'est précisément dans ce cas, et sur un court-circuit franc, qu'il faut une coupure qui ne dépende pas d'une électronique. Les règles nautiques (ABYC E-11, et E-13 pour le lithium) demandent un fusible près de la batterie quel que soit le BMS.
  - **Pouvoir de coupure.** Si le BMS est en panne, une LiFePO4 de 100 Ah peut débiter plusieurs milliers d'ampères en court-circuit (environ 13 V sur quelques milliohms de résistance interne). Le fusible doit couper ce courant sans arc soutenu. Ordres de grandeur, à confirmer sur les fiches : MEGA environ 2 000 A sous 32 V, MRBF (fusible sur borne de batterie) 10 000 A sous 14 V, classe T 20 000 A. **Le MEGA prévu par A-H2 pour le plomb ne suffit pas** ; le MRBF ou la classe T conviennent. Le courant de court-circuit de la batterie choisie, s'il est donné sur sa fiche, tranche.
  - **Choix proposé : un fusible MRBF vissé sur la borne + de la batterie.** Il remplace le fusible MEGA de A-H2 côté servitude (et son tronçon non protégé wire161), coûte bien moins cher qu'une classe T avec son support, et se place au plus près de la batterie, dans le coffre. La classe T reste la solution si la fiche de la batterie l'exige, ou pour une batterie de plus de 200 Ah.
  - **Calibre** : il protège le câble de 35 mm² (wire006) tout en laissant passer le guindeau et les pointes de consommation. Environ 200 A sans le démarrage direct ; environ 300 A avec le niveau 2 du démarrage de secours, ce qui demandera de vérifier le câble (wire006 en 50 mm², déjà envisagé à long terme par A-H2). À fixer avec le câblage.
- **Étude D** : le SmartShunt se règle sur la chimie LiFePO4 ; l'alarme de charge basse prévient avant la coupure du BMS. Sans couplage, le démarreur ne traverse plus le shunt.
- **Bilan énergétique** : la capacité utile passe d'environ 55 Ah à 80-90 Ah. Le DC/DC consomme quelques milliampères en veille. Avec la masse de ses chargeurs côté charges du shunt, toute la charge de la LiFePO4 est comptée.
- **Coffre** : la LiFePO4 doit être solidement fixée (sangle, cales) et ses bornes protégées par un capot. Le coffre n'a plus besoin d'être ventilé pour le gaz, mais une LiFePO4 n'aime pas la chaleur : le coffre est contre le coffre moteur, température à surveiller.
- **Ancienne batterie** : à déposer en déchetterie ou chez un revendeur (reprise obligatoire).
