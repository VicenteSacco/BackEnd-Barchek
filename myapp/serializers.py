# serializers.py
from rest_framework import serializers
from .models import Alcohol, InventarioFinal,Reporte,Administrador,Barra,Listaaalcohol,ListaDeAlcohol,Bartender,InventarioFinal

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

class InventarioFinalSerializer(serializers.ModelSerializer):
    stock_total = serializers.SerializerMethodField()

    class Meta:
        model = InventarioFinal
        fields = ['id', 'reporte', 'alcohol', 'stock_normal', 'stock_ia', 'liquidez_lista', 'stock_total']

    def get_stock_total(self, obj):
        normal = obj.stock_normal or 0
        ia = obj.stock_ia or 0
        return normal + ia
