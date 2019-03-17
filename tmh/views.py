from django.shortcuts import render
from json import loads
# Create your views here.
from facial_recognition import get_embeddings_for_image_datas
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
        people = Person.objects.all()
        first_name = ""
        last_name = ""
        middle_name = ""
        name_to_call_me = ""
        home_city = ""
        home_state = ""
        home_zip = ""
        dob = ""
        dob_year = ""
        hair = ""
        eyes = ""
        race = ""
        sex = ""
        height = ""
        weight = ""
        remove_list = []
        for entry in data:
            if data[entry] is None:
                remove_list.append(entry)
        for entry in remove_list:
            data.pop(entry, None)
        if "first_name" in data:
            first_name = data["first_name"]
        if "last_name" in data:
            last_name = data["last_name"]
        if "middle_name" in data:
            middle_name = data["middle_name"]
        if "name_to_call_me" in data:
            name_to_call_me = data["name_to_call_me"]
        if "home_city" in data:
            home_city = data["home_city"]
        if "home_state" in data:
            home_state = data["home_state"]
        if "home_zip" in data:
            home_zip = data["home_zip"]
        if "dob" in data:
            dob = data["dob"]
        if "dob_year" in data:
            dob_year = data["dob_year"]
        if "hair" in data:
            hair = data["hair"]
        if "eyes" in data:
            eyes = data["eyes"]
        if "race" in data:
            race = data["race"]
        if "sex" in data:
            sex = data["sex"]
        if "height" in data:
            height = data["height"]
        if "weight" in data:
            weight = data["weight"]

        persons = []
        for peep in people:
            if peep.search(first_name, last_name, middle_name, name_to_call_me, home_city,
                           home_state, home_zip, dob, dob_year, hair, eyes, race, sex, height,
                           weight):
                persons.append(peep)

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
