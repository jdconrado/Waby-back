from django.db import models

# Create your models here.

class Pedido (models.Model):
    receta=models.TextField()
    especificaciones=models.TextField()
    precioTotal=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    fecha_creado=models.DateTimeField()