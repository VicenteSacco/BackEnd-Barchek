from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Administrador, Bartender, Barra
from .serializers import AdministradorSerializer, BartenderSerializer, BarraSerializer

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
        # 1. Buscar al bartender por su nombre
        bartender = Bartender.objects.get(nombre=username)
        
        # 2. Verificar que el bartender tenga un administrador asignado
        if not bartender.idadministrador:
            return Response({'error': 'Este usuario no tiene un administrador asignado'}, status=status.HTTP_403_FORBIDDEN)

        # 3. Obtener el administrador y validar su PIN
        admin = bartender.idadministrador
        
        # El PIN del admin se compara directamente (es un número)
        if str(admin.pin) != pin:
            return Response({'error': 'PIN de administrador incorrecto'}, status=status.HTTP_401_UNAUTHORIZED)
            
        # Opcional: Validar si el PIN ha expirado
        if admin.is_pin_expired():
            return Response({'error': 'El PIN ha expirado'}, status=status.HTTP_401_UNAUTHORIZED)

        # 4. Si todo es correcto, generar un token para el bartender
        refresh = RefreshToken.for_user(bartender)
        
        # 5. Buscar todas las barras asociadas a ese administrador
        barras = Barra.objects.filter(idadministrador=admin.id)
        
        # 6. Serializar los datos para la respuesta
        user_serializer = BartenderSerializer(bartender)
        barras_serializer = BarraSerializer(barras, many=True)

        return Response({
            'token': str(refresh.access_token),
            'refresh': str(refresh),
            'user': user_serializer.data,
            'bars': barras_serializer.data, # Devolvemos la lista de barras
        })

    except Bartender.DoesNotExist:
        return Response({'error': 'Bartender no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)