---
hypothese: E-H5
titre: Variante de E-H1, chargeur de quai au coffre de cockpit
etat: retenue
resume: Même installation que E-H1, l'Orion XS et le shunt dans la niche de la contremarche, mais le chargeur de quai Blue Smart IP67 va dans le coffre de cockpit tribord, près du boîtier d'arrivée 230 V. Sa sortie 12 V rejoint la niche en 10 mm² (environ 5 m), avec son fusible de 25 A à la source et son négatif côté « bord » du shunt.
points_forts:
  - Libère le bas du fond de la niche, la plus grande surface qu'y prenait le Blue Smart.
  - Câble 230 V court, le C10 du chargeur est dans le même coffre.
  - Boîtier IP67, fait pour un coffre exposé ; plus de chaleur du chargeur dans la niche.
points_faibles:
  - Deux câbles de 10 mm² d'environ 5 m à passer entre le coffre et la niche (Q64), environ 75 € de plus.
  - Chute d'environ 0,57 V (4,7 %) à 17 A, câbles fournis du chargeur compris, non compensée (le Blue Smart IP67 ne prend pas en charge VE.Smart, 16/10) ; fin de charge au quai plus lente.
  - Jonction des câbles 12 V fournis du chargeur sur le 10 mm², dans le coffre.
decision: "14/10/2026 : retenue par l'utilisateur. L'Orion XS et le shunt restent dans la niche de la contremarche (E-H1), le Blue Smart va au coffre de cockpit. E-H4 écartée."
---

# E-H5 · Variante : chargeur de quai au coffre de cockpit

Variante de [E-H1](../H1-lifepo4/proposition.md). Base : **E-H1**. Câblage : [cablage.yaml](cablage.yaml). Nomenclature (différence avec E-H1) : [nomenclature.yaml](nomenclature.yaml). Folio cible : [2o, circuit servitude](folio-2o-circuit-servitude.svg) ; le circuit moteur reste celui du [folio 2h](../H1-lifepo4/folio-2h-circuit-moteur.svg).

## Ce qui change par rapport à E-H1

| Élément | E-H1 | E-H5 |
|---|---|---|
| Blue Smart IP67 12/17 | Niche de la contremarche, en bas du fond | Coffre de cockpit tribord, près du boîtier d'arrivée 230 V |
| Fusible de 25 A (node059, node060) | Côté batterie du coupe-circuit de servitude (node020) | Inchangé : il reste à la source du câble, dans la niche |
| Sortie + (wire064) | 4 mm², 0,5 m | **10 mm²**, environ 5 m (Q64) |
| Retour − (wire059) | 4 mm², 0,5 m, sur node022 | **10 mm²**, environ 5 m, sur node022 (côté « bord » du shunt) |
| 230 V (wire311 à wire313) | 3 × 1,5 mm², environ 4 m | 3 × 1,5 mm², environ 1 m |
| Orion XS, shunt, autres fusibles | Niche de la contremarche | Inchangés |

## Section de la sortie 12 V

S = 2 × L × I × 0,0175 / ΔU = 2 × 5 × 17 × 0,0175 / 0,36 ≈ 8,3 mm², soit **10 mm²** (ΔU = 3 %). Avec 10 mm², la chute est d'environ 0,31 V à 17 A, fusible et wire056 compris (2,6 %). Le fusible de 25 A, à la source dans la niche, protège le 10 mm² comme les câbles fournis du chargeur.

La longueur de 5 m vient de Q50 (coffre de cockpit → coffre de la batterie) ; le trajet jusqu'à la niche est à mesurer (Q64). Au-delà de 6 m environ, il faudrait passer en 16 mm².

## Chute de tension et fin de charge

Le chargeur règle sa tension à ses bornes : sans correction, il verrait la batterie 0,3 V plus haut qu'elle n'est et passerait trop tôt en fin de charge. Le SmartShunt mesure la tension à la batterie et la transmet au Blue Smart par le réseau **VE.Smart** (VictronConnect), qui compense la chute de ses câbles. Compatibilité à vérifier dans VictronConnect, à la mise en service.

**Correction du 16/10** : le Blue Smart IP67 ne prend pas en charge le réseau VE.Smart (liste de compatibilité de Victron), et la chute n'est donc pas compensée. Avec les câbles fournis du chargeur (12 AWG, 1,40 m), elle atteint environ 0,57 V (4,7 %) à 17 A. Elle ralentit la fin de charge sans risque pour la batterie ; les réglages du chargeur et du shunt en tiennent compte. Détail dans [dimensionnement.md](../../../commun/dimensionnement.md#chute-de-tension-du-chargeur-de-quai-1610) et [reglages-charge-et-shunt.md](../../../documentation-technique/reglages-charge-et-shunt.md).

La chute dans wire010 (shunt → − de la batterie, 1 m de 35 mm², environ 0,5 mΩ) ne fausse que la tension lue par le shunt, de moins de 10 mV en charge, et pas l'état de charge, compté en ampères-heures : elle ne justifie pas de rapprocher le shunt de la batterie (question de l'utilisateur, 14/10).

## Niche de la contremarche

Sans le Blue Smart, la niche reçoit le shunt et l'Orion XS (haut du fond) et les fusibles (milieu du fond) : voir [Implantation dans la niche](../H1-lifepo4/proposition.md#implantation-dans-la-niche-1410) dans E-H1. Le bas du fond reste libre pour le passage des câbles, dont les deux 10 mm² qui arrivent du coffre de cockpit.

## Décision

**14/10/2026** : retenue par l'utilisateur. L'installation cible (`cible/cible.yaml`) applique E-H5, et donc E-H1 avec elle. Le folio 2i de E-H1 est archivé : le folio 2o le remplace pour le circuit servitude.
