from django.shortcuts import render

# Create your views here.

from .models import Person
from .models import ImageData


def index(request):
    persons = Person.objects.all()
    images = ImageData.objects.all()
    context = {'persons': persons, 'images': images}
    return render(request, 'tmh/index.html', context)
