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
- **Q2** Télécommande du guindeau : d'où vient son 12 V, et est-il protégé par un fusible ?
- **Q12** Longueurs réelles des fils du tableau de servitude, circuit par circuit.
  → 27/09 : pas d'information pour l'instant. À mesurer lors d'un démontage du tableau.
- **Q25** Tableau Scheiber 2 voies :
  - Sur quelles bornes des coupe-circuits sont pris son + et sa masse ? Y a-t-il un fusible sur ce départ ?
  - Quelles sections pour son alimentation, pour le départ vers l'EPS 100 et pour le départ vers la pompe de cale ?
  - Où est reliée la masse de la pompe de cale ?
  - Comment le câble de 3,5 mm² est-il raccordé aux bornes de l'EPS 100, prévues pour des cosses SV 2-4 (2,5 mm² au plus) ? Est-ce du 3,5 mm² ou de l'AWG 12 (3,3 mm²) ?

### Équipements

- **Q5** Pompe de cale : marque et modèle, pour confirmer le fusible de 10 A.
  → 27/09 : pas d'information.
- **Q7** Feux de navigation, de mouillage et projecteur : LED ou incandescents ?
- **Q8** Autoradio : le fil de mémoire permanente est-il présent, et branché sur un + permanent ?
  → 27/09 : sans doute présent, branchement à vérifier.
- **Q9** Éclairage intérieur : emplacement des 5 ou 6 lampes et trajet des câbles.
  → 27/09 : pas d'information.
- **Q10** Pilote automatique de barre franche : marque et modèle.
  → 27/09 : pilote de barre franche. À demander à Julie pour le reste.
- **Q11** Radar : marque, modèle et point d'alimentation. Le sondeur est-il celui intégré au GPSMAP xsv ?
  → 27/09 : pas d'information.

### Moteur

- **Q13** La plaque signalétique indique 3GMD (et non 3GM30). Le moteur est-il refroidi à l'eau de mer (pompe à eau de mer seule) ou à l'eau douce (vase d'expansion avec bouchon de liquide de refroidissement, échangeur) ? Décisif pour le chauffe-eau (étude B).
- **Q14** Alternateur : ampérage, borne de sortie (B+), présence d'une borne W pour un compte-tours.
  → 27/09 : à demander à Julie.

### Pour les études B (chauffe-eau) et C (solaire)

- **Q19** Place disponible pour un ballon de 10 à 15 L : volume, distance au moteur et au circuit d'eau douce.

### Réseau 230 V

- **Q26** Reste du réseau 230 V :
  - Le boîtier du chargeur (différentiel 30 mA / 25 A, disjoncteur 10 A) est-il l'un des « 2 boîtiers, un par bord » de l'état des lieux ?
  - Comment l'autre boîtier est-il alimenté, et que protègent ses disjoncteurs (prises, EPS 100 du frigo, éclairage LED) ?
  - Sections et couleurs des fils, depuis la prise de quai jusqu'au chargeur.

## Réponses

- **Q3** Tableau Scheiber 2 voies : d'où viennent son alimentation et sa masse ?
  → 27/09 : des coupe-circuits situés juste à côté. Fils ajoutés au relevé (wire022, wire023) ; bornes exactes et sections reportées en Q25.
- **Q4** Pompe de cale : y a-t-il déjà un flotteur ?
  → 27/09 : non, la pompe est manuelle.
- **Q6** EPS 100 : quelle section maximale acceptent les bornes ?
  → 27/09 : bornes à vis d'environ 8 mm de large, prévues pour des cosses à fourche SV 2-4, soit AWG 16-14 (1,5 à 2,5 mm²).
- **Q15** Calibre du disjoncteur thermique du guindeau.
  → 27/09 : 50 A, d'après la documentation constructeur.
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
