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

    body = JSONParser().parse(request)["data"]
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

@csrf_exempt
@require_http_methods(['GET'])
def get_allIngredientes(request):
    try:
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse({
            'status':'Succesful',
            'result': serializer.data
        })
    except:
        return JsonResponse({
            'status':'Error',
            'result':'Hubo un error al cargar los ingredientes.'
        })
        
@csrf_exempt
@require_http_methods(['PUT'])
def actualizar_ingrediente(request, pk):
    try:
        body = JSONParser().parse(request)
        usuario = Usuario.objects.get(pk=pk)
        serializer = UsuarioSerializer(usuario, data=body["data"] )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({
                'status':'Succesful',
                'result': serializer.data
            })
        else:
            return JsonResponse({
            'status':'Error',
            'result':'Hubo un error comprando con el modelo.'
            })
    except:
        return JsonResponse({
            'status':'Error',
            'result':'Hubo un error al actualizar el ingrediente.'
        })
