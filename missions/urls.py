from django.urls import path

from .views import MissionCreateView, random_mission


namespace = "missions"

urlpatterns = [
    path("", MissionCreateView.as_view(), name="home"),
    path("random/", random_mission, name="random"),
]
