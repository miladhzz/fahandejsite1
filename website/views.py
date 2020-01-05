# from django.http import HttpResponse
from django.shortcuts import render
from . import models
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    sliders = models.Slider.objects.all()[:3]
    # gallery_footer
    try:
        gallery_footer = models.Gallery.objects.get(category__name='Gallery Footer').pictures.all()
    except ObjectDoesNotExist:
        gallery_footer = None
    
    # product 3 top 
    product_3_top = models.Product.objects.filter(category__name='3 Top Product')[:3]

    # Banner 2 top


    print(product_3_top_3)
    return render(request, "index.html", {'sliders': sliders,
                                          'gallery_footer': gallery_footer,
                                          'product_3_top': product_3_top})
