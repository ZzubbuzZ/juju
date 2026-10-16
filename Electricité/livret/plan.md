# Livret électrique de Juju : plan

Plan proposé le 13/10/2026, rédaction commencée le 16/10. La conduite en cas de panne de la batterie moteur est arrêtée depuis le 13/10 : booster pour le démarrage, sélecteur 3 positions pour le guindeau (E-H1).

**But.** Un livret court, imprimable, rangé à la table à carte, pour **utiliser** l'installation au quotidien et **réagir** en cas de problème. Le manuel du bord ([documentation-technique](../documentation-technique/README.md)) garde le montage, les réglages et l'entretien détaillé ; le livret y renvoie. Chaque consigne cite les repères posés à bord (numéros de fils, coupe-circuits, disjoncteurs).

## Plan

**0. Mode d'emploi** (1 page) : comment lire le livret, pictogrammes, où trouver les schémas.

**1. Juju en une page**
- Schéma simplifié : quai → 230 V ; batterie moteur → démarreur, alternateur, guindeau ; LiFePO4 → servitude ; Orion XS entre les deux.
- Plan d'implantation réduit : batteries, platine, tableaux, boîtiers 230 V.
- Les organes de coupure : coupe-circuits, différentiel, disjoncteurs.

**2. Fonctionnement normal** (une liste de vérifications par situation)
1. Arrivée à bord : mise sous tension, ordre des coupe-circuits, lecture du shunt.
2. Au quai : branchement de la prise, différentiel, chargeurs (un C10 chacun), ballon sur le 230 V, frigo.
3. Départ au moteur : démarrage, Orion XS à allumer en partant et à couper au port, feux de navigation.
4. Au mouillage et à la voile : budget d'énergie, seuils de charge, ballon sur batterie (disjoncteur 12 V), guindeau moteur tournant.
5. Lire l'état des batteries : tensions et pourcentages de repère (plomb, LiFePO4), alarme de charge basse.
6. Quitter le bord, pour une courte ou une longue absence ; hivernage électrique.
7. Vérifier le fonctionnement des organes : tour complet, circuit par circuit, en notant le courant de chacun sur le shunt (ajouté le 16/10).

**3. En cas de problème** (une fiche par situation : symptôme → vérifications → action)
1. **Odeur de brûlé, fumée** : ce qu'on coupe d'abord, dans l'ordre. Fiche prioritaire, en tête.
2. Plus rien sur la servitude : BMS coupé, MEGA fondu, coupe-circuit ; réarmement du BMS.
3. Le moteur ne démarre pas : causes électriques traitées au verso de la fiche 2.3 (recharge de secours par l'Orion XS, booster) ; reste à couvrir les autres causes (gasoil, démarreur).
4. La LiFePO4 ne charge pas : au moteur (Orion XS), au quai (Blue Smart).
5. Le guindeau ne répond pas : disjoncteur 70 A, fusible 5 A de la télécommande, position du sélecteur (1 moteur, 2 servitude en secours ; ne pas basculer guindeau en marche).
6. Un circuit du tableau ne marche plus : fusibles, calibres, rechanges.
7. Pas de 230 V, ou le différentiel déclenche : borne du port, recherche du circuit en défaut.
8. Le frigo ne refroidit pas : EPS 100, tension.
9. Le ballon affiche E2 ou E4, ou la soupape goutte.
10. La pompe à eau tourne sans arrêt ; eau dans les fonds (pompe de cale manuelle).

**4. Fiches de référence**
- Tableau des protections : chaque fusible et disjoncteur, avec son calibre, son circuit et son emplacement.
- Pièces de rechange et outillage à bord, booster compris.
- Notices utiles, page par page.

**5. Entretien courant** : calendrier d'une page, renvoyant au manuel du bord.

## Décisions du 16/10

1. **Format** : A4. Une fiche réflexe tient sur un recto ; son verso porte les explications.
2. **Lecteurs** : le chef de bord, ou un équipier qui cherche une information sans connaître l'installation. Chaque consigne dit où se trouve l'organe à manœuvrer.
3. **Installation décrite** : la cible (après travaux). Tant que les travaux ne sont pas finis, le livret ne s'applique pas tel quel à bord.
4. **Emplacement** : ce dossier, `livret/`. Une fiche par fichier dans `fiches/`, numérotée comme le plan.

## Points à trancher

- **Booster sur une batterie moteur défectueuse** (16/10) : la procédure prévue le 13/10 (E-H1 : coupe-circuit moteur ouvert, pinces côté charges du coupe-circuit moteur et sur la masse moteur) laisse l'alternateur tourner sans batterie dès qu'on retire le booster, ce qui peut l'abîmer. À arrêter avant de l'écrire dans la fiche 2.3 : garder le booster branché le temps de la manœuvre, remplacer la batterie avant de repartir, ou autre.
- **Rechanges** : fusibles MEGA de 300 A et MIDI de la niche à prévoir dans la fiche 4.2.

## Avancement

| Fiche | État |
|---|---|
| [2.1 Mise sous tension, à l'arrivée à bord](fiches/2-1-mise-sous-tension.md) | Rédigée le 16/10 |
| [2.3 Démarrer le moteur, partir au moteur](fiches/2-3-demarrage-moteur.md) | Rédigée le 16/10, batterie moteur faible au verso ; procédure de démarrage intégrée le 17/10 (Q70) ; attend la fin de Q70 (vannes, voyants, arrêt), Q71 (booster) et le point à trancher sur le booster |
| [2.7 Vérifier le fonctionnement des organes](fiches/2-7-verification-organes.md) | Rédigée le 16/10 ; seuils du BMS : Q68 |
| [3.1 Odeur de brûlé, fumée](fiches/3-1-brule-fumee.md) | Rédigée le 16/10 ; attend Q66 (extincteurs) et Q67 (coupure du BMS par l'application) |
| [3.2 Plus rien sur la servitude](fiches/3-2-panne-servitude.md) | Rédigée le 16/10 ; attend Q72 (réarmement du BMS) et Q73 (matériel de secours) |
