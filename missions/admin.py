from django.contrib import admin

from .models import Mission


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "experience_level",
        "client_type",
        "duration",
        "daily_rate",
        "contact",
    ]
    list_filter = [
        "client_type",
        "daily_rate",
        "duration",
        "contact",
        "experience_level",
    ]
