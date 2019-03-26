from django.contrib import admin
from .models import Person, ImageData, InferenceTask, CfgLookup

# Register your models here.

admin.site.register(Person)
admin.site.register(ImageData)
admin.site.register(InferenceTask)
admin.site.register(CfgLookup)
