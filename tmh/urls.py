from django.urls import path

from . import views

urlpatterns = [
    path('fr', views.facial_recognition, name='fr'),
    path('', views.index, name='index'),
]
