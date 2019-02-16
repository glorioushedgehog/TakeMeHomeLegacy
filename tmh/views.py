from django.shortcuts import render

# Create your views here.

from .models import Person
from .models import ImageData


def index(request):
    persons = Person.objects.all()
    images = ImageData.objects.all()
    context = {'persons': persons, 'images': images}
    return render(request, 'tmh/index.html', context)


def search_by_demographics(request):
    if request.method == 'POST':
        print("HEllo")


def search_by_picture(request):
    return None
