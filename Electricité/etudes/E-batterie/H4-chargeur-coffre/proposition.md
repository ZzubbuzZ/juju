---
hypothese: E-H4
titre: Variante de E-H1, chargeur de quai et shunt dans le coffre de la batterie
etat: proposee
resume: Même installation que E-H1, mais le chargeur de quai Blue Smart et le shunt de l'étude D sont posés dans le coffre de la LiFePO4 au lieu de la contremarche. Choix sur place, selon la place disponible dans la contremarche.
points_forts:
  - Câbles 12 V et négatifs du chargeur et du shunt très courts, tout dans le même coffre.
  - Le chargeur charge directement sur la borne + de la batterie, même coupe-circuit ouvert.
  - La contremarche n'a à recevoir que l'Orion XS et ses fusibles.
points_faibles:
  - L'alimentation 230 V du chargeur fait le trajet jusqu'à la cabine de poupe, environ 6 m.
  - Coffre à ouvrir pour accéder au shunt et au chargeur ; un peu de chaleur près de la batterie en pleine charge.
  - Les fils de mesure du shunt et wire180 remontent à la platine, environ 1 à 1,2 m.
decision: "05/10/2026 : variante retenue ou non sur place, face à E-H1 (chargeur et shunt dans la contremarche)."
---

# E-H4 · Variante : chargeur de quai et shunt dans le coffre de la batterie

Variante de [E-H1](../H1-lifepo4/proposition.md). Base : **E-H1**. Câblage : [cablage.yaml](cablage.yaml), [folio 2i](folio-2i-coffre.svg). Pas de nomenclature propre : le matériel est celui de E-H1, à quelques mètres de câble près.

## Ce qui change par rapport à E-H1

| Élément | E-H1 (contremarche) | E-H4 (coffre de la batterie) |
|---|---|---|
| Shunt (étude D) | Près du coupe-circuit des négatifs | Dans le coffre, contre la batterie |
| wire009 (− batterie → shunt) | 1 m | 0,2 m |
| wire180 (shunt → node005) | 0,2 m | 1 m, sur le trajet de l'ancien wire009 |
| Fils de mesure du shunt (wire182, wire184) | 0,5 m | 1,2 m |
| Blue Smart | Contremarche, + sur node009 par un fusible de 25 A | Coffre, + sur la borne + de la batterie (node007) par un fusible de 25 A, avant le fusible de 300 A |
| Négatif du Blue Smart (wire212) | Sur node005 | Côté « bord » du shunt (node087), dans le coffre |
| 230 V du Blue Smart (wire213 à wire215) | Environ 4 m | Environ 6 m (Q50) |

Dans les deux cas, les négatifs de l'Orion XS et du Blue Smart reviennent côté « bord » du shunt : toute la charge de la LiFePO4 est comptée.

## Comment choisir sur place

- **Place dans la contremarche** pour le Blue Smart (boîtier IP67 aux câbles sortants) et le shunt, à côté de l'Orion XS : si elle suffit, E-H1 garde tout au même endroit, accessible par l'ouverture côté cabine de poupe.
- Sinon, **E-H4** : le coffre de la batterie a de la place (Q51), mais il faut l'ouvrir pour y accéder, et laisser un peu d'air autour du chargeur.
