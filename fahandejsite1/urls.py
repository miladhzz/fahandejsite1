"""fahandejsite1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from website import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = i18n_patterns(
    path('loginmodir/', admin.site.urls),
    path('', views.index, name='index'),
    path('fa/', views.index, name='index_fa'),
    path('c/', views.index, name='set_language'),
    path('product/<str:slug>/', views.product_detail, name='product_detail'),
    path('article/<str:slug>/', views.article_detail, name='article_detail'),
    path('about/', views.about_us, name='about_us'),
    prefix_default_language=False
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

