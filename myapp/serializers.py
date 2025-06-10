from rest_framework import serializers
from .models import Administrador, Barra, Categoría, Alcohol, CarouselItem, ListaDeAlcohol, Reporte

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ['id', 'correo_electronico', 'contraseña', 'pin']

class BarraSerializer(serializers.ModelSerializer):
    administrador = AdministradorSerializer(read_only=True)
    administrador_id = serializers.PrimaryKeyRelatedField(
        queryset=Administrador.objects.all(), source='administrador', write_only=True
    )

    class Meta:
        model = Barra
        fields = ['id', 'numero_de_barra', 'cantidad_bartender', 'nombre_de_la_barra', 'administrador', 'administrador_id']

class CategoríaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoría
        fields = ['id', 'nombre']

class AlcoholSerializer(serializers.ModelSerializer):
    categoria = CategoríaSerializer(read_only=True)
    categoria_id = serializers.PrimaryKeyRelatedField(
        queryset=Categoría.objects.all(), source='categoria', write_only=True
    )

    class Meta:
        model = Alcohol
        fields = ['id', 'codigo_de_barra', 'stock_actual', 'cantidad_cc', 'marca', 'año', 'ia', 'nombre', 'categoria', 'categoria_id']

class CarouselItemSerializer(serializers.ModelSerializer):
    alcohol = AlcoholSerializer(read_only=True)
    alcohol_id = serializers.PrimaryKeyRelatedField(
        queryset=Alcohol.objects.all(), source='alcohol', write_only=True
    )

    class Meta:
        model = CarouselItem
        fields = ['id', 'alcohol', 'alcohol_id', 'titulo', 'descripcion']

class ListaDeAlcoholSerializer(serializers.ModelSerializer):
    barra = BarraSerializer(read_only=True)
    barra_id = serializers.PrimaryKeyRelatedField(
        queryset=Barra.objects.all(), source='barra', write_only=True
    )
    administrador = AdministradorSerializer(read_only=True)
    administrador_id = serializers.PrimaryKeyRelatedField(
        queryset=Administrador.objects.all(), source='administrador', write_only=True
    )
    alcoholes = AlcoholSerializer(many=True, read_only=True)
    alcoholes_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Alcohol.objects.all(), source='alcoholes', write_only=True
    )

    class Meta:
        model = ListaDeAlcohol
        fields = ['id', 'nombre', 'barra', 'barra_id', 'administrador', 'administrador_id', 'alcoholes', 'alcoholes_ids']

class ReporteSerializer(serializers.ModelSerializer):
    administrador = AdministradorSerializer(read_only=True)
    administrador_id = serializers.PrimaryKeyRelatedField(
        queryset=Administrador.objects.all(), source='administrador', write_only=True
    )

    class Meta:
        model = Reporte
        fields = ['id', 'administrador', 'administrador_id', 'fecha']
