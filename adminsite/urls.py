from django.urls import path
from . import views


app_name = 'adminsite'
urlpatterns = [
    path('', views.admin_index, name='admin'),
    path('update-settings/', views.update_settings, name='update_settings'),
    path('logout/', views.logout_user, name="logout"),
    path('list-article/', views.list_article, name="list_article"),
    path('add-article/', views.add_article, name="add_article"),
    path('edit-article/<int:pk>/', views.edit_article, name="edit_article"),
    path('list-product/', views.list_product, name="list_product"),
    path('add-product/', views.add_product, name="add_product"),
    path('edit-product/<int:pk>/', views.edit_product, name="edit_product"),
    path('add-picture/', views.add_picture, name="add_picture"),
    path('list-picture/', views.list_picture, name="list_picture"),
]
