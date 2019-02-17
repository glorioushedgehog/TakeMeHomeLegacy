from django.shortcuts import render
from json import loads
# Create your views here.

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
        index = 0
        for indiv in persons:
            id = indiv.primarykey
            newQuerySet = ImageData.objects.filter(primarykey=id)
            if index == 0:
                images = newQuerySet
                index += 1
            else:
                images.union(newQuerySet)

        context = {'persons': persons, 'images': images}
        return render(request, 'tmh/demographic_search.html', context)


def search_by_picture(request):
    if request.is_ajax():
        print("yes")
    # search_result = search.search(request.body)
    return None


def upload(request):
    return render(request, 'tmh/imageupload.html', {})
