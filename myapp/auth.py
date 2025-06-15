from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Administrador
from .serializers import AdministradorSerializer, BartenderSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    correo = request.data.get('correoelectronico')
    password = request.data.get('contrasena')
    
    try:
        admin = Administrador.objects.get(correoelectronico=correo)
        if check_password(password, admin.contrasena):
            refresh = RefreshToken.for_user(admin)
            return Response({
                'token': str(refresh.access_token),
                'refresh': str(refresh),
                'user': AdministradorSerializer(admin).data
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    except Administrador.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    serializer = AdministradorSerializer(data=request.data)
    if serializer.is_valid():
        # Hash the password before saving
        password = serializer.validated_data['contrasena']
        serializer.validated_data['contrasena'] = make_password(password)
        admin = serializer.save()
        
        # Generate tokens
        refresh = RefreshToken.for_user(admin)
        return Response({
            'token': str(refresh.access_token),
            'refresh': str(refresh),
            'user': serializer.data
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
@permission_classes([AllowAny])
def bartender_login(request):
    username = request.data.get('nombre')
    pin = request.data.get('pin')

    if not username or not pin:
        return Response({'error': 'Nombre y PIN son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        bartender = Bartender.objects.get(nombre=username)
        # check_password compara el PIN enviado con el PIN hasheado en la BD
        if check_password(pin, bartender.pin):
            refresh = RefreshToken.for_user(bartender)
            serializer = BartenderSerializer(bartender)

            return Response({
                'token': str(refresh.access_token),
                'refresh': str(refresh),
                'user': serializer.data # Enviamos los datos del bartender serializados
            })
        return Response({'error': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
    except Bartender.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)