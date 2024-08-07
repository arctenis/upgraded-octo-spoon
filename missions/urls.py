from django.urls import path

from .views import MissionCreateView

urlpatterns = [
    path("", MissionCreateView.as_view(), name="home"),
]
