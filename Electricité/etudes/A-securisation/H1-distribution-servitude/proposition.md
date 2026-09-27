# A-H1 · Distribution de servitude

Hypothèse de l'étude A (sécurisation). Base : le [relevé](../../../releve/etat-des-lieux.md).

- Données : [cablage.yaml](cablage.yaml), qui liste les ajouts et suppressions par rapport au relevé.
- Schémas : [folio 2a](folio-2a-distribution.svg) (distribution, tableau Scheiber) et [folio 2b](folio-2b-tableau-servitude.svg) (12 circuits de la table à carte).

Statut : **proposition**. Les longueurs sont estimées pour un Gib'Sea 31. Elles sont à mesurer à bord (Q12), puis il faut recalculer les sections avec la formule ci-dessous.

## 1. Ce que traite cette hypothèse

- **A1** (tableau de la table à carte alimenté sans protection) : **traitée**. Barrette + et fusible de 50 A à la source.
- **Pompe de cale** : sa masse est ramenée côté batteries et elle devient automatique. Une pompe branchée sur node006 est coupée quand on ferme le bateau.
- **Ne traite pas** A2 (fusibles de batterie), A3 (cosses), A4 (fusibles du coupleur et du chargeur) ni A5 (section du guindeau). Ces points relèvent d'autres hypothèses de l'étude A.

## 2. Hypothèses de calcul

Section minimale : `S (mm²) = 2 × L × I × 0,0175 / ΔU`

- L = longueur aller en m, I = courant en A, ΔU = chute de tension admise en V.
- ΔU = **3 % (0,36 V)** pour ce qui touche à la sécurité : feux de navigation, électronique, pilote, pompe de cale, frigo.
- ΔU = **10 % (1,2 V)** pour le confort : éclairage, projecteur, prises, pompe à eau.
- Section plancher : **1,5 mm²**, pour la tenue mécanique et pour rester compatible avec un fusible de 10 A.
- Pour limiter le nombre de rouleaux à acheter, seulement 5 sections : 1,5 / 2,5 / 4 / 6 / 10 mm². Câble marin étamé, cosses serties et gaine thermo à colle.
- Couleurs : + rouge, − noir, comme dans l'existant. Marquer chaque fil de son numéro (wireXXX) avec des manchons aux deux extrémités.

