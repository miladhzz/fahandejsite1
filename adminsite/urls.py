from django.urls import path
from . import views


app_name = 'adminsite'
urlpatterns = [
    path('', views.update_settings, name='admin'),
    path('logout/', views.logout_user, name="logout"),
]
