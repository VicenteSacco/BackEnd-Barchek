# serializers.py
from rest_framework import serializers
from .models import Alcohol,Reporte,Administrador,Barra,Listaaalcohol,ListaDeAlcohol

class AlcoholSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alcohol
        fields = '__all__'


class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields= '__all__'

class BarraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barra
        fields = '__all__'

class ListaaalcoholSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listaaalcohol
        fields = '__all__'

class ListaDeAlcoholSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaDeAlcohol
        fields = '__all__'