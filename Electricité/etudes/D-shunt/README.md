# Étude D · Shunt

**Objectif** : mesurer et surveiller la consommation des équipements de servitude. Etablir la quantité d'energie disponible dans la batterie servitude. Surveiller la tension de la batterie moteur.

**Base** : le relevé. L'étude A (sécurisation) doit être décidée avant le câblage définitif. La position du shunt vis à vis de la mise en commun des masses des batteries et l'opportunité d'un shunt sur la batterie moteur sont aussi à prendre en compte. Finalement, une "Build Of Materials" et une estimation du cout pour chaque hypothèse permettra le choix.

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

L'emplacement b regroupe les organes de coupure et de mesure au même endroit. Il faudra confirmer la longueur réelle de wire009 (Q30).

## Batterie moteur : un second shunt n'est pas nécessaire

L'objectif fixé pour la batterie moteur est de **surveiller sa tension**, pas de compter ses ampères-heures. La plupart des moniteurs de batterie ont une entrée auxiliaire de tension prévue pour ça : un seul fil fin, protégé par un fusible à la borne + de la batterie moteur. Un second shunt ne se justifierait que pour suivre l'état de charge de la batterie moteur, ce qui a peu d'intérêt pour une batterie qui ne sert qu'à démarrer.

## Questions préalables

- **Place pour le shunt** (Q27, traitée) : deux emplacements possibles, voir ci-dessus.
- **Lecture souhaitée** : l'application sur smartphone suffit-elle, ou faut-il un afficheur fixe à la table à carte ? C'est un choix à faire, qui distingue les hypothèses H1 et H2.
- **Place pour un afficheur** (Q28, traitée) : oui, à la place de l'ancien indicateur de charge à aiguille du tableau de servitude. H2 ne demande donc aucune découpe nouvelle.
- **Longueur réelle de wire009** : Q30.

## Hypothèses à explorer

Les modèles cités sont des exemples de familles de produits. Leurs caractéristiques (entrée auxiliaire, longueur de câble fournie, consommation propre) sont à vérifier sur les fiches techniques au moment du choix.

| | Principe | Lecture | Batterie moteur | Remarques |
|---|---|---|---|---|
| H1 | Shunt connecté seul (type Victron SmartShunt 500 A) | Application sur smartphone | Tension par l'entrée auxiliaire | Le plus simple à poser : rien à percer au tableau |
| H2 | Moniteur avec afficheur (type Victron BMV-712) | Afficheur rond encastré à la table à carte, et application | Tension par l'entrée auxiliaire | Lecture sans téléphone, mais un câble de données à tirer depuis la cabine de poupe |
| H3 | Moniteur multi-shunts (type Simarine) | Afficheur couleur | Second shunt, ou mesure de tension | Peut aussi lire des jauges de réservoir ; plus cher, surdimensionné si on ne suit que les batteries |
| H4 | Moniteur générique bas coût (shunt et afficheur sans marque) | Afficheur | Selon le modèle | Précision, consommation propre et tenue en milieu marin incertaines |

Pour chaque hypothèse retenue : un `cablage.yaml` (suppression de wire009, ajout du shunt et de ses fils) et la nomenclature chiffrée demandée dans l'objectif.

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

En attente.
