# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
    product_3_top = models.Product.objects.filter(category__name='3 Top Product', draft=False)[:3]

    # Offer Box 2
    article_offer_2 = models.Article.objects.filter(category__name='Offer Box 2', draft=False)[:2]

    # product middle
    product_middle = models.Product.objects.order_by('?').filter(category__name='product middle', draft=False)

    # Article 3 Bottom
    article_3_bottom = models.Article.objects.filter(category__name='3 Bottom Article', draft=False)[:3]

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
    product_pictures = product.pictures.all()
    product_comments = models.CommentProduct.objects.filter(product=product, active=True)
    return render(request, "product_detail.html", {'product': product,
                                                   'product_pictures': product_pictures,
                                                   'product_comments': product_comments})


def article_detail(request, slug):
    article = get_object_or_404(models.Article, slug=slug)
    article_comments = models.CommentArticle.objects.filter(article=article, active=True)
    return render(request, "article_detail.html", {'article': article,
                                                   'article_comments': article_comments})


def about_us(request):
    return render(request, "about.html")


def contact_us(request):
    return render(request, "contact_us.html")

