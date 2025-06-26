# serializers.py
from rest_framework import serializers
from .models import Alcohol, InventarioFinal,Reporte,Administrador,Barra,Listaaalcohol,ListaDeAlcohol,Bartender,InventarioFinal

class AlcoholSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alcohol
        fields = '__all__'


class InventarioFinalSerializer(serializers.ModelSerializer):
    stock_total = serializers.SerializerMethodField()

    class Meta:
        model = InventarioFinal
        fields = ['id', 'alcohol', 'stock_normal', 'stock_ia', 'stock_total']
        read_only_fields = ['id', 'stock_total']

    def get_stock_total(self, obj):
        normal = obj.stock_normal or 0
        ia = obj.stock_ia or 0
        return normal + ia
 

class ReporteSerializer(serializers.ModelSerializer):
    inventarios = InventarioFinalSerializer(many=True, write_only=True)

    class Meta:
        model = Reporte
        fields = '__all__'

    def create(self, validated_data):
        inventarios_data = validated_data.pop('inventarios')
        reporte = Reporte.objects.create(**validated_data)
        for inventario in inventarios_data:
            InventarioFinal.objects.create(reporte=reporte, **inventario)
        return reporte
    
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





