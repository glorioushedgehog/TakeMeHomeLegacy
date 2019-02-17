from django.shortcuts import render

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
        print("HEllo")


def search_by_picture(request):
    if request.is_ajax():
        print("yes")
    search_result = search.search(request.body)
    return None


def upload(request):
    return render(request, 'tmh/imageupload.html', {})
