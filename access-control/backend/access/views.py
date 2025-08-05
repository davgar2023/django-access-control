from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from .models import AccessPoint, AccessEvent
from .serializers import AccessPointSerializer, AccessEventSerializer, UserRegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

class AccessPointViewSet(viewsets.ModelViewSet):
    queryset = AccessPoint.objects.all()
    serializer_class = AccessPointSerializer
    permission_classes = [permissions.IsAuthenticated]

class AccessEventViewSet(viewsets.ModelViewSet):
    queryset = AccessEvent.objects.select_related('access_point', 'user').all()
    serializer_class = AccessEventSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Crea un evento asignando el usuario autenticado automáticamente
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
