from django.shortcuts import render
from json import loads
# Create your views here.
from facial_recognition import get_embeddings_for_image_datas
from tmh import demographic_search
from .models import Person
from .models import ImageData
from facial_recognition import search


def index(request):
    persons = Person.objects.all()
    images = ImageData.objects.all()
    context = {'persons': persons, 'images': images}
    return render(request, 'tmh/index.html', context)


def search_by_demographics(request):
    if request.method == 'POST':
        data = loads(request.body)
        persons = demographic_search.get_matching_persons(data)
        from math import ceil
        large_row_size = 4
        medium_row_size = 2
        persons_by_large_row = []
        for i in range(ceil(len(persons) / large_row_size)):
            a_row = []
            for j in range(large_row_size):
                if i * large_row_size + j >= len(persons):
                    break
                a_row.append(persons[i * large_row_size + j])
            persons_by_large_row.append(a_row)

        persons_by_medium_row = []
        for i in range(ceil(len(persons) / medium_row_size)):
            a_row = []
            for j in range(medium_row_size):
                if i * medium_row_size + j >= len(persons):
                    break
                a_row.append(persons[i * medium_row_size + j])
            persons_by_medium_row.append(a_row)

        images = ImageData.objects.none()
        for individual in persons:
            an_id = individual.primarykey
            new_query_set = ImageData.objects.filter(primarykey=an_id)
            images = images.union(new_query_set)
        # persons = people
        # images = ImageData.objects.all()
        context = {
            'persons': persons,
            'persons_by_large_row': persons_by_large_row,
            'persons_by_medium_row': persons_by_medium_row,
            'images': images
        }
        return render(request, 'tmh/demographic_search.html', context)


def search_by_picture(request):
    keys = search.search(ImageData.objects.all(), request.body)
    persons = Person.objects.none()
    images = ImageData.objects.none()
    for key in keys:
        persons = persons.union(Person.objects.filter(primarykey=key))
        images = ImageData.objects.filter(primarykey=key)
    context = {'persons': persons, 'images': images}
    return render(request, 'tmh/demographic_search.html', context)


def upload(request):
    return render(request, 'tmh/imageupload.html', {})


def generate_embeddings(request):
    get_embeddings_for_image_datas.generate_embeddings()
