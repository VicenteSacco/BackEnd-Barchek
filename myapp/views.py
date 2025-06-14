
from django.shortcuts import redirect, get_object_or_404
from .models import Alcohol
from .forms import AlcoholForm  # lo crearás en el paso siguiente
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Alcohol,Reporte,Administrador,ListaDeAlcohol,Listaaalcohol,Barra
from .serializers import AlcoholSerializer,ReporteSerializer,AdministradorSerializer,BarraSerializer,ListaaalcoholSerializer,ListaDeAlcoholSerializer

# Listar y crear alcoholes (GET, POST)
class AlcoholListCreate(generics.ListCreateAPIView):
    queryset = Alcohol.objects.all()
    serializer_class = AlcoholSerializer

# Actualizar o eliminar un alcohol (GET, PUT, PATCH, DELETE)
class AlcoholRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alcohol.objects.all()
    serializer_class = AlcoholSerializer

# Listar y crear Reportes (GET, POST)
class ReporteListCreate(generics.ListCreateAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer   

# Actualizar o eliminar un Reportes (GET, PUT, PATCH, DELETE)
class ReporteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

# Listar y crear Administrador (GET, POST)
class AdministradorListCreate(generics.ListCreateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

# Actualizar o eliminar un Administrador (GET, PUT, PATCH, DELETE)
class AdministradorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

# Listar y crear Barra (GET, POST)
class BarraListCreate(generics.ListCreateAPIView):
    queryset = Barra.objects.all()
    serializer_class = BarraSerializer

# Actualizar o eliminar una Barra (GET, PUT, PATCH, DELETE)
class BarraRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Barra.objects.all()
    serializer_class = BarraSerializer

# Listar y crear lista a alcohol (GET, POST)
class ListaaalcoholListCreate(generics.ListCreateAPIView):
    queryset = Listaaalcohol.objects.all()
    serializer_class = ListaaalcoholSerializer

# Actualizar o eliminar una lista a alcohol (GET, PUT, PATCH, DELETE)
class ListaaalcoholRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listaaalcohol.objects.all()
    serializer_class = ListaaalcoholSerializer

# Listar y crear lista de alcohol (GET, POST)
class ListaDeAlcoholListCreate(generics.ListCreateAPIView):
    queryset = ListaDeAlcohol.objects.all()
    serializer_class = ListaDeAlcoholSerializer

# Actualizar o eliminar una lista de alcohol (GET, PUT, PATCH, DELETE)
class ListaDeAlcoholRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListaDeAlcohol.objects.all()
    serializer_class = ListaDeAlcoholSerializer




# Listar todos los registros
def alcohol_list(request):
    alcoholes = Alcohol.objects.all()
    return render(request, 'myapp/alcohol_list.html', {'alcoholes': alcoholes})

# Crear un nuevo registro
def alcohol_create(request):
    if request.method == 'POST':
        form = AlcoholForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alcohol_list')
    else:
        form = AlcoholForm()
    return render(request, 'myapp/alcohol_form.html', {'form': form})

# Editar un registro existente
def alcohol_update(request, pk):
    alcohol = get_object_or_404(Alcohol, pk=pk)
    if request.method == 'POST':
        form = AlcoholForm(request.POST, instance=alcohol)
        if form.is_valid():
            form.save()
            return redirect('alcohol_list')
    else:
        form = AlcoholForm(instance=alcohol)
    return render(request, 'myapp/alcohol_form.html', {'form': form})

# Eliminar un registro
def alcohol_delete(request, pk):
    alcohol = get_object_or_404(Alcohol, pk=pk)
    if request.method == 'POST':
        alcohol.delete()
        return redirect('alcohol_list')
    return render(request, 'myapp/alcohol_confirm_delete.html', {'alcohol': alcohol}) 
    
def login_view(request):
    return render(request, 'myapp/login.html')

def register_view(request):
    return render(request, 'myapp/register.html')

def dashboard_view(request):
    return render(request, 'myapp/dashboard.html') 
    