# from django.http import HttpResponse
from django.shortcuts import render
from . import models
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    sliders = models.Slider.objects.all()[:3]
    # gallery_footer = None
    try:
        gallery_footer = models.Gallery.objects.get(category__name='Gallery Footer').pictures.all()
    except ObjectDoesNotExist:
        gallery_footer = None
    print(gallery_footer)
    return render(request, "index.html", {'sliders': sliders,
                                          'gallery_footer': gallery_footer})
