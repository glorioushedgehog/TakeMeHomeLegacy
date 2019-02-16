from django.shortcuts import render

# Create your views here.

from .models import Person
from .models import ImageData
from .forms import UploadImageForm
from facial_recognition.infer import get_embedding_from_file


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


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            embedding = get_embedding_from_file(request.FILES['image'])
            return render(request, 'tmh/facial_recognition.html', {'form': form, 'embedding': embedding})
    else:
        form = UploadImageForm()
    return render(request, 'tmh/facial_recognition.html', {'form': form})
