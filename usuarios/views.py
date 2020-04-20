from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Usuario
from .serializers import UsuarioSerializer
import json
from django.utils import timezone

# Create your views here.
@csrf_exempt
@require_http_methods(['POST'])
def crear_usuario(request):

    body = JSONParser().parse(request)
    i = UsuarioSerializer(data={
        "nombre":body["nombre"],
        "apellido":body["apellido"],
        "email":body["email"],
        "password":body["password"]
    })
    try:
        if i.is_valid():
            i.save()
            return JsonResponse({
                'status':'Succesful',
                'result':'Usuario creado.'
            })
        else:
            return JsonResponse({
            'status':'Error',
            'result':'Los campos no son validos.',
        })
    except:
        return JsonResponse({
            'status':'Error',
            'result':'Hubo un error al crear el usuario.'
        })
