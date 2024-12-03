from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from .models import Usuario, InfoHorno, InfoProduccion, InfoTina, InfoGerm, InfoAnalisis, UsuarioGroup
from .serializers import CustomTokenObtainPairSerializer, UserSerializer, InfoHornoSerializer, InfoProduccionSerializer, InfoAnalisisSerializer, InfoGermSerializer, InfoTinaSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk=None):
        if pk is None:
            # Obtener todos los usuarios
            users = Usuario.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        else:
            # Obtener un usuario específico
            user = get_object_or_404(Usuario, pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)

    def post(self, request):
        # Crear un nuevo usuario
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        # Obtener el usuario que se va a actualizar
        user = get_object_or_404(Usuario, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            # Verifica si la contraseña está en los datos enviados
            if 'password' in request.data:
                # Cifra la contraseña antes de guardarla
                new_password = request.data['password']
                user.set_password(new_password)
                user.save(update_fields=['password'])  # Guarda solo la contraseña
            else:
                # Si no hay contraseña, guarda solo los demás campos
                serializer.save()

            # Refrescar el objeto usuario para asegurarse de que los cambios se reflejan
            user.refresh_from_db()

            # Devolver la información del usuario actualizado
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

        # Si los datos no son válidos, devuelve los errores del serializador
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = get_object_or_404(Usuario, pk=pk)

            # Eliminar registros relacionados manualmente
            from django.contrib.admin.models import LogEntry
            from rest_framework.authtoken.models import Token
            from django.db.models import Q

            LogEntry.objects.filter(user=user).delete()
            Token.objects.filter(user=user).delete()

            # Eliminar registros en grupos relacionados
            from usuarios.models import UsuarioGroup  # Ajusta según el nombre real
            UsuarioGroup.objects.filter(user=user).delete()

            # Eliminar el usuario
            user.delete()
            return Response({"detail": "Usuario eliminado correctamente"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    
class InfoHornoListView(APIView):
    # permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados
    permission_classes = [permissions.AllowAny]  # Permitir acceso a todos
  

    def get(self, request):
        # Verifica cuántos registros devuelve la consulta
        hornos = InfoHorno.objects.all()
        print(f"Registros encontrados: {hornos.count()}")  # Debugging
        
        # Serializa los datos
        serializer = InfoHornoSerializer(hornos, many=True)
        return Response(serializer.data)
    
class InfoProduccionListView(APIView):
    # permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados
    permission_classes = [permissions.AllowAny]  # Permitir acceso a todos
  

    def get(self, request):
        # Verifica cuántos registros devuelve la consulta
        hornos = InfoProduccion.objects.all()
        print(f"Registros encontrados: {hornos.count()}")  # Debugging
        
        # Serializa los datos
        serializer = InfoProduccionSerializer(hornos, many=True)
        return Response(serializer.data)
    
class InfoTinaListView(APIView):
    # permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados
    permission_classes = [permissions.AllowAny]  # Permitir acceso a todos
  

    def get(self, request):
        # Verifica cuántos registros devuelve la consulta
        objetos = InfoTina.objects.all()
        print(f"Registros encontrados: {objetos.count()}")  # Debugging
        
        # Serializa los datos
        serializer = InfoTinaSerializer(objetos, many=True)
        return Response(serializer.data)
    
class InfoGermListView(APIView):
    # permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados
    permission_classes = [permissions.AllowAny]  # Permitir acceso a todos
  

    def get(self, request):
        # Verifica cuántos registros devuelve la consulta
        objetos = InfoGerm.objects.all()
        print(f"Registros encontrados: {objetos.count()}")  # Debugging
        
        # Serializa los datos
        serializer = InfoGermSerializer(objetos, many=True)
        return Response(serializer.data)
    
class InfoAnalisisListView(APIView):
    # permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados
    permission_classes = [permissions.AllowAny]  # Permitir acceso a todos
  

    def get(self, request):
        # Verifica cuántos registros devuelve la consulta
        objetos = InfoAnalisis.objects.all()
        print(f"Registros encontrados: {objetos.count()}")  # Debugging
        
        # Serializa los datos
        serializer = InfoAnalisisSerializer(objetos, many=True)
        return Response(serializer.data)
    