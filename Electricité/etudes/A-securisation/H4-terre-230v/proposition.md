# A-H4 · Terre 230 V

Hypothèse de l'étude A. Base : le relevé. Anomalie traitée : **A8** (terre 230 V et masse 12 V reliées nulle part, pas d'isolateur galvanique). Principes détaillés dans le [README de l'étude](../README.md#terre-230-v--bonnes-pratiques).

Nomenclature : [nomenclature.yaml](nomenclature.yaml). Le `cablage.yaml` et la mise à jour du folio 3 seront faits une fois l'hypothèse retenue.

## Principe

1. **Isolateur galvanique** en série sur le conducteur de terre, juste après la prise de quai, dans le coffre de cockpit tribord : entre la terre de la prise (node205) et la barrette de terre du boîtier d'arrivée (node212), à la place de wire034.
2. **Liaison terre / masse 12 V en un point unique** : un fil vert-jaune de la barrette de terre du boîtier d'arrivée vers le négatif 12 V, **côté batteries du coupe-circuit des négatifs** (node005). Ainsi, la liaison n'est jamais ouverte par ce coupe-circuit. Le boîtier d'arrivée et la platine des coupe-circuits sont proches : quelques mètres de fil suffisent.

## Variante : ne pas relier la terre à la masse 12 V

C'est un choix défendable, et répandu. Le différentiel 30 mA protège les personnes dans le cas le plus courant : un appareil 230 V en défaut, touché par quelqu'un. Sans liaison, il n'y a pas non plus de chemin galvanique vers les autres bateaux, donc pas besoin d'isolateur.

Ce que la liaison apporte en plus : si un défaut met du 230 V sur le circuit 12 V (panne interne du chargeur ou de l'EPS 100), tout le 12 V, y compris le bloc moteur, passe à 230 V par rapport à l'eau. Sans liaison, le différentiel ne déclenche qu'au moment où un courant s'écoule vers la terre, par exemple à travers quelqu'un qui touche le moteur. Il coupera alors dès que la fuite dépasse 30 mA, en quelques dizaines de millisecondes, ce qui protège normalement la personne, mais après le contact. Avec la liaison, il coupe dès l'apparition du défaut, avant tout contact.

| | Avec liaison + isolateur | Sans liaison |
|---|---|---|
| Défaut 230 V sur un appareil touché | différentiel | différentiel |
| Défaut 230 V sur le circuit 12 V | coupure immédiate | coupure au premier contact |
| Corrosion par les autres bateaux | bloquée par l'isolateur | pas de chemin |
| Coût | environ 140 € | 0 € |
| Conformité ISO 13297 / ABYC E-11 | oui | non |

Dans les deux cas, **tester le différentiel régulièrement** avec son bouton de test.

## À ne pas confondre : couper la terre du ponton

Il y a deux « terres » à bord, et deux liaisons distinctes :

- **(1) terre du ponton ↔ terre 230 V du bord** : le conducteur vert-jaune du câble de quai, qui arrive aux prises, au chargeur et à l'EPS 100. **Elle existe et doit rester.**
- **(2) terre 230 V du bord ↔ masse 12 V** : c'est la liaison discutée plus haut. Elle n'existe pas aujourd'hui (A8).

**Ne pas faire (2)** est la variante ci-dessus : défendable. Et c'est elle qui supprime le problème de corrosion galvanique. Sans (2), aucune pièce immergée (hélice, arbre, anode, tous reliés au 12 V par le moteur) n'est reliée à la terre du ponton, donc aucun courant galvanique ne circule vers les autres bateaux. L'isolateur galvanique ne sert que si l'on fait (2).

**Ne pas faire (1)**, c'est-à-dire couper le vert-jaune à la prise de quai, est **à proscrire**. Ce conducteur est la protection principale des appareils à carcasse métallique. Aujourd'hui, si le chargeur a un défaut d'isolement, sa carcasse est reliée à la terre du ponton : le courant de défaut s'écoule et le différentiel déclenche aussitôt. Sans (1), la carcasse reste sous 230 V, sans rien déclencher, jusqu'à ce que quelqu'un la touche en étant en contact avec l'eau, le ponton ou une autre masse. Le différentiel coupera alors, mais c'est le corps de cette personne qui ferme le circuit. En cas de différentiel défaillant, rien ne la protège. C'est aussi contraire aux règles d'installation en port (NF C 15-100, section 709) et aux normes nautiques.

Le seul moyen d'isoler complètement le bord du ponton sans perdre la protection est un **transformateur d'isolement** : plusieurs centaines d'euros, et une trentaine de kilos. C'est disproportionné pour Juju.

**Conclusion** : garder (1), et choisir entre « (2) avec isolateur galvanique » et « ni (2) ni isolateur ». Dans les deux cas, pas de problème de corrosion galvanique.

## Selon la réponse à Q31

- **Disjoncteurs bipolaires** : si les disjoncteurs 10 A et 16 A ne coupent que la phase, les remplacer par des modèles phase + neutre. Jusqu'à 6 disjoncteurs (2 à l'arrivée, 2 par boîtier de distribution). Non chiffré tant que Q31 n'est pas tranchée.
- **Plafonnier** : s'il est métallique (classe I), raccorder le conducteur de terre déjà présent dans son câble 3 × 1,5 mm². Aucun achat.
