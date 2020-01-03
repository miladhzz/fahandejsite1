# from django.http import HttpResponse
from django.shortcuts import render
from . import models


def index(request):
    sliders = models.Slider.objects.all()[:3]
    gallery_footer = models.Gallery.objects.get(category__name='Gallery Footer').pictures
    print(gallery_footer)
    return render(request, "index.html", {'sliders': sliders,
                                          'gallery_footer': gallery_footer})
