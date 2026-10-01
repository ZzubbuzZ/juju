# Étude D · Shunt

**Objectif** : mesurer et surveiller la consommation des équipements de servitude. Etablir la quantité d'energie disponible dans la batterie servitude. Surveiller la tension de la batterie moteur.

**Base** : le programme retenu de l'étude A (A-H4, qui cumule A-H2), décidé le 30/09. Les fils de mesure du shunt partent ainsi en aval des fusibles de 400 A. La position du shunt vis à vis de la mise en commun des masses des batteries et l'opportunité d'un shunt sur la batterie moteur sont aussi à prendre en compte. Finalement, une "Build Of Materials" et une estimation du cout pour chaque hypothèse permettra le choix.

## Où placer le shunt

Un shunt ne compte que le courant qui le traverse. Pour mesurer la batterie de servitude, **son négatif, et lui seul, doit passer par le shunt** ; toutes les charges et toutes les sources de charge restent de l'autre côté.

Sur Juju, cette place existe déjà (voir le [folio 1](../../schemas/folio-1-actuel.svg)) :

```
avant :  node008 (− batterie servitude) ──── wire009, 35 mm², 1 m ────► node005 (CC masse, côté batteries)
après :  node008 ── câble court ──► [SHUNT] ── câble court ──► node005
```

Ce que cette position mesure correctement :

- **Toutes les charges de servitude**, y compris la pompe de cale automatique prévue par A-H1, dont la masse revient sur node005.
- **Le chargeur de quai** : sa masse (wire005) arrive sur node005, donc du côté charges du shunt. Sa charge de la batterie de servitude est comptée.
- **L'alternateur, via le coupleur** : le courant de charge revient par la masse commune, puis traverse le shunt vers la batterie de servitude.
- **Le démarreur, quand le coupe-circuit de couplage est fermé** : la batterie de servitude participe alors au démarrage, et ce courant de plusieurs centaines d'ampères traverse le shunt. Il faut donc un shunt dimensionné en conséquence (500 A).

Le coupe-circuit des négatifs (node005 → node006) reste en aval du shunt. Le shunt continue donc de mesurer bateau coupé : consommation résiduelle, pompe de cale, chargeur de quai.

La mise en commun des masses ne gêne pas la mesure, tant que **seul le négatif de la batterie de servitude** est raccordé côté batterie du shunt. La batterie moteur reste sur node005 par wire004, sans passer par le shunt.

### Deux emplacements possibles

wire009 part du coffre de la batterie de servitude, traverse la cloison vers le compartiment moteur, puis remonte derrière la descente jusqu'au coupe-circuit des négatifs (Q27). Électriquement, le shunt peut se placer à n'importe quel point de ce fil. Deux emplacements sont pratiques :

| | Emplacement | Pour | Contre |
|---|---|---|---|
| a | Au départ, dans le coffre de la batterie de servitude (cabine de poupe) | Fil d'alimentation du shunt très court jusqu'au + de la batterie | Coffre à ouvrir pour y accéder ; humidité éventuelle au fond du coffre |
| b | À l'arrivée, derrière la descente, près du coupe-circuit des négatifs | Accessible par l'ouverture côté cabine de poupe, avec le coupleur ; près du tableau et de la table à carte | Fil d'alimentation du shunt plus long, jusqu'à la batterie ou au côté batterie du coupe-circuit de servitude (node009) |

L'emplacement b regroupe les organes de coupure et de mesure au même endroit. wire009 ne fait que 1 m (Q30, confirmé le 29/09) : la batterie est juste derrière la paroi latérale du bloc moteur, et la contremarche des coupe-circuits juste au-dessus. Le fil d'alimentation du shunt reste donc court dans les deux cas, ce qui ôte à a son principal avantage.

## Batterie moteur : un second shunt n'est pas nécessaire

L'objectif fixé pour la batterie moteur est de **surveiller sa tension**, pas de compter ses ampères-heures. La plupart des moniteurs de batterie ont une entrée auxiliaire de tension prévue pour ça : un seul fil fin, protégé par un fusible à la borne + de la batterie moteur. Un second shunt ne se justifierait que pour suivre l'état de charge de la batterie moteur, ce qui a peu d'intérêt pour une batterie qui ne sert qu'à démarrer.

## Questions préalables

