# Étude A · Sécurisation de l'existant

**Objectif** : qu'aucun câble du bord ne puisse chauffer sans qu'une protection coupe avant, et que la sécurité (pompe de cale, feux) ne dépende pas d'une manœuvre oubliée. Tout cela sans changer de technologie de batterie : cette étude est un prérequis aux études B et C.

**Base** : le relevé (branche `main`). Anomalies à traiter : [anomalies.md](../../releve/anomalies.md).

## Hypothèses

| | Contenu | Anomalies traitées | État |
|---|---|---|---|
| [H1](H1-distribution-servitude/proposition.md) | Barrette + de servitude avec fusibles, tableau de la table à carte refait (12 circuits), tableau Scheiber protégé, pompe de cale rendue automatique | A1, A6 | Rédigée, à valider · mise à jour avec les réponses du 27/09 |
| H2 | Fusibles en sortie de batterie (MRBF sur les bornes) et fusibles sur les fils du coupleur et du chargeur | A2, A4 | À écrire |
| H3 | Cosses serties sur la batterie moteur, câble du guindeau entre relais et moteur selon la notice Lewmar | A3, A5 | À écrire |

H2 et H3 complètent H1 plutôt qu'elles ne la concurrencent. La décision finale sera probablement « H1 + H2 + H3 », avec `base: A-H1` pour H2, puis `base: A-H2` pour H3.

## Critères de comparaison

- Anomalies traitées et risque résiduel.
- Coût du matériel (câble, fusibles, barrettes, cosses).
- Travail à bord (nombre de fils à tirer, accès).
- Compatibilité avec un futur passage au LiFePO4 : fusible de classe T sur la batterie de servitude, place pour un shunt.

## Décision

En attente.
