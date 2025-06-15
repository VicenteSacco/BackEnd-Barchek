# serializers.py
from rest_framework import serializers
from .models import Alcohol,Reporte,Administrador,Barra,Listaaalcohol,ListaDeAlcohol,Bartender

class AlcoholSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alcohol
        fields = '__all__'


class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporte
        fields = '__all__'

class AdministradorSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = Administrador
        fields = ['id', 'correoelectronico', 'contrasena', 'role', 'pin']
        extra_kwargs = {
            'contrasena': {'write_only': True}
        }
    
    def get_role(self, obj):
        # You can implement your role logic here
        # For now, let's return 'admin' for all users
        return 'admin'

class BarraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barra
        fields = '__all__'

class ListaaalcoholSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listaaalcohol
        fields = ['idlista','idalcohol']

class ListaDeAlcoholSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaDeAlcohol
        fields = '__all__'

class BartenderSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = Bartender
        # Quitamos el campo 'pin' de la lista
        fields = ['id', 'nombre', 'idbarra', 'idadministrador', 'role']

    def get_role(self, obj):
        return 'bartender'
