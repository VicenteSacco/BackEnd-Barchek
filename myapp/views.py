
from django.shortcuts import redirect, get_object_or_404
from .models import Alcohol
from .forms import AlcoholForm  # lo crearás en el paso siguiente
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Alcohol,Reporte,Administrador,ListaDeAlcohol,Listaaalcohol,Barra,Bartender
from .serializers import AlcoholSerializer,ReporteSerializer,AdministradorSerializer,BarraSerializer,ListaaalcoholSerializer,ListaDeAlcoholSerializer,BartenderSerializer
from .services import process_image_for_liquid_estimation
from rest_framework import status
import random
from django.utils.timezone import now
from django.shortcuts import get_list_or_404
from rest_framework.exceptions import ValidationError



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

    def perform_create(self, serializer):
        idadmin = self.request.data.get('idadministrador')

        if not idadmin:
            raise ValidationError({'idadministrador': 'Este campo es obligatorio'})

        # Filtrar las listas del administrador
        listas = ListaDeAlcohol.objects.filter(idadministrador=idadmin)
        if not listas.exists():
            raise ValidationError({'idlista': 'Debes crear primero una lista para poder crear una barra.'})

        # Seleccionar la primera lista del admin por defecto
        lista = listas.first()
        serializer.save(idlista=lista)

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


# Listar y crear lista de Bartender (GET, POST)
class BartenderListCreate(generics.ListCreateAPIView):
    queryset = Bartender.objects.all()
    serializer_class = BartenderSerializer

    def perform_create(self, serializer):
        idadmin = self.request.data.get('idadministrador')

        if not idadmin:
            raise ValidationError({'idadministrador': 'Este campo es obligatorio'})

        # Filtrar las barras del administrador
        barras = Barra.objects.filter(idadministrador=idadmin)
        if not barras.exists():
            raise ValidationError({'idbarra': 'Debes crear primero una barra para poder crear un bartender.'})

        # Seleccionar la primera barra del admin por defecto
        barra = barras.first()
        serializer.save(idbarra=barra)


    
# Actualizar o eliminar un Bartender (GET, PUT, PATCH, DELETE)
class BartenderRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bartender.objects.all()
    serializer_class = BartenderSerializer

class EstimateLiquidView(APIView):
    """
    Recibe una imagen de una botella en base64 y devuelve la estimación
    de la fracción de líquido restante procesada por una IA.
    """
    def post(self, request, *args, **kwargs):
        image_data = request.data.get('image')
        drink_id = request.data.get('drinkId') # Mantenemos drinkId por si lo usas a futuro

        # Validación de la entrada
        if not image_data or drink_id is None:
            return Response(
                {"error": "Los campos 'image' (en base64) y 'drinkId' son requeridos."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Llama al servicio de IA para procesar la imagen
            result = process_image_for_liquid_estimation(image_data)
            return Response(result, status=status.HTTP_200_OK)
        
        except ValueError as e:
            # Captura errores de validación específicos (ej: fracción fuera de rango)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e:
            # Captura cualquier otro error del servicio de IA y lo loguea
            print(f"Error en EstimateLiquidView: {e}") 
            return Response(
                {"error": "Ocurrió un error al procesar la imagen con el servicio de IA."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
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
    
def login_view(request):
    return render(request, 'myapp/login.html')

def register_view(request):
    return render(request, 'myapp/register.html')

def dashboard_view(request):
    return render(request, 'myapp/dashboard.html') 

def _process_liquid_estimation_request(image_data: str, drink_id: int):
    """
    Función auxiliar para procesar la lógica de estimación de líquido.
    Captura y maneja las excepciones del servicio.
    """
    if not image_data:
        # Devuelve un error específico que la vista pueda capturar
        raise ValueError("El campo 'image' es requerido.")
    if drink_id is None:
        raise ValueError("El campo 'drinkId' es requerido.")
    try:
        drink_id = int(drink_id)
    except ValueError:
        raise ValueError("El 'drinkId' debe ser un número entero válido.")

    try:
        result = process_image_for_liquid_estimation(image_data, drink_id)
        return result
    except ValueError as e:
        # Relanza errores de validación específicos del servicio
        raise e
    except Exception as e:
        # Relanza cualquier otro error inesperado
        raise Exception(f"Error inesperado al procesar la solicitud: {e}")

class RegenerarPinAdministrador(APIView):
    def patch(self, request, pk):
        try:
            admin = Administrador.objects.get(pk=pk)
        except Administrador.DoesNotExist:
            return Response({'error': 'Administrador no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        # Si el PIN ha expirado o el usuario lo solicita → generar uno nuevo
        if admin.is_pin_expired() or request.data.get('forzar', False):
            nuevo_pin = admin.regenerate_pin()
            return Response({'mensaje': 'PIN regenerado correctamente.', 'nuevo_pin': nuevo_pin})

        return Response({'mensaje': 'El PIN aún es válido.', 'pin_actual': admin.pin})
    
class BuscarListasPorAdmin(APIView):
    def get(self, request, pk):
        try:
            admin = Administrador.objects.get(pk=pk)
        except Administrador.DoesNotExist:
            return Response({'error': 'Administrador no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        listas = ListaDeAlcohol.objects.filter(idadministrador=admin.id)
        serializer = ListaDeAlcoholSerializer(listas, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BuscarAlcoholesPorLista(APIView):
    def get(self, request, pk):
        try:
            lista = ListaDeAlcohol.objects.get(pk=pk)
        except ListaDeAlcohol.DoesNotExist:
            return Response({'error': 'Lista de alcohol no encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        relaciones = Listaaalcohol.objects.filter(idlista=lista.id)
        serializer = ListaaalcoholSerializer(relaciones, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class BuscarBarrasPorAdmin(APIView):
    def get(self, request, pk):
        try:
            admin = Administrador.objects.get(pk=pk)
        except Administrador.DoesNotExist:
            return Response({'error': 'Administrador no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        barras = Barra.objects.filter(idadministrador=admin.id)
        serializer = BarraSerializer(barras, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
class BartendersPorAdministradorConBarra(APIView):
    def get(self, request, pk):
        bartenders = Bartender.objects.filter(idadministrador=pk).exclude(idbarra__isnull=True)
        serializer = BartenderSerializer(bartenders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


