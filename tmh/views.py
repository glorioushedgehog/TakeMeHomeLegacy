from django.shortcuts import render
from json import loads
from facial_recognition import get_embeddings_for_image_datas
from tmh import demographic_search
from tmh.context_generators import context_from_person_list
from tmh.forms import ImageUploadForm
from .models import Person
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
        return render(request, 'tmh/demographic_search.html', context)


def search_by_picture(request):
    keys = search.search(ImageData.objects.all(), request.body)
    persons = []
    for key in keys:
        persons.append(Person.objects.get(pk=key))
    context = context_from_person_list(persons)
    return render(request, 'tmh/demographic_search.html', context)


def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            the_image = form.cleaned_data['image']
            keys = search.search_by_image(ImageData.objects.all(), the_image)
            persons = []
            for key in keys:
                persons.append(Person.objects.get(pk=key))
            context = context_from_person_list(persons)
            return render(request, 'tmh/demographic_search.html', context)
    #         m = ExampleModel.objects.get(pk=course_id)
    #         m.model_pic = form.cleaned_data['image']
    #         m.save()
    #         return HttpResponse('image upload success')
    # return HttpResponseForbidden('allowed only via POST')


def upload(request):
    return render(request, 'tmh/imageupload.html', {})


def generate_embeddings(request):
    get_embeddings_for_image_datas.generate_embeddings()
