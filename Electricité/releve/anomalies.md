# Anomalies constatées

Défauts de l'installation existante, par ordre de gravité. Ils sont repérés par des pastilles orange sur le folio 1. L'étude A (sécurisation) doit tous les traiter.

Format d'une ligne (lu par `outils/verifier.py`) : `- **An** texte`.

- **A1** wire019 : 6 mm² sur 3 m sans aucune protection, depuis l'entrée du disjoncteur du guindeau jusqu'au tableau de la table à carte. En cas de court-circuit, rien ne coupe avant la batterie.
- **A2** Aucun fusible en sortie des batteries moteur et servitude.
- **A3** Cosses non serties sur les câbles de la batterie moteur, qui sont abîmés par le connecteur actuel.
- **A4** Fils du coupleur et du chargeur (wire002, wire003, wire007, wire008, 6 mm²) branchés en direct sur les batteries, sans fusible.
- **A5** wire020 et wire021 : 10 mm² entre le relais et le moteur du guindeau, pour environ 80 A. Vérifier la section préconisée par Lewmar.
- **A6** wire022 : l'alimentation du tableau Scheiber part des coupe-circuits, a priori sans fusible en amont. Même risque que A1 (point de raccordement et section à confirmer, Q25).
