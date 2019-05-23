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
    # sort choices alphabetically
    eyes_choices.sort()
    hair_choices.sort()
    organization_choices.sort()
    race_choices.sort()
    record_type_choices.sort()
    emergency_contact_relationship_choices.sort()
    sex_choices.sort()
    home_state_choices.sort()
    default_choices.sort()

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
