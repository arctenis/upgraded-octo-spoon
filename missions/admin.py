from django.contrib import admin

from .models import Mission, Technology, Language


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
    search_fields = ["client_type", "daily_rate", "contact", "experience_level"]


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
