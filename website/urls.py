from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fa/', views.index, name='index_fa'),
    path('c/', views.index, name='set_language'),
    path('product/<str:slug>/', views.product_detail, name='product_detail'),
    path('article/<str:slug>/', views.article_detail, name='article_detail'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
]
