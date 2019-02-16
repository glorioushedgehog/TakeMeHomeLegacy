from django.urls import path

from . import views

urlpatterns = [
    path('search_by_demographics', views.search_by_demographics, name='search_by_demographics'),
    path('fr', views.facial_recognition, name='fr'),
    path('upload_image', views.upload_image, name='upload_image'),
    path('', views.index, name='index'),
]
