from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from .models import Ingrediente
from .serializers import IngredienteSerializer
import json

# Create your views here.
@csrf_exempt
@require_http_methods(['POST'])
def crear_ingrediente(request):

    body = JSONParser().parse(request)
    i = IngredienteSerializer(data=body["data"])
    try:
        if i.is_valid():
            i.save()
            return JsonResponse({
                'status':'Succesful',
                'result':'Ingrediente creado.'
            })
        else:
            return JsonResponse({
            'status':'Error',
            'result':'Los campos no son validos.',
        })
    except:
        return JsonResponse({
            'status':'Error',
            'result':'Hubo un error al crear el ingrediente.'
        })

    