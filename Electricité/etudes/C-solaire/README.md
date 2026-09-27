# Étude C · Panneaux solaires

**Objectif** : tenir au mouillage sans faire tourner le moteur pour recharger.

**Base** : le relevé et le [bilan énergétique](../../commun/bilan-energetique.yaml).

## Constat de départ

Le bilan estimé donne environ **65 Ah par jour au mouillage** et 92 Ah par jour en navigation (moteur non compté). Or une batterie de servitude de 110 Ah au plomb ne fournit qu'environ 55 Ah sans être abîmée (décharge à 50 %). Elle ne tient donc même pas une journée au mouillage. Trois leviers sont à combiner :

1. **Mesurer** plutôt qu'estimer : un shunt sur la batterie de servitude. Il est prévu dans les critères de l'étude A.
2. **Produire** : c'est l'objet de cette étude.
3. **Stocker** davantage : LiFePO4, plus de capacité utile. Ce serait une étude à part entière, qui ferait évoluer le coupleur et le chargeur.

## Questions préalables

- **Q17** : port d'attache et zone de navigation. L'ensoleillement dépend beaucoup de la latitude et de la saison.
- **Q18** : bimini, capote, portique, surfaces libres et ombrage de la bôme.

## Hypothèses à explorer

| | Principe | Ordre de grandeur | Dépend de |
|---|---|---|---|
| H1 | Panneaux rigides sur un portique ou un bimini | 150 à 250 Wc | Q18 (support existant ou à créer) |
| H2 | Panneaux souples sur le rouf ou la capote | 100 à 150 Wc | Q18, ombrage |
| H3 | Panneau mobile orientable, posé au mouillage | 100 Wc | rangement à bord |

Pour chaque hypothèse : production en Ah par jour selon la saison (d'après Q17), régulateur MPPT à choisir, et raccordement sur la barrette de servitude de l'étude A (fusible à la batterie et au régulateur).

## Critères de comparaison

- Part du bilan au mouillage couverte, en été et à mi-saison.
- Coût, fixation, ombrage, fardage et esthétique.
- Compatibilité avec un futur passage au LiFePO4 (profil de charge du régulateur).

## Décision

En attente des réponses à Q17 et Q18.