- **Place pour le shunt** (Q27, traitée) : deux emplacements possibles, voir ci-dessus.
- **Lecture souhaitée** : l'application sur smartphone suffit-elle, ou faut-il un afficheur fixe à la table à carte ? C'est un choix à faire, qui distingue les hypothèses H1 et H2.
- **Place pour un afficheur** (Q28, traitée) : oui, à la place de l'ancien indicateur de charge à aiguille du tableau de servitude. H2 ne demande donc aucune découpe nouvelle, sous réserve du diamètre du trou.
- **Indicateur à aiguille** (Q41, ouverte) : branchement, diamètre du trou et profondeur libre derrière le tableau. Utile pour H2 seulement.
- **Longueur réelle de wire009** (Q30, traitée) : 1 m confirmé.
- **Traceur Garmin et réseau NMEA 2000** (Q44, ouverte) : modèle exact, réseau existant ou non, emplacement et alimentation. Utile pour H6 seulement.

## Hypothèses

Les modèles cités sont des exemples de familles de produits. Leurs caractéristiques (entrée auxiliaire, longueur de câble fournie, consommation propre) sont à vérifier sur les fiches techniques au moment du choix. Les coûts sont ceux que calcule `outils/verifier.py` à partir des nomenclatures : prix catalogue du 01/10/2026 pour le moniteur (relevés par recherche web, liens dans chaque nomenclature), estimations pour les accessoires. La page de consultation présente la même comparaison, avec les liens.

| | Principe | Lecture | Batterie moteur | Coût estimé | État |
|---|---|---|---|---|---|
| [H1](H1-shunt-connecte/proposition.md) | Shunt connecté seul (type Victron SmartShunt 500 A) | Application sur smartphone | Tension par l'entrée auxiliaire | environ 160 € | Rédigée, [folio 2e](H1-shunt-connecte/folio-2e-shunt.svg) |
| [H2](H2-moniteur-afficheur/proposition.md) | Moniteur avec afficheur (type Victron BMV-712 Smart) | Afficheur rond à la place de l'indicateur à aiguille, et application | Tension par l'entrée auxiliaire | environ 165 €, plus l'adaptation de la découpe (Q41) | Rédigée, [folio 2f](H2-moniteur-afficheur/folio-2f-afficheur.svg) |
| [H3](H3-simarine-pico/proposition.md) | Moniteur multi-capteurs (Simarine Pico et shunt SC503) | Afficheur couleur | Second shunt, ou mesure de tension | environ 400 € | Non développée, à écarter : voir ci-dessous |
| [H4](H4-moniteur-generique/proposition.md) | Moniteur générique bas coût (type Junctek KH140F, 400 A) | Afficheur et application | Selon le modèle | environ 90 € | Non développée, à écarter : voir ci-dessous |
| [H5](H5-cerbo-gx-touch/proposition.md) | SmartShunt de H1, centrale Victron Cerbo GX et écran tactile GX Touch 50 | Écran 5 pouces à la table à carte, application, portail VRM | Tension par l'entrée auxiliaire du shunt | environ 675 € | Rédigée, [folio 2g](H5-cerbo-gx-touch/folio-2g-cerbo.svg) ; place à relever (Q43) |
| [H6](H6-cerbo-traceur-garmin/proposition.md) | SmartShunt de H1 et centrale Victron Cerbo-S GX sans écran, données transmises au traceur Garmin par NMEA 2000 | Traceur GPSMAP 7407 quand il est allumé, application, portail VRM | Tension par l'entrée auxiliaire du shunt (affichage sur le traceur à vérifier) | environ 600 €, 485 € si le traceur est déjà sur un réseau NMEA 2000 | Rédigée sans câblage, en attente de Q44 |

H1 et H2 se posent de la même façon : shunt à l'emplacement b, wire009 repris sur le shunt, wire180 (35 mm²) vers le coupe-circuit des négatifs, et deux fils de mesure de 0,75 mm² protégés à leur source par un fusible de 1 A (wire181 à wire184). H2 ajoute le câble de données wire185 et l'afficheur. Nouveaux numéros : node086 à node095, wire180 à wire185. H5 reprend H1 et ajoute un Cerbo GX alimenté après le coupe-circuit de servitude (fusible 3 A), relié au shunt par VE.Direct et à l'écran : node340 à node346, wire186 à wire190.

