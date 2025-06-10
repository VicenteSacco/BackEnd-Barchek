from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from .models import Administrador, Barra, Categoría, Alcohol, CarouselItem, ListaDeAlcohol, Reporte
from .serializers import (
    AdministradorSerializer,
    BarraSerializer,
    CategoríaSerializer,
    AlcoholSerializer,
    CarouselItemSerializer,
    ListaDeAlcoholSerializer,
    ReporteSerializer,
)
from django.http import HttpResponse

class HelloWorldAPI(APIView):
    def get(self, request):
        return Response({"message": "Hello, world! This is your API."}, status=status.HTTP_200_OK)

def root_view(request):
    return HttpResponse("Welcome to the Django backend API.")

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

class BarraViewSet(viewsets.ModelViewSet):
    queryset = Barra.objects.all()
    serializer_class = BarraSerializer

class CategoríaViewSet(viewsets.ModelViewSet):
    queryset = Categoría.objects.all()
    serializer_class = CategoríaSerializer

class AlcoholViewSet(viewsets.ModelViewSet):
    queryset = Alcohol.objects.all()
    serializer_class = AlcoholSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['categoria__nombre']

class CarouselItemViewSet(viewsets.ModelViewSet):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer

class ListaDeAlcoholViewSet(viewsets.ModelViewSet):
    queryset = ListaDeAlcohol.objects.all()
    serializer_class = ListaDeAlcoholSerializer

class ReporteViewSet(viewsets.ModelViewSet):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer
