---
hypothese: B-H1
titre: Ballon Carbest CozyWater 10C sur le 230 V, circuit d'eau à pression réduite
etat: retenue
resume: Un ballon CozyWater 10C de 10 L (800 W en 230 V, 200 W en 12 V) chauffe l'eau au quai, branché sur une prise dédiée alimentée par le second C10 du boîtier tribord. Un réducteur de pression réglé à 1,5 bar à la sortie de la pompe met l'eau froide et l'eau chaude à la même pression, quelle que soit la coupure de la pompe ; un vase d'expansion de 1 L absorbe la dilatation de l'eau chaude pour que la soupape de 3 bar reste fermée. L'entrée 12 V n'est pas raccordée ici (B-H3).
points_forts:
  - Ballon commandé, panneau de commande à minuterie et soupape de 3 bar fournis.
  - 800 W en 230 V, environ 45 min pour chauffer 10 L de 15 à 60 °C ; 3,5 A seulement sur un C10.
  - "Eau froide et eau chaude à la même pression (1,5 bar) : mitigeurs équilibrés, pas de refoulement de l'eau froide vers le côté chaud."
  - La pression du circuit ne dépend plus de la coupure de la pompe, qui varie ; le réducteur amortit aussi les à-coups de la pompe.
  - La soupape ne goutte pas à chaque chauffe ; essai prévu jusqu'à 75 °C (environ 2,4 bar attendus).
  - Résistance 12 V de 200 W déjà dans le ballon, prête pour B-H3 (surplus solaire, LiFePO4 de l'étude E).
points_faibles:
  - Eau chaude au quai seulement, tant que B-H3 n'est pas câblée.
  - Sur une borne de 6 A, le ballon et les deux chargeurs dépassent la borne ; couper un chargeur pendant la chauffe.
  - Pression ramenée de 2,8 à 1,5 bar à tous les robinets, eau froide comprise.
  - Encombrement (270 × 400 × 290 mm) et fixations prévues pour 60 kg (Q19).
  - La notice exige une vidange complète à l'hivernage, même si le ballon n'a pas servi.
decision: "07/10/2026 : ballon Carbest CozyWater 10C commandé par l'utilisateur. Prise dédiée plutôt que câble coupé et raccordé au disjoncteur (Q56, notice). Réducteur à 1,5 bar à la sortie de la pompe, pour tout le circuit, et vase de 1 L gonflé à 1,4 bar, après mesure de la coupure de la pompe. Étude fusionnée dans main le 07/10 ; restent l'emplacement exact (Q19), le second C10 (Q42), le circuit d'eau existant (Q54) et les raccords (Q55)."
---

# B-H1 · Ballon CozyWater 10C sur le 230 V, circuit d'eau à pression réduite

Hypothèse de l'étude B. Base : **le relevé**. Câblage : [cablage.yaml](cablage.yaml) (prise dédiée sur le second C10).

Nomenclature : [nomenclature.yaml](nomenclature.yaml). Schémas : [folio 2l](folio-2l-cozywater-eau.svg) (circuit d'eau), [folio 2m](folio-2m-cozywater-230v.svg) (alimentation électrique). Notices : [ballon](../documentation/670600_670601_670604_carbest_boiler%20Cozywater.pdf), pages 59 à 71 en français ; [pompe](../../../releve/documentation/SEAFLO-Notice-pompe-41-series-SFDP1-045-040.pdf).

## Le ballon

| | CozyWater 10C (réf. 670604) |
|---|---|
| Volume | 10 L, cuve inox 304 isolée |
| Résistances | 800 W en 230 V, 200 W en 12 V ; le 230 V est choisi seul quand les deux tensions sont là |
| Température | réglable de 25 à 75 °C ; coupure de sécurité à 80 °C (code E4) ; arrêt en cas de marche à sec (E2) |
| Pression | 2,5 bar en service, 3 bar au plus ; soupape de 3 bar fournie, **à utiliser obligatoirement** |
| Dimensions, poids | 270 × 400 × 290 mm (Ø × L × H), 6,9 kg à vide, environ 17 kg plein |
| Pose | à plat, ou debout raccords vers le bas ; fixations pour 60 kg ; endroit sec et ventilé, **jamais recouvert ni isolé** |
| 230 V | câble avec fiche Schuko ; « uniquement une prise avec contact de protection », 16 A au plus, différentiel recommandé ; « aucune modification […] au câblage électrique » |
| 12 V | interrupteur et relais de 30 A, fusible de 30 A à la source, 6 mm² au moins (B-H3) |
| Commande | panneau fourni : marche, température, minuterie, codes d'erreur |

Deux écarts avec la fiche du revendeur ([Camping-Car Plus](https://www.camping-car-plus.com/chaud-froid-gaz/chauffages-chauffe-eau/chauffe-eau-electrique-carbest-cozywater-10l-12-230v-12938.html)), qui annonce 660 W en 230 V et une pose « horizontale uniquement ». Cette étude suit la notice ; la plaque du ballon tranchera (Q55). La fiche donne aussi des raccords de 1/2" mâle et un câble de 1,2 m, à vérifier à réception (Q55).

## Électricité : une prise dédiée (décision du 07/10)

Le ballon tire **3,5 A**. Le boîtier tribord a déjà ce que demande la notice : différentiel 30 mA à l'arrivée, puis des disjoncteurs de 10 et 16 A, sous les 16 A de la notice.

**Raccordement retenu** (folio 2m) : une **prise 16 A avec terre, compatible Schuko**, posée près du boîtier tribord, seule sur le **second C10** du boîtier (node306, node307), par un câble 3G1,5 de 1,5 m environ (wire300 / wire301 / wire302). Le ballon se coupe seul au disjoncteur, sans toucher aux prises du bord, comme avec un raccordement direct.

**Pourquoi pas le câble directement au disjoncteur** (proposition de l'utilisateur, Q56) : il faudrait couper la fiche, ce que la notice interdit (« aucune modification structurelle à l'appareil ou au câblage électrique », « uniquement une prise avec contact de protection »). La garantie en dépend sans doute. La prise dédiée coûte une quinzaine d'euros et garde la fiche intacte ; elle permet aussi de débrancher le ballon pour l'hivernage ou une intervention.

**Si le second C10 n'est pas libre** (Q42) : ajouter un disjoncteur 1P+N de 10 A dans le boîtier, s'il reste de la place sur le rail, ou à défaut brancher la prise dédiée sur le C16 des prises tribord. Seul le départ de wire300 change.

**Puissance au quai** (voir le README) : environ 650 W sans le ballon, avec les deux chargeurs de l'étude E, soit environ **1 450 W avec le ballon**.

| Borne | Disponible | Bilan |
|---|---|---|
| Saint-Chamas, 16 A | environ 3 700 W | sans contrainte |
| Escale à 10 A | environ 2 300 W | sans contrainte, sauf bouilloire |
| Escale à 6 A | environ 1 400 W | **juste** : couper un chargeur, ou chauffer quand les batteries sont pleines (les chargeurs ne tirent alors presque plus rien) |

La minuterie du panneau permet de chauffer la nuit ou en fin de charge.

## Eau : les réglages (restatués le 07/10)

### Le problème

La pompe du bord (Seaflo SFDP1-045-040) se coupe, d'après sa référence, à **40 psi, soit 2,8 bar**. Sa notice ne donne ni la coupure ni le redémarrage, et **la coupure observée à bord varie** (Q54). La soupape du ballon s'ouvre à **3 bar**, et une soupape de ce type commence souvent à goutter un peu avant : on vise **2,7 bar au plus**.

En chauffant, l'eau se dilate, et le ballon est enfermé entre la pompe et les robinets fermés :

| Chauffe de 10 L depuis 15 °C | jusqu'à 60 °C | jusqu'à 70 °C | jusqu'à 75 °C |
|---|---|---|---|
| Dilatation | 0,16 L | 0,22 L | 0,25 L |

Un vase d'expansion n'absorbe que ce qui entre entre la pression de repos du circuit et 2,7 bar. Avec une pompe qui laisse le circuit à 2,8 bar, il n'absorbe rien : la soupape rejetterait 0,15 à 0,25 L à chaque chauffe.

### Pourquoi la coupure variable de la pompe compte

Trois causes probables, que la notice de la pompe évoque :

- le **pressostat** est mécanique : sa coupure se décale avec l'usure et d'un cycle à l'autre ;
- le **bypass** de la pompe (« reduces cycling ») renvoie l'eau dans la pompe quand le débit est faible ; s'il s'ouvre près de la coupure, la pompe met plus ou moins longtemps à s'arrêter ;
- une **tension basse** (batterie en fin de décharge) empêche la pompe d'atteindre sa coupure (notice, « Pump fails to turn off »). La LiFePO4 de l'étude E, à tension plus stable, devrait réduire cet effet.

### Et si la coupure de la pompe était réglable ?

La notice de la pompe ne décrit qu'un réglage, celui du **bypass**, et demande de le confier à un professionnel : un mauvais réglage peut abîmer la pompe. Elle ne dit pas que le pressostat se règle. Supposons quand même qu'on puisse baisser la coupure à 1,7 bar, sans réducteur, avec un redémarrage vers 1 bar et le vase gonflé à 0,9 bar :

| Coupure de la pompe | Vase de 1 L : absorbe entre la coupure et 2,7 bar | Suffit pour 75 °C (0,25 L) ? |
|---|---|---|
| 1,7 bar, comme réglée | 0,19 L | non : il faudrait un vase de 2 L |
| 2,2 bar, si elle dérive de 0,5 bar | 0,08 L | non, la soupape rejette 0,17 L |
| 2,8 bar, comme aujourd'hui | 0 L | non |
| **Réducteur réglé à 1,5 bar** | **0,31 L, quelle que soit la coupure** | **oui** |

**Le réducteur reste justifié.** Sans lui, le volume absorbé dépend d'une coupure qui varie : c'est justement le défaut constaté. Le réducteur tient sa pression à 0,1 bar près, pour 34 €. Baisser la coupure ne servirait à rien de plus et toucherait à un réglage que la notice déconseille.

### Le circuit retenu : un réducteur pour tout le circuit

Le réducteur est placé **à la sortie de la pompe**, avant le premier té. Toute l'eau du bord, froide et chaude, est à 1,5 bar :

pompe (2,8 bar, variable) → flexible court → **réducteur 1,5 bar** → té vers les robinets d'eau froide et l'entrée froide des mitigeurs → **vanne d'arrêt** → té du **vase de 1 L** → **soupape 3 bar** → ballon → **vanne d'arrêt** → entrée chaude des mitigeurs.

Pourquoi à la sortie de la pompe plutôt que sur l'entrée du ballon seule (première version de B-H1) :

- **Mitigeurs équilibrés** : avec 2,8 bar à l'eau froide et 1,5 bar à l'eau chaude, l'eau froide l'emporte au mitigeur, la température varie, et l'eau froide peut refouler vers le côté chaud. À pressions égales, le mitigeur (thermostatique ou non) fonctionne comme prévu.
- **Pression stable partout**, malgré la coupure variable de la pompe.
- Le réducteur **amortit les à-coups** de la pompe à membrane, et soulage tuyaux et raccords.
- Contrepartie : l'eau froide passe de 2,8 à 1,5 bar. C'est la pression de nombreuses pompes de bateau ; le débit au robinet baisse un peu.

Règles du montage :

- **Aucun clapet anti-retour entre le vase et le ballon** : il isolerait le ballon du vase, et la soupape rejetterait de nouveau à chaque chauffe. Le vase est **après la vanne d'arrêt** du ballon : le ballon reste protégé même si on ferme cette vanne pendant une chauffe.
- **Rien entre la soupape et le ballon** (notice). Le tuyau de vidange de la soupape va vers un évier ou hors du bateau, jamais dans les fonds.
- **Flexible court entre la pompe et le réducteur** : la notice de la pompe demande un tuyau souple à sa sortie (vibrations) et déconseille les raccords métalliques directement sur la pompe.
- Les deux vannes d'arrêt (notice, « protection antigel ») résistent à l'eau chaude ; elles isolent le ballon pour la vidange, ou pour se servir de l'eau froide sans remplir un ballon vide.
- Le réducteur est en 1/2" : il réduit un peu le passage par rapport au tuyau de 19 mm demandé par la notice de la pompe, sans gêne au débit d'un bateau.

### Les réglages, dans l'ordre

1. **Mesurer la pompe.** Monter le réducteur réglé au maximum (4 bar) : sa sortie suit alors la pompe, et son manomètre la mesure (vérifier à réception qu'il est bien côté sortie). Ouvrir puis fermer un robinet une dizaine de fois, batterie au repos puis en charge, et noter chaque **coupure** et chaque **redémarrage**.
   - Coupure la plus basse **de 2 bar ou plus** : régler à 1,5 bar (étape 3).
   - Coupure la plus basse **entre 1,7 et 2 bar** : régler à 1,2 bar et gonfler le vase à 1,1 bar ; le vase absorbe alors 0,39 L, encore mieux.
   - Plus bas : la pompe a un problème (pressostat, bypass, tension) ; à traiter avant.
   - Le **redémarrage** n'impose rien au réglage : contrairement à ce qu'indiquait la première version, la pompe repasse par sa coupure à chaque cycle et remet toujours le réducteur à sa consigne. Il sert seulement à suivre l'état de la pompe.
2. **Gonfler le vase** à la consigne moins 0,1 bar, soit **1,4 bar**, circuit sans pression : pompe coupée au tableau, un robinet ouvert jusqu'à ce que l'eau ne coule plus. Valve de pneu, pompe à vélo à manomètre. Livré à 0,7 bar, il faut le regonfler.
3. **Régler le réducteur à 1,5 bar** : pompe en marche, ouvrir un robinet un instant, le refermer, lire la pression au repos ; ajuster et recommencer.
4. **Remplir et purger le ballon** (notice, page 65) : soupape fermée, levier horizontal ; un robinet sur chaud, ouvert jusqu'à ce que l'eau coule sans air ; vérifier l'étanchéité.
5. **Essai de chauffe** : robinets fermés, chauffer à 75 °C en suivant le manomètre. Attendu : **environ 2,0 bar à 60 °C et 2,4 bar à 75 °C**. La soupape ne doit pas goutter. Au-delà de 2,7 bar : regonfler le vase (étape 2) ou vérifier qu'aucun clapet ne l'isole.

Volume absorbé par le vase entre la consigne et 2,7 bar (loi de Boyle-Mariotte, pressions absolues) :

| Vase, réducteur à 1,5 bar | absorbe | couvre |
|---|---|---|
| 0,75 L (SFAT-075-125-01) | 0,23 L | une chauffe jusqu'à 70 °C, juste |
| **1 L (SFAT-100-125-01)** | **0,31 L** | une chauffe jusqu'à 75 °C, avec la dilatation des tuyaux |

**Mitigeur thermostatique (option)** : la notice recommande de chauffer à 70 °C au moins de temps en temps contre les bactéries. Un mitigeur thermostatique à la sortie du ballon limite l'eau au robinet vers 45 °C et prolonge la réserve. Avec des pressions égales, il fonctionne bien. À décider selon les robinets du bord (Q54).

Ces réglages seront repris dans la [documentation technique](../../../documentation-technique/README.md) (section « circuit d'eau », à écrire).

## À relever ou à confirmer

- **Q19** : emplacement exact du ballon dans le cabinet de toilette (réponse du 07/10 : a priori), avec la place pour le vase, la soupape et les vannes.
- **Q42** : le second C10 du boîtier tribord est-il libre ? Sinon, disjoncteur ajouté ou C16 des prises tribord.
- **Q54** : circuit d'eau existant (tuyau, robinets, mitigeurs) ; coupure et redémarrage de la pompe, mesurés avec le réducteur (étape 1).
- **Q55** (reformulée le 07/10) : à la livraison du ballon, filetage de ses raccords et de la soupape, longueur de ses trois câbles, puissance inscrite sur la plaque.
