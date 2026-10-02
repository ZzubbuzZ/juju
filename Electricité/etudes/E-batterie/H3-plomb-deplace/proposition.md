---
hypothese: E-H3
titre: Plomb déplacé hors des cabines
etat: ecartee
resume: La batterie au plomb quitte la cabine de poupe pour un coffre ventilé hors des cabines, par exemple le coffre de cockpit tribord, près de la batterie moteur. Ses câbles de 35 mm² jusqu'aux coupe-circuits sont rallongés.
points_forts:
  - L'hydrogène n'est plus dégagé dans une cabine.
  - Coupleur, couplage et chargeur conservés.
points_faibles:
  - Emplacement à trouver (Q46) ; le coffre de cockpit tribord est déjà occupé par la batterie moteur et le chargeur.
  - Câbles plus longs, donc plus de chute de tension, notamment pour le guindeau, alimenté par cette batterie.
  - Capacité utile inchangée, environ 55 Ah.
decision: "02/10/2026 : écartée, Julie retient la batterie LiFePO4 (H1)."
---

# E-H3 · Plomb déplacé hors des cabines

Hypothèse de l'étude E, à étudier selon la réponse à Q46. Base : **A-H4**.

Nomenclature : [nomenclature.yaml](nomenclature.yaml), environ **190 €**, pour une distance supposée de 4 m entre le nouvel emplacement et les coupe-circuits.

## Principe

Déplacer la batterie dans un coffre qui communique avec l'extérieur, comme le coffre de cockpit, où l'hydrogène s'évacue sans traverser une cabine. Elle reste au plomb : coupleur, couplage et chargeur sont conservés.

Les câbles de la batterie de servitude jusqu'à la platine des coupe-circuits (wire161, wire006 et wire009) sont remplacés par des câbles plus longs. Leur section se calcule avec la distance réelle et le courant du guindeau (environ 60 A), qui passe par cette batterie : à 4 m aller, 35 mm² donnent environ 0,24 V de chute pour 60 A, soit 2 %, ce qui reste acceptable ; au-delà, passer en 50 mm².

## À étudier

- **Emplacement** (Q46) : place disponible, ventilation du coffre vers l'extérieur, fixation d'une batterie de 25 à 30 kg, distance aux coupe-circuits.
- **Câblage** : nouveaux fils (wire006 et wire009 remplacés), fusible de 400 A de A-H2 à reporter près de la batterie.
- **Étude D** : le shunt reste sur le négatif de la batterie de servitude ; son emplacement b (près des coupe-circuits) reste valable.
