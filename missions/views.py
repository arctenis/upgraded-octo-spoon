from django.views import View
from django.shortcuts import render, redirect

from .forms import MissionForm
from .models import Mission


def random_mission(request):
    random_mission = Mission.objects.order_by("?").first()
    context = {"random_mission": random_mission}
    return render(request, "missions/random_mission.html", context)


class MissionCreateView(View):
    def get(self, request):
        mission_form = MissionForm()
        random_mission = Mission.objects.order_by("?").first()
        context = {"mission_form": mission_form, "random_mission": random_mission}
        return render(request, "missions/mission_form.html", context)

    def post(self, request):
        mission_form = MissionForm(request.POST)
        if mission_form.is_valid():
            mission_form.save()
            return redirect("home")
        random_mission = Mission.objects.order_by("?").first()
        context = {"mission_form": mission_form, "random_mission": random_mission}
        return render(request, "missions/mission_form.html", context)
