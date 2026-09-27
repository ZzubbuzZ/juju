# Anomalies constatées

Défauts de l'installation existante, par ordre de gravité. Ils sont repérés par des pastilles orange sur le folio 1. L'étude A (sécurisation) doit traiter toutes les anomalies en cours. Une anomalie qui s'avère infondée passe dans « Levées », avec la raison, et garde son numéro.

Format d'une ligne (lu par `outils/verifier.py`) : `- **An** texte`.

- **A1** wire019 : 6 mm² sur 3 m sans aucune protection, depuis l'entrée du disjoncteur du guindeau jusqu'au tableau de la table à carte. En cas de court-circuit, rien ne coupe avant la batterie.
- **A2** Aucun fusible en sortie des batteries moteur et servitude.
- **A3** Cosses non serties sur les câbles de la batterie moteur, qui sont abîmés par le connecteur actuel.
- **A4** Fils du coupleur et du chargeur (wire002, wire003, wire007, wire008, 6 mm²) branchés en direct sur les batteries, sans fusible.
- **A6** wire022 : l'alimentation du tableau Scheiber (6 mm²) est prise sur node010, côté charges du coupe-circuit de servitude, sans fusible. Même risque que A1.
- **A7** wire027 et wire028 : le câble étamé qui relie l'EPS 100 au groupe froid est vissé directement dans les bornes, prévues pour des cosses à fourche SV 2-4. Contact médiocre : échauffement et chute de tension au démarrage du compresseur, qui se coupe en sous-tension.
- **A8** Terre 230 V et masse 12 V ne sont reliées nulle part, et il n'y a pas d'isolateur galvanique. Les normes nautiques (ISO 13297, ABYC E-11) demandent une liaison en un point unique, pour qu'un défaut 230 V sur une partie métallique du circuit 12 V fasse déclencher le différentiel. Cette liaison se pose avec un isolateur galvanique (étude A, H4).

## Levées

- **A5** wire020 et wire021 : 10 mm² entre le relais et le moteur du guindeau.
  → 27/09 : levée. L'estimation de 80 A n'était étayée par aucune donnée. 700 W sous 12 V donnent environ 60 A, et la notice Lewmar (tableau 7.5) indique un courant normal de 50 A. Sur 0,5 m, 10 mm² à 60 A ne perdent qu'environ 0,1 V (0,9 %) ; les abaques admettent même 6 mm² jusqu'à environ 1,4 m pour 50 A. Même si 700 W était la puissance mécanique du moteur (environ 85 A absorbés), la chute resterait d'environ 1,2 %.