**Pourquoi ne pas développer H3 et H4** (à confirmer) :

- **H3** : son intérêt est de lire aussi les jauges de réservoir et plusieurs batteries. Juju n'a pas de jauge à relier, et l'objectif ne demande qu'une tension pour la batterie moteur. Elle coûte plus du double de H2 sans répondre à un besoin listé, et son kit standard n'a qu'un shunt de 300 A.
- **H4** : l'état de charge se calcule en additionnant le courant pendant des jours. Une petite erreur à faible courant (veille, pompe de cale) ou une dérive du zéro fausse le résultat, et c'est justement la consommation de veille que l'étude doit surveiller (détection du court-circuit résistif de A-H2). Sa tenue en milieu marin et sa consommation propre sont inconnues. Son shunt de 400 A est en outre sous les 500 A visés. L'économie, environ 75 €, ne compense pas une mesure à laquelle on ne peut pas se fier.

## Critères de comparaison

- **Mesure** : précision à faible courant (consommation de veille), calibre du shunt (500 A à cause du démarrage couplé), tension de la batterie moteur.
- **Lecture** : afficheur fixe ou application, alarme de tension basse.
- **Évolutions** : compatibilité LiFePO4 (réglage de la chimie) ; dialogue avec un futur régulateur solaire (étude C) et un futur chargeur.
- **Consommation propre** du moniteur, qui s'ajoute au bilan.
- **Coût** : nomenclature complète (shunt, câbles, cosses, fusibles de l'alimentation et de l'entrée auxiliaire, afficheur, câble de données).
- **Pose** : accès à la batterie de servitude, trajet des câbles.

## Ce que l'étude apporte aux autres

Une fois le shunt posé, un protocole simple permet de remplacer les estimations de [bilan-energetique.yaml](../../commun/bilan-energetique.yaml) par des mesures : allumer les circuits un par un, noter le courant, puis passer leur `statut` de `estime` à `releve`. Les études B (chauffe-eau) et C (solaire) se dimensionneront alors sur des chiffres réels.

## Décision

En attente. Le choix porte sur la lecture : smartphone seul (H1) ou afficheur fixe (H2).

Proposition de Claude (01/10) : **H2**. L'afficheur prend la place de l'indicateur à aiguille sans découpe nouvelle, l'alarme de tension basse est visible sans téléphone, et un shunt connecté seul (H1) n'accepte pas d'afficheur dédié : une lecture fixe ne pourrait s'y ajouter que par l'écran d'un Cerbo GX (H5), bien plus cher. Aux prix relevés le 01/10, les deux coûtent le même prix, environ 165 €. À trancher, ainsi que l'écartement de H3 et H4.

H5 (ajoutée le 01/10 à la demande de l'utilisateur) est l'option « tableau de bord » : environ quatre fois le prix de H2, avec une consommation d'environ 0,3 A tant que le Cerbo GX est allumé. Elle se justifie si l'on prévoit d'autres appareils Victron (régulateur solaire de l'étude C, chargeur, LiFePO4) ; sinon H2 donne la même mesure pour beaucoup moins. Elle peut aussi venir plus tard : le SmartShunt (H1) comme le BMV-712 (H2) ont un port VE.Direct et se raccordent au Cerbo GX sans rien racheter ; avec H2, l'afficheur rond reste en service à côté de l'écran.

H6 (ajoutée le 01/10 à la demande de l'utilisateur) est une variante de H5 : le traceur Garmin sert d'afficheur à la place du GX Touch 50. Le GPSMAP 7407 n'accepte pas l'application Victron complète (OneHelm), mais il lit en NMEA 2000 l'état de charge, la tension et le courant publiés par le Cerbo. Elle n'économise qu'environ 75 € sur H5, car il faut créer le réseau NMEA 2000, sauf s'il existe déjà (Q44). Elle se justifie surtout si un réseau NMEA 2000 est prévu de toute façon pour d'autres instruments. H5 peut d'ailleurs passer au Cerbo-S GX, comme H6, pour environ 610 €.

Avant la pose : répondre à Q41 (branchement de l'indicateur à aiguille, diamètre du trou) pour H2, à Q43 (place du Cerbo GX et de l'écran) pour H5 et H6, à Q44 (traceur et réseau NMEA 2000) pour H6.
