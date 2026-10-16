---
hypothese: E-H5
titre: Variante de E-H1, chargeur de quai au coffre de cockpit
etat: retenue
resume: Même installation que E-H1, l'Orion XS et le shunt dans la niche de la contremarche, mais le chargeur de quai Blue Smart IP67 va dans le coffre de cockpit tribord, près du boîtier d'arrivée 230 V. Sa sortie 12 V rejoint la niche par les câbles fournis du chargeur (12 AWG, 1,40 m, trajet d'environ 1,2 m), avec son fusible de 25 A à la source et son négatif côté « bord » du shunt.
points_forts:
  - Libère le bas du fond de la niche, la plus grande surface qu'y prenait le Blue Smart.
  - Câble 230 V court, le C10 du chargeur est dans le même coffre.
  - Boîtier IP67, fait pour un coffre exposé ; plus de chaleur du chargeur dans la niche.
points_faibles:
  - "Trajet d'environ 1,2 m pour 1,40 m de câble fourni (Q64, 16/10) : 20 cm de marge, à vérifier à la pose."
  - "Chute d'environ 0,27 V (2,2 %) à 17 A, non compensée : le Blue Smart IP67 ne prend pas en charge VE.Smart (16/10)."
decision: "14/10/2026 : retenue par l'utilisateur. L'Orion XS et le shunt restent dans la niche de la contremarche (E-H1), le Blue Smart va au coffre de cockpit. E-H4 écartée. 16/10 : trajet d'environ 1,2 m (Q64) ; sortie 12 V par les câbles fournis du chargeur, sans rallonge de 10 mm² (choix de l'utilisateur)."
---

# E-H5 · Variante : chargeur de quai au coffre de cockpit

Variante de [E-H1](../H1-lifepo4/proposition.md). Base : **E-H1**. Câblage : [cablage.yaml](cablage.yaml). Nomenclature (différence avec E-H1) : [nomenclature.yaml](nomenclature.yaml). Folio cible : [2o, circuit servitude](folio-2o-circuit-servitude.svg) ; le circuit moteur reste celui du [folio 2h](../H1-lifepo4/folio-2h-circuit-moteur.svg).

## Ce qui change par rapport à E-H1

| Élément | E-H1 | E-H5 |
|---|---|---|
| Blue Smart IP67 12/17 | Niche de la contremarche, en bas du fond | Coffre de cockpit tribord, près du boîtier d'arrivée 230 V |
| Fusible de 25 A (node059, node060) | Côté batterie du coupe-circuit de servitude (node020) | Inchangé : il reste à la source du câble, dans la niche |
| Sortie + (wire064) | 4 mm², 0,5 m | **Câble rouge fourni**, 12 AWG, 1,40 m (16/10) |
| Retour − (wire059) | 4 mm², 0,5 m, sur node022 | **Câble noir fourni**, 12 AWG, 1,40 m, sur node022 (côté « bord » du shunt) |
| 230 V (wire311 à wire313) | 3 × 1,5 mm², environ 4 m | 3 × 1,5 mm², environ 1 m |
| Orion XS, shunt, autres fusibles | Niche de la contremarche | Inchangés |

## Section de la sortie 12 V

**16/10 : les câbles fournis suffisent.** Le trajet du coffre de cockpit à la niche fait environ 1,2 m : 60 cm dans le coffre, puis 60 cm à travers le compartiment moteur (Q64). Les câbles livrés avec le chargeur (rouge et noir, 12 AWG, soit environ 3,3 mm², 1,40 m) y arrivent seuls ; la rallonge de 10 mm² et sa jonction dans le coffre, prévues pour les 5 m de Q50, sont abandonnées (choix de l'utilisateur). La marge n'est que de 20 cm : si le câble ne suffit pas à la pose, une courte rallonge reste possible.

Chute à 17 A : 2 × 1,4 × 17 × 0,0175 / 3,3 ≈ 0,25 V, plus environ 0,02 V pour le pont wire056 et le fusible, soit **0,27 V (2,2 %)**, sous les 3 %. Le fusible de 25 A, à la source dans la niche, protège le câble fourni, que Victron équipe lui-même d'un fusible de 30 A. Ce fusible de 30 A reste en place côté chargeur : il protège le chargeur contre une inversion de polarité. Détail : [dimensionnement.md](../../../commun/dimensionnement.md#chute-de-tension-du-chargeur-de-quai-1610).

*Calcul du 14/10, dépassé : pour 5 m, S = 2 × 5 × 17 × 0,0175 / 0,36 ≈ 8,3 mm², soit 10 mm².*

## Chute de tension et fin de charge

Le chargeur règle sa tension à ses bornes : sans correction, il verrait la batterie un peu plus haut qu'elle n'est et passerait trop tôt en fin de charge. L'idée du 14/10 était que le SmartShunt transmette la tension mesurée à la batterie par le réseau **VE.Smart**.

**Correction du 16/10** : le Blue Smart IP67 ne prend pas en charge le réseau VE.Smart (liste de compatibilité de Victron) : la chute n'est pas compensée. Avec les câbles fournis seuls, elle n'est que d'environ 0,27 V à 17 A et 0,06 V à 4 A, en fin de charge. Les réglages du chargeur et du shunt en tiennent compte : [reglages-charge-et-shunt.md](../../../documentation-technique/reglages-charge-et-shunt.md).

La chute dans wire010 (shunt → − de la batterie, 1 m de 35 mm², environ 0,5 mΩ) ne fausse que la tension lue par le shunt, de moins de 10 mV en charge, et pas l'état de charge, compté en ampères-heures : elle ne justifie pas de rapprocher le shunt de la batterie (question de l'utilisateur, 14/10).

## Niche de la contremarche

Sans le Blue Smart, la niche reçoit le shunt et l'Orion XS (haut du fond) et les fusibles (milieu du fond) : voir [Implantation dans la niche](../H1-lifepo4/proposition.md#implantation-dans-la-niche-1410) dans E-H1. Le bas du fond reste libre pour le passage des câbles, dont les deux 10 mm² qui arrivent du coffre de cockpit.

## Décision

**14/10/2026** : retenue par l'utilisateur. L'installation cible (`cible/cible.yaml`) applique E-H5, et donc E-H1 avec elle. Le folio 2i de E-H1 est archivé : le folio 2o le remplace pour le circuit servitude.

**16/10/2026** : trajet d'environ 1,2 m (Q64). La sortie 12 V passe par les câbles fournis du chargeur, sans rallonge (choix de l'utilisateur) ; nomenclature réduite d'environ 75 €.
