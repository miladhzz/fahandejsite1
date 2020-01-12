from django.urls import path
from . import views


app_name = 'adminsite'
urlpatterns = [
    path('', views.update_settings, name='admin'),
    path('logout/', views.logout_user, name="logout"),
    path('add-article/', views.add_article, name="add_article"),
    path('add-product/', views.add_product, name="add_product"),
]
