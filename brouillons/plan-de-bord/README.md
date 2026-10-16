# Plan de bord : brouillon

Nouveau folio vu de dessus recensant les objets importants du bord (fusées de détresse, gilets de sauvetage…), plus détaillé que les plans d'implantation électriques (folios 0 et 5).

Phases :

1. Fond de plan vide, redessiné d'après `plan-emmenagements-constructeur.jpg` : fait le 16/10 (`folio-6-plan-de-bord.svg`, aperçu `apercu.png`), puis corrigé d'après les remarques de l'utilisateur. Écarts voulus avec le plan constructeur : lavabo de la cabine de poupe déposé (placard conservé), table du carré représentée repliée, quille et liston non dessinés. Portes avec leur ouverture : cabine de poupe, cabinet de toilette, cabine de proue. Textures (reprises de `plan_voilier_v2.svg`) : planchers en lames sur deux niveaux (carré et cuisine ; cabine de poupe, table à carte et cabinet de toilette), arrêtés au milieu des assises ; matelassage capitonné des assises et de la couchette de proue ; vaigrages en lattes brun clair, du bord au dossier, dans le carré et la cabine de proue ; teck des bancs du cockpit.
2. Données des objets dans le relevé : nom, description, couleur, zone, affichage sur ce plan.
3. Légendes dessinées sur le folio.

`python brouillons/plan-de-bord/plan_bord.py` régénère le SVG ; il reprend le bloc `<style>` du folio 0 et y ajoute les classes `amg`, `amg-f`, `amg-b`, `amg-l`, `halo`, `sol-b`, `sol-h`, `mat`, `teck`, `teck-j`, `vaig`, `vaig-l`, les variables de couleur des textures et leurs motifs (`<defs>`), à reporter dans tous les folios et dans `page.py` à l'intégration.

Hors de `Electricité/` tant que l'emplacement définitif n'est pas décidé (proposé : `Electricité/livret/`, ou un dossier propre à l'armement) ; le vérificateur ne le contrôle donc pas encore.
