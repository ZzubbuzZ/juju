# Étude A · Sécurisation de l'existant

**Objectif** : qu'aucun câble du bord ne puisse chauffer sans qu'une protection coupe avant, et que la sécurité (pompe de cale, feux) ne dépende pas d'une manœuvre oubliée. Tout cela sans changer de technologie de batterie : cette étude est un prérequis aux études B et C.

**Base** : le relevé (branche `main`). Anomalies à traiter : [anomalies.md](../../releve/anomalies.md).

## Pistes d'amélioration et coûts

Chaque hypothèse a son dossier : une `proposition.md` (le quoi et le pourquoi) et une `nomenclature.yaml` (le matériel chiffré, par lot). Les lots sont réalisables séparément. Les montants ci-dessous sont ceux que calcule `outils/verifier.py` à partir des nomenclatures : **ce sont des estimations du 28-29/09/2026**, à remplacer par des prix catalogue ou de devis. Le vérificateur compte les prix encore estimés.

| Priorité | Hypothèse · lot | Anomalies | Coût estimé | Décision du 30/09 | Enjeu |
|---|---|---|---|---|---|
| 1 | [H2](H2-fusibles-batteries/proposition.md) · fusible de 50 A à la source de wire019 (repris de H1) | A1 | 31 € | retenu | Tableau de la table à carte alimenté sans aucune protection : risque d'incendie |
| 1 | H2 · fusible de 30 A à la source de wire022 (tableau Scheiber) | A6 | 31 € | retenu (01/10) | Tableau Scheiber alimenté sans aucune protection : risque d'incendie |
| 2 | H2 · fusibles de 400 A près des deux batteries | A2 | 80 € | retenu (option A, 400 A) | Rien ne coupe un court-circuit sur les câbles de batterie |
| 2 | H2 · fusibles des départs : chargeur 30 A, coupleur 40 A | A4 | 91 € | retenu | Quatre câbles de 6 mm² branchés en direct sur les batteries |
| 3 | [H5](H5-passages-cloison/proposition.md) · une dizaine de passages de cloison | A9 | 44 € | retenu | Usure de l'isolant sur l'arête des trous, jusqu'au court-circuit |
| 3 | [H3](H3-cosses/proposition.md) · cosses de la batterie moteur | A3 | 14 € | retenu, câbles conservés | Contacts dégradés sur le circuit du démarreur |
| 3 | H3 · raccordement de l'EPS 100 | A7 | 17 € | retenu | Contact médiocre, coupures du frigo au démarrage du compresseur |
| 3 | H3 · outillage de sertissage | | 75 € | retenu | Sert à toutes les hypothèses |
| 4 | [H4](H4-terre-230v/proposition.md) · remplacement du différentiel d'arrivée par un type A | | 60 € | retenu | Seule protection des personnes en 230 V ; modèle actuel sans documentation (Q36) |
| 5 | H4 · isolateur galvanique maison, sans liaison terre / masse 12 V | A8 | 58 € | retenu | Précaution contre la corrosion par le ponton si une liaison apparaît |
| – | H1 · barrette + regroupant les départs | | 165 € | différé | Simplifie la distribution ; A1 et A6 sont déjà traités par les fusibles de H2 |
| – | H1 · pompe de cale automatique, fusibles de 3 A | A10 | 68 € | différé | Pompe mise en route à la main, sans flotteur ; protégée en 10 A au lieu de 3 A |
| – | H1 · recâblage du tableau de la table à carte | | 407 € | différé | Fiabilité et lisibilité plus que sécurité |
| – | H2 · wire006 refait en 50 mm² | A2 | 30 € | différé, long terme | Court-circuit partiel sur le câble de la batterie de servitude, plus probable avec l'usure ; à surveiller d'ici là par l'historique des consommations (étude D) |
| – | H4 · transformateur d'isolement | A8 | environ 430 € | écarté | Supprimait tout lien avec le ponton |

**Total retenu : environ 500 €**, outillage compris. Les lots différés représentent environ 670 € de plus, dont une partie (la barrette de H1) rendrait le fusible de 31 € inutile.

**Ordre proposé** : les priorités 1 et 2 suppriment les risques d'incendie pour environ 230 €. Tout se passe autour des batteries et de la platine des coupe-circuits, donc en une journée à bord. Les passages de cloison et les cosses (priorité 3) se font dans la foulée, sur les mêmes câbles et avec le même outillage. Le 230 V (priorités 4 et 5) se fait à part, câble de quai débranché.

**Risque accepté en attendant les lots différés** : A10 (pompe de cale protégée en 10 A au lieu de 3 A). A6 est traité depuis le 01/10 par un fusible de 30 A (H2).

