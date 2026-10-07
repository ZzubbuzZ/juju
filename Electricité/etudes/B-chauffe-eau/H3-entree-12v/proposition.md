---
hypothese: B-H3
titre: Entrée 12 V du ballon (200 W), sur la LiFePO4 et le surplus solaire
etat: proposee
resume: L'entrée 12 V de 200 W du CozyWater 10C (B-H1) est raccordée à la batterie de servitude LiFePO4 (E-H1) par un relais de 30 A commandé par un interrupteur, avec un fusible de 30 A à la source et du câble de 6 mm², comme le demande la notice. Elle sert quand le surplus solaire (étude C) ou une batterie pleine le permettent.
points_forts:
  - Eau chaude hors du quai, sans autre appareil ni convertisseur ; la résistance est déjà dans le ballon.
  - Câblage court et simple (relais, fusible, interrupteur) ; le ballon passe seul sur le 230 V au quai.
  - Le relais pourra être commandé plus tard par la sortie de délestage d'un régulateur solaire (étude C).
points_faibles:
  - "Chauffe lente : environ 2 h 40 pour 10 L de 15 à 60 °C."
  - "Environ 45 Ah par chauffe : au mouillage, la consommation passe d'environ 60 à environ 105 Ah par jour, et l'autonomie de la LiFePO4 d'environ trois jours à un jour et demi."
  - "Au moteur, l'alternateur de 20 A (Q14), bridé à 15 A par le DC/DC, ne couvre pas les 17 A du ballon."
  - Sans régulateur à sortie de délestage, la commande reste manuelle ; un oubli vide la batterie jusqu'à la coupure du BMS.
  - Point de raccordement et longueur à définir avec l'emplacement du ballon (Q19).
---

# B-H3 · Entrée 12 V du ballon, sur la LiFePO4 et le surplus solaire

Hypothèse de l'étude B. Base prévue : **E-H1** (LiFePO4 de 200 Ah, retenue), complément de **B-H1** (ballon CozyWater 10C). Le câblage (`cablage.yaml`, folio) sera écrit quand l'emplacement du ballon (Q19) et le point de raccordement seront connus.

Nomenclature : [nomenclature.yaml](nomenclature.yaml).

## Ce que demande la notice

Notice du CozyWater 10C, page 67, schéma « connexion 12 V CC » :

- un **interrupteur** commande un **relais de 30 A au moins** (contact à fermeture, bornes 30 et 87) dans le câble positif, « pour éviter que la batterie ne se décharge accidentellement » ;
- un **fusible de 30 A** sur le positif, le plus près possible de la source ;
- du câble de **6 mm² au moins** ;
- le négatif n'a pas besoin de fusible s'il revient directement à la masse de la batterie (cas A de la notice). Sur Juju, il reviendra à la barre de masse de la servitude, côté « bord » du shunt (étude D), pour que le shunt compte la consommation du ballon.

## Section du câble

Courant : 200 W / 12 V, soit environ **17 A**. Circuit de confort, donc ΔU = 10 % (1,2 V) :

S = 2 × L × 17 × 0,0175 / 1,2 ≈ 0,5 × L mm², soit 2,5 mm² jusqu'à 5 m de câble.

Mais le fusible de 30 A imposé par la notice doit protéger le câble : c'est lui qui fixe la section. Retenu : **6 mm²**, comme la notice. Une longueur de plus de 12 m demanderait davantage, ce qui est peu probable.

## Effet sur le bilan

Chauffer 10 L de 15 à 60 °C demande environ 0,52 kWh, soit environ **45 Ah** sur la LiFePO4 avec les pertes, en 2 h 40.

| Situation | Sans le ballon | Avec une chauffe par jour |
|---|---|---|
| Mouillage ([bilan](../../../commun/bilan-energetique.yaml)) | environ 60 Ah/jour | environ 105 Ah/jour |
| Autonomie de la LiFePO4 (160 à 180 Ah utiles) | environ 3 jours | environ 1,5 jour |

Au moteur, le DC/DC de l'étude E charge la LiFePO4 à 15 A environ (alternateur de 20 A, Q14) : le ballon consomme plus que la charge. L'entrée 12 V n'est donc rentable qu'avec un **surplus solaire** : environ 200 W de panneaux en plein soleil, en plus de la consommation du bord. C'est l'étude C qui dira si ce surplus existe.

En attendant, l'entrée 12 V reste utile pour une chauffe ponctuelle, batterie pleine, la veille d'un retour au port.

## Commande

1. **Maintenant** : interrupteur à voyant près du panneau de commande du ballon. Le voyant rappelle que le ballon tire sur la batterie.
2. **Avec l'étude C** : la bobine du relais est commandée par la sortie de délestage (« load ») du régulateur solaire, ou par un relais programmable (Cerbo GX, étude D), qui n'enclenche le ballon que batterie pleine et panneaux en production. L'interrupteur reste en série pour pouvoir tout couper.

La bobine d'un relais automobile consomme environ 0,15 A pendant la chauffe, ce qui est négligeable devant les 17 A du ballon.

## À décider

- Point de raccordement du + : départ de la distribution de servitude (étude A) ou directement à la batterie, selon l'emplacement du ballon (Q19).
- Commande définitive, avec l'étude C.
