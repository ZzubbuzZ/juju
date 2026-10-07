---
hypothese: B-H3
titre: Entrée 12 V du ballon (200 W), sur la LiFePO4 et le surplus solaire
etat: retenue
resume: L'entrée 12 V de 200 W du CozyWater 10C (B-H1) est câblée en permanence, à côté du 230 V ; le ballon choisit seul le 230 V quand il est là. Elle part du côté charges du coupe-circuit de servitude par un fusible de 30 A et du câble de 6 mm², à travers un relais de 30 A commandé par un interrupteur à voyant près du ballon, comme le demande la notice. Elle sert quand le surplus solaire (étude C) ou une batterie pleine le permettent.
points_forts:
  - Eau chaude hors du quai, sans autre appareil ni convertisseur ; la résistance est déjà dans le ballon.
  - Câblage court et simple (relais, fusible, interrupteur) ; le ballon passe seul sur le 230 V au quai.
  - Le relais pourra être commandé plus tard par la sortie de délestage d'un régulateur solaire (étude C).
points_faibles:
  - "Chauffe lente : environ 2 h 40 pour 10 L de 15 à 60 °C."
  - "Environ 45 Ah par chauffe : au mouillage, la consommation passe d'environ 60 à environ 105 Ah par jour, et l'autonomie de la LiFePO4 d'environ trois jours à un jour et demi."
  - "Au moteur, l'alternateur de 20 A (Q14), bridé à 15 A par le DC/DC, ne couvre pas les 17 A du ballon."
  - Sans régulateur à sortie de délestage, la commande reste manuelle ; un oubli vide la batterie jusqu'à la coupure du BMS.
  - Trajet et longueur du câble de 6 mm² à relever à bord (Q57).
decision: "08/10/2026 : retenue par l'utilisateur, les deux entrées du ballon câblées en permanence. Départ du + côté charges du coupe-circuit de servitude (node010), proposé par Claude. Relais et interrupteur près du ballon. Longueurs à mesurer (Q57)."
---

# B-H3 · Entrée 12 V du ballon, sur la LiFePO4 et le surplus solaire

Hypothèse de l'étude B, **retenue le 08/10**. Base : **B-H1** (le ballon et son 230 V), côté batterie **E-H1** (LiFePO4 de 200 Ah) : node010 et node006, où se raccorde l'entrée 12 V, sont les mêmes dans le relevé et dans les études A, D et E.

Câblage : [cablage.yaml](cablage.yaml). Schéma : [folio 2n](folio-2n-cozywater-12v.svg). Nomenclature : [nomenclature.yaml](nomenclature.yaml).

## Deux entrées câblées en permanence

Le ballon a ses deux résistances et choisit seul sa source : « la commande sélectionne automatiquement l'alimentation 230 volts si les deux tensions sont disponibles » (notice, page 64). Le 230 V (B-H1) et le 12 V restent donc branchés tous les deux. Au quai, le ballon chauffe sur le 230 V ; dès que le 230 V disparaît, il passe sur le 12 V **si le relais est fermé**. L'interrupteur décide donc si le ballon a le droit de tirer sur la batterie. C'est pour ça que la notice l'exige, même avec un câblage permanent.

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

## Commande

1. **Maintenant** : interrupteur à voyant près du panneau de commande du ballon. Le voyant rappelle que le ballon tire sur la batterie.
2. **Avec l'étude C** : la bobine du relais est commandée par la sortie de délestage (« load ») du régulateur solaire, ou par un relais programmable (Cerbo GX, étude D), qui n'enclenche le ballon que batterie pleine et panneaux en production. L'interrupteur reste en série pour pouvoir tout couper.

La bobine d'un relais automobile consomme environ 0,15 A pendant la chauffe, ce qui est négligeable devant les 17 A du ballon.

## Câblage (08/10)

Folio 2n. Puissance en 6 mm², commande en 0,75 mm² :

| Fil | De → vers | Rôle |
|---|---|---|
| wire306 | fusible 30 A (node309) → relais, borne 30 (node310) | +, de la platine au ballon, environ 3 m |
| wire307 | relais, borne 87 (node311) → ballon 12 V + (node318) | + commuté |
| wire308 | ballon 12 V − (node319) → node006 | −, côté « bord » du shunt, environ 3 m |
| wire309 | fusible 1 A (node315) → interrupteur (node316) | alimentation de la commande, prise sur la borne 30 |
| wire310 | interrupteur (node317) → relais, borne 86 (node312) | commande de la bobine |
| wire311 | relais, borne 85 (node313) → node319 | − de la bobine |
| wire312 | voyant (node380) → node319 | − du voyant |

- **Départ à node010**, côté charges du coupe-circuit de servitude, comme les autres départs de la platine : ouvrir le coupe-circuit coupe aussi le ballon. Le fusible de 30 A (node308, node309) est monté sur le goujon.
- **Relais et interrupteur près du ballon**, dans le cabinet de toilette : un seul câble de 6 mm² fait le trajet depuis la platine, avec son retour. La commande est prise sur la borne 30 du relais, à travers un fusible de 1 A : le fil de 0,75 mm² n'est pas protégé par le fusible de 30 A.
- **Retour sur node006** : le shunt (étude D) compte la consommation du ballon.
- Chute de tension sur 3 m de 6 mm² à 17 A : environ 0,3 V, soit 2,5 %.
- Numéros : node308 à node319 (fin de la plage de l'étude B) et node380, pris dans la plage de réserve ; wire306 à wire312.

## Reste à faire

- Mesurer le trajet de la platine au ballon (Q57) et la longueur des fils 12 V du ballon (Q55).
- Commande par le régulateur solaire, avec l'étude C.