Dépendances : H4 modifie le folio 3 (isolateur à la place de wire034, nouveau différentiel). A5 (section du guindeau) a été levée le 27/09 : elle n'est plus à traiter.

## Terre 230 V : bonnes pratiques

Question posée dans l'état des lieux : la terre n'arrive qu'aux prises, et la coque en polyester ne conduit pas. Que faut-il faire ?

La coque isolante ne change rien au principe : à bord, **la protection contre les chocs électriques repose sur le conducteur de terre ramené jusqu'à la terre du quai, et sur le différentiel 30 mA**. Le différentiel est déjà en place à l'arrivée ; c'est la protection principale. Les points à examiner, dans les termes des normes nautiques (ISO 13297, ABYC E-11), à confirmer sur leur texte au moment de la décision :

1. **Terre sur tout appareil de classe I**, c'est-à-dire à carcasse métallique : prises, chargeur et plafonnier, qui est métallique et dont la terre est raccordée (Q31). Un appareil de classe II (double isolation, marqué d'un double carré) n'en a pas besoin : c'est le cas de l'EPS 100, dont la fiche n'a pas de contact de terre (Q38).
2. **Coupure bipolaire**. À quai, la phase et le neutre peuvent être inversés. Un disjoncteur qui ne coupe que la phase peut laisser un appareil sous tension par le neutre. Le disjoncteur d'arrivée au moins doit couper les deux conducteurs. À bord, le DT40 et les DNX3 le font (Q31).
3. **Liaison entre la terre 230 V et la masse 12 V**. Les normes nautiques la demandent en un point unique : si un défaut met du 230 V sur une partie métallique du circuit 12 V (carcasse du chargeur, bloc moteur), le courant de défaut trouve un chemin vers la terre du quai et le différentiel déclenche.
4. **Isolateur galvanique**. Cette même liaison relie les masses métalliques immergées (hélice, arbre, anodes) à celles des autres bateaux du ponton, par la terre du quai : c'est une source de corrosion galvanique. Un isolateur galvanique sur le conducteur de terre, à l'arrivée, bloque ces faibles courants tout en laissant passer un courant de défaut. Un transformateur d'isolement supprime complètement le lien avec le ponton ; plus lourd et plus cher, il est décrit comme variante dans [H4](H4-terre-230v/proposition.md#variante--transformateur-disolement).

Relevé du 28/09 : la terre et la masse 12 V ne sont reliées nulle part, et il n'y a pas d'isolateur galvanique (A8). H4 portera donc au minimum sur la liaison et l'isolateur. La coupure bipolaire des disjoncteurs et la terre du plafonnier ont été vérifiées depuis (Q31, 30/09).

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

**30/09** : programme retenu dans le tableau des [pistes d'amélioration](#pistes-damélioration-et-coûts). En résumé :

- **H1** différée ; ses fusibles de source (50 A pour wire019, A1 ; 30 A pour wire022, A6) sont repris dans H2 le 01/10.
- **H2** option A, avec des fusibles de 400 A sur les deux batteries, câbles de batterie conservés en 35 mm² (écart accepté) ; départs à 30 A (chargeur) et 40 A (coupleur, relais de 40 A).
- **H3** cosses serties, câbles conservés.
- **H4** terre du ponton conservée à travers un isolateur galvanique maison, sans liaison à la masse 12 V ; différentiel remplacé par un type A ; transformateur écarté.
- **H5** une dizaine de passages de cloison.

**Câblage (01/10)** : [H2](H2-fusibles-batteries/cablage.yaml) (base : le relevé, [folio 2c](H2-fusibles-batteries/folio-2c-fusibles.svg)) puis [H4](H4-terre-230v/cablage.yaml) (base : A-H2, [folio 2d](H4-terre-230v/folio-2d-terre.svg)) : le modèle de A-H4 cumule tout le programme retenu. H3 et H5 n'ajoutent ni ne suppriment aucun fil. Nouveaux numéros : node070 à node085, node256 et node257, wire160 à wire167, wire170 et wire171.

**Fusionnée dans `main`.** L'étude E (fusionnée le 08/10) modifie ce programme côté servitude : fusible de batterie de 300 A au lieu de 400 A, coupleur et sortie 2 du Dolphin déposés avec leurs fusibles (wire163 à wire165), sortie 1 du Dolphin protégée à la batterie moteur. Les calibres de 50 A (wire019) et de 400 A (wire001) dépendent de l'isolant des câbles existants (Q58). Reste à faire : poser le tag de révision.
