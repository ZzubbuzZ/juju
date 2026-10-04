---
hypothese: D-H6
titre: SmartShunt et Cerbo-S GX, lecture sur le traceur Garmin
etat: proposee
resume: Le SmartShunt de D-H1, lu par une centrale Victron Cerbo-S GX sans écran, qui transmet les données de la batterie au traceur Garmin GPSMAP 7407 par un réseau NMEA 2000. Le traceur sert d'afficheur à la place du GX Touch 50 de D-H5.
points_forts:
  - Pas d'écran supplémentaire à placer à la table à carte ; la batterie s'affiche sur l'écran déjà utilisé en navigation.
  - Garde les atouts de D-H5 pour la suite (régulateur solaire de l'étude C, chargeur, LiFePO4), avec le portail VRM et l'écran du Cerbo affichable sur téléphone.
  - Un réseau NMEA 2000 servira aussi aux futurs instruments (sondeur, anémomètre, AIS).
points_faibles:
  - Environ 560 €, soit 3 fois le prix de H2 ; environ 440 € si le traceur est déjà sur un réseau NMEA 2000 (Q44).
  - Lecture seulement quand le traceur est allumé ; au mouillage, traceur éteint, il faut l'application.
  - Le traceur n'est pas compatible avec l'intégration complète de Victron (application OneHelm) ; il n'affiche que les données transmises en NMEA 2000, sans les menus ni les alarmes du Cerbo GX.
  - Consommation du Cerbo-S GX, environ 0,2 A, tant qu'il est allumé.
---

# D-H6 · SmartShunt et Cerbo-S GX, lecture sur le traceur Garmin

Hypothèse de l'étude D, ajoutée le 01/10 à la demande de l'utilisateur. Base : **D-H1** (même SmartShunt, même position, mêmes fils de mesure). Variante de **D-H5** : le traceur Garmin de Juju remplace l'écran GX Touch 50.

Nomenclature : [nomenclature.yaml](nomenclature.yaml), environ **560 €**. Le câblage (`cablage.yaml` et folio) sera écrit après la réponse à Q44 : il dépend de la présence d'un réseau NMEA 2000 et de l'emplacement du traceur, que le relevé ne connaît pas.

## Compatibilité du traceur

Le relevé note un **Garmin GPSMAP 7407 xsv ou xdv** (statut estimé, Q44). Les deux appartiennent à la série GPSMAP 7400/7600 ; la réponse ne change pas selon le modèle.

Victron propose deux façons d'afficher un GX sur un traceur Garmin :

| | Intégration | GPSMAP 7407 |
|---|---|---|
| Application OneHelm | Page Victron complète sur le traceur (état du bord, commandes), par câble Ethernet | **Non** : Victron et Garmin ne la proposent que sur les séries GPSMAP 8400/8600, 722/922/1222 Plus et leurs successeurs. La série 7400/7600 n'y figure pas. |
| NMEA 2000 | Le GX publie les mesures sur le réseau NMEA 2000 ; le traceur les affiche dans ses jauges et champs de données | **Oui** : le manuel de la série 7400/7600 liste en réception les PGN 127506 (état de charge, autonomie restante), 127507 (chargeur) et 127508 (tension, courant, température de la batterie). |

C'est donc la seconde voie que retient H6 : **le traceur ne remplace l'écran que pour la lecture**. Le réglage du shunt et du Cerbo GX se fait par l'application VictronConnect, ou par l'écran du Cerbo affiché à distance (« Remote Console ») sur un téléphone relié au Wi-Fi du Cerbo.

À vérifier sur le traceur une fois raccordé : les pages qui affichent ces données, la tension de la batterie moteur (le Cerbo la transmet-il comme une seconde batterie ?), et les alarmes possibles côté traceur.

## Principe

```
SmartShunt ── VE.Direct ──► Cerbo-S GX ── VE.Can / NMEA 2000 ──► réseau NMEA 2000 ──► traceur Garmin
```

- **Cerbo-S GX** plutôt que Cerbo GX : sans écran, les entrées que le Cerbo GX a en plus (réservoirs résistifs, températures, second bus CAN pour BMS) ne servent pas sur Juju. Il a trois ports VE.Direct et un bus VE.Can, ce qui suffit pour le shunt, le régulateur solaire et le chargeur. Environ 65 € de moins. Si une batterie LiFePO4 à BMS sur bus CAN est retenue plus tard, le Cerbo GX redevient le bon choix.
- **Réseau NMEA 2000** : un câble principal avec un bouchon à chaque bout, un connecteur en T par appareil (traceur, Cerbo, alimentation) et une alimentation 12 V protégée par un fusible. Le kit de démarrage Garmin en fournit l'essentiel ; il faut un troisième T.
- **Câble Victron VE.Can vers NMEA 2000** (micro-C mâle) entre le Cerbo et son T. La seconde prise VE.Can du Cerbo reçoit un bouchon VE.Can. Dans le Cerbo, activer la sortie NMEA 2000 (« NMEA 2000-out »).

Le Cerbo-S GX est alimenté comme le Cerbo GX de D-H5 : côté charges du coupe-circuit de servitude, par un fusible de 3 A à la source, et il s'éteint bateau coupé. Le SmartShunt continue de compter.

## Comparaison avec D-H5

| | D-H5 | D-H6 |
|---|---|---|
| Lecture | Écran GX Touch 50, toujours disponible | Traceur, quand il est allumé |
| Fonctions de l'écran | Complètes (menus, alarmes, historique) | Lecture des mesures seulement |
| Place à trouver (Q43) | Cerbo GX et écran de 13 × 9 cm | Cerbo-S GX seulement |
| Consommation | Environ 0,3 A (Cerbo GX et écran) | Environ 0,2 A (Cerbo-S GX seul), plus le traceur quand on le consulte |
| Coût | Environ 635 € | Environ 560 €, ou 440 € si le réseau NMEA 2000 existe |

La différence de prix est faible : le kit NMEA 2000 et le câble VE.Can coûtent à peu près le prix de l'écran. H6 l'emporte si le traceur est déjà sur un réseau NMEA 2000, ou si un tel réseau est prévu de toute façon pour d'autres instruments.

À noter : D-H5 peut aussi passer au Cerbo-S GX, ce qui la ramène à environ 570 €.

## Conséquences

- **Bilan énergétique** : la fiche Victron du Cerbo-S GX est à consulter pour sa consommation exacte ; l'ordre de grandeur retenu ici, 0,2 A, est une estimation. Au mouillage, Cerbo-S allumé 24 h : environ 5 Ah par jour (modification à faire sur `main` si H6 est retenue).
- **Réseau NMEA 2000** : son alimentation consomme peu, mais elle reste un départ de plus au tableau. Son emplacement dépend du trajet du câble principal entre le traceur et le Cerbo (Q44).
- **Le traceur et ses accessoires** (sondeur, éventuel réseau existant) ne sont pas modifiés.

## Sources

- Victron, intégration aux traceurs par application, modèles Garmin compatibles : https://www.victronenergy.com/media/pg/Cerbo_GX/en/marine-mfd-integration-by-app.html
- Garmin, manuel GPSMAP 7400/7600, liste des PGN NMEA 2000 : https://www8.garmin.com/manuals/webhelp/gpsmap7400-7600/EN-US/GUID-0C4B3FAB-3E41-438C-B31E-9B5489790913.html
- Garmin, appareils compatibles OneHelm (communiqué) : https://www.garmin.com/en-US/newsroom/?p=3880
