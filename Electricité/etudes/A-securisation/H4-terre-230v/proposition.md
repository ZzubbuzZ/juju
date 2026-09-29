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
| Risque de corrosion galvanique par les autres bateaux | faible : l'isolateur bloque les tensions galvaniques (quelques dixièmes de volt) sous son seuil d'environ 1,2 V. Le risque redevient entier si l'isolateur claque en court-circuit, panne typique d'une diode, sans que rien ne le signale | nul : pas de chemin entre les pièces immergées et le ponton |
| Pièces touchées si le risque se réalise | les métaux immergés reliés au négatif 12 V : l'arbre et l'hélice par le moteur (si l'accouplement est métallique), l'anode si elle leur est reliée. L'anode se consomme d'abord, en quelques semaines au lieu d'une saison ; une fois usée, l'hélice (bronze) et l'arbre sont attaqués | aucune |
| Coût | environ 140 € | 0 € |
| Conformité ISO 13297 / ABYC E-11 | oui | non |

Pour situer l'isolateur : la liaison (2) **sans** isolateur mettrait les pièces ci-dessus en permanence en contact avec la terre du ponton, donc avec les pièces immergées de tous les bateaux branchés au quai. Le métal le moins noble de l'ensemble, souvent l'anode de Juju, se consommerait au profit des autres.

Deux points restent à vérifier à bord, car ils conditionnent la colonne « Sans liaison » :

- **Liaison cachée : écartée.** Certains chargeurs relient leur négatif de sortie à leur boîtier, donc à la terre, ce qui ferait exister la liaison (2) sans isolateur. Ce n'est le cas d'aucun des deux appareils : la notice du Dolphin annonce des sorties « isolées », et l'EPS 100 n'est pas relié à la terre (cordon à fiche deux contacts, Q38). Une mesure à l'ohmmètre le confirmerait sans frais : câble de quai débranché, entre la broche de terre de la prise de quai et le négatif 12 V, on doit lire un circuit ouvert.
- **Pièces immergées réellement reliées au 12 V** : présence et emplacement de l'anode, type d'accouplement de l'arbre, liaison éventuelle de la dérive en fonte, des passe-coques ou de la sonde du sondeur à la masse. Non relevé à ce jour.

Dans les deux cas, **tester le différentiel régulièrement** avec son bouton de test.

## Que contient un isolateur galvanique ?

Deux bornes seulement et un gros radiateur : ce n'est pas une arnaque, c'est ce qu'on attend de cet appareil.

- **Deux bornes**, parce qu'il se place en série sur un seul conducteur, la terre : une borne côté ponton, une borne côté bord. Il ne touche ni à la phase ni au neutre.
- **Dedans**, des diodes de puissance : deux branches montées tête-bêche, chacune de deux diodes en série. Sous environ 1,2 V, dans un sens comme dans l'autre, aucune ne conduit : les courants galvaniques, qui naissent de quelques dixièmes de volt, sont bloqués. Au-delà, elles conduisent : un courant de défaut 230 V, alternatif, passe dans les deux sens et fait déclencher les protections. Certains modèles ajoutent un condensateur en parallèle, pour laisser passer les petites fuites alternatives des filtres, ou un voyant de contrôle.
- **Le radiateur**, parce que ces diodes doivent conduire tout le courant de défaut, jusqu'à ce qu'une protection coupe, sans se détruire. Chaque diode dissipe environ 0,7 V fois le courant : à 16 A, une vingtaine de watts pour l'ensemble. D'où la taille du boîtier, et d'où le calibre de l'isolateur, à choisir au moins égal à celui de la protection d'arrivée : à vérifier sur la notice du modèle retenu, face au différentiel de 25 A de Juju.

Le prix paie surtout ce radiateur et la tenue garantie au courant de défaut. C'est ce qui distingue un isolateur sérieux d'un bloc de diodes premier prix : une diode qui lâche **en circuit ouvert** coupe la terre du ponton sans que rien ne le signale, et l'on perd la liaison (1) en croyant l'avoir. Une qui lâche en court-circuit ne fait que supprimer la protection galvanique.

Rappel : l'isolateur ne sert que si l'on fait la liaison (2). Dans la variante sans liaison, il n'a pas d'utilité.

## À ne pas confondre : couper la terre du ponton

Il y a deux « terres » à bord, et deux liaisons distinctes :

- **(1) terre du ponton ↔ terre 230 V du bord** : le conducteur vert-jaune du câble de quai, qui arrive aux prises et au chargeur (pas à l'EPS 100, dont le cordon n'a pas de terre). **Elle existe et doit rester.**
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
| Fuites permanentes des filtres électroniques (chargeur) | écoulées par le vert-jaune | la carcasse « pique » légèrement au toucher |
| Risque de corrosion galvanique | nul tant que la liaison (2) n'est pas faite (ou faite avec un isolateur) : la terre du ponton n'atteint que la carcasse du chargeur et les prises, hors de l'eau | nul |
| Pièces touchées | aucune pièce immergée | aucune |

**Conclusion** : sans (1), on garde la protection, mais on passe de deux protections indépendantes à une seule, et le défaut n'est découvert qu'au premier contact. Surtout, **on n'y gagne rien** : le problème de corrosion galvanique est déjà absent tant que la liaison (2) n'existe pas, ce qui est le cas aujourd'hui. Moins de sécurité pour aucun bénéfice : on garde (1).

Le différentiel porte donc presque tout. Deux vérifications s'imposent (Q36) :

- **son type** : un chargeur à découpage peut produire des fuites que le type AC détecte mal ; le type A est préférable ;
- **son fonctionnement** : appuyer sur le bouton de test en début de saison, puis régulièrement, en environnement salin.

Le seul moyen d'isoler complètement le bord du ponton sans rien perdre est un **transformateur d'isolement** : plusieurs centaines d'euros et une trentaine de kilos, disproportionné pour Juju.

**En résumé** : garder (1), et choisir entre « (2) avec isolateur galvanique » et « ni (2) ni isolateur ».

## Selon la réponse à Q31

- **Disjoncteurs bipolaires** : si les disjoncteurs 10 A et 16 A ne coupent que la phase, les remplacer par des modèles phase + neutre. Jusqu'à 4 disjoncteurs (2 à l'arrivée, 2 dans le boîtier tribord ; la boîte de dérivation bâbord n'en a pas). Non chiffré tant que Q31 n'est pas tranchée.
- **Plafonnier** : s'il est métallique (classe I), raccorder le conducteur de terre déjà présent dans son câble 3 × 1,5 mm². Aucun achat.
