# Étude A · Sécurisation de l'existant

**Objectif** : qu'aucun câble du bord ne puisse chauffer sans qu'une protection coupe avant, et que la sécurité (pompe de cale, feux) ne dépende pas d'une manœuvre oubliée. Tout cela sans changer de technologie de batterie : cette étude est un prérequis aux études B et C.

**Base** : le relevé (branche `main`). Anomalies à traiter : [anomalies.md](../../releve/anomalies.md).

## Pistes d'amélioration et coûts

Chaque hypothèse a son dossier : une `proposition.md` (le quoi et le pourquoi) et une `nomenclature.yaml` (le matériel chiffré, par lot). Les lots sont réalisables séparément. Les montants ci-dessous sont ceux que calcule `outils/verifier.py` à partir des nomenclatures : **ce sont des estimations du 28-29/09/2026**, à remplacer par des prix catalogue ou de devis. Le vérificateur compte les prix encore estimés.

| Priorité | Hypothèse · lot | Anomalies | Coût estimé | Enjeu |
|---|---|---|---|---|
| 1 | [H1](H1-distribution-servitude/proposition.md) · distribution : barrette + et fusibles des tableaux | A1, A6 | 165 € | Deux câbles alimentés sans aucune protection : risque d'incendie |
| 2 | [H2](H2-fusibles-batteries/proposition.md) · fusibles de 300 A sur les bornes des deux batteries, wire006 refait en 50 mm² | A2 | 136 € | Rien ne coupe un court-circuit sur les câbles de batterie |
| 2 | H2 · fusibles des départs coupleur et chargeur | A4 | 87 € | Quatre câbles de 6 mm² branchés en direct sur les batteries |
| 3 | [H5](H5-passages-cloison/proposition.md) · passages de cloison | A9 | 44 € | Usure de l'isolant sur l'arête des trous, jusqu'au court-circuit |
| 3 | [H3](H3-cosses/proposition.md) · cosses de la batterie moteur | A3 | 14 € (+60 € si les câbles sont à changer) | Contacts dégradés sur le circuit du démarreur |
| 3 | H3 · raccordement de l'EPS 100 | A7 | 17 € | Contact médiocre, coupures du frigo au démarrage du compresseur |
| 3 | H3 · outillage de sertissage | | 75 € | Sert à toutes les hypothèses |
| 4 | H1 · pompe de cale automatique, fusibles de 3 A | A10 | 68 € | Pompe mise en route à la main, sans flotteur ; protégée en 10 A au lieu de 3 A |
| 5 | [H4](H4-terre-230v/proposition.md) · isolateur galvanique et liaison terre / masse 12 V | A8 | 136 € (0 € dans la variante sans liaison) | Défaut 230 V sur le circuit 12 V ; corrosion au ponton |
| 5 | H4 · disjoncteurs phase + neutre | | à chiffrer, selon Q31 | Seulement si les disjoncteurs actuels ne coupent que la phase |
| 6 | H1 · recâblage du tableau de la table à carte | | 407 € | Fiabilité et lisibilité (« plat de spaghettis ») plus que sécurité ; peut être différé |

**Total des priorités 1 à 5 : environ 740 €** (605 € sans la liaison à la terre), outillage compris. Le recâblage complet du tableau de servitude ajoute environ 410 €.

**Ordre proposé** : les priorités 1 et 2 suppriment les risques d'incendie pour environ 390 €. Tout se passe autour des batteries et de la platine des coupe-circuits, donc en une journée à bord. Les passages de cloison et les cosses (priorité 3) se font dans la foulée, sur les mêmes câbles et avec le même outillage.

Dépendances : H2 dimensionne le fusible de la batterie de servitude en tenant compte des départs créés par H1, et H4 modifie le folio 3. A5 (section du guindeau) a été levée le 27/09 : elle n'est plus à traiter.

## Terre 230 V : bonnes pratiques

Question posée dans l'état des lieux : la terre n'arrive qu'aux prises, et la coque en polyester ne conduit pas. Que faut-il faire ?

