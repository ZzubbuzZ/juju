# A-H2 · Fusibles de batterie

Hypothèse de l'étude A. Base : le relevé, ou A-H1 si elle est retenue. Anomalies traitées : **A2** (aucun fusible en sortie des batteries) et **A4** (fils du coupleur et du chargeur sans fusible).

Nomenclature : [nomenclature.yaml](nomenclature.yaml). Le `cablage.yaml` et le folio seront faits une fois les calibres arrêtés.

## Principe

Un fusible protège le câble qui part de lui, et se place à sa source. Aujourd'hui, un court-circuit sur n'importe quel câble branché sur une batterie n'est coupé par rien.

### Batterie de servitude

- **Un fusible sur la borne +**, de type MRBF, vissé directement sur la borne. Il protège wire006 (35 mm²) et tout ce qui est en aval.
- **Calibre à arrêter, entre 150 et 250 A.** Il doit laisser passer, en même temps, le guindeau (50 A en courant normal, disjoncteur de 70 A), le tableau de la table à carte (fusible de 50 A dans H1) et le tableau Scheiber (30 A). Il doit aussi supporter un **démarrage de secours, coupe-circuit de couplage fermé** : la batterie de servitude alimente alors le démarreur, et un fusible de 150 A risque de fondre. Deux choix : dimensionner pour ce démarrage (250 A, à comparer à la tenue du câble de 35 mm²), ou accepter qu'un démarrage couplé ne soit possible que sur la batterie moteur. À trancher avec l'intensité du démarreur du 3GMD.

### Batterie moteur

Les normes nautiques dispensent le circuit du démarreur de fusible, à cause du courant de démarrage. Mais le risque est le même que côté servitude : wire001 fait 2 m, et s'il frotte contre une masse, rien ne coupe. **On pose donc aussi un fusible MRBF sur la borne + de la batterie moteur**, de calibre supérieur au courant de démarrage (250 à 300 A, à arrêter avec l'intensité du démarreur du 3GMD). Il ne fondra pas au démarrage, mais il coupera un court-circuit franc.

Les départs secondaires (coupleur, chargeur) doivent aussi être protégés : c'est l'objet de A4.

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

- Intensité du démarreur du Yanmar 3GMD (à ajouter aux questions si cette hypothèse est retenue).
- Calibre du coupleur Scheiber 38.14700.
