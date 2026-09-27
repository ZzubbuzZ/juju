# Étude A · Sécurisation de l'existant

**Objectif** : qu'aucun câble du bord ne puisse chauffer sans qu'une protection coupe avant, et que la sécurité (pompe de cale, feux) ne dépende pas d'une manœuvre oubliée. Tout cela sans changer de technologie de batterie : cette étude est un prérequis aux études B et C.

**Base** : le relevé (branche `main`). Anomalies à traiter : [anomalies.md](../../releve/anomalies.md).

## Hypothèses

| | Contenu | Anomalies traitées | État |
|---|---|---|---|
| [H1](H1-distribution-servitude/proposition.md) | Barrette + de servitude avec fusibles, tableau de la table à carte refait (12 circuits), tableau Scheiber protégé, pompe de cale rendue automatique | A1, A6 | Rédigée, à valider · mise à jour avec les réponses du 27/09 |
| H2 | Fusibles en sortie de batterie (MRBF sur les bornes) et fusibles sur les fils du coupleur et du chargeur | A2, A4 | À écrire |
| H3 | Cosses serties : câbles de la batterie moteur, liaison EPS 100 → groupe froid (cosses à fourche SV 2-4) | A3, A7 | À écrire |
| H4 | Terre 230 V : terre sur tous les appareils de classe I, liaison terre / masse 12 V, isolateur galvanique, disjoncteurs bipolaires | à définir après Q31 | À écrire |

A5 (section du guindeau) a été levée le 27/09 : elle n'est plus à traiter.

H2 et H3 complètent H1 plutôt qu'elles ne la concurrencent. La décision finale sera probablement « H1 + H2 + H3 », avec `base: A-H1` pour H2, puis `base: A-H2` pour H3.

## Terre 230 V : bonnes pratiques

Question posée dans l'état des lieux : la terre n'arrive qu'aux prises, et la coque en polyester ne conduit pas. Que faut-il faire ?

La coque isolante ne change rien au principe : à bord, **la protection contre les chocs électriques repose sur le conducteur de terre ramené jusqu'à la terre du quai, et sur le différentiel 30 mA**. Le différentiel est déjà en place à l'arrivée ; c'est la protection principale. Les points à examiner, dans les termes des normes nautiques (ISO 13297, ABYC E-11), à confirmer sur leur texte au moment de la décision :

1. **Terre sur tout appareil de classe I**, c'est-à-dire à carcasse métallique : prises, chargeur, EPS 100, et le plafonnier s'il est métallique. Un appareil de classe II (double isolation, marqué d'un double carré) n'en a pas besoin. D'où la question Q31 sur le plafonnier : son câble en 3 × 1,5 mm² contient déjà un conducteur de terre, qu'il suffirait de raccorder.
2. **Coupure bipolaire**. À quai, la phase et le neutre peuvent être inversés. Un disjoncteur qui ne coupe que la phase peut laisser un appareil sous tension par le neutre. Le disjoncteur d'arrivée au moins doit couper les deux conducteurs (Q31).
3. **Liaison entre la terre 230 V et la masse 12 V**. Les normes nautiques la demandent en un point unique : si un défaut met du 230 V sur une partie métallique du circuit 12 V (carcasse du chargeur, bloc moteur), le courant de défaut trouve un chemin vers la terre du quai et le différentiel déclenche.
4. **Isolateur galvanique**. Cette même liaison relie les masses métalliques immergées (hélice, arbre, anodes) à celles des autres bateaux du ponton, par la terre du quai : c'est une source de corrosion galvanique. Un isolateur galvanique (ou un transformateur d'isolement) sur le conducteur de terre, à l'arrivée, bloque ces faibles courants tout en laissant passer un courant de défaut.

La réponse à Q31 dira ce qui existe déjà. L'hypothèse H4 en découlera.

## Critères de comparaison

- Anomalies traitées et risque résiduel.
- Coût du matériel (câble, fusibles, barrettes, cosses).
- Travail à bord (nombre de fils à tirer, accès).
- Compatibilité avec un futur passage au LiFePO4 : fusible de classe T sur la batterie de servitude, place pour un shunt.

## Décision

En attente.