La coque isolante ne change rien au principe : à bord, **la protection contre les chocs électriques repose sur le conducteur de terre ramené jusqu'à la terre du quai, et sur le différentiel 30 mA**. Le différentiel est déjà en place à l'arrivée ; c'est la protection principale. Les points à examiner, dans les termes des normes nautiques (ISO 13297, ABYC E-11), à confirmer sur leur texte au moment de la décision :

1. **Terre sur tout appareil de classe I**, c'est-à-dire à carcasse métallique : prises, chargeur, EPS 100, et le plafonnier s'il est métallique. Un appareil de classe II (double isolation, marqué d'un double carré) n'en a pas besoin. D'où la question Q31 sur le plafonnier : son câble en 3 × 1,5 mm² contient déjà un conducteur de terre, qu'il suffirait de raccorder.
2. **Coupure bipolaire**. À quai, la phase et le neutre peuvent être inversés. Un disjoncteur qui ne coupe que la phase peut laisser un appareil sous tension par le neutre. Le disjoncteur d'arrivée au moins doit couper les deux conducteurs (Q31).
3. **Liaison entre la terre 230 V et la masse 12 V**. Les normes nautiques la demandent en un point unique : si un défaut met du 230 V sur une partie métallique du circuit 12 V (carcasse du chargeur, bloc moteur), le courant de défaut trouve un chemin vers la terre du quai et le différentiel déclenche.
4. **Isolateur galvanique**. Cette même liaison relie les masses métalliques immergées (hélice, arbre, anodes) à celles des autres bateaux du ponton, par la terre du quai : c'est une source de corrosion galvanique. Un isolateur galvanique (ou un transformateur d'isolement) sur le conducteur de terre, à l'arrivée, bloque ces faibles courants tout en laissant passer un courant de défaut.

Relevé du 28/09 : la terre et la masse 12 V ne sont reliées nulle part, et il n'y a pas d'isolateur galvanique (A8). H4 portera donc au minimum sur la liaison et l'isolateur. Restent à relever : la coupure bipolaire des disjoncteurs et la classe du plafonnier (Q31).

## Elements supplémentaires

- Je ne vois pas de fusible en sortie de batterie. Il est souvent recommandé de placer un fusible en sortie de batterie, en effet le cable allant de node007 à CC servitude ne fait d'un metre, mais il peut entrer en contact avec une masse et provoquer de graves dégats s'il s'enflamme. Il faut traiter les 2 batteries de cette façon, non?
  - → Oui. C'est l'anomalie A2, traitée par H2, qui prévoit désormais un fusible MRBF sur la borne + des deux batteries. Côté moteur, les normes dispensent le démarreur de fusible, mais un fusible de calibre supérieur au courant de démarrage ne gêne pas le démarrage et coupe un court-circuit franc.
- Les passages de cloison sont de simple trous au travers desquels passent les cables, sans plus de protection. Comment protéger efficacement les cables à ces endroits?
  - → Nouvelle anomalie A9 et hypothèse H5 : un passe-fil en caoutchouc dans chaque trou, et surtout des colliers vissés de part et d'autre de la cloison, pour que le câble ne bouge plus contre l'arête. Pas de mastic, qui masque l'usure. Recensement des passages : Q35.
- Si relier la terre à bord et à quai pose un problème d'isolation galvanique, peut-être pouvons-nous ne pas le faire, sachant qu'un différentiel à bord s'occupe de préserver la sécurité des passagers?
  - → Tout dépend de quelle liaison on parle ; voir [H4, « À ne pas confondre »](H4-terre-230v/proposition.md#à-ne-pas-confondre--couper-la-terre-du-ponton). Ne pas relier la terre 230 V à la masse 12 V : défendable, et cela suffit à supprimer la corrosion galvanique. Couper la terre du ponton : le différentiel protégerait encore les personnes, mais on perdrait la coupure immédiate au défaut et la redondance, sans rien gagner, puisque la corrosion galvanique est déjà évitée sans la liaison terre / masse 12 V. On garde la terre du ponton.

## Critères de comparaison

- Anomalies traitées et risque résiduel.
- Coût du matériel (câble, fusibles, barrettes, cosses).
- Travail à bord (nombre de fils à tirer, accès).
- Compatibilité avec un futur passage au LiFePO4 : fusible de classe T sur la batterie de servitude, place pour un shunt.

## Décision

En attente.
