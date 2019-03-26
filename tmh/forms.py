from django import forms
from django.forms import ModelForm

from tmh.models import Person


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            'dob_year',
            'height',
            'weight',
            'sex',
            'hair',
            'eyes',
            'race',

            'last_name',
            'first_name',
            'middle_name',
            'name_to_call_me',

            'braclet_id',
            'record_type',
            'organization',

            'home_address',
            'home_city',
            'home_state',
            'home_zip',
            'home_phone',
        ]
