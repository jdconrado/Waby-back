from django.db import models
from usuarios.models import Usuarios

# Create your models here.

class Pedido (models.Model):
    especificaciones=models.TextField()
    precioTotal=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    fecha_creado=models.DateTimeField()
    userId=models.ForeignKey(Usuarios,on_delete=models.CASCADE)