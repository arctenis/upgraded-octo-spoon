from django.views import View
from django.shortcuts import render, redirect

from .forms import MissionForm


class MissionCreateView(View):
    def get(self, request):
        mission_form = MissionForm()
        context = {"mission_form": mission_form}
        return render(request, "missions/mission_form.html", context)

    def post(self, request):
        mission_form = MissionForm(request.POST)
        if mission_form.is_valid():
            mission_form.save()
            return redirect("home")
        context = {"mission_form": mission_form}
        return render(request, "missions/mission_form.html", context)
