
from django.db import models
import uuid

class Temperatura(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    value = models.IntegerField(verbose_name='Valor')
    fecha = models.DateTimeField(auto_now_add = True)
    codigoSensor = models.CharField(verbose_name ='codigoSensor', max_length=20)
    origen = models.CharField(verbose_name = 'origen', max_length = 50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)