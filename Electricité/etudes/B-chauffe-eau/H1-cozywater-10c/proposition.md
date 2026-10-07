---
hypothese: B-H1
titre: Ballon Carbest CozyWater 10C sur le 230 V, circuit d'eau à pression réduite
etat: retenue
resume: Un ballon CozyWater 10C de 10 L (800 W en 230 V, 200 W en 12 V) chauffe l'eau au quai, branché sur une prise du bord. Un réducteur de pression réglé à 1,5 bar et un vase d'expansion de 1 L, entre la pompe et le ballon, absorbent la dilatation de l'eau chaude pour que la soupape de 3 bar reste fermée. L'entrée 12 V n'est pas raccordée ici (B-H3).
points_forts:
  - Ballon commandé, panneau de commande à minuterie et soupape de 3 bar fournis.
  - 800 W en 230 V, environ 45 min pour chauffer 10 L de 15 à 60 °C ; 3,5 A seulement sur le C16 ou le C10 du boîtier tribord.
  - Résistance 12 V de 200 W déjà dans le ballon, prête pour B-H3 (surplus solaire, LiFePO4 de l'étude E).
  - Aucun fil 12 V ni 230 V à poser si une prise existante convient (Q56).
  - La soupape ne goutte plus à chaque chauffe, et le réducteur protège aussi le ballon des à-coups de la pompe.
points_faibles:
  - Eau chaude au quai seulement, tant que B-H3 n'est pas câblée.
  - Sur une borne de 6 A, le ballon et les deux chargeurs dépassent la borne ; couper un chargeur pendant la chauffe.
  - Pression réduite à 1,5 bar au robinet d'eau chaude, contre 2,8 bar à l'eau froide.
  - Encombrement (270 × 400 × 290 mm) et fixations prévues pour 60 kg (Q19).
  - La notice exige une vidange complète à l'hivernage, même si le ballon n'a pas servi.
decision: "07/10/2026 : ballon Carbest CozyWater 10C commandé par l'utilisateur. Réducteur de pression et vase de 1 L proposés par Claude, à confirmer. Emplacement (Q19), circuit d'eau existant (Q54), raccords (Q55) et prise (Q56) à relever."
---

# B-H1 · Ballon CozyWater 10C sur le 230 V, circuit d'eau à pression réduite

Hypothèse de l'étude B. Base : **le relevé**. Pas de `cablage.yaml` pour l'instant : si le ballon se branche sur une prise existante (Q56), aucun fil n'est ajouté. Un départ dédié (second C10, Q42) serait écrit ici une fois choisi.

Nomenclature : [nomenclature.yaml](nomenclature.yaml). Schéma : [folio 2l](folio-2l-cozywater.svg). Notice : [documentation/](../documentation/670600_670601_670604_carbest_boiler%20Cozywater.pdf), pages 59 à 71 en français.

## Le ballon

| | CozyWater 10C (réf. 670604) |
|---|---|
| Volume | 10 L, cuve inox 304 isolée |
| Résistances | 800 W en 230 V, 200 W en 12 V ; le 230 V est choisi seul quand les deux tensions sont là |
| Température | réglable de 25 à 75 °C ; coupure de sécurité à 80 °C (code E4) ; arrêt en cas de marche à sec (E2) |
| Pression | 2,5 bar en service, 3 bar au plus ; soupape de 3 bar fournie, **à utiliser obligatoirement** |
| Dimensions, poids | 270 × 400 × 290 mm (Ø × L × H), 6,9 kg à vide, environ 17 kg plein |
| Pose | à plat, ou debout raccords vers le bas ; fixations pour 60 kg ; endroit sec et ventilé, **jamais recouvert ni isolé** |
| 230 V | câble avec fiche Schuko ; prise avec terre, protégée par 16 A au plus, différentiel recommandé |
| 12 V | interrupteur et relais de 30 A, fusible de 30 A à la source, 6 mm² au moins (B-H3) |
| Commande | panneau fourni : marche, température, minuterie, codes d'erreur |

Deux écarts avec la fiche du revendeur ([Camping-Car Plus](https://www.camping-car-plus.com/chaud-froid-gaz/chauffages-chauffe-eau/chauffe-eau-electrique-carbest-cozywater-10l-12-230v-12938.html)), qui annonce 660 W en 230 V et une pose « horizontale uniquement ». Cette étude suit la notice ; la plaque du ballon tranchera (Q55). La fiche donne aussi des raccords de 1/2" mâle et un câble de 1,2 m, à vérifier à réception (Q55).

## Électricité : le 230 V suffit

Le ballon tire **3,5 A**. Le boîtier tribord a déjà ce que demande la notice : différentiel 30 mA à l'arrivée, puis le C16 des prises tribord, ou le second C10 s'il est libre (Q42). Les deux calibres restent sous les 16 A de la notice. Aucun calibre n'est à changer.

Reste la fiche Schuko : elle entre dans une prise française si la prise accepte les fiches hybrides, ce qui est le cas de la plupart des prises récentes. À vérifier sur la prise choisie (Q56). Sinon, remplacer la prise, pas la fiche : la notice interdit de modifier le câblage du ballon.

**Puissance au quai** (voir le README) : environ 650 W sans le ballon, avec les deux chargeurs de l'étude E, soit environ **1 450 W avec le ballon**.

| Borne | Disponible | Bilan |
|---|---|---|
| Saint-Chamas, 16 A | environ 3 700 W | sans contrainte |
| Escale à 10 A | environ 2 300 W | sans contrainte, sauf bouilloire |
| Escale à 6 A | environ 1 400 W | **juste** : couper un chargeur, ou chauffer quand les batteries sont pleines (les chargeurs ne tirent alors presque plus rien) |

La minuterie du panneau permet de chauffer la nuit ou en fin de charge.

## Eau : la question de la pression

### Le problème

La pompe du bord (Seaflo SFDP1-045-040, relevé) se coupe à **40 psi, soit 2,8 bar**. La soupape du ballon s'ouvre à **3 bar**, et une soupape de ce type commence souvent à goutter un peu avant.

En chauffant, l'eau se dilate, et le ballon est enfermé entre le clapet de la pompe et le robinet fermé :

| Chauffe de 10 L depuis 15 °C | jusqu'à 60 °C | jusqu'à 70 °C | jusqu'à 75 °C |
|---|---|---|---|
| Dilatation | 0,16 L | 0,22 L | 0,25 L |

Après un puisage, la pompe remet le circuit à 2,8 bar. Il ne reste que 0,1 à 0,2 bar avant la soupape. Dans cette plage, un vase d'expansion n'absorbe presque rien, quels que soient sa taille et son gonflage : environ 0,02 L pour un vase de 0,75 L. La soupape rejetterait donc 0,15 à 0,25 L à chaque chauffe, et goutterait peut-être sans chauffe, aux à-coups de la pompe.

### La solution : réduire la pression du ballon

1. **Réducteur de pression réglé à 1,5 bar** sur l'arrivée d'eau froide du ballon, après le té qui alimente les robinets d'eau froide. Le réducteur se ferme dès que la pression en aval dépasse son réglage : il isole le ballon de la pompe.
2. **Vase d'expansion de 1 L** entre le réducteur et le ballon, **gonflé à 1,4 bar** (réglage du réducteur moins 0,1 bar), mesuré circuit vidé et sans pression, à la valve de pneu.
3. **Soupape de 3 bar** sur l'entrée du ballon, comme le demande la notice, son tuyau de vidange conduit hors du bateau ou dans un évier, jamais dans les fonds.

Volume absorbé par le vase entre 1,5 et 2,7 bar (loi de Boyle-Mariotte, pressions absolues) :

| Vase | absorbe | couvre |
|---|---|---|
| 0,75 L (SFAT-075-125-01) | 0,23 L | une chauffe jusqu'à 70 °C, juste |
| **1 L (SFAT-100-125-01)** | **0,31 L** | une chauffe jusqu'à 75 °C, avec la dilatation des tuyaux |

D'où le vase de 1 L. Les deux sont livrés gonflés à 0,7 bar : il faut les regonfler. Le vase est sur l'eau froide, il ne voit pas l'eau chaude.

Le réglage de 1,5 bar est un point de départ : il doit rester sous la pression de redémarrage de la pompe, sinon la pompe ne remplit plus le vase. Elle est à mesurer (Q54) ; le manomètre du réducteur suffit pour ça.

**Variante écartée** : changer la pompe pour une pompe à coupure basse (1,5 bar environ). Elle baisserait aussi la pression à l'eau froide et coûterait plus cher que le réducteur.

### Le circuit

Dans l'ordre, de la pompe au robinet (folio 2l) :

pompe (2,8 bar) → té vers les robinets d'eau froide → **vanne d'arrêt** → **réducteur 1,5 bar** → té du **vase de 1 L** → **soupape 3 bar** → ballon → **vanne d'arrêt** → mitigeur.

Les deux vannes d'arrêt sont demandées par la notice (« protection antigel ») : elles isolent le ballon pour le vidanger à l'hivernage, ou pour se servir de l'eau froide sans remplir un ballon vide. Elles doivent résister à l'eau chaude.

**Mitigeur thermostatique (option)** : la notice recommande de chauffer à 70 °C au moins de temps en temps contre les bactéries. Un mitigeur thermostatique à la sortie du ballon limite l'eau au robinet vers 45 °C. Il prolonge aussi la réserve, puisque l'eau très chaude est mélangée à l'eau froide. À décider selon les robinets du bord (Q54).

## À relever ou à confirmer

- **Q19** : emplacement du ballon, avec la place pour le réducteur, le vase et les vannes.
- **Q42** : le second C10 du boîtier tribord est-il libre ? Un départ dédié permettrait de couper le ballon seul.
- **Q54** : circuit d'eau existant, robinets, pression de redémarrage de la pompe.
- **Q55** : raccords et câbles du ballon, à sa réception.
- **Q56** : prise 230 V à utiliser, compatible avec la fiche Schuko.
