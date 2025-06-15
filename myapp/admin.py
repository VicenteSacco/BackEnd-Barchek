from django.contrib import admin
from django.contrib import admin
from .models import Administrador, Alcohol, ListaDeAlcohol, Barra, Reporte, Bartender

admin.site.register(Administrador)
admin.site.register(Alcohol)
admin.site.register(ListaDeAlcohol)
admin.site.register(Barra)
admin.site.register(Reporte)
admin.site.register(Bartender)