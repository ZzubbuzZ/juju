# Questions à relever à bord

La liste à emporter lors de la prochaine visite.

**Pour répondre**, écrire la réponse juste sous la question, en retrait, précédée de `→` :

```
- **Q21** Disjoncteur du guindeau : cabine de proue ou cabine de poupe ? …
  → 12/10 : cabine de poupe, fixé sous l'ouverture. Calibre 80 A. Photo : disj-guindeau.jpg
```

Une réponse partielle ou un « je ne sais pas » est utile aussi. Les photos vont dans `photos/`. Ensuite, demander à Claude d'« intégrer les réponses » : les données, les schémas et cette liste sont mis à jour, et les questions traitées passent dans « Réponses ».

Format d'une question (lu par `outils/verifier.py`) : `- **Qn** texte`.

## Ouvertes

### Câblage existant

- **Q1** Tableau moteur (contact, jauges) : est-il branché sur le câble du démarreur (node031) ? Avec ou sans fusible ?
  → 29/09 : le faisceau d'origine Yanmar comporte un porte-fusible ; on ne sait pas encore si le motoriste de Juju l'a conservé.
  → 30/09 : sera vérifié, et traité si nécessaire, lors de la pose du compte-tours.
- **Q42** Boîtier de distribution 230 V du cabinet de toilette : quatre disjoncteurs Legrand DNX3, numérotés 1 à 4 : C10, C10, C16, C16 (photo Boitier-230v-cabinet-toilette.jpg). Quel circuit sur chacun ? Le relevé connaît l'éclairage (10 A), les prises tribord et les prises bâbord (16 A) : que protège le second 10 A, ou est-il libre ?
  → 01/10 : à vérifier lors d'une visite.
- **Q12** Longueurs réelles des fils du tableau de servitude, circuit par circuit.
  → 27/09 : pas d'information pour l'instant. À mesurer lors d'un démontage du tableau.

### Équipements

- **Q8** Autoradio : le fil de mémoire permanente est-il présent, et branché sur un + permanent ?
  → 27/09 : sans doute présent, branchement à vérifier.
- **Q9** Éclairage intérieur : emplacement des 6 points lumineux LED et trajet des câbles.
  → 27/09 : pas d'information.
- **Q11** Radar : marque, modèle et point d'alimentation. Le sondeur est-il celui intégré au GPSMAP xsv ?
  → 27/09 : pas d'information.

### Moteur

- **Q14** Alternateur : ampérage exact (plaque), borne de sortie (B+), présence d'une borne W pour un compte-tours.
  → 27/09 : à demander à Julie.
  → 28/09 : d'après les spécifications et les photos, l'alternateur d'origine donne 20 A au plus ; celui de Juju semble plus récent mais semblable. Plaque et bornes à relever.
- **Q40** Pièces immergées reliées au moteur, donc à la masse 12 V (vérifiable depuis le bord) : l'accouplement entre l'arbre de l'inverseur et l'arbre d'hélice est-il métallique, ou comporte-t-il un manchon isolant (flector) ? Un câble de mise à la masse arrive-t-il sur le tube d'étambot ? Conditionne la coupure du différentiel sans liaison terre / masse 12 V (A-H4).

### Pour les études B (chauffe-eau) et C (solaire)

- **Q19** Place disponible pour un ballon de 10 à 15 L : volume, distance au moteur et au circuit d'eau douce.
  → 28/09 : pas encore de réponse.
  → 07/10 : le ballon commandé (Carbest CozyWater 10C) mesure 270 × 400 × 290 mm (Ø × L × H) et pèse 6,9 kg à vide, environ 17 kg plein. Il se pose à plat, ou debout raccords vers le bas, dans un endroit sec et ventilé (il ne doit pas être recouvert ni isolé). Les fixations doivent tenir 60 kg. Il faut aussi de la place pour le réducteur de pression, le vase d'expansion et les deux vannes d'arrêt, la soupape doit rester accessible et son tuyau de vidange doit pouvoir sortir à l'extérieur ou dans un évier. Quels emplacements possibles, et à quelle distance du circuit d'eau, d'une prise 230 V et du tableau de servitude ?
