import time
from threading import Thread

from django.core.serializers import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from json import loads
from facial_recognition import get_embeddings_for_image_datas
from facial_recognition.search import init_inference_task
from facial_recognition.search import get_matching_persons
from tmh import demographic_search
from tmh.context_generators import context_from_person_list
from tmh.forms import ImageUploadForm
from .models import Person, InferenceTask
from .models import ImageData
from facial_recognition import search


def index(request):
    persons = Person.objects.all()
    images = ImageData.objects.all()
    context = {'persons': persons, 'images': images}
    return render(request, 'tmh/index.html', context)


def person_details(request, primary_key):
    a_person = Person.objects.get(pk=primary_key)
    image_data = None
    query_set = ImageData.objects.filter(primarykey=primary_key)
    if query_set.count() > 0:
        image_data = query_set[0]
    age = 'TODO'
    context = {'person': a_person, 'image_data': image_data, 'age': age}
    return render(request, 'tmh/person_details.html', context)


def search_by_demographics(request):
    if request.method == 'POST':
        data = loads(request.body)
        persons = demographic_search.get_matching_persons(data)
        context = context_from_person_list(persons)
        return render(request, 'tmh/search_result_cards.html', context)


def search_by_picture_old(request):
    keys = search.search(ImageData.objects.all(), request.body)
    persons = []
    for key in keys:
        persons.append(Person.objects.get(pk=key))
    context = context_from_person_list(persons)
    return render(request, 'tmh/search_result_cards.html', context)


def doit(n):
    for _ in range(n):
        print(3)
        time.sleep(1)


def search_by_picture_not_as_old(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            thread = Thread(target=doit, args=(5,))
            thread.start()
            the_image = form.cleaned_data['image']
            keys = search.search_by_image(ImageData.objects.all(), the_image)
            #print("skipping actually look for image matches")
            persons = []
            for key in keys:
                persons.append(Person.objects.get(pk=key))
            context = context_from_person_list(persons)
            return render(request, 'tmh/search_results.html', context)
    #         m = ExampleModel.objects.get(pk=course_id)
    #         m.model_pic = form.cleaned_data['image']
    #         m.save()
    #         return HttpResponse('image upload success')
    # return HttpResponseForbidden('allowed only via POST')


def search_by_picture(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            the_image = form.cleaned_data['image']
            inference_task_id = init_inference_task(the_image)
            context = {'inference_task_id': inference_task_id}
            return render(request, 'tmh/search_results.html', context)


def inference_complete(request, inference_task_id):
    task = InferenceTask.objects.get(id=inference_task_id)
    json_response = {
        'done': task.state == task.DONE,
        'error': task.state == task.ERROR,
    }
    return JsonResponse(json_response)


def inference_progress(request, inference_task_id):
    task = InferenceTask.objects.get(id=inference_task_id)
    context = {'task': task}
    return render(request, 'tmh/inference_progress.html', context)


def search_results(request, inference_task_id):
    image_datas = ImageData.objects.all()
    task = InferenceTask.objects.get(id=inference_task_id)
    if task.embedding is None:
        return HttpResponseNotFound()
    keys = get_matching_persons(task.embedding, image_datas)
    # we are now done with the inference task, so delete it
    task.delete()
    persons = []
    for key in keys:
        persons.append(Person.objects.get(pk=key))
    context = context_from_person_list(persons)
    return render(request, 'tmh/search_result_cards.html', context)


def generate_embeddings(request):
    get_embeddings_for_image_datas.generate_embeddings()
