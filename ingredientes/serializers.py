from rest_framework import serializers
from .models import Ingrediente

class IngredienteSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Ingrediente
        fields='__all__'