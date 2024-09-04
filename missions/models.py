from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ["name"]


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Mission(models.Model):
    title = models.CharField(max_length=100)
    experience_level = models.IntegerField(
        error_messages={"invalid": "Doit être un nombre entier compris entre 1 et 40"}
    )
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
    duration = models.IntegerField(
        error_messages={"invalid": "Doit être un nombre entier compris entre 1 et 1000"}
    )
    description = models.TextField(
        error_messages={"invalid": "Doit faire moins de 1000 caractères"},
        max_length=1000,
    )
    daily_rate = models.IntegerField(
        error_messages={
            "invalid": "Doit être un nombre entier compris entre 100 et 2000"
        }
    )  # in euros
    contact = models.CharField(
        max_length=1,
        choices=[
            ("1", "Réseau"),
            ("2", "Linkedin"),
            ("3", "Plateforme de Freelance (Malt, Comet, Creme de la Creme...)"),
        ],
    )
    stack = models.ManyToManyField(
        Technology,
        blank=True,
        related_name="missions",
    )
    languages = models.ManyToManyField(
        Language,
        blank=True,
        related_name="missions",
    )
    personal_url = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
