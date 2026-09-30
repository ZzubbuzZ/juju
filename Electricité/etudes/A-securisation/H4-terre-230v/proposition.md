# A-H4 · Terre 230 V

Hypothèse de l'étude A. Base : le relevé. Anomalie traitée : **A8** (terre 230 V et masse 12 V reliées nulle part, pas d'isolateur galvanique). Principes détaillés dans le [README de l'étude](../README.md#terre-230-v--bonnes-pratiques).

Nomenclature : [nomenclature.yaml](nomenclature.yaml). Le `cablage.yaml` et la mise à jour du folio 3 restent à faire.

## Décision du 30/09

- **Terre du ponton ↔ terre du bord (1)** : conservée, à travers un **[isolateur galvanique maison](#isolateur-maison-retenu)**, à la place de wire034.
- **Liaison terre / masse 12 V (2)** : **non faite**. Un défaut 230 V sur le circuit 12 V s'écoule par l'arbre, l'hélice et l'eau, et fait déclencher le différentiel sans attendre un contact (voir la variante ci-dessous), à condition que l'arbre soit relié électriquement au moteur : **à vérifier depuis le bord** (Q40 : accouplement entre l'arbre de l'inverseur et l'arbre d'hélice, câble de masse sur le tube d'étambot).
- L'isolateur est donc aujourd'hui une **précaution** : tant que (2) n'existe pas, il n'y a aucun courant galvanique à bloquer. Il servira si une liaison apparaît plus tard : chauffe-eau de l'étude B en H3, ou appareil dont le négatif serait relié au boîtier.
- **Transformateur d'isolement** : écarté.
- **Différentiel d'arrivée** : [remplacé par un type A](#remplacement-du-différentiel-darrivée-q36) (Q36).
- **Disjoncteurs** : tous coupent déjà la phase et le neutre (Q31), aucun achat.

## Principe étudié

La décision ne retient que le point 1, avec un isolateur maison ; le point 2 reste décrit pour mémoire.

1. **Isolateur galvanique** en série sur le conducteur de terre, juste après la prise de quai, dans le coffre de cockpit tribord : entre la terre de la prise (node205) et la barrette de terre du boîtier d'arrivée (node212), à la place de wire034.
2. **Liaison terre / masse 12 V en un point unique** : un fil vert-jaune de la barrette de terre du boîtier d'arrivée vers le négatif 12 V, **côté batteries du coupe-circuit des négatifs** (node005). Ainsi, la liaison n'est jamais ouverte par ce coupe-circuit. Le boîtier d'arrivée et la platine des coupe-circuits sont proches : quelques mètres de fil suffisent.

## Variante : ne pas relier la terre à la masse 12 V

C'est un choix défendable, et répandu. Le différentiel 30 mA protège les personnes dans le cas le plus courant : un appareil 230 V en défaut, touché par quelqu'un. Sans liaison, il n'y a pas non plus de chemin galvanique vers les autres bateaux, donc pas besoin d'isolateur.

Ce que la liaison apporte en plus : si un défaut met du 230 V sur le circuit 12 V (panne interne du chargeur ou de l'EPS 100), tout le 12 V, y compris le bloc moteur, passe à 230 V par rapport à l'eau. Avec la liaison, le courant de défaut part par le vert-jaune et le différentiel coupe aussitôt.

Sans liaison, il coupe aussi sans attendre un contact, **si une pièce reliée au 12 V trempe dans l'eau**. Le courant s'écoule alors par l'arbre, l'hélice et le tube d'étambot, puis par l'eau jusqu'à la terre, sans repasser par le neutre : le différentiel voit le déséquilibre et coupe dès 30 mA. L'eau de mer, et même l'eau saumâtre de l'étang de Berre, conduit assez pour que ce courant dépasse largement ce seuil. **L'avantage de la liaison disparaît donc pratiquement**, pourvu que l'arbre soit relié électriquement au moteur : accouplement métallique, sans manchon isolant (voir les pièces immergées ci-dessous). Sinon, le différentiel ne coupe qu'au moment où un courant traverse quelqu'un qui touche le moteur : après le contact.

Le tableau compare aussi une troisième variante, le [transformateur d'isolement](#variante--transformateur-disolement), décrite plus bas.

| | Avec liaison + isolateur | Sans liaison (retenue, avec isolateur en précaution) | Transformateur d'isolement (écarté) |
|---|---|---|---|
| Défaut 230 V sur un appareil touché | différentiel | différentiel | différentiel |
| Défaut 230 V sur le circuit 12 V | coupure immédiate | coupure immédiate si l'arbre est relié au moteur (fuite par l'hélice et l'eau) ; sinon, au premier contact | coupure immédiate |
| Risque de corrosion galvanique par les autres bateaux | faible : l'isolateur bloque les tensions galvaniques (quelques dixièmes de volt) sous son seuil d'environ 1,2 V. Le risque redevient entier si l'isolateur claque en court-circuit, panne typique d'une diode, sans que rien ne le signale | nul : pas de chemin entre les pièces immergées et le ponton | nul : aucun conducteur ne relie le bord au ponton, la terre du quai s'arrête au transformateur |
| Pièces touchées si le risque se réalise | les métaux immergés reliés au négatif 12 V : l'arbre et l'hélice par le moteur (si l'accouplement est métallique), l'anode si elle leur est reliée. L'anode se consomme d'abord, en quelques semaines au lieu d'une saison ; une fois usée, l'hélice (bronze) et l'arbre sont attaqués | aucune | aucune |
| Inversion phase / neutre à la prise du ponton | à couvrir par des disjoncteurs phase + neutre (Q31) | idem | sans effet à bord : le neutre est défini au secondaire |
| Poids et place | un boîtier de la taille d'une main | rien | environ 10 kg pour le modèle de 2 000 W |
| Au ponton de 6 A | sans effet | sans effet | courant d'appel à la mise sous tension : un modèle à démarrage progressif est indispensable |
| Coût | environ 140 € (60 € en fabrication maison, module de rechange compris) | 0 € | environ 430 € |
| Conformité ISO 13297 / ABYC E-11 | oui | non | oui |

Pour situer l'isolateur : la liaison (2) **sans** isolateur mettrait les pièces ci-dessus en permanence en contact avec la terre du ponton, donc avec les pièces immergées de tous les bateaux branchés au quai. Le métal le moins noble de l'ensemble, souvent l'anode de Juju, se consommerait au profit des autres.

Deux points restent à vérifier à bord, car ils conditionnent la colonne « Sans liaison » :

- **Liaison cachée : écartée.** Certains chargeurs relient leur négatif de sortie à leur boîtier, donc à la terre, ce qui ferait exister la liaison (2) sans isolateur. Ce n'est le cas d'aucun des deux appareils : la notice du Dolphin annonce des sorties « isolées », et l'EPS 100 n'est pas relié à la terre (cordon à fiche deux contacts, Q38). Une mesure à l'ohmmètre le confirmerait sans frais : câble de quai débranché, entre la broche de terre de la prise de quai et le négatif 12 V, on doit lire un circuit ouvert.
- **Pièces immergées réellement reliées au 12 V** (Q40) : type d'accouplement entre l'arbre de l'inverseur et l'arbre d'hélice, câble de masse sur le tube d'étambot, anode ; liaison éventuelle de la dérive en fonte, des passe-coques ou de la sonde du sondeur à la masse. Tout se vérifie depuis le bord.

Dans tous les cas, **tester le différentiel régulièrement** avec son bouton de test.

## Variante : transformateur d'isolement

**Écartée le 30/09**, pour son prix. Décrite pour mémoire.

Au lieu de filtrer la terre du quai, on coupe tout lien électrique entre le bord et le ponton : l'énergie passe par le champ magnétique d'un transformateur 230 V / 230 V, et le bord crée son propre réseau.

1. **Primaire, côté quai** : le transformateur se place entre la prise de quai et le boîtier d'arrivée, dans le coffre de cockpit tribord. La phase et le neutre du quai arrivent au primaire à travers un disjoncteur phase + neutre (intégré à certains modèles). La terre du quai ne va qu'à l'écran placé entre les deux enroulements, et au boîtier selon le modèle : suivre sa notice. Elle ne pénètre pas plus loin à bord ; wire034 disparaît.
2. **Secondaire, côté bord** : un des deux fils du secondaire devient le neutre du bord, relié à la terre du bord au transformateur. C'est la liaison terre-neutre qu'on ne pouvait pas faire à bord sans transformateur (voir le cas du chauffe-eau) : ici, le bord définit lui-même son neutre, et l'inversion au ponton ne compte plus. Le différentiel 30 mA existant reste en aval, dans le boîtier d'arrivée : un courant de défaut qui part vers la terre du bord revient au secondaire par la liaison terre-neutre, sans repasser par le différentiel, qui coupe.
3. **Liaison terre du bord ↔ masse 12 V** (node005), comme au point 2 du principe. Elle ne pose plus de problème de corrosion, puisque la terre du bord ne touche plus le ponton : on garde la coupure immédiate d'un défaut 230 V sur le circuit 12 V, sans isolateur.

**Ce qu'il règle** : la corrosion galvanique par le ponton, sans diodes ni risque de panne silencieuse ; l'inversion phase / neutre ; la liaison terre / masse 12 V ; le ballon à double résistance de l'étude B (H3), sans restriction.

**Ce qu'il coûte** :

- **Prix** : 381,60 € TTC pour le Victron 2000 W avec démarrage progressif (ITR040202041, prix remisé relevé sur mon-camping-car.com le 30/09), environ 430 € avec le raccordement.
- **Poids et place** : environ 10 kg pour ce modèle, à loger près de la prise de quai.
- **Puissance** : un modèle de 2 000 W couvre largement la prise de 6 A de Saint-Chamas (1 400 W). Sur une borne de 16 A, il limitera le bord à ses 2 000 W : suffisant pour un chauffe-eau de 500 W, le chargeur et le frigo. Un modèle de 3 600 W lève la limite, au prix d'une dizaine de kilos de plus.
- **Courant d'appel** : à la mise sous tension, un transformateur appelle un courant bien supérieur à son courant nominal. Sur une borne de 6 A, cela suffit à la faire déclencher : un démarrage progressif (« soft start ») est indispensable, à vérifier sur la fiche du modèle.
- **Pertes** : quelques dizaines de watts consommés en permanence tant que le bord est branché, même sans rien d'allumé.

## Que contient un isolateur galvanique ?

Deux bornes seulement et un gros radiateur : ce n'est pas une arnaque, c'est ce qu'on attend de cet appareil.

- **Deux bornes**, parce qu'il se place en série sur un seul conducteur, la terre : une borne côté ponton, une borne côté bord. Il ne touche ni à la phase ni au neutre.
- **Dedans**, des diodes de puissance : deux branches montées tête-bêche, chacune de deux diodes en série. Sous environ 1,2 V, dans un sens comme dans l'autre, aucune ne conduit : les courants galvaniques, qui naissent de quelques dixièmes de volt, sont bloqués. Au-delà, elles conduisent : un courant de défaut 230 V, alternatif, passe dans les deux sens et fait déclencher les protections. Certains modèles ajoutent un condensateur en parallèle, pour laisser passer les petites fuites alternatives des filtres, ou un voyant de contrôle.
- **Le radiateur et les grosses diodes** répondent à deux cas qui ne se produisent que si le différentiel ne fait pas son travail, ou à l'instant du défaut :
  - **la pointe d'un défaut franc** : une phase qui touche une carcasse fait passer dans la terre plusieurs centaines d'ampères, voire davantage, pendant les quelques dizaines de millisecondes que met le différentiel à couper. Les diodes doivent encaisser cette pointe sans s'ouvrir : c'est une question de taille de puce, pas de radiateur ;
  - **un défaut qui dure** : si le différentiel est défaillant, ou absent comme sur beaucoup de bateaux (les normes, ABYC A-28 notamment, sont écrites pour ce cas), un défaut résistif peut faire passer dans la terre un courant juste inférieur au calibre d'un disjoncteur, sans que rien ne coupe. L'isolateur doit alors le supporter indéfiniment : environ 1,5 V × 16 A, soit 20 à 25 W en continu, dans un coffre fermé et chaud, sans ventilation. D'où le radiateur, dimensionné avec une marge large pour que les diodes restent froides.

Le prix paie surtout cette tenue garantie. C'est ce qui distingue un isolateur sérieux d'un bloc de diodes premier prix : une diode qui lâche **en circuit ouvert** coupe la terre du ponton sans que rien ne le signale, et l'on perd la liaison (1) en croyant l'avoir. Une qui lâche en court-circuit ne fait que supprimer la protection galvanique.

### Quel modèle ?

À Juju, avec un différentiel de 30 mA en tête, le courant de défaut ne dure normalement que quelques dizaines de millisecondes : le calibre en continu ne sert qu'en secours, si le différentiel est défaillant. Le calibre du différentiel (25 A) n'entre donc pas en compte ; c'est celui des disjoncteurs de départ (10 et 16 A) qui fixe le courant qu'un défaut durable peut faire passer. Critères :

1. **Calibre de 16 A** : suffisant, puisqu'aucun départ n'est protégé au-delà de 16 A. La mention « à choisir au moins égal au différentiel de 25 A » d'une version précédente était trop prudente.
2. **Défaillance en court-circuit garantie**, jamais en circuit ouvert (« fail-safe » au sens d'ABYC A-28) : c'est le critère principal, à lire sur la fiche technique. À défaut, un **voyant ou un contrôleur d'état**, qui signale une diode ouverte.
3. Un **condensateur intégré** est un plus, pas une nécessité : il écoule les petites fuites alternatives des filtres du chargeur sans décaler le seuil des diodes.

Le Victron VDI-16 satisfait le premier critère ; le deuxième est à vérifier sur sa fiche. Un montage maison coûte bien moins cher, mais sans garantie de fabricant sur la tenue à la pointe de défaut ni sur le mode de défaillance : il faut compenser par des diodes largement dimensionnées et un contrôle régulier. C'est la solution retenue.

### Isolateur maison (retenu)

**Composant** : un **pont redresseur monophasé de puissance**, en module à bornes à vis et semelle métallique, de 100 A et 1 000 V au moins, avec un courant de pointe admissible (IFSM) d'au moins 1 000 A. Un pont contient exactement les quatre diodes d'un isolateur : en reliant ses bornes + et − par un pont de cuivre, les deux bornes « ~ » deviennent les deux bornes de l'isolateur, avec deux diodes en série dans chaque sens. Un petit pont de 35 ou 50 A (IFSM de 400 A) tiendrait le courant permanent, mais pas avec certitude la pointe d'un défaut franc pendant le temps de coupure du différentiel : on prend large, l'écart de prix est de quelques euros.

**Montage** :

1. Le module sur un radiateur en aluminium, avec de la pâte thermique, dans un boîtier étanche fixé près de la prise de quai, dans le coffre de cockpit tribord.
2. Borne « ~ » 1 : la terre de la prise de quai (node205). Borne « ~ » 2 : la barrette de terre du boîtier d'arrivée (node212). Les deux fils en vert-jaune 2,5 mm², comme le reste de la terre ; ils remplacent wire034.
3. Repérer le boîtier : « Isolateur galvanique : à contrôler chaque saison ».

**Contrôle**, à inscrire dans l'entretien, en début de saison et après tout déclenchement du différentiel sur un défaut : câble de quai débranché, multimètre en position « diode » entre les deux bornes « ~ », dans un sens puis dans l'autre.

| Lecture | Signification | Que faire |
|---|---|---|
| environ 0,9 à 1,2 V dans les deux sens | correct | rien |
| 0 V, ou presque, dans un sens au moins | diode en court-circuit : la terre passe, la protection galvanique est perdue | remplacer le module, sans urgence |
| « OL » (circuit ouvert) dans un sens au moins | diode ouverte : **la terre du ponton ne passe plus** | ne plus brancher le bord au quai avant d'avoir remplacé le module |

Un module de rechange à bord permet de réparer sur place : la nomenclature en prévoit deux.

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

Le seul moyen d'isoler complètement le bord du ponton sans rien perdre est le **transformateur d'isolement** : voir [sa variante](#variante--transformateur-disolement). Il ne supprime pas la protection qu'apporte (1) : il la remplace par une terre propre au bord.

**En résumé** : garder (1), et choisir entre trois variantes : « (2) avec isolateur galvanique », « ni (2) ni isolateur », ou « transformateur d'isolement », qui fait (2) sans isolateur.

## Cas du chauffe-eau (étude B)

Un chauffe-eau 230 V est l'appareil le plus exposé du bord : une résistance plongée dans l'eau, une cuve le plus souvent métallique, et des tuyaux qui amènent cette eau jusqu'à l'évier et la douche. Si la gaine de la résistance se fend, la phase se retrouve dans l'eau.

- **Avec la terre du ponton (1)** : la cuve est reliée au vert-jaune, le courant de défaut s'y écoule, le différentiel coupe aussitôt. Personne n'a rien touché.
- **Sans (1)** : l'eau et la cuve restent sous tension sans que rien ne coupe. Le premier qui ouvre un robinet en ayant les pieds mouillés devient le chemin vers la terre ; le différentiel le coupe, mais après le contact.

Le chauffe-eau confirme donc la conclusion précédente : **la liaison (1) est indispensable**, et le ballon, de classe I, doit être raccordé à la terre.

**Pourquoi ne pas relier la terre au neutre à bord, à la place du quai ?** Ce serait refaire à bord la liaison terre-neutre qui existe à terre, chez le distributeur. Le différentiel fonctionnerait, puisque le courant de défaut reviendrait par la terre sans repasser par lui. Mais la prise du ponton ne garantit pas quel conducteur est la phase : une fois sur deux, les carcasses du bord seraient reliées à la phase. Et si le neutre du ponton est coupé en amont, la terre du bord ne serait plus reliée à rien. Cette liaison n'est admise qu'au secondaire d'un transformateur d'isolement, où le bord crée son propre réseau. Sans transformateur, la terre du bord se relie à celle du quai, et seulement à elle.

**Conséquence pour l'étude B, hypothèse H3** (résistance 12 V sur le surplus solaire, dans le même ballon) : la cuve, reliée à la terre, porterait aussi une résistance 12 V. Si le négatif de cette résistance touche la cuve, ou si la résistance 230 V se fend, la terre et le 12 V se rejoignent par le ballon : la liaison (2) existe alors de fait, sans isolateur, avec la corrosion galvanique qui va avec. Et un défaut de la résistance 230 V peut mettre du 230 V sur le circuit 12 V, le cas même où la liaison (2) fait couper le différentiel avant tout contact. **Si B-H3 est retenue, il faut la liaison (2).** L'isolateur étant déjà en place, il suffira d'ajouter le fil vers node005. Avec B-H1 (résistance 230 V seule), la décision du 30/09 reste valable.

## Remplacement du différentiel d'arrivée (Q36)

L'appareil actuel, un Power Safe ID55225, n'a aucune documentation trouvable : on ne connaît ni son type ni son âge, et il porte à lui seul la protection des personnes. Il est remplacé par un modèle courant, au format modulaire du boîtier :

- **Interrupteur différentiel bipolaire**, qui coupe la phase et le neutre. Un interrupteur suffit : les surintensités sont déjà coupées en aval par le DT40 C10 et le 16 A d'arrivée. Un disjoncteur différentiel ajouterait cette protection pour le câblage interne du boîtier, sans nécessité ici.
- **30 mA**, pour la protection des personnes.
- **Type A** : il détecte les fuites alternatives et les fuites « redressées » que produisent les appareils électroniques, comme le chargeur. Le type AC ne voit que les premières. Les types F et B, faits pour les onduleurs et les variateurs, ne sont pas nécessaires à bord.
- **Calibre de 40 A** : ce calibre est celui du courant qu'il supporte, pas une protection. Il doit dépasser celui des protections placées en aval ; 40 A est le calibre courant, et le moins cher, de ces appareils.

Tester son bouton chaque mois en saison : en atmosphère saline, un mécanisme qui ne sert jamais finit par se gripper.

## Disjoncteurs (Q31)

Le DT40 C10 du chargeur et les DNX3 C10 et C16 du boîtier tribord sont des modèles phase + neutre, qui coupent les deux conducteurs : l'inversion de la phase et du neutre à la prise du ponton est couverte, **aucun achat**. Seul le modèle du 16 A d'arrivée n'a pas été relevé.

- **Plafonnier** : métallique, et sa terre est raccordée (Q31, 30/09). Rien à faire.
