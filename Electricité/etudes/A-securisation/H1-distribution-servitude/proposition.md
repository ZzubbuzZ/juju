# A-H1 · Distribution de servitude

Hypothèse de l'étude A (sécurisation). Base : le [relevé](../../../releve/etat-des-lieux.md).

- Données : [cablage.yaml](cablage.yaml), qui liste les ajouts et suppressions par rapport au relevé.
- Schémas : [folio 2a](folio-2a-distribution.svg) (distribution, tableau Scheiber) et [folio 2b](folio-2b-tableau-servitude.svg) (12 circuits de la table à carte).

**Décision du 30/09 : hypothèse différée**, sauf un **fusible de 50 A à la source de wire019** (node010, sortie du coupe-circuit de servitude), qui traite A1 seul, sans barrette. Ce fusible est décrit, câblé et chiffré dans [A-H2](../H2-fusibles-batteries/proposition.md) (wire166), avec les autres fusibles à la source. Le jour où H1 sera reprise, elle devra partir de A-H4 (qui cumule le programme retenu) et supprimer ce fusible au profit de la barrette. A6 (tableau Scheiber) et A10 (pompe de cale) restent en l'état pour l'instant ; le recâblage du tableau de la table à carte attendra. La suite du document décrit la solution complète, pour le jour où elle sera reprise.

Statut : **proposition**. Les longueurs sont estimées pour un Gib'Sea 31. Elles sont à mesurer à bord (Q12), puis il faut recalculer les sections avec la formule ci-dessous.

## 1. Ce que traite cette hypothèse

