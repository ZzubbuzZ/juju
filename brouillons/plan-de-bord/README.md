# Plan de bord : brouillon

Nouveau folio vu de dessus recensant les objets importants du bord (fusées de détresse, gilets de sauvetage…), plus détaillé que les plans d'implantation électriques (folios 0 et 5).

Phases :

1. Fond de plan vide, redessiné d'après `plan-emmenagements-constructeur.jpg` : fait le 16/10 (`folio-6-plan-de-bord.svg`, aperçu `apercu.png`).
2. Données des objets dans le relevé : nom, description, couleur, zone, affichage sur ce plan.
3. Légendes dessinées sur le folio.

`python brouillons/plan-de-bord/plan_bord.py` régénère le SVG ; il reprend le bloc `<style>` du folio 0 et y ajoute les classes `amg`, `amg-f`, `amg-l`, `deck` et `halo`, à reporter dans tous les folios et dans `page.py` à l'intégration.

Hors de `Electricité/` tant que l'emplacement définitif n'est pas décidé (proposé : `Electricité/livret/`, ou un dossier propre à l'armement) ; le vérificateur ne le contrôle donc pas encore.
