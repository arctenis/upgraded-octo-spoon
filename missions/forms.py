from django import forms

from .models import Mission


class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = [
            "title",
            "client_type",
            "duration",
            "description",
            "daily_rate",
            "contact",
        ]
