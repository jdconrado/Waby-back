from django.db import models
from pedidos.models import Pedido

# Create your models here.

class Ingrediente(models.Model):
    nombre_ing=models.CharField(max_length=100)
    stock=models.IntegerField(default=0)
    precio=models.FloatField(default=0)
    tipo=models.CharField(max_length=50)

    def __str__(self): #When calling for the object, this will let us identify what question it is.
        return self.nombre_ing

class ListaIngredientes(models.Model):
    ingred = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    pedidoId = models.ForeignKey(Pedido, on_delete=models.CASCADE)