- **Q54** Circuit d'eau douce existant : volume et position du réservoir ; type et diamètre du tuyau ; trajet de la pompe Seaflo jusqu'aux robinets (cuisine, cabinet de toilette) ; modèle des robinets (eau froide seule ou mitigeur) ; présence d'un vase ou d'un accumulateur. Avec un manomètre sur un robinet : pression à laquelle la pompe redémarre (la coupure est annoncée à 2,8 bar). Conditionne le réglage du réducteur et du vase (B-H1).
- **Q55** À la réception du ballon : filetage et diamètre de l'entrée d'eau froide, de la sortie d'eau chaude et de la soupape ; longueur du câble du panneau de commande, du câble 230 V et des fils 12 V. Où poser le panneau de commande ?
- **Q56** Prise 230 V qui alimentera le ballon : le câble du ballon se termine par une fiche Schuko. Les prises du bord ont-elles une terre à broche (norme française) ? La fiche Schuko y entre si la prise accepte les fiches hybrides. Laquelle utiliser, sur quel disjoncteur (voir Q42) ?

### Pour l'étude D (shunt)

- **Q44** Traceur Garmin GPSMAP 7407 : modèle exact (xsv ou xdv, étiquette au dos) et version du logiciel (Paramètres > Système > Informations système). Est-il raccordé à un réseau NMEA 2000 (câble à connecteur rond à 5 broches, connecteurs en T, bouchons de terminaison) ? Si oui, où passe le câble principal, et d'où vient son alimentation 12 V ? Où est placé le traceur, et d'où vient son alimentation ? Conditionne D-H6 (lecture du shunt sur le traceur).
  → 05/10 : à voir lors de la prochaine visite.

## Réponses

