from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('search_by_demographics', views.search_by_demographics, name='search_by_demographics'),
    path('search_by_picture', views.search_by_picture, name='search_by_picture'),
    path('<str:primary_key>/person_details', views.person_details, name='person_details'),
    path('<int:inference_task_id>/inference_complete', views.inference_complete, name='inference_complete'),
    path('<int:inference_task_id>/inference_progress', views.inference_progress, name='inference_progress'),
    path('<int:inference_task_id>/search_results', views.search_results, name='search_results'),

    path('facial_recognition_coverage', views.facial_recognition_coverage, name='facial_recognition_coverage'),
    path('generate_embeddings', views.generate_embeddings, name='generate_embeddings'),
    path('dropdown_options', views.dropdown_options, name='dropdown_options'),

    path('', views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
