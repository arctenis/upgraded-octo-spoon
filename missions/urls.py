from django.urls import path

from .views import MissionCreateView


namespace = "missions"

urlpatterns = [
    path("", MissionCreateView.as_view(), name="home"),
]
