from django.contrib import admin

# Register your models here.
from .models import Instrumentos

#Registrar el modelo Instrumento en el admin
admin.site.register(Instrumentos)