# from django.http import HttpResponse
from django.shortcuts import render
from . import models


def index(request):
    sliders = models.Slider.objects.all()[:3]
    print(sliders)
    return render(request, "index.html", {'sliders': sliders})
