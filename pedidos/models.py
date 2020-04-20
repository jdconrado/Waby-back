from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Pedido (models.Model):
    receta=JSONField(default=list, blank=True, null=True)
    especificaciones=models.TextField()
    precioTotal=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    fecha_creado=models.DateTimeField()