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
        ]
        labels = {
            "title": "Titre",
            "experience_level": "Niveau d'expérience en années",
            "client_type": "Type de client",
            "duration": "Durée en jours",
            "description": "Description",
            "daily_rate": "Taux journalier",
            "contact": "Contact",
        }
