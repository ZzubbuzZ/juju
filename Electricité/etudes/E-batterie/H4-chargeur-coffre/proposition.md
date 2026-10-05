---
hypothese: E-H4
titre: Variante de E-H1, Orion XS, chargeur de quai et shunt dans le coffre de la batterie
etat: proposee
resume: Même installation que E-H1, mais l'Orion XS, le chargeur de quai Blue Smart et le shunt de l'étude D sont posés dans le coffre de la LiFePO4 au lieu de la contremarche. Choix sur place, selon la place disponible dans la contremarche.
points_forts:
  - Câbles de sortie et négatifs de l'Orion XS, du chargeur et du shunt très courts, tout dans le même coffre.
  - L'Orion XS et le chargeur chargent directement sur la borne + de la batterie, même coupe-circuit ouvert.
  - La contremarche ne reçoit que l'interrupteur de l'Orion XS et le fusible de son entrée.
points_faibles:
  - L'entrée de l'Orion XS (16 mm², environ 1,5 m) et l'alimentation 230 V du chargeur (environ 6 m) font le trajet jusqu'à la cabine de poupe.
  - Le fil de commande de l'Orion XS fait environ 2 m.
  - Coffre à ouvrir pour accéder à l'Orion XS, au shunt et au chargeur ; un peu de chaleur près de la batterie en pleine charge.
  - Les fils de mesure du shunt et wire180 remontent à la platine, environ 1 à 1,2 m.
decision: "05/10/2026 : variante retenue ou non sur place, face à E-H1 (tout dans la contremarche)."
---

# E-H4 · Variante : Orion XS, chargeur de quai et shunt dans le coffre de la batterie

Variante de [E-H1](../H1-lifepo4/proposition.md). Base : **E-H1**. Câblage : [cablage.yaml](cablage.yaml). Folios cibles : [2j, circuit moteur](folio-2j-circuit-moteur.svg) et [2k, circuit servitude](folio-2k-circuit-servitude.svg). Pas de nomenclature propre : le matériel est celui de E-H1, à quelques mètres de câble près.

## Ce qui change par rapport à E-H1

| Élément | E-H1 (contremarche) | E-H4 (coffre de la batterie) |
|---|---|---|
| Orion XS | Contremarche, près de la platine | Coffre de la batterie |
| Entrée de l'Orion XS (wire203, 16 mm²) | 0,5 m | Environ 1,5 m, du fusible de 70 A de la platine (node003) jusqu'au coffre |
| Sortie de l'Orion XS (wire204, wire205) | Sur node009, fusible de 70 A à la platine | Sur la borne + de la batterie (node007), fusible de 70 A dans le coffre, avant le fusible de 300 A |
| Négatif de l'Orion XS (wire206) | Sur node005 | Côté « bord » du shunt (node087), dans le coffre |
| Commande de l'Orion XS (wire209) | 0,5 m | Environ 2 m, de l'interrupteur (contremarche) jusqu'au coffre |
| Shunt (étude D) | Près du coupe-circuit des négatifs | Dans le coffre, contre la batterie |
| wire009 (− batterie → shunt) | 1 m | 0,2 m |
| wire180 (shunt → node005) | 0,2 m | 1 m, sur le trajet de l'ancien wire009 |
| Fils de mesure du shunt (wire182, wire184) | 0,5 m | 1,2 m |
| Blue Smart | Contremarche, + sur node009 par un fusible de 25 A | Coffre, + sur la borne + de la batterie (node007) par un fusible de 25 A, avant le fusible de 300 A |
| Négatif du Blue Smart (wire212) | Sur node005 | Côté « bord » du shunt (node087), dans le coffre |
| 230 V du Blue Smart (wire213 à wire215) | Environ 4 m | Environ 6 m (Q50) |

Le fusible de l'entrée de l'Orion XS reste à la platine, à la source de wire203, et l'interrupteur à voyant reste près du tableau Scheiber. Dans les deux cas, les négatifs de l'Orion XS et du Blue Smart reviennent côté « bord » du shunt : toute la charge de la LiFePO4 est comptée.

**Entrée de l'Orion XS sur 1,5 m** : la notice demande 16 mm² jusqu'à 5 m, la section de E-H1 suffit.

## Comment choisir sur place

- **Place dans la contremarche** pour l'Orion XS, le Blue Smart (boîtier IP67 aux câbles sortants) et le shunt : si elle suffit, E-H1 garde tout au même endroit, accessible par l'ouverture côté cabine de poupe.
- Sinon, **E-H4** : le coffre de la batterie a de la place (Q51), mais il faut l'ouvrir pour y accéder, et laisser un peu d'air autour du chargeur et de l'Orion XS.
