from pydoc import ModuleScanner
from django.contrib import admin
from .models import Questions, Profile

admin.site.register(Questions)
admin.site.register(Profile)

# Register your models here.
