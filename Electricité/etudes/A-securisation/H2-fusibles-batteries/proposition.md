# A-H2 · Fusibles de batterie

Hypothèse de l'étude A. Base : le relevé, ou A-H1 si elle est retenue. Anomalies traitées : **A2** (aucun fusible en sortie des batteries) et **A4** (fils du coupleur et du chargeur sans fusible).

Nomenclature : [nomenclature.yaml](nomenclature.yaml). Le `cablage.yaml` et le folio seront faits une fois les calibres arrêtés.

## Principe

Un fusible protège le câble qui part de lui, et se place à sa source. Aujourd'hui, un court-circuit sur n'importe quel câble branché sur une batterie n'est coupé par rien.

### Ce que dit le démarreur

D'après le manuel d'atelier Yanmar : **60 A à vide, 200 à 275 A en démarrage normal** (zone de puissance maximale), et **460 A rotor bloqué**, pendant une fraction de seconde au lancement. Un fusible supporte largement plus que son calibre pendant quelques secondes. Un calibre de 300 A laisse donc passer un démarrage, y compris la pointe à 460 A, mais fond en quelques millisecondes sur un court-circuit franc, qui fait plusieurs milliers d'ampères. La courbe temps-courant du fusible choisi est à vérifier au moment de l'achat.

### Batterie moteur

Les normes nautiques dispensent le circuit du démarreur de fusible. Mais wire001 fait 2 m, et s'il frotte contre une masse, rien ne coupe. **Fusible MRBF de 300 A sur la borne +.** Il ne gêne pas le démarrage et coupe un court-circuit franc.

### Batterie de servitude

En temps normal, le circuit de servitude tire au plus 160 A environ : guindeau (50 A en courant normal), tableau de la table à carte (50 A), tableau Scheiber (30 A), pompe de cale. Mais il y a le **démarrage de secours** : on ferme le coupe-circuit de couplage parce que la batterie moteur est à plat, et c'est alors la batterie de servitude qui fournit seule les 200 à 275 A du démarreur, à travers son fusible.

| | Option A (recommandée) | Option B |
|---|---|---|
| Fusible de la batterie de servitude | 300 A | 200 A |
| Démarrage de secours couplé | possible | le fusible risque de fondre |
| wire006 (batterie → coupe-circuit, 1 m) | remplacé par du 50 mm², pour que le câble tienne le calibre du fusible | conservé en 35 mm² |
| Coût supplémentaire | environ 30 € (câble et cosses) | 0 € |

Un fusible doit rester adapté à la tenue du câble qu'il protège. Avec 300 A, le 35 mm² actuel est trop juste, d'où son remplacement dans l'option A ; il ne fait qu'un mètre. Les valeurs de tenue sont à confirmer dans les tables de la norme ISO 10133 au moment de l'achat. Avec l'option A, les deux batteries ont le même fusible : une seule référence de rechange à bord.

### Départs du coupleur et du chargeur (A4)

Quatre fils de 6 mm² partent directement des bornes côté batterie des coupe-circuits (node003 et node009) :

| Fil | Départ | Fusible proposé | Pourquoi |
|---|---|---|---|
| wire003 | chargeur, sortie batterie moteur | 30 A | le chargeur débite 20 A au plus |
| wire008 | chargeur, sortie batterie servitude | 30 A | idem |
| wire002 | coupleur, côté batterie moteur | 50 A | le coupleur transmet le courant de l'alternateur (environ 20 A), mais, à sa fermeture, deux batteries très inégales peuvent échanger davantage ; 50 A reste dans la tenue du 6 mm² |
| wire007 | coupleur, côté batterie servitude | 50 A | idem |

Les porte-fusibles se fixent près de la platine des coupe-circuits, dans la zone accessible par l'ouverture côté cabine de poupe.

## Questions liées

- Calibre du coupleur Scheiber 38.14700.
- Choix entre les options A et B pour la batterie de servitude.
