"""Api_cour URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from .import views


from rest_framework.routers import DefaultRouter
from .apiviews import MoisViewSet, ModuleViewSet, ChapitreViewSet, CoursViewSet, User_coursViewSet
router = DefaultRouter()
router.register('mois', MoisViewSet, base_name='categorie')
router.register('module', ModuleViewSet, base_name='house')
router.register('chapitre', ChapitreViewSet, base_name='article')
router.register('cours', CoursViewSet, base_name='location')
router.register('couruser', User_coursViewSet, base_name='info')


urlpatterns = [
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += router.urls