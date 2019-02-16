from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('search_by_demographics', views.search_by_demographics, name='search_by_demographics'),
    path('fr', views.facial_recognition, name='fr'),
    path('', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