| Circuit | Consommation retenue | L aller est. | Remarque |
|---|---|---|---|
| Feu bicolore | 25 W → 2,1 A | 8 m | hypothèse incandescent ; en LED, les sections restent valables |
| Feu de poupe | 10 W → 0,8 A | 5 m | |
| Feu de tête de mât (moteur) | 25 W → 2,1 A | 3 m + 7 m dans le mât | |
| Feu de mouillage | 10 W → 0,8 A | 3 m + 12 m dans le mât | |
| Projecteur | 35 W → 2,9 A | 3 m + 6 m dans le mât | |
| Pompe à eau Seaflow | 15 A max | 3 m | |
| Autoradio | 5 A | 1,5 m | |
| Prises 12v (x2) | 10 A au total | 3 m + 1 m | |
| Éclairage (5-6 lampes) | 5 A (incandescent) | 8 m (départ vers l'avant) | |
| Compas | 0,1 A | 3 m | |
| Pilote | 5 A en pointe | 5 m | modèle à préciser |
| VHF GX2200 | 6 A en émission | 1 m | |
| GPS / instruments | 3 A | 1 m | GPS 7407 + répéteur + loch + anémomètre |
| Frigo CU-55 | 5 A au démarrage | 4 à 6 m depuis la batterie | le compresseur Danfoss se coupe en sous-tension |
| Pompe de cale | 6 A | 3 m | |

## 3. Distribution depuis la batterie de servitude

Aujourd'hui, tout part de node010 sans protection. Je propose une barrette + unique, placée juste après le coupe-circuit de servitude. Le disjoncteur du guindeau et deux fusibles (type MIDI ou ANL) sont vissés directement dessus, un par départ.

```
node009 ─(coupe-circuit servitude)─ node010 ──35mm²── node060 BARRETTE + SERVITUDE
                                                        ├─ disjoncteur guindeau (existant) ── node020
                                                        ├─ fusible 50A ── node062 ──10mm²──► tableau table à carte (node100)
                                                        └─ fusible 30A ── node064 ── 6mm²──► tableau Scheiber 2 voies (node050)
```

Chute de tension de l'alimentation du tableau (10 mm², 3 m) : environ 1,3 % à 15 A (usage courant) et 3,5 % à 40 A (pointe).

## 4. Tableau Scheiber 2 voies (contremarche)

Proposition de principe :

- **Frigo** : il reste derrière le coupe-circuit de servitude. Le fusible de 15 A est celui que préconise Danfoss pour ce compresseur : on le garde.
- **Pompe de cale** : elle devient une pompe **automatique permanente**. Le flotteur est alimenté en direct depuis la batterie, avant le coupe-circuit, par son propre fusible. L'interrupteur du tableau sert à la marche forcée (manuelle). La masse de la pompe revient **côté batteries** (node005) : la pompe fonctionne donc même quand tous les coupe-circuits sont ouverts.

```
                         BATTERIE SERVITUDE
                               │
                            node009 (avant coupe-circuit)
                               │
                          [F 10A]  ← porte-fusible à moins de 18 cm de la borne
                               │ node066
                               │ 2,5mm² rouge (wire107)
                               ▼
                        ┌─────────────┐
                        │  FLOTTEUR   │ node054 → node055
                        └──────┬──────┘
                               │ 2,5mm² (wire108)
                               ▼
  TABLEAU SCHEIBER 2 VOIES   ┌─────────────────┐
  node050 (+) ◄── 6mm² ──────┤ + POMPE DE CALE ├── node056
  (depuis F30A, node064)     └─────────────────┘      ▲
   │                                 │ node057        │
   ├─[15A]─[I FRIGO]── node052       │ 2,5mm² noir    │ 2,5mm² (wire109)
   │                     │           ▼ (wire110)      │
   │                  6mm²        node005             │
   │                     ▼        MASSE CÔTÉ          │
   │            EPS 100 (node042)  BATTERIES          │
   │                     │                            │
   │            EPS 100 → groupe froid (node044 → node040)
   │                                                  │
   └─[10A]─[I POMPE MANU]── node053 ──────────────────┘

  node051 (−) du tableau ── 6mm² noir ──► node006   (masse du frigo)
```

Le flotteur et l'interrupteur manuel sont branchés en parallèle sur le + de la pompe. Il n'y a pas besoin de diode.

## 5. Données

La netlist et la wirelist de cette hypothèse sont dans [cablage.yaml](cablage.yaml) : nœuds node050 à node066 et node120 à node153, fils wire100 à wire153. Trois fils du relevé sont supprimés et remplacés : wire016 par wire103, wire017 par wire100, wire019 par wire102.

Chute de tension calculée pour chaque fil (longueurs estimées) :

| Fil | Circuit | Section | ΔU |
|---|---|---|---|
| wire107 | pompe de cale auto | 2,5 mm² | 2,1 % |
| wire120 | feu bicolore | 2,5 mm² | 2,0 % |
| wire122 | feu de poupe | 1,5 mm² | 0,8 % |
| wire124 + wire130 | feu de tête de mât | 2,5 mm² | 2,5 % |
| wire126 + wire132 | feu de mouillage | 2,5 mm² | 1,5 % |
| wire128 + wire134 | projecteur | 2,5 mm² | 3,0 % |
| wire136 | pompe à eau | 2,5 mm² | 5,3 % à 15 A (environ 3 % en régime normal) |
| wire138 | autoradio | 1,5 mm² | 1,5 % |
| wire140 | prises 12 V | 2,5 mm² | 3,5 % |
| wire144 | éclairage (départ) | 2,5 mm² | 4,7 % en incandescent |
| wire148 | pilote | 4 mm² | 1,8 % |
| wire102 | alimentation du tableau | 10 mm² | 1,3 % à 15 A, 3,5 % à 40 A |

## 6. Questions liées

Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12 et Q16, dans [questions.md](../../../releve/questions.md).
