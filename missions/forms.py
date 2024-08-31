from django import forms

from .models import Mission


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = [
            "title",
            "experience_level",  # in years
            "client_type",
            "duration",
            "description",
            "daily_rate",
            "contact",
            "stack_a",
            "stack_b",
            "stack_c",
            "language_a",
            "language_b",
            "personal_url",
        ]
        labels = {
            "title": "Titre",
            "experience_level": "Niveau d'expérience en années",
            "client_type": "Type de client",
            "duration": "Durée en jours",
            "description": "Description",
            "daily_rate": "Taux journalier",
            "contact": "Contact",
            "stack_a": "Techno",
            "stack_b": "Techno",
            "stack_c": "Techno",
            "language_a": "Langage",
            "language_b": "Langage",
            "personal_url": "URL personnelle (site perso, linkedin, github...)",
        }
