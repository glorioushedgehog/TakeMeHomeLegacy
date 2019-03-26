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
from tmh.forms import ImageUploadForm, PersonForm
from .models import Person, InferenceTask, CfgLookup
from .models import ImageData
from facial_recognition import search


def index(request):
    persons = Person.objects.all()
    images = ImageData.objects.all()
    #context = {'persons': persons, 'images': images}
    #return render(request, 'tmh/index.html', context)

    form = PersonForm()
    context = {'persons': persons, 'images': images, 'form': form}
    return render(request, 'tmh/index.html', {'form': form})


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
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            persons = demographic_search.get_matching_persons(form.cleaned_data)
            context = context_from_person_list(persons)
            return render(request, 'tmh/search_results.html', context)
        else:
            return render(request, 'tmh/search_results.html', {})
    return index(request)


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


def dropdown_options(request):
    eyes_choices = []
    hair_choices = []
    organization_choices = []
    race_choices = []
    record_type_choices = []
    emergency_contact_relationship_choices = []
    sex_choices = []
    home_state_choices = []

    def hi():
        print("af")

    default_choices = []
    config_options = CfgLookup.objects.all()
    for an_option in config_options:
        a_tuple = (an_option.choice.strip(), an_option.description.strip())
        if an_option.typeid == 1:
            eyes_choices.append(a_tuple)
        if an_option.typeid == 2:
            hair_choices.append(a_tuple)
        if an_option.typeid == 3:
            organization_choices.append(a_tuple)
        if an_option.typeid == 4:
            race_choices.append(a_tuple)
        if an_option.typeid == 5:
            record_type_choices.append(a_tuple)
        if an_option.typeid == 6:
            emergency_contact_relationship_choices.append(a_tuple)
        if an_option.typeid == 7:
            sex_choices.append(a_tuple)
        if an_option.typeid == 8:
            home_state_choices.append(a_tuple)
        if an_option.typeid == 9:
            default_choices.append(a_tuple)
    print("EYES_CHOICES = (")
    for a_choice in eyes_choices:
        print("\t" + str(a_choice) + ",")
    print(")")
    print("HAIR_CHOICES = (")
    for a_choice in hair_choices:
        print("\t" + str(a_choice) + ",")
    print(")")
    print("ORGANIZATION_CHOICES = (")
    for a_choice in organization_choices:
        print("\t" + str(a_choice) + ",")
    print(")")
    print("RACE_CHOICES = (")
    for a_choice in race_choices:
        print("\t" + str(a_choice) + ",")
    print(")")
    print("RECORD_TYPE_CHOICES = (")
    for a_choice in record_type_choices:
        print("\t" + str(a_choice) + ",")
    print(")")
    print("EMERGENCY_CONTACT_RELATIONSHIP_CHOICES = (")
    for a_choice in emergency_contact_relationship_choices:
        print("\t" + str(a_choice) + ",")
    print(")")
    print("SEX_CHOICES = (")
    for a_choice in sex_choices:
        print("\t" + str(a_choice) + ",")
    print(")")
    print("HOME_STATE_CHOICES = (")
    for a_choice in home_state_choices:
        print("\t" + str(a_choice) + ",")
    print(")")
    print("DEFAULT_CHOICES = {")
    for a_choice in default_choices:
        print("\t'" + a_choice[0] + "': '" + a_choice[1] + "',")
    print("}")
    return HttpResponse("see output in python console")
