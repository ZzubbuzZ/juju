# Étude C · Panneaux solaires

**Objectif** : tenir au mouillage sans faire tourner le moteur pour recharger.

**Base** : le relevé et le [bilan énergétique](../../commun/bilan-energetique.yaml).

## Constat de départ

Le bilan estimé donne environ **60 Ah par jour au mouillage** et 87 Ah par jour en navigation (moteur non compté ; feu de mouillage à LED, Q7). Or une batterie de servitude de 110 Ah au plomb ne fournit qu'environ 55 Ah sans être abîmée (décharge à 50 %). Elle ne tient donc même pas une journée au mouillage. Une LiFePO4 de 100 Ah, proposée par l'étude E (H1), en fournirait 80 à 90.

Le moteur n'y suffit pas non plus : l'alternateur donne environ **20 A au plus** (Q14), et moins en pratique une fois la batterie à moitié chargée. Récupérer 50 Ah demande donc plusieurs heures de moteur. Le solaire est le seul moyen réaliste de tenir au mouillage.

Trois leviers sont à combiner :

1. **Mesurer** plutôt qu'estimer : un shunt sur la batterie de servitude (étude D).
2. **Produire** : c'est l'objet de cette étude.
3. **Stocker** davantage : c'est l'étude E (batterie de servitude). Sa recommandation, une LiFePO4 chargée par un DC/DC au moteur et un chargeur dédié au quai, est d'abord motivée par l'hydrogène dégagé dans la cabine de poupe (A11), mais elle double aussi la capacité utile.

## Questions préalables

- **Q17** (traitée le 27/09) : étang de Berre (Saint-Chamas), navigation en Méditerranée. C'est l'un des sites les mieux ensoleillés de France.
- **Q18** (traitée le 27/09) : **une capote seulement**, pas de bimini ni de portique.

## Dimensionnement commun avec l'étude E

Le solaire et la batterie se dimensionnent ensemble, à partir d'un même objectif d'autonomie : **combien de jours d'affilée Juju doit-il tenir au mouillage sans moteur ni quai, à quelle saison, et avec combien de jours sans soleil ?** Plus il y a de panneaux, plus la batterie peut être petite, et inversement. Par exemple, avec 200 Wc en été, la batterie n'a plus qu'à passer la nuit (environ 30 Ah) et quelques jours couverts ; sans solaire, chaque jour au mouillage demande environ 60 Ah stockés. Cet objectif reste à fixer par l'utilisateur.

## Ordre de grandeur de la production

Pour 100 Wc en Provence, il faut compter **environ 25 à 35 Ah par jour en été et 10 à 15 Ah en hiver**, selon l'orientation, l'ombrage de la bôme et le régulateur. Pour couvrir les 60 Ah par jour estimés au mouillage, il faut donc **environ 200 Wc en été**. Ces chiffres sont à affiner avec PVGIS (outil gratuit de la Commission européenne) pour Saint-Chamas, et avec un bilan mesuré au shunt.

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
- Profil de charge du régulateur : LiFePO4 si l'étude E (H1) est retenue, plomb sinon. Un régulateur réglable couvre les deux cas.

## Décision

Prochaine étape : chiffrer H1, H2 et H3 avec PVGIS, puis les confronter au bilan mesuré dès qu'un shunt sera posé (étude D). Fixer avec l'étude E l'objectif d'autonomie qui dimensionne à la fois les panneaux et la batterie.