- **A1** (tableau de la table à carte alimenté sans protection) : **traitée**. Barrette + et fusible de 50 A à la source.
- **A6** (tableau Scheiber alimenté sans protection) : **traitée**. Fusible de 30 A sur la barrette ; le + du tableau (wire022) est repris sur ce fusible par wire104. La masse existante (wire023, déjà en 6 mm²) est conservée.
- **Pompe de cale** : sa mise en route est aujourd'hui manuelle, faute de flotteur (Q4). Elle devient automatique, et sa masse est ramenée côté batteries : une pompe branchée sur node006 serait coupée quand on ferme le bateau.
- **A10** (pompe de cale protégée en 10 A au lieu de 3 A) : **traitée**. Le fusible du flotteur est de 3 A, et celui de la voie pompe du tableau Scheiber passe de 10 A à 3 A.
- **Ne traite pas** A2 (fusibles de batterie), A3 (cosses) ni A4 (fusibles du coupleur et du chargeur). Ces points relèvent d'autres hypothèses de l'étude A.

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
| Feu bicolore | 25 W → 2,1 A | 8 m | incandescent (Q7) ; en LED, les sections restent valables |
| Feu de poupe | 10 W → 0,8 A | 5 m | |
| Feu de tête de mât (moteur) | 25 W → 2,1 A | 3 m + 7 m dans le mât | |
| Feu de mouillage | 2 W → 0,2 A | 3 m + 12 m dans le mât | LED (Q7) |
| Projecteur | 35 W → 2,9 A | 3 m + 6 m dans le mât | |
| Pompe à eau Seaflo SFDP1-045-040 | 15 A max | 3 m | la notice demande un fusible de 30 A, que 2,5 mm² ne supportent pas ; 15 A conservés (protection du câble), 20 A si le fusible fond au démarrage |
| Autoradio | 5 A | 1,5 m | |
| Prises 12v (x2) | 10 A au total | 3 m + 1 m | |
| Éclairage (5-6 lampes) | 5 A (incandescent) | 8 m (départ vers l'avant) | |
| Compas | 0,1 A | 3 m | |
| Pilote | 5 A en pointe | 5 m | Raymarine ST2000+ (Q10) |
| VHF GX2200 | 6 A en émission | 1 m | |
| GPS / instruments | 3 A | 1 m | GPS 7407 + répéteur + loch + anémomètre |
| Frigo CU-55 | 5 A au démarrage | 4 à 6 m depuis la batterie | le compresseur Danfoss se coupe en sous-tension |
| Pompe de cale | 3 A | 3 m | Attwood Tsunami T500, fusible de 3 A (Q5) |

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

Proposition de principe (schéma : [folio 2a](folio-2a-distribution.svg)) :

- **Alimentation du tableau** : le + part du fusible de 30 A de la barrette, en 6 mm² (wire104), au lieu de node010 (wire022). Si le câble existant est assez long, il suffit de déplacer sa cosse. La masse reste wire023.
- **Frigo** : liaison inchangée (wire024, wire025, puis wire027 et wire028 en 3,5 mm² vers le groupe froid). Le fusible de 15 A est celui que préconise Danfoss pour ce compresseur : on le garde. Les bornes de l'EPS 100 n'acceptent que des cosses SV 2-4 (2,5 mm² au plus). La liaison vers le groupe froid est aujourd'hui vissée sans cosse (A7, traitée par H3). Le départ du tableau vers l'EPS 100 et son retour (wire024, wire025) sont eux aussi en 3,5 mm² (Q29, Q37). Si la chute de tension s'avère trop forte, il faudra monter en section jusqu'à un bornier placé près de l'EPS, puis finir en 2,5 mm² sur quelques centimètres.
- **Pompe de cale** : elle devient une pompe **automatique permanente**. Le flotteur est alimenté en direct depuis la batterie, avant le coupe-circuit, par son propre fusible de 3 A (wire106 à wire108), calibre demandé par le fabricant de la pompe (Attwood Tsunami T500, Q5). L'interrupteur du tableau reste la marche forcée, par le fil existant wire026, déjà en 2,5 mm², conservé ; le fusible de 10 A de cette voie est remplacé par un 3 A (A10). La masse de la pompe revient **côté batteries** (node005, wire110) : la pompe fonctionne donc même quand tous les coupe-circuits sont ouverts. **Le fil actuel wire036, qui relie cette masse à la barrette du tableau, doit être déposé** : sinon la pompe relierait les deux côtés du coupe-circuit des négatifs, qui ne couperait plus rien.

Le flotteur et l'interrupteur manuel sont branchés en parallèle sur le + de la pompe. Il n'y a pas besoin de diode.

## 5. Données

La netlist et la wirelist de cette hypothèse sont dans [cablage.yaml](cablage.yaml) : nœuds node054, node055 et node060 à node066 et node120 à node153, fils wire100 à wire104, wire106 à wire108, wire110 et wire120 à wire153. Cinq fils du relevé sont supprimés et remplacés : wire016 par wire103, wire017 par wire100, wire019 par wire102, wire022 par wire104 et wire036 par wire110.

Chute de tension calculée pour chaque fil (longueurs estimées) :

| Fil | Circuit | Section | ΔU |
|---|---|---|---|
| wire107 | pompe de cale auto | 2,5 mm² | 1,1 % |
| wire104 | alimentation du tableau Scheiber | 6 mm² | 1,1 % à 11 A |
| wire120 | feu bicolore | 2,5 mm² | 2,0 % |
| wire122 | feu de poupe | 1,5 mm² | 0,8 % |
| wire124 + wire130 | feu de tête de mât | 2,5 mm² | 2,5 % |
| wire126 + wire132 | feu de mouillage | 2,5 mm² | 0,4 % (LED ; 2,5 mm² gardé, même câble que les autres feux du mât) |
| wire128 + wire134 | projecteur | 2,5 mm² | 3,0 % |
| wire136 | pompe à eau | 2,5 mm² | 5,3 % à 15 A (environ 3 % en régime normal) |
| wire138 | autoradio | 1,5 mm² | 1,5 % |
| wire140 | prises 12 V | 2,5 mm² | 3,5 % |
| wire144 | éclairage (départ) | 2,5 mm² | 4,7 % en incandescent |
| wire148 | pilote | 4 mm² | 1,8 % |
| wire102 | alimentation du tableau | 10 mm² | 1,3 % à 15 A, 3,5 % à 40 A |

## 6. Questions liées

Ouvertes : Q8, Q9, Q11 et Q12, dans [questions.md](../../../releve/questions.md). Déjà traitées et prises en compte : Q4 (pas de flotteur), Q5 (pompe Attwood Tsunami T500, fusible de 3 A), Q7 (seul le feu de mouillage est à LED), Q10 (pilote ST2000+), Q29 et Q37 (départ et retour du frigo en 3,5 mm²), Q6 (bornes de l'EPS 100), Q16 (liaison EPS 100 → groupe froid), Q25 (raccordement du tableau Scheiber et de la pompe).
