from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('search_by_demographics', views.search_by_demographics, name='search_by_demographics'),
    path('search_by_picture', views.search_by_picture, name='search_by_picture'),
    path('upload', views.upload, name='upload'),
    path('', views.index, name='index'),
    path('generate_embeddings', views.generate_embeddings, name='generate_embeddings'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
