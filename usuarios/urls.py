from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import CustomTokenObtainPairView, UserListView, InfoHornoListView, InfoProduccionListView, InfoTinaListView, InfoGermListView, InfoAnalisisListView 

urlpatterns = [
    path('usuarios/', UserListView.as_view(), name='user-list'),  # Ruta para listar o crear usuarios
    path('usuarios/<int:pk>/', UserListView.as_view(), name='user-detail'),  # Ruta para obtener, actualizar o eliminar un usuario por ID
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('info-horno/', InfoHornoListView.as_view(), name='info-horno-list'),
    path('info-tina/', InfoTinaListView.as_view(), name='info-tina-list'),
    path('info-germ/', InfoGermListView.as_view(), name='info-germ-list'),
    path('info-analisis/', InfoAnalisisListView.as_view(), name='info-analisis-list'),
    path('info-produccion/', InfoProduccionListView.as_view(), name='info-produccion-list'),
]
