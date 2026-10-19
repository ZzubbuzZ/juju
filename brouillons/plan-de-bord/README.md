# Plan de bord : brouillon

Nouveau folio vu de dessus recensant les objets importants du bord (fusées de détresse, gilets de sauvetage…), plus détaillé que les plans d'implantation électriques (folios 0 et 5).

Phases :

1. Fond de plan vide, redessiné d'après `plan-emmenagements-constructeur.jpg` : fait le 16/10 (`folio-6-plan-de-bord.svg`, aperçu `apercu.png`), puis corrigé d'après les remarques de l'utilisateur. Écarts voulus avec le plan constructeur : lavabo de la cabine de poupe déposé (son emplacement est marqué en pointillés sur le meuble bas, conservé avec le placard), couchette de la cabine de poupe montrée par un arrachement du cockpit à main levée (côté bâbord, jusqu'à l'axe), bord bâbord en arc jusqu'au placard avec vaigrage côté coque, pièce amovible d'accès à la batterie dans son coin avant tribord, penderie tribord de la cabine de proue supprimée (la couchette va jusqu'au carré), table du carré représentée repliée, quille et liston non dessinés. Portes avec leur ouverture : cabine de poupe, cabinet de toilette, cabine de proue. Textures (reprises de `plan_voilier_v2.svg`) : planchers en lames sur deux niveaux (carré et cuisine ; cabine de poupe, table à carte et cabinet de toilette), arrêtés au milieu des assises ; matelassage capitonné des assises et de la couchette de proue ; vaigrages brun clair, du bord au dossier, dans le carré et la cabine de proue ; teck des bancs du cockpit.
2. Données des objets : premier essai le 19/10 dans `objets.yaml`, d'après la feuille Google « Emplacement trucs bateau » (lue sans la modifier). Chaque objet a un numéro, une catégorie (couleur de la pastille), son emplacement en clair et ses positions sur le plan, toutes estimées. À reporter dans le relevé quand les emplacements seront confirmés.
3. Légendes : premier essai, pastilles numérotées sur le plan (cerclées de tirets quand la feuille dit « à confirmer ») et liste par bord dans les cadres du haut et du bas, avec la clé des couleurs.

Questions ouvertes (phase 2) :

- **PB1** Vanne de coupure de gaz, « placard sous évier à gauche cabinet de toilette » : sous le lavabo du cabinet de toilette (placée là) ou sous l'évier de la cuisine ?
- **PB2** Coupe-câble, « coffre avant tribord "outillage" » : coffre sous la couchette de proue côté tribord (placé là), ou coffre de pont ?
- **PB3** Réservoir de gazole, « derrière la cabine bâbord » : au fond de la couchette de poupe, sous le cockpit (placé là) ?
- **PB4** « Coupe-circuits (étouffoir) » : la tirette d'arrêt du moteur, ou les coupe-circuits électriques de la descente ? Le tableau de commande est-il sous la marche du haut (placé là) ou du bas ?
- **PB5** Pompe de cale manuelle, « cockpit bâbord » : sur l'hiloire, le banc ou le plancher ? Que veut dire « équipier de descente » ?
- **PB6** Coffre arrière bâbord (gilets, fusibles de rechange) : il n'est pas dessiné. Sous l'arrière du banc bâbord ? Dimensions ?
- Seconde couverture anti-feu « au cockpit, à définir » : non placée. Ligne « rajouter partie électrique importante » : quels éléments (coupe-circuits, tableau de servitude, disjoncteurs…) ?

`python brouillons/plan-de-bord/plan_bord.py` régénère le SVG ; il reprend le bloc `<style>` du folio 0 et y ajoute les classes `amg`, `amg-f`, `amg-b`, `amg-d`, `amg-l`, `arr`, `halo`, `sol-b`, `sol-h`, `mat`, `teck`, `teck-j`, `vaig`, `vaig-f`, `obj`, `conf` et les classes de catégorie, les variables de couleur des textures et leurs motifs (`<defs>`), à reporter dans tous les folios et dans `page.py` à l'intégration.

Hors de `Electricité/` tant que l'emplacement définitif n'est pas décidé (proposé : `Electricité/livret/`, ou un dossier propre à l'armement) ; le vérificateur ne le contrôle donc pas encore.
