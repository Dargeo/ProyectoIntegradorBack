from rest_framework import viewsets
from .models import Temperatura
from .serializers import TemperaturaSerializer

class TemperaturaViewSet(viewsets.ModelViewSet):
    queryset = Temperatura.objects.all().order_by('-created')
    serializer_class = TemperaturaSerializer