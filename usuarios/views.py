from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Usuarios
from django.contrib.auth import login, authenticate, logout
#from .serializers import UsuarioSerializer
import json
from django.utils import timezone

# Create your views here.


@csrf_exempt
@require_http_methods(['POST'])
def crear_usuario(request):
    body = JSONParser().parse(request)["data"]
    # i = UsuarioSerializer(data={
    #     "nombre":body["nombre"],
    #     "apellido":body["apellido"],
    #     "email":body["email"],
    #     "password":body["password"]
    # })
    try:
        user = Usuarios.objects.create_user(body["email"], body["password"])
        user.name = body["name"]
        user.lastname = body["lastname"]
        user.save()
        return JsonResponse({
            'status': 'Success',
            'result': 'Se ha creado correctamente.'
        })
    except:
        return JsonResponse({
            'status': 'Error',
            'result': 'Hubo un error al crear el usuario.'
        })

@csrf_exempt
@require_http_methods(['POST'])
def logoutv(request):
    try:
        logout(request)
        return JsonResponse({
            'status':'Success',
            'result':'Log Out'
        })
    except:
        return JsonResponse({
            'status':'Error',
            'result':'Something went wrong'
        })

@csrf_exempt
@require_http_methods(['POST'])
def log(request):
    body = JSONParser().parse(request)["data"]
    try:
        user = authenticate(body["email"], body["password"])
        print(user)
        if user is not None:
            login(request,user)
            print("we did it perhaps?")
            return JsonResponse({
                'status': 'Success',
                'result': 'Se ha creado correctamente.'
            })
    except:
        return JsonResponse({
            'status': 'Error',
            'result': 'Hubo un error al crear el usuario.'
        })
