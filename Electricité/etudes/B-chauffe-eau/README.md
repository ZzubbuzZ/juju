# Étude B · Chauffe-eau

**Objectif** : de l'eau chaude à bord, avec un ballon de 10 à 15 L.

**Base** : le relevé. L'étude A (sécurisation) doit être décidée avant le câblage définitif. Le réseau 230 V est relevé ([folio 3](../../schemas/folio-3-230v.svg)) : boîtier d'arrivée avec différentiel 30 mA, 10 A pour le chargeur, 16 A pour le reste ; à tribord, un départ 16 A alimente les prises de la cuisine et du frigo. Un ballon pourrait se brancher sur ce départ, ou mieux sur un disjoncteur dédié dans le boîtier d'arrivée.

## Questions préalables

- **Q13** (ouverte) : la plaque indique 3GMD. Un échangeur sur le circuit moteur n'est possible que si le moteur a un circuit d'eau douce (vase d'expansion, échangeur). À vérifier à bord.
- **Q19** (ouverte) : place disponible pour le ballon, distance au moteur et au circuit d'eau douce.
- **Q20** (traitée le 27/09) : **6 A au ponton de Saint-Chamas, soit environ 1 400 W pour tout le bord.**

## La contrainte des 6 A au ponton

| Consommateur 230 V | Puissance approximative |
|---|---|
| Chargeur de quai en pleine charge (20 A côté 12 V) | 300 à 350 W |
| Frigo par l'EPS 100 | environ 60 W |
| Éclairage LED | négligeable |
| **Reste disponible** | **environ 1 000 W**, sans marge pour une bouilloire ou un radiateur |

Conséquences :

- La résistance du ballon doit rester **petite, de l'ordre de 500 W**. Un modèle de 800 à 1 200 W ferait déclencher la borne du ponton dès que le chargeur tourne.
- À 500 W, chauffer 15 L de 15 °C à 60 °C demande environ 0,8 kWh, soit **1 h 30 à 2 h** avec les pertes. C'est acceptable pour un ballon qui reste branché au ponton.
- Une autre option est le délestage : couper le chargeur pendant la chauffe, avec un relais ou un simple interrupteur.

## Hypothèses à explorer

| | Principe | Eau chaude au quai | En navigation | Au mouillage | Dépend de |
|---|---|---|---|---|---|
| H1 | Résistance 230 V seule (500 W au plus) | oui | non | non | Q19 |
| H2 | Résistance 230 V + échangeur sur le circuit moteur | oui | oui, moteur en marche | non | Q13 (circuit d'eau douce obligatoire) |
| H3 | Résistance 230 V + résistance 12 V sur le surplus solaire | oui | partiel | partiel | étude C, régulateur avec sortie de délestage |
| H4 | Résistance 230 V alimentée par un convertisseur en navigation | oui | oui | oui | à chiffrer pour l'écarter proprement : 500 W représentent environ 45 A sur une batterie de 110 Ah au plomb |

## Critères de comparaison

- Disponibilité de l'eau chaude selon la situation (quai, navigation, mouillage).
- Effet sur le bilan énergétique ([bilan-energetique.yaml](../../commun/bilan-energetique.yaml)).
- Coût, place, plomberie et câblage 230 V à ajouter.

## Décision

En attente des réponses à Q13 et Q19.
