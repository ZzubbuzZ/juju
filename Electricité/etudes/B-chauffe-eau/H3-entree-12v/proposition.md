---
hypothese: B-H3
titre: Entrée 12 V du ballon (200 W), sur la LiFePO4 et le surplus solaire
etat: retenue
resume: L'entrée 12 V de 200 W du CozyWater 10C (B-H1) est câblée en permanence, à côté du 230 V ; le ballon choisit seul le 230 V quand il est là. Elle part du côté charges du coupe-circuit de servitude par un disjoncteur 12 V CC de 30 A à commande manuelle, qui protège le câble de 6 mm² et sert d'interrupteur « ballon sur batterie » ; ni relais ni interrupteur à voyant (décision du 12/10, écart à la notice). Elle sert quand le surplus solaire (étude C) ou une batterie pleine le permettent.
points_forts:
  - Eau chaude hors du quai, sans autre appareil ni convertisseur ; la résistance est déjà dans le ballon.
  - "Câblage minimal : un disjoncteur et un câble de 6 mm² aller et retour ; le ballon passe seul sur le 230 V au quai."
  - Aucune consommation au repos (pas de bobine de relais, pas de voyant).
points_faibles:
  - "Chauffe lente : environ 2 h 40 pour 10 L de 15 à 60 °C."
  - "Environ 45 Ah par chauffe : au mouillage, la consommation passe d'environ 60 à environ 105 Ah par jour, et l'autonomie de la LiFePO4 d'environ trois jours à un jour et demi."
  - "Au moteur, l'alternateur de 20 A (Q14), bridé à 15 A par le DC/DC, ne couvre pas les 17 A du ballon."
  - "Commande manuelle à la platine ; l'état de chauffe se lit sur le panneau de commande du ballon. Un oubli vide la batterie jusqu'à la coupure du BMS."
  - "Écart à la notice, qui demande un relais et un interrupteur ; mais elle est commune au CozyWater 10 (sans panneau) et au 10C. Une commande automatique (étude C) demandera d'ajouter un organe commandé."
  - Trajet et longueur du câble de 6 mm² à relever à bord (Q57).
decision: "08/10/2026 : retenue par l'utilisateur, les deux entrées du ballon câblées en permanence. Départ du + côté charges du coupe-circuit de servitude (node010), proposé par Claude. Relais et interrupteur près du ballon. Longueurs à mesurer (Q57). 12/10 : disjoncteur 12 V CC de 30 A à commande manuelle à la place du fusible ; relais et interrupteur à voyant supprimés par l'utilisateur (consommation de la bobine)."
---

# B-H3 · Entrée 12 V du ballon, sur la LiFePO4 et le surplus solaire

Hypothèse de l'étude B, **retenue le 08/10**. Base : **B-H1** (le ballon et son 230 V), côté batterie **E-H1** (LiFePO4 de 200 Ah) : node010 et node006, où se raccorde l'entrée 12 V, sont les mêmes dans le relevé et dans les études A, D et E.

Câblage : [cablage.yaml](cablage.yaml). Schéma : [folio 2n](folio-2n-cozywater-12v.svg). Nomenclature : [nomenclature.yaml](nomenclature.yaml).

## Deux entrées câblées en permanence

Le ballon a ses deux résistances et choisit seul sa source : « la commande sélectionne automatiquement l'alimentation 230 volts si les deux tensions sont disponibles » (notice, page 64). Le 230 V (B-H1) et le 12 V restent donc branchés tous les deux. Au quai, le ballon chauffe sur le 230 V ; dès que le 230 V disparaît, il passe sur le 12 V **si le disjoncteur est fermé**. Le disjoncteur décide donc si le ballon a le droit de tirer sur la batterie : c'est le rôle que la notice donne à son interrupteur et à son relais, « pour éviter que la batterie ne se décharge accidentellement ».

## Ce que demande la notice

Notice du CozyWater 10C, page 67, schéma « connexion 12 V CC » :

- un **interrupteur** commande un **relais de 30 A au moins** (contact à fermeture, bornes 30 et 87) dans le câble positif, « pour éviter que la batterie ne se décharge accidentellement » ;
- un **fusible de 30 A** sur le positif, le plus près possible de la source ;
- du câble de **6 mm² au moins** ;
- le négatif n'a pas besoin de fusible s'il revient directement à la masse de la batterie (cas A de la notice). Sur Juju, il reviendra à la barre de masse de la servitude, côté « bord » du shunt (étude D), pour que le shunt compte la consommation du ballon.

## Section du câble

Courant : 200 W / 12 V, soit environ **17 A**. Circuit de confort, donc ΔU = 10 % (1,2 V) :

S = 2 × L × 17 × 0,0175 / 1,2 ≈ 0,5 × L mm², soit 2,5 mm² jusqu'à 5 m de câble.

Mais le fusible de 30 A imposé par la notice doit protéger le câble : c'est lui qui fixe la section. Retenu : **6 mm²**, comme la notice. Une longueur de plus de 12 m demanderait davantage, ce qui est peu probable.

## Effet sur le bilan

Chauffer 10 L de 15 à 60 °C demande environ 0,52 kWh, soit environ **45 Ah** sur la LiFePO4 avec les pertes, en 2 h 40.

| Situation | Sans le ballon | Avec une chauffe par jour |
|---|---|---|
| Mouillage ([bilan](../../../commun/bilan-energetique.yaml)) | environ 60 Ah/jour | environ 105 Ah/jour |
| Autonomie de la LiFePO4 (160 à 180 Ah utiles) | environ 3 jours | environ 1,5 jour |

