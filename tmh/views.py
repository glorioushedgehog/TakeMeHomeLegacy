from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import render
from facial_recognition.search import init_inference_task, create_image_datas
from facial_recognition.search import get_matching_persons
from tmh import demographic_search
from tmh.context_generators import grid_of_persons, facial_recognition_coverage, person_details_context
from tmh.forms import ImageUploadForm, PersonForm
from .models import Person, InferenceTask, CfgLookup
from .models import ImageData


def index(request):
    image_form = ImageUploadForm()
    demographics_form = PersonForm()
    context = {'image_form': image_form, 'demographics_form': demographics_form}
    return render(request, 'tmh/index.html', context)


def person_details(request, primary_key):
    a_person = Person.objects.get(pk=primary_key)
    context = person_details_context(a_person)
    return render(request, 'tmh/person_details.html', context)


def search_by_demographics(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            persons = demographic_search.get_matching_persons(form.cleaned_data)
            context = grid_of_persons(persons)
            return render(request, 'tmh/search_results.html', context)
        else:
            return render(request, 'tmh/search_results.html', {})
    return index(request)


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
        'success': task.state == task.SUCCESS,
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
    context = grid_of_persons(persons)
    return render(request, 'tmh/search_result_cards.html', context)


def manage_facial_recognition(request):
    people = Person.objects.all()
    context = facial_recognition_coverage(people)
    return render(request, 'tmh/manage_facial_recognition.html', context)


def prepare_for_facial_recognition(request):
    create_image_datas(Person.objects.all())
    return HttpResponse()


def dropdown_options(request):
    def print_choices(choice_list):
        for choice in choice_list:
            print("\t" + str(choice) + ",")
        print(")")
    choices = [[] for _ in range(10)]
    config_options = CfgLookup.objects.all()
    for an_option in config_options:
        a_tuple = (an_option.choice.strip(), an_option.description.strip())
        choices[an_option.typeid].append(a_tuple)
    # sort choices alphabetically
    for list_of_choices in choices:
        list_of_choices.sort()
    print("EYES_CHOICES = (")
    print_choices(choices[1])
    print("HAIR_CHOICES = (")
    print_choices(choices[2])
    print("ORGANIZATION_CHOICES = (")
    print_choices(choices[3])
    print("RACE_CHOICES = (")
    print_choices(choices[4])
    print("RECORD_TYPE_CHOICES = (")
    print_choices(choices[5])
    print("EMERGENCY_CONTACT_RELATIONSHIP_CHOICES = (")
    print_choices(choices[6])
    print("SEX_CHOICES = (")
    print_choices(choices[7])
    print("HOME_STATE_CHOICES = (")
    print_choices(choices[8])
    print("DEFAULT_CHOICES = {")
    for a_choice in choices[9]:
        print("\t'" + a_choice[0] + "': '" + a_choice[1] + "',")
    print("}")
    return HttpResponse("see output in python console")
