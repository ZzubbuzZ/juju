# Étude B · Chauffe-eau

**Objectif** : de l'eau chaude à bord, avec un ballon de 10 à 15 L.

**Décision du 07/10** : ballon **Carbest CozyWater 10C** (10 L, 230 V 800 W et 12 V 200 W), commandé. Voir [B-H1](H1-cozywater-10c/proposition.md) (230 V et circuit d'eau) et [B-H3](H3-entree-12v/proposition.md) (entrée 12 V). Notice : [documentation/](documentation/).

**Base** : le relevé. L'étude A (sécurisation) doit être décidée avant le câblage définitif. Le réseau 230 V est relevé ([folio 3](../../schemas/folio-3-230v.svg)) :

- boîtier d'arrivée (coffre de cockpit tribord) : différentiel 30 mA / 25 A, puis un disjoncteur de 10 A pour le chargeur et un de 16 A pour le reste du bord ;
- boîtier de distribution tribord (cabinet de toilette) : quatre disjoncteurs Legrand DNX3, C10 pour l'éclairage, C16 pour les prises tribord (cuisine, frigo, toilette), C16 pour les prises bâbord, et un **second C10 dont le circuit est inconnu (Q42)**.

Le ballon pourrait se brancher sur une prise tribord, ou mieux sur un départ dédié : le second C10 s'il est libre (Q42), sinon un disjoncteur ajouté. Tout ce qui passe par le boîtier tribord reste limité par le 16 A d'arrivée.

## Questions préalables

- **Q13** (traitée le 28/09) : le 3GMD est refroidi directement à l'eau de mer. Il n'a pas de circuit d'eau douce sur lequel brancher un ballon à échangeur.
- **Q19** (ouverte) : place disponible pour le ballon, distance au moteur et au circuit d'eau douce. Contraintes du CozyWater 10C ajoutées le 07/10.
- **Q20** (traitée, corrigée le 01/10) : les bornes de quai du port de Saint-Chamas fournissent **16 A, soit environ 3 700 W**. Ce calibre n'est pas garanti en escale, où il est souvent plus faible (les exemples ci-dessous prennent 10 et 6 A). La première réponse (6 A au ponton) venait de la presse.
- **Q42** (ouverte) : circuit du second disjoncteur de 10 A du boîtier tribord, peut-être libre pour le ballon.
- **Q54** (ouverte) : circuit d'eau douce existant, robinets, pression de redémarrage de la pompe.
- **Q55** (ouverte) : raccords et câbles du ballon, à sa réception.
- **Q56** (ouverte) : prise 230 V compatible avec la fiche Schuko du ballon.

## La puissance disponible au quai

| Consommateur 230 V | Puissance approximative |
|---|---|
| Chargeur de quai Dolphin en pleine charge (20 A côté 12 V) | 300 à 350 W |
| Second chargeur, si l'étude E (H1, LiFePO4) est retenue | environ 250 W |
| Frigo par l'EPS 100 | environ 60 W |
| Éclairage LED | négligeable |
| **Total sans le ballon** | **environ 650 W** |

| Borne | Puissance | Reste pour le ballon |
|---|---|---|
| Saint-Chamas, 16 A | environ 3 700 W | environ 3 000 W : le CozyWater (800 W) passe sans difficulté, avec une bouilloire en plus |
| Escale à 10 A | environ 2 300 W | environ 1 600 W : le ballon passe, mais pas avec une bouilloire |
| Escale à 6 A | environ 1 400 W | environ 750 W : les 800 W du ballon passent tout juste ; couper un chargeur pendant la chauffe, ou chauffer batteries pleines |

Conséquences :

- **À Saint-Chamas, la puissance n'est plus une contrainte.** À 800 W, chauffer les 10 L du CozyWater de 15 °C à 60 °C demande environ 0,52 kWh, soit **environ 45 min** avec les pertes.
- **En escale, il faut pouvoir réduire la puissance.** Deux solutions : un ballon à **résistance de 500 à 750 W**, qui convient partout au prix d'une chauffe plus lente, ou un **interrupteur de délestage** qui coupe le ballon (ou les chargeurs) sur une borne faible.
- Le disjoncteur de 16 A d'arrivée limite de toute façon l'ensemble des prises et du ballon à environ 3 700 W.

## Hypothèses à explorer

| | Principe | Eau chaude au quai | En navigation | Au mouillage | Dépend de |
|---|---|---|---|---|---|
| [H1](H1-cozywater-10c/proposition.md) | **Retenue** : CozyWater 10C sur le 230 V (800 W), circuit d'eau à pression réduite | oui | non | non | Q19, Q42, Q54 à Q56 |
| ~~H2~~ | ~~Résistance 230 V + échangeur sur le circuit moteur~~ | | | | **Écartée** (Q13) : moteur refroidi à l'eau de mer. Faire passer de l'eau de mer dans le ballon l'exposerait à la corrosion et au sel ; il faudrait remotoriser ou ajouter un circuit d'eau douce |
| [H3](H3-entree-12v/proposition.md) | **Proposée** : entrée 12 V (200 W) du même ballon, sur la LiFePO4 et le surplus solaire | oui | partiel | partiel | étude C, E-H1, Q19 |
| H4 | Résistance 230 V alimentée par un convertisseur en navigation | oui | oui | oui | à chiffrer pour l'écarter proprement : 500 W représentent environ 45 A en 12 V, et une chauffe complète (0,8 kWh) environ 65 Ah, l'essentiel d'une LiFePO4 de 100 Ah (étude E) et plus que ce que le plomb actuel peut fournir |

## Critères de comparaison

- Disponibilité de l'eau chaude selon la situation (quai, navigation, mouillage).
- Effet sur le bilan énergétique ([bilan-energetique.yaml](../../commun/bilan-energetique.yaml)).
- Coût, place, plomberie et câblage 230 V à ajouter.

## Décision

Sans H2, l'eau chaude en navigation et au mouillage ne peut venir que de l'électricité : H3 (surplus solaire, étude C) ou H4 (convertisseur, peu réaliste même avec une LiFePO4, étude E).

**07/10 : le chauffe-eau commandé est un Carbest CozyWater 10C.** Il a les deux résistances : il réalise H1 au quai et rend H3 possible sans autre achat que le câblage 12 V.

## Suivi

| Tâche | Où | État |
|---|---|---|
| Vérifier que l'installation est correctement calibrée | B-H1 (230 V), B-H3 (12 V) | 230 V : rien à changer (3,5 A sur un C16 ou un C10, différentiel 30 mA) ; fiche Schuko à vérifier (Q56). 12 V : relais et fusible 30 A, 6 mm² |
| Trouver l'emplacement du ballon | Q19 | à relever à bord |
| Éléments du circuit d'eau pressurisé : pompe, vase, chauffe-eau, vanne de sécurité, robinet | B-H1, folio 2l | pompe Seaflo conservée ; réducteur 1,5 bar + vase Seaflo 1 L (SFAT-100-125-01) ; soupape 3 bar fournie ; robinet selon Q54 |
| Relais de commande, fusibles | B-H3 | relais 30 A, fusible 30 A, interrupteur à voyant |
| Afficheur | B-H1 | fourni avec le ballon (panneau de commande, minuterie) |
| Pression du vase pour perdre le moins d'eau par la soupape | B-H1 | la pompe coupe à 2,8 bar, trop près des 3 bar de la soupape : réducteur à 1,5 bar, vase gonflé à 1,4 bar |
| Petit matériel | nomenclatures de B-H1 et B-H3 | raccords à confirmer à réception (Q55) |
