# Étude B · Chauffe-eau

**Objectif** : de l'eau chaude à bord, avec un ballon de 10 à 15 L.

**Base** : le relevé. L'étude A (sécurisation) doit être décidée avant le câblage définitif. Le circuit 230 V n'est pas encore relevé (folio 3 à faire), or il conditionne toutes les hypothèses.

## Questions préalables

- **Q13** : 3GM30 ou 3GM30F ? Un échangeur sur le circuit moteur n'est possible qu'avec un circuit d'eau douce (3GM30F).
- **Q19** : place disponible pour le ballon, distance au moteur et au circuit d'eau douce.
- **Q20** : puissance disponible sur la prise de quai. Elle est partagée avec le chargeur (20 A côté 12 V, soit environ 300 W côté 230 V) et avec l'EPS 100 du frigo.

## Hypothèses à explorer

| | Principe | Eau chaude au quai | En navigation | Au mouillage | Dépend de |
|---|---|---|---|---|---|
| H1 | Résistance 230 V seule | oui | non | non | Q20 |
| H2 | Résistance 230 V + échangeur sur le circuit moteur | oui | oui, moteur en marche | non | Q13 (3GM30F obligatoire) |
| H3 | Résistance 230 V + résistance 12 V sur le surplus solaire | oui | partiel | partiel | étude C, régulateur avec sortie de délestage |
| H4 | Résistance 230 V alimentée par un convertisseur en navigation | oui | oui | oui | à chiffrer pour l'écarter proprement : 500 W représentent environ 45 A sur une batterie de 110 Ah au plomb |

## Critères de comparaison

- Disponibilité de l'eau chaude selon la situation (quai, navigation, mouillage).
- Effet sur le bilan énergétique ([bilan-energetique.yaml](../../commun/bilan-energetique.yaml)).
- Coût, place, plomberie et câblage 230 V à ajouter.

## Décision

En attente des réponses à Q13, Q19 et Q20, et du relevé 230 V.
