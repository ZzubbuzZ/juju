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
- **Q3** Tableau Scheiber 2 voies : d'où viennent son alimentation et sa masse ? Quelles sections ?
- **Q12** Longueurs réelles des fils du tableau de servitude, circuit par circuit.
- **Q15** Calibre du disjoncteur thermique du guindeau.
- **Q16** Fils EPS 100 → groupe froid : section et longueur.

### Équipements

- **Q4** Pompe de cale : y a-t-il déjà un flotteur (pompe automatique) ?
- **Q5** Pompe de cale : marque et modèle, pour confirmer le fusible de 10 A.
- **Q6** EPS 100 : quelle section maximale acceptent les bornes ?
- **Q7** Feux de navigation, de mouillage et projecteur : LED ou incandescents ?
- **Q8** Autoradio : y a-t-il un fil de mémoire permanente ?
- **Q9** Éclairage intérieur : emplacement des 5 ou 6 lampes et trajet des câbles.
- **Q10** Pilote automatique : marque, modèle, barre franche ou roue ?
- **Q11** Radar : marque, modèle et point d'alimentation. Le sondeur est-il celui intégré au GPSMAP xsv ?

### Moteur

- **Q13** Le moteur est-il un 3GM30 (refroidi à l'eau de mer) ou un 3GM30F (circuit d'eau douce avec échangeur) ? Décisif pour le chauffe-eau (étude B).
- **Q14** Alternateur : ampérage, borne de sortie (B+), présence d'une borne W pour un compte-tours.

### Pour les études B (chauffe-eau) et C (solaire)

- **Q17** Port d'attache et zone de navigation habituelle (pour estimer l'ensoleillement).
- **Q18** Bimini, capote, portique : lesquels existent ? Quelles surfaces libres sur le pont et le rouf, et quelles zones sont ombragées par la bôme ?
- **Q19** Place disponible pour un ballon de 10 à 15 L : volume, distance au moteur et au circuit d'eau douce.
- **Q20** Prise de quai : calibre du disjoncteur de quai (10 ou 16 A) et puissance habituellement disponible au port.

### Implantation

- **Q21** Disjoncteur du guindeau : cabine de proue ou cabine de poupe ? Il est décrit « sous l'ouverture d'accès aux coupe-circuits », ouverture qui donne sur la cabine de poupe, et wire017 ne mesure que 0,5 m depuis les coupe-circuits.
- **Q22** De quel bord sont la cuisine et la table à carte ?
- **Q23** Chargeur de quai : d'où vient son 230 V (quel boîtier, quel disjoncteur, quelle section) ?
- **Q24** Plan d'aménagement du Gib'Sea 31 (brochure, notice, photo du plan) à déposer dans `releve/photos/`, pour le plan d'implantation.

## Réponses

_Aucune pour l'instant._
