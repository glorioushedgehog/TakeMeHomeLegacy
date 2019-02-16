from django.shortcuts import render

# Create your views here.

from .models import Person
from .models import ImageData


def index(request):
    persons = Person.objects.all()
    images = ImageData.objects.all()
    context = {'persons': persons, 'images': images}
    return render(request, 'tmh/index.html', context)


def facial_recognition(request):
    persons = Person.objects.all()
    images = ImageData.objects.all()
    context = {'persons': persons, 'images': images}
    return render(request, 'tmh/facial_recognition.html', context)


def search_by_demographics(request):
    if request.method == 'POST':
        print("HEllo")
