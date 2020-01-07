# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import activate


def index(request):
    sliders = models.Slider.objects.all()[:3]
    # gallery_footer
    try:
        gallery_footer = models.Gallery.objects.get(category__name='Gallery Footer').pictures.all()
    except ObjectDoesNotExist:
        gallery_footer = None
    
    # product 3 top 
    product_3_top = models.Product.objects.filter(category__name='3 Top Product')[:3]

    # Offer Box 2
    article_offer_2 = models.Article.objects.filter(category__name='Offer Box 2', draft=False)[:2]

    # product middle
    product_middle = models.Product.objects.order_by('?').filter(category__name='product middle')

    # Article 3 Bottom
    article_3_bottom = models.Article.objects.filter(category__name='3 Bottom Article')[:3]

    # print(article_3_bottom)
    # activate('fa')
    return render(request, "index.html", {'sliders': sliders,
                                          'gallery_footer': gallery_footer,
                                          'product_3_top': product_3_top,
                                          'article_offer_2': article_offer_2,
                                          'product_middle': product_middle,
                                          'article_3_bottom': article_3_bottom})


def product_detail(request, slug):
    product = get_object_or_404(models.Product, slug=slug)
    return render(request, "product_detail.html", {'product': product})



def article_detail(request, slug):
    article = get_object_or_404(models.Article, slug=slug)
    return render(request, "article_detail.html", {'article': article})