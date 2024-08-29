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
3. [X] Créer le formulaire
4. [X] Créer la vue pour le formulaire
5. [X] Créer la vue pour l'expérience affichée
6. [X] Afficher la date de l'expérience de façon plus lisible
8. [X] Afficher le type d'entreprise, la valeur de la liste 'choices'
10. [X] Coder le template de base
11. [X] Coder le template pour le formulaire
13. [X] Coder le template partiel pour l'affichage de l'expérience
15. [X] Coder le modèle 'mission'
16. [X] Ajouter la sauvegarde de données dans la vue du formulaire
19. [X] Ajouter HTMX
21. [X] Modifier le design avec du pur CSS
14. [ ] Coder le template partiel pour les remerciements
9. [ ] Créer la vue pour la recherche
12. [ ] Coder le template pour la recherche
7. [ ] Ajouter la stack technique au modèle
17. [ ] Protéger la page admin avec honeypot
18. [ ] Coder la recherche
20. [ ] Coder le bouton "Une autre expérience"
22. [ ] Coder une page responsive
23. [ ] Améliorer le footer :
		1. [ ] Ajouter un lien vers mon Linkedin
24. [ ] Ajouter des tests
25. [ ] Déployer :
		1. [ ] Github Actions
		2. [ ] Render ou PythonAnywhere ou mon VPS
