# Étude C · Panneaux solaires

**Objectif** : tenir au mouillage sans faire tourner le moteur pour recharger.

**Base** : le relevé et le [bilan énergétique](../../commun/bilan-energetique.yaml).

## Constat de départ

Le bilan estimé donne environ **65 Ah par jour au mouillage** et 92 Ah par jour en navigation (moteur non compté). Or une batterie de servitude de 110 Ah au plomb ne fournit qu'environ 55 Ah sans être abîmée (décharge à 50 %). Elle ne tient donc même pas une journée au mouillage. Trois leviers sont à combiner :

1. **Mesurer** plutôt qu'estimer : un shunt sur la batterie de servitude. Il est prévu dans les critères de l'étude A.
2. **Produire** : c'est l'objet de cette étude.
3. **Stocker** davantage : LiFePO4, plus de capacité utile. Ce serait une étude à part entière, qui ferait évoluer le coupleur et le chargeur.

## Questions préalables

- **Q17** (traitée le 27/09) : étang de Berre (Saint-Chamas), navigation en Méditerranée. C'est l'un des sites les mieux ensoleillés de France.
- **Q18** (traitée le 27/09) : **une capote seulement**, pas de bimini ni de portique.

## Ordre de grandeur de la production

Pour 100 Wc en Provence, il faut compter **environ 25 à 35 Ah par jour en été et 10 à 15 Ah en hiver**, selon l'orientation, l'ombrage de la bôme et le régulateur. Pour couvrir les 65 Ah par jour estimés au mouillage, il faut donc **environ 200 Wc en été**. Ces chiffres sont à affiner avec PVGIS (outil gratuit de la Commission européenne) pour Saint-Chamas, et avec un bilan mesuré au shunt.

## Hypothèses à explorer

| | Principe | Ordre de grandeur | Dépend de |
|---|---|---|---|
| H1 | Panneaux rigides sur un portique ou un bimini **à créer** | 150 à 250 Wc | coût et fardage du support, seule hypothèse qui atteint facilement 200 Wc |
| H2 | Panneaux souples sur le rouf ou sur la capote | 100 à 150 Wc | ombrage de la bôme et des voiles, tenue sur la toile de capote |
| H3 | Panneau mobile orientable, posé au mouillage | 100 Wc | rangement à bord |

Pour chaque hypothèse : production en Ah par jour selon la saison (PVGIS, Saint-Chamas), régulateur MPPT à choisir, et raccordement sur la barrette de servitude de l'étude A (fusible à la batterie et au régulateur).

## Critères de comparaison

- Part du bilan au mouillage couverte, en été et à mi-saison.
- Coût, fixation, ombrage, fardage et esthétique.
- Compatibilité avec un futur passage au LiFePO4 (profil de charge du régulateur).

## Décision

Prochaine étape : chiffrer H1, H2 et H3 avec PVGIS, puis les confronter au bilan mesuré dès qu'un shunt sera posé (étude A).
