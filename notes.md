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
7. [X] Afficher le type d'entreprise, la valeur de la liste 'choices'
8. [X] Coder le template de base
9. [X] Coder le template pour le formulaire
10. [X] Coder le template partiel pour l'affichage de l'expérience
11. [X] Coder le modèle 'mission'
12. [X] Ajouter la sauvegarde de données dans la vue du formulaire
13. [X] Ajouter HTMX
14. [X] Modifier le design avec du pur CSS
15. [X] Coder le bouton "Une autre expérience"
16. [X] Ajouter la stack technique au modèle
17. [X] Modifier les messages d'erreur du formulaire :
	1. [X] Traduire en français
	2. [X] Modifier le style
18. [X] Améliorer le footer :
		1. [X] Ajouter un lien vers mon Linkedin
19. [X] Protéger la page admin en changeant la route
20. [X] Déployer :
		1. [X] Render ou PythonAnywhere ou mon VPS
21. [ ] Gérer les fichiers statiques avec Whitenoise
22. [ ] Afficher un message de remerciements après l'envoi du formulaire (modal)
23. [ ] Coder le template partiel pour les remerciements
24. [ ] Coder la recherche :
	1. [ ] Créer la vue pour la recherche
25. [ ] Coder le template pour la recherche
26. [ ] Coder une page responsive
27. [ ] Ajouter des tests
