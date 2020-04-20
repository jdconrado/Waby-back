from rest_framework import serializers
from .models import Ingrediente,ListaIngredientes

class IngredienteSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Ingrediente
        fields='__all__'

class ListaIgnSerializer (serializers.ModelSerializer):

    class Meta:
        model = ListaIngredientes
        fields = '__all__'