
from django.shortcuts import redirect, get_object_or_404
from .models import Alcohol
from .forms import AlcoholForm  # lo crearás en el paso siguiente
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Alcohol
from .serializers import AlcoholSerializer

# Listar y crear alcoholes (GET, POST)
class AlcoholListCreate(generics.ListCreateAPIView):
    queryset = Alcohol.objects.all()
    serializer_class = AlcoholSerializer

# Actualizar o eliminar un alcohol (GET, PUT, PATCH, DELETE)
class AlcoholRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alcohol.objects.all()
    serializer_class = AlcoholSerializer


class SeleccionAlcoholView(APIView):
    def post(self, request, pk):
        """Marca un alcohol como seleccionado."""
        try:
            alcohol = Alcohol.objects.get(pk=pk)
            alcohol.seleccionado = True
            alcohol.save()
            serializer = AlcoholSerializer(alcohol)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Alcohol.DoesNotExist:
            return Response(
                {"error": "Alcohol no encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk):
        """Desmarca un alcohol como seleccionado."""
        try:
            alcohol = Alcohol.objects.get(pk=pk)
            alcohol.seleccionado = False
            alcohol.save()
            serializer = AlcoholSerializer(alcohol)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Alcohol.DoesNotExist:
            return Response(
                {"error": "Alcohol no encontrado"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
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
    