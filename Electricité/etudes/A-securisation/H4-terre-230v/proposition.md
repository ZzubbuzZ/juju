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

**Ne pas faire (1)**, c'est-à-dire couper le vert-jaune à la prise de quai : que perd-on, puisque le différentiel 30 mA est en tête de tout le 230 V ?

Ce qu'il faut d'abord reconnaître : **le différentiel est bien la protection des personnes, et il fonctionne sans conducteur de terre.** Il compare le courant qui part par la phase à celui qui revient par le neutre. Si quelqu'un touche une carcasse sous tension en étant en contact avec l'eau, le ponton ou le quai, le courant qui le traverse revient à la source par la terre, pas par le neutre : le différentiel voit l'écart et coupe dès 30 mA, en quelques dizaines de millisecondes. C'est pour ce cas qu'il existe. Au ponton, la terre seule ne suffirait d'ailleurs sans doute pas à faire déclencher un disjoncteur ordinaire : dans les deux cas, c'est le différentiel qui coupe.

La vraie différence est donc **le moment où il coupe** :

| | Avec la terre du ponton (1) | Sans (1) |
|---|---|---|
| Un appareil à carcasse métallique a un défaut | le courant part par le vert-jaune, le différentiel coupe aussitôt, personne n'a rien touché | rien ne se passe : la carcasse reste sous tension, sans que personne le sache |
| Quelqu'un touche cette carcasse | rien, c'est déjà coupé | il reçoit une décharge, brève, que le différentiel coupe : normalement sans gravité, mais à bord, un sursaut peut suffire à une chute ou à un homme à la mer |
| Le différentiel est défaillant (collé, oxydé) | le défaut n'est pas coupé, mais la carcasse est reliée au ponton, ce qui limite sa tension | rien ne protège la personne |
| Fuites permanentes des filtres électroniques (chargeur, EPS 100) | écoulées par le vert-jaune | la carcasse « pique » légèrement au toucher |
| Corrosion galvanique | aucune, tant que la liaison (2) n'est pas faite | aucune |

**Conclusion** : sans (1), on garde la protection, mais on passe de deux protections indépendantes à une seule, et le défaut n'est découvert qu'au premier contact. Surtout, **on n'y gagne rien** : le problème de corrosion galvanique est déjà absent tant que la liaison (2) n'existe pas, ce qui est le cas aujourd'hui. Moins de sécurité pour aucun bénéfice : on garde (1).

Le différentiel porte donc presque tout. Deux vérifications s'imposent (Q36) :

- **son type** : un chargeur à découpage peut produire des fuites que le type AC détecte mal ; le type A est préférable ;
- **son fonctionnement** : appuyer sur le bouton de test en début de saison, puis régulièrement, en environnement salin.

Le seul moyen d'isoler complètement le bord du ponton sans rien perdre est un **transformateur d'isolement** : plusieurs centaines d'euros et une trentaine de kilos, disproportionné pour Juju.

**En résumé** : garder (1), et choisir entre « (2) avec isolateur galvanique » et « ni (2) ni isolateur ».

## Selon la réponse à Q31

- **Disjoncteurs bipolaires** : si les disjoncteurs 10 A et 16 A ne coupent que la phase, les remplacer par des modèles phase + neutre. Jusqu'à 6 disjoncteurs (2 à l'arrivée, 2 par boîtier de distribution). Non chiffré tant que Q31 n'est pas tranchée.
- **Plafonnier** : s'il est métallique (classe I), raccorder le conducteur de terre déjà présent dans son câble 3 × 1,5 mm². Aucun achat.
