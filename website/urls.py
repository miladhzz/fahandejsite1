from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.index, name='index'),
    path('product/<str:slug>/', views.product_detail, name='product_detail'),
    path('product/', views.product_list, name='product_list'),
    path('article/<str:slug>/', views.article_detail, name='article_detail'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
]
