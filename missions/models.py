from django.db import models


class Mission(models.Model):
    title = models.CharField(max_length=100)
    client_type = models.CharField(
        max_length=1,
        choices=[
            ("1", "Petite Entreprise (1-10 employés)"),
            ("2", "Moyenne Entreprise (11-50 employés)"),
            ("3", "Grande Entreprise (50+ employés)"),
            ("4", "Startup"),
            ("5", "Particulier"),
            ("6", "Association"),
        ],
    )
    duration = models.IntegerField()  # in days
    description = models.TextField()
    daily_rate = models.IntegerField()  # in euros
    contact = models.CharField(
        max_length=1,
        choices=[
            ("1", "Réseau"),
            ("2", "Linkedin"),
            ("3", "Plateforme de Freelance (Malt, Comet, Creme de la Creme...)"),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