- **Q48** Tableau moteur : existe-t-il un + 12 V présent seulement quand la clé de contact est tournée (borne du contacteur à clé, voyant de charge, fil « D+ » de l'alternateur) ? Quel trajet jusqu'à la platine des coupe-circuits ? Un fil fin y commanderait le chargeur DC/DC (E-H1). Voir aussi Q1.
  → 03/10 : possible, mais ce + est pris sur la batterie moteur. Une commande à la table à carte demanderait de tirer un fil + moteur supplémentaire. Trajet du tableau moteur à la platine non relevé.
  → 05/10 : commande manuelle, par un interrupteur près du tableau Scheiber 2 voies (contremarche de la descente).
- **Q51** Batterie LiFePO4 commandée (Humsienk 12 V 200 Ah Plus) : 521 × 238 × 221 mm, 26,4 kg, bornes M8. Tient-elle dans le coffre de la cabine de poupe (longueur, largeur et hauteur intérieures, hauteur sous le couvercle avec les câbles et le fusible sur la borne) ? Le plancher du coffre supporte-t-il 26 kg sanglés ? Sinon, quel autre emplacement ? Q45 supposait une batterie de la taille du plomb actuel.
  → 05/10 : la place n'est pas un problème (même réponse que Q45).
- **Q52** Chargeur de quai commandé (Victron Blue Smart IP67 12/17) : version à une sortie « (1) » ou avec sortie de maintien « (1+Si) » ? Conditionne son câblage (E-H1).
  → 05/10 : référence BPC121713006, achetée 118 €.
- **Q53** Blue Smart IP67 12/17 placé près de la LiFePO4, dans la cabine de poupe : est-il livré avec une fiche 230 V ? Y a-t-il une prise 230 V proche (table à carte, armoire derrière la table à carte), ou faut-il tirer un câble 3 × 1,5 mm² d'environ 5 m depuis le disjoncteur de 10 A du chargeur (coffre de cockpit tribord) ? Par où passerait-il ?
  → 05/10 : un câble depuis le disjoncteur du chargeur de quai (C10) jusqu'à une prise dédiée, ou un boîtier de raccordement avec bornes Wago. Le chargeur et le shunt iront ensemble, dans la contremarche de la descente ou dans le coffre de la batterie : à décider sur place, selon la place dans la contremarche.
- **Q46** Coffre de la batterie de servitude : a-t-il une aération (trou, grille, tuyau) ? Pourrait-on faire sortir un évent vers l'extérieur (cockpit, tableau arrière) ou vers le compartiment moteur, et sur quelle longueur ? Existe-t-il un autre emplacement possible, ventilé et hors des cabines (coffre de cockpit tribord près de la batterie moteur, coffre bâbord), et à quelle distance de la platine des coupe-circuits ?
  → 05/10 : sans objet, la batterie au plomb est remplacée par une LiFePO4 (E-H1), qui ne dégage pas de gaz : plus besoin d'aération.
- **Q50** Longueur du trajet d'un câble 12 V entre le coffre de cockpit tribord (chargeur Dolphin) et le coffre de la batterie de servitude (cabine de poupe), par où il passerait, et cloisons à traverser. Sert à choisir la section de la sortie du second chargeur de quai (E-H1).
  → 05/10 : environ 5 m.
- **Q43** Place pour un Cerbo GX (boîtier d'environ 15 × 8 × 3 cm) près de la platine des coupe-circuits, derrière la descente ; et pour l'écran GX Touch 50 (environ 13 × 9 cm, en saillie ou encastré, profondeur environ 2 cm) à la table à carte : où, et faut-il découper le tableau ? Conditionne D-H5.
  → 05/10 : place incertaine, et la solution est trop chère de toute façon : D-H5 rejetée.
- **Q41** Indicateur de charge à aiguille du tableau de servitude, que l'afficheur du moniteur remplacerait (Q28) : comment est-il branché (fil +, masse, disjoncteur du tableau) ? Diamètre du trou de découpe (52 mm, le format courant des cadrans ?) et profondeur libre derrière le tableau. Conditionne la pose de l'afficheur (D-H2).
  → 03/10 : pas un problème, il y a la place pour l'afficheur. Branchement et diamètre exact non relevés : à voir à la pose.
- **Q45** Batterie de servitude : marque et référence exactes. Est-ce une batterie « ouverte » (bouchons sur le dessus, même scellés) ou une batterie étanche AGM ou gel (mention VRLA, AGM ou Gel sur l'étiquette) ? Dimensions de la batterie (longueur × largeur × hauteur) et dimensions intérieures du coffre.
  → 03/10 : il y a de la place dans le coffre, on adaptera au besoin. Marque, type et dimensions non relevés : sans objet si la batterie est remplacée (E-H1).
- **Q47** Hivernage : Juju reste-t-il à flot l'hiver, et le bateau est-il utilisé ou chargé au quai par temps de gel ? Une batterie LiFePO4 ne doit pas être chargée en dessous de 0 °C.
  → 03/10 : navigation en Méditerranée, batterie à l'intérieur du bateau : le gel n'est pas jugé un problème.
- **Q49** Coffre de cockpit tribord : reste-t-il la place, près du chargeur Dolphin, pour un second chargeur de quai d'environ 20 × 10 × 6 cm ? Sinon, y a-t-il une place sèche près de la batterie de servitude, et par où passerait un câble 230 V ? Distance entre le coffre de cockpit tribord et le coffre de la batterie de servitude.
  → 03/10 : à côté du chargeur Dolphin, dans le coffre de cockpit tribord. Distance jusqu'à la batterie de servitude : Q50.
- **Q31** Détails du réseau 230 V :
  - Le plafonnier 230 V est-il métallique (classe I, terre obligatoire) ou en plastique à double isolation (classe II, marqué d'un double carré) ?
  → 28/09 : terre 230 V et masse 12 V séparées, pas d'isolateur galvanique (anomalie A8). Boîtier tribord sur la cloison entre le cabinet de toilette et le coffre de cockpit. Raccordement des prises (étoile ou chaîne) : non relevé, jugé secondaire.
  → 29/09 : correction, il n'y a pas de disjoncteur à bâbord. Le « boîtier bâbord » est une simple boîte de dérivation, à l'arrière gauche de la table à carte (+ 1 PE). Seul le boîtier tribord porte deux disjoncteurs (10 A éclairage, 16 A prises).
  → 30/09 : chargeur sur un Merlin Gerin DT40 C10, éclairage et prises sur des Legrand DNX3 C10 et C16 : modèles phase + neutre, qui coupent les deux conducteurs. Le boîtier tribord porte un C10 (éclairage) et deux C16 (prises, un par bord). Cinq prises : table à carte et armoire derrière la table à carte (bâbord), groupe froid, cuisine et cabinet de toilette (tribord). Modèle du 16 A d'arrivée non relevé.
  → 30/09 : le plafonnier est métallique, et sa terre est raccordée (wire068).
  → 01/10 : correction, le boîtier tribord est dans le cabinet de toilette, et il porte quatre disjoncteurs : C10, C10, C16, C16 (photo Boitier-230v-cabinet-toilette.jpg ; affectation : Q42).
- **Q38** EPS 100 : son cordon 230 V n'a pas de terre (fiche à deux contacts). Son boîtier est-il en plastique, et porte-t-il le double carré de la classe II ? Un boîtier métallique sans terre serait une anomalie.
  → 30/09 : la fiche n'a pas de contact de terre : l'appareil est donc de classe II, conçu pour fonctionner sans terre.
- **Q39** Coffre de cockpit tribord, près de la prise de quai : reste-t-il la place de fixer un transformateur d'isolement (15 à 30 kg, le volume d'une boîte à chaussures), sur une cloison ou un fond solide, à l'abri des embruns ?
  → 30/09 : sans objet, le transformateur d'isolement est écarté (A-H4).
- **Q35** Passages de cloison : combien y en a-t-il, avec quel diamètre de trou, et combien de câbles passent dans chacun ? Au minimum : batterie de servitude → compartiment moteur, compartiment moteur → descente, et les passages vers l'avant (guindeau, tableau).
  → 30/09 : une dizaine de passages ; diamètres non relevés, la nomenclature de A-H5 prévoit un assortiment.
- **Q36** Différentiel 30 mA du boîtier d'arrivée : de quel type est-il (AC, A ou F, symbole imprimé sur l'appareil) ? Déclenche-t-il quand on appuie sur son bouton de test ? Un chargeur à découpage peut produire des fuites que le type AC détecte mal.
  → 30/09 : Power Safe ID55225, aucune documentation trouvée, type inconnu. Remplacement étudié dans A-H4.
- **Q3** Tableau Scheiber 2 voies : d'où viennent son alimentation et sa masse ?
  → 27/09 : des coupe-circuits situés juste à côté. Fils ajoutés au relevé (wire022, wire023) ; bornes exactes et sections reportées en Q25.
- **Q4** Pompe de cale : y a-t-il déjà un flotteur ?
  → 27/09 : non, la pompe est manuelle.
  → 29/09 : précision, la pompe est électrique ; c'est sa mise en route qui est manuelle (interrupteur du tableau Scheiber), faute de flotteur.
- **Q6** EPS 100 : quelle section maximale acceptent les bornes ?
  → 27/09 : bornes à vis d'environ 8 mm de large, prévues pour des cosses à fourche SV 2-4, soit AWG 16-14 (1,5 à 2,5 mm²).
- **Q15** Calibre du disjoncteur thermique du guindeau.
  → 27/09 : 50 A, d'après la documentation constructeur.
  → 28/09 : correction après lecture de la notice (tableau 7.5) : 50 A est le courant normal du Pro-Series 1000 ; le disjoncteur préconisé est de 70 A. Calibre installé à lire (Q34).
  → 29/09 : 70 A, lu sur l'appareil (Q34).
- **Q16** Fils EPS 100 → groupe froid : section et longueur.
  → 27/09 : 3,5 mm², longueur estimée à 3 m (wire027, wire028).
- **Q17** Port d'attache et zone de navigation habituelle.
  → 27/09 : étang de Berre (port de Saint-Chamas), navigation en Méditerranée.
- **Q18** Bimini, capote, portique : lesquels existent ?
  → 27/09 : une capote seulement.
- **Q20** Prise de quai : calibre du disjoncteur de quai.
  → 27/09 : à Saint-Chamas, 12 A à quai mais 6 A seulement au ponton. Juju aura une place au ponton : **6 A, soit environ 1 400 W au total**.
  → 01/10 : correction, les bornes de quai du port fournissent **16 A, soit environ 3 700 W** (l'information précédente venait de la presse). Ce calibre n'est pas garanti en escale, où il est souvent plus faible.
- **Q21** Disjoncteur du guindeau : cabine de proue ou cabine de poupe ?
  → 27/09 : cabine de poupe (erreur dans la première description).
- **Q22** De quel bord sont la cuisine et la table à carte ?
  → 27/09 : table à carte à bâbord, cuisine à tribord.
- **Q23** Chargeur de quai : d'où vient son 230 V ?
  → 27/09 : d'un boîtier de distribution voisin, alimenté par la prise de quai EU placée sous le banc tribord du cockpit. Le boîtier contient un différentiel 30 mA / 25 A et un disjoncteur 10 A pour le chargeur.
- **Q24** Plan d'aménagement du Gib'Sea 31.
  → 27/09 : `photos/gibsea-31-drawing.jpg` (plan de brochure, de faible résolution).
- **Q25** Tableau Scheiber 2 voies : raccordement, sections, masse de la pompe, raccordement de l'EPS 100.
  → 28/09 : + sur node010 et masse sur node006, en 6 mm² (wire022, wire023), sans fusible (A6). Départ pompe en 2,5 mm² (wire026). Masse de la pompe sur la barrette du tableau (wire036). Câble étamé vissé sans cosse sur l'EPS 100 (nouvelle anomalie A7) ; la différence entre 3,5 mm² et AWG 12 est sans conséquence. Section du départ frigo reportée en Q29.
- **Q26** Reste du réseau 230 V.
  → 28/09 : trois boîtiers. Boîtier d'arrivée (coffre de cockpit tribord) : différentiel 30 mA / 25 A, disjoncteurs 10 A (chargeur) et 16 A (reste du bord). Deux boîtiers de distribution, un par bord, avec 10 A pour l'éclairage et 16 A pour les prises. Tribord : prise du frigo (EPS 100), prise de la cuisine, plafonnier. Bâbord : prise de la table à carte, prise du carré. Prises en 3 × 2,5 mm², éclairage en 3 × 1,5 mm², arrivée et chargeur en 3 × 2,5 mm². Détails reportés en Q31. Schéma : folio 3.
  → 29/09 : correction (Q31), le boîtier bâbord est une simple boîte de dérivation, sans disjoncteur.
- **Q27** Place pour le shunt près de la batterie de servitude.
  → 28/09 : wire009 part du coffre de batterie, traverse la cloison vers le compartiment moteur, puis remonte derrière la descente jusqu'au coupe-circuit des négatifs. Le shunt peut donc se placer soit au départ, dans le coffre de batterie, soit à l'arrivée, derrière la descente, accessible par l'ouverture côté cabine de poupe (voir étude D). Longueur à vérifier : Q30.
- **Q28** Place pour un afficheur à la table à carte.
  → 28/09 : oui, en remplacement de l'ancien indicateur de charge à aiguille.
- **Q13** Refroidissement du moteur 3GMD.
  → 28/09 : refroidissement direct à l'eau de mer (spécifications constructeur et photos), sans trace de modification. L'échangeur pour le chauffe-eau (étude B, H2) est donc exclu.
- **Q33** Que désigne le « puits de dérive » ?
  → 28/09 : la quille est en deux parties : un aileron lesté en polyester et une dérive relevable en fonte, qui remonte dans un puits situé entre la table à carte et la cuisine (plus en arrière que sur la première version du folio 0).
- **Q2** Télécommande du guindeau : d'où vient son 12 V, et est-il protégé par un fusible ?
  → 29/09 : du + d'entrée du relais du guindeau (node022), à travers un fusible de 5 A (wire061 à wire064).
- **Q5** Pompe de cale : marque et modèle, pour confirmer le fusible de 10 A.
  → 27/09 : pas d'information.
  → 29/09 : Attwood Tsunami T500 (réf. 4606 / 4640). Fusible recommandé par le fabricant : 3 A. Le fusible de 10 A du tableau Scheiber protège bien le câble de 2,5 mm², mais pas le moteur de la pompe (nouvelle anomalie A10).
- **Q7** Feux de navigation, de mouillage et projecteur : LED ou incandescents ?
  → 29/09 : seul le feu de mouillage est à LED ; les feux de navigation et le projecteur sont à incandescence.
- **Q10** Pilote automatique de barre franche : modèle exact.
  → 27/09 : pilote de barre franche. À demander à Julie pour le reste.
  → 28/09 : la photo Vue-tableau-table-a-carte montre une notice « ST1000 Plus & ST2000 Plus » : Raymarine ST1000+ ou ST2000+, à confirmer.
  → 29/09 : Raymarine ST2000+.
- **Q29** Tableau Scheiber : section du départ frigo vers l'EPS 100 (wire024), et le retour de l'EPS 100 arrive-t-il bien sur la barrette de masse du tableau (wire025) ?
  → 29/09 : départ en 3,5 mm² ; le retour arrive bien sur la barrette de masse du tableau. Section du retour : Q37.
- **Q37** Retour de l'EPS 100 vers la barrette de masse du tableau Scheiber (wire025) : même câble de 3,5 mm² que le départ (wire024) ?
  → 29/09 : oui, 3,5 mm² aussi.
- **Q30** Longueur réelle de wire009 (− batterie de servitude → coupe-circuit des négatifs).
  → 29/09 : 1 m confirmé. La batterie est juste derrière la paroi latérale du bloc moteur, et la contremarche des coupe-circuits juste au-dessus.
- **Q32** Répétiteur GPS MLR FX312 : où est-il fixé ?
  → 29/09 : en deux parties : l'unité principale à la table à carte, et un écran déporté au-dessus de la descente, côté cockpit.
- **Q34** Calibre inscrit sur le disjoncteur du guindeau.
  → 29/09 : 70 A, conforme à la notice Lewmar.
