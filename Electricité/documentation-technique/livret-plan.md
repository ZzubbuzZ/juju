# Livret électrique de Juju : plan (exécution différée)

Plan proposé le 13/10/2026, mis de côté à la demande de l'utilisateur : la conduite à tenir en cas de panne de la batterie moteur n'est pas arrêtée (booster, sélecteur du guindeau). Rédaction à reprendre une fois ce point tranché.

**But.** Un livret court, imprimable, rangé à la table à carte, pour **utiliser** l'installation au quotidien et **réagir** en cas de problème. Le manuel du bord ([README](README.md) de ce dossier) garde le montage, les réglages et l'entretien détaillé ; le livret y renvoie. Chaque consigne cite les repères posés à bord (numéros de fils, coupe-circuits, disjoncteurs).

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

**3. En cas de problème** (une fiche par situation : symptôme → vérifications → action)
1. **Odeur de brûlé, fumée** : ce qu'on coupe d'abord, dans l'ordre. Fiche prioritaire, en tête.
2. Plus rien sur la servitude : BMS coupé, MEGA fondu, coupe-circuit ; réarmement du BMS.
3. Le moteur ne démarre pas : recharge de secours par l'Orion XS, puis booster (procédure à arrêter, voir plus haut).
4. La LiFePO4 ne charge pas : au moteur (Orion XS), au quai (Blue Smart).
5. Le guindeau ne répond pas : disjoncteur 70 A, fusible 5 A de la télécommande (et sélecteur, s'il est retenu).
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

## Questions à trancher avant la rédaction

1. Format : A5 plastifié à la table à carte, ou A4 ; fiches réflexes recto seul ?
2. Lecteurs : le propriétaire seul, ou aussi un équipier qui ne connaît pas l'installation (niveau de détail) ?
3. Installation décrite : la cible (après travaux), en marquant ce qui n'est pas encore posé, ou l'existant au fur et à mesure ?
4. Emplacement : un dossier `livret/` à côté de `documentation-technique/`, imprimable en PDF comme la page de consultation ?

Première fiche à rédiger une fois le plan validé : « odeur de brûlé, fumée ».
