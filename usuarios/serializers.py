from rest_framework import serializers
from .models import Usuario, InfoHorno, InfoProduccion, InfoAnalisis, InfoGerm, InfoTina
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'rut', 'role', 'password']
        
class InfoHornoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoHorno
        fields = '__all__'

class InfoProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoProduccion
        fields = '__all__'

class InfoAnalisisSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoAnalisis
        fields = '__all__'

class InfoGermSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoGerm
        fields = '__all__'

class InfoTinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoTina
        fields = '__all__'

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agregar campos personalizados al token
        token['id'] = user.id  # Incluye el ID del usuario
        token['username'] = user.username  # Incluye el nombre de usuario (opcional)
        token['role'] = user.role  # Incluye el nombre de usuario (opcional)

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Agregar campos adicionales a la respuesta del token
        data['id'] = self.user.id
        data['username'] = self.user.username
        data['role'] = self.user.role

        return data