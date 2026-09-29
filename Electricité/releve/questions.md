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
- **Q12** Longueurs réelles des fils du tableau de servitude, circuit par circuit.
  → 27/09 : pas d'information pour l'instant. À mesurer lors d'un démontage du tableau.
- **Q35** Passages de cloison : combien y en a-t-il, avec quel diamètre de trou, et combien de câbles passent dans chacun ? Au minimum : batterie de servitude → compartiment moteur, compartiment moteur → descente, et les passages vers l'avant (guindeau, tableau).

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

### Pour les études B (chauffe-eau) et C (solaire)

- **Q19** Place disponible pour un ballon de 10 à 15 L : volume, distance au moteur et au circuit d'eau douce.
  → 28/09 : pas encore de réponse.

### Réseau 230 V

- **Q31** Détails du réseau 230 V :
  - Les disjoncteurs 10 A et 16 A coupent-ils la phase et le neutre (bipolaires, ou « phase + neutre ») ? À quai en France, la phase et le neutre peuvent être inversés.
  - Le plafonnier 230 V est-il métallique (classe I, terre obligatoire) ou en plastique à double isolation (classe II, marqué d'un double carré) ?
  - Boîte de dérivation bâbord : « + 1 PE » désigne-t-il la prise de la table à carte, montée sur la boîte ou juste à côté ?
  → 28/09 : terre 230 V et masse 12 V séparées, pas d'isolateur galvanique (anomalie A8). Boîtier tribord sur la cloison entre le cabinet de toilette et le coffre de cockpit. Raccordement des prises (étoile ou chaîne) : non relevé, jugé secondaire.
  → 29/09 : correction, il n'y a pas de disjoncteur à bâbord. Le « boîtier bâbord » est une simple boîte de dérivation, à l'arrière gauche de la table à carte (+ 1 PE). Seul le boîtier tribord porte deux disjoncteurs (10 A éclairage, 16 A prises).
- **Q36** Différentiel 30 mA du boîtier d'arrivée : de quel type est-il (AC, A ou F, symbole imprimé sur l'appareil) ? Déclenche-t-il quand on appuie sur son bouton de test ? Un chargeur à découpage peut produire des fuites que le type AC détecte mal.
- **Q38** EPS 100 : son cordon 230 V n'a pas de terre (fiche à deux contacts). Son boîtier est-il en plastique, et porte-t-il le double carré de la classe II ? Un boîtier métallique sans terre serait une anomalie.

## Réponses

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