Au moteur, le DC/DC de l'étude E charge la LiFePO4 à 15 A environ (alternateur de 20 A, Q14) : le ballon consomme plus que la charge. L'entrée 12 V n'est donc rentable qu'avec un **surplus solaire** : environ 200 W de panneaux en plein soleil, en plus de la consommation du bord. C'est l'étude C qui dira si ce surplus existe.

En attendant, l'entrée 12 V reste utile pour une chauffe ponctuelle, batterie pleine, la veille d'un retour au port.

## Commande (décision du 12/10)

La notice demande un interrupteur qui commande un relais de 30 A. L'utilisateur les supprime : le **disjoncteur 12 V CC de 30 A**, à la platine, sert d'interrupteur « ballon sur batterie ». Ouvert, le ballon ne peut pas tirer sur la batterie ; fermé, il chauffe sur le 12 V dès que le 230 V manque.

- **Consommation du relais** : la bobine d'un relais automobile tire environ 0,15 A (1,8 W), mais seulement quand l'interrupteur est fermé, pas en permanence. Laissé fermé 24 h, cela ferait environ 3,6 Ah par jour, le voyant en plus. Sans relais, cette perte disparaît.
- **Le voyant n'est pas nécessaire** (remarque de l'utilisateur, 12/10) : la notice est commune au CozyWater 10, sans panneau, et au 10C, dont le panneau de commande affiche l'état de marche, la température et les erreurs (notice, pages 61 à 64 : « panneau de commande/affichage (CozyWater 10C uniquement) »). Sur le 10C, c'est le panneau qui renseigne ; on manœuvre seulement le disjoncteur à la platine, dans la descente, à côté de la table à carte.
- **Le disjoncteur doit pouvoir servir d'interrupteur** : un modèle à levier ou à bascule, prévu pour être manœuvré souvent (les disjoncteurs de bateau « switchable », ou un modulaire marqué DC). Un disjoncteur thermique à simple bouton de réarmement ne convient pas.
- **Avec l'étude C** : une commande automatique par le régulateur solaire demandera un organe commandé. Pour ne rien consommer au repos : un relais bistable (il ne consomme qu'au basculement), ou un interrupteur électronique de batterie (type Victron BatteryProtect, quelques mA, avec en plus une coupure en tension basse). Le disjoncteur resterait en amont.

## Câblage (08/10, simplifié le 12/10)

Folio 2n. Tout en 6 mm² :

| Fil | De → vers | Rôle |
|---|---|---|
| wire306 | disjoncteur 30 A (node309) → ballon 12 V + (node318) | +, de la platine au ballon, environ 3 m |
| wire308 | ballon 12 V − (node319) → node006 | −, côté « bord » du shunt, environ 3 m |

wire307 et wire309 à wire312, node310 à node317 et node380 (relais, fusible de 1 A, interrupteur à voyant) sont supprimés le 12/10 ; ils n'avaient pas été posés.

- **Départ à node010**, côté charges du coupe-circuit de servitude, comme les autres départs de la platine : ouvrir le coupe-circuit coupe aussi le ballon. Le disjoncteur de 30 A (node308, node309) est fixé au plus près du goujon, par un câble court de 6 mm².
- **Disjoncteur à la place du fusible** (décision du 12/10). Il remplit le rôle que la notice demande au fusible de 30 A, il se réarme sans pièce de rechange et sert d'interrupteur du 12 V du ballon. Quatre points pour le choisir :
  - **prévu pour le courant continu** : marqué « DC », 12/24 V CC ou plus. Un disjoncteur modulaire de tableau 230 V, sans marquage DC, ne convient pas : un arc en courant continu ne s'éteint pas de lui-même au passage par zéro, et l'appareil peut ne pas couper. Conviennent : un disjoncteur de bateau à levier ou à bascule, ou un modulaire marqué DC (gamme photovoltaïque) ;
  - **manœuvrable** : il sert d'interrupteur, donc un modèle à levier ou à bascule, pas à simple bouton de réarmement ;
  - **30 A**, comme le fusible : il protège le 6 mm² et le ballon tire 17 A, sans déclenchement intempestif ;
  - **pouvoir de coupure** : une LiFePO4 de 200 Ah peut débiter plusieurs milliers d'ampères en court-circuit. Le MEGA de 300 A en tête de la batterie (E-H1) reste la protection de secours ; prendre de préférence un disjoncteur annoncé pour au moins 1 000 à 3 000 A en 12 V CC (notice du modèle).
- **Ballon sous la table à carte** (posé le 12/10) : un seul câble de 6 mm² fait le trajet depuis la platine, avec son retour.
- **Retour sur node006** : le shunt (étude D) compte la consommation du ballon.
- Chute de tension sur 3 m de 6 mm² à 17 A : environ 0,3 V, soit 2,5 %.
- Numéros : node308, node309, node318, node319 ; wire306 et wire308.

## Reste à faire

- Mesurer le trajet de la platine au ballon (Q57) et la longueur des fils 12 V du ballon (Q55).
- **À reprendre avec l'étude C** (remarque conservée le 12/10) : pour une commande automatique par le régulateur solaire, ajouter en aval du disjoncteur un organe commandé qui ne consomme rien au repos, relais bistable ou coupe-batterie électronique (type Victron BatteryProtect, quelques mA, avec coupure en tension basse).
