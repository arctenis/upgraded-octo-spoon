# Dev indés

Cette application Django contient un formulaire où les développeur indépendants
(freelance) peuvent anonymement partager leurs expériences, les données sur leur dernière
mission, leur tarif journalier moyen, la durée de la mission, l'intitulé du
poste (fullstack, backend, frontend, etc), le type d'entreprise (startup, PME,
grand groupe), le secteur d'activité (banque, assurance, e-commerce, etc), la
localisation (Paris, Lyon, Bordeaux, etc), le nombre de jours travaillés par
semaine, etc.

La page unique contient le formulaire, un formulaire de recherche parmi les
expériences enregistrées, et un affichage aléatoire d'une expérience
(l'utilisateur peut en voir d'autres en cliquant sur le bouton "Suivante").

Les données sont stockées dans une base de données SQLite.

Pas besoin de frameworks frontend. Peut-être HTMX et AlpineJS si besoin.

J'utilise PicoCSS pour la mise en forme.

1. [X] Initialiser un projet Django
2. [X] Créer l'application `missions`
4. [ ] Créer le formulaire
3. [ ] Créer la vue pour le formulaire
5. [ ] Créer la vue pour l'expérience affichée
6. [ ] Créer la vue pour la recherche
7. [ ] Coder le template de base
8. [ ] Coder le template pour le formulaire
9. [ ] Coder le template pour la recherche
10. [ ] Coder le template partiel pour l'affichage de l'expérience
11. [ ] Coder le template partiel pour les remerciements
12. [ ] Coder le modèle 'mission'
13. [ ] Ajouter la sauvegarde de données dans la vue du formulaire
14. [ ] Protéger le formulaire avec honeypot
15. [ ] Coder la recherche
