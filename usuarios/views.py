from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
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
    try:
        print(body["tipo"])
        if body["tipo"]:
            user = Usuarios.objects.create_admin(body["email"], body["password"])
        else:
            user = Usuarios.objects.create_user(body["email"], body["password"])
        user.name = body["name"]
        user.lastname = body["lastname"]
        user.save()
        token = Token.objects.get_or_create(user=user)[0]
        js = str(token)
        return JsonResponse({
            'status': 'Success',
            'result': js
        })
    except Exception as e:
        print(e)
        return JsonResponse({
            'status': 'Error',
            'result': 'Hubo un error al crear el usuario.'
        })


@csrf_exempt
@require_http_methods(['POST'])
def getid(request,token):
    try:
        id=Token.objects.get(key=token)
        userid=id.user_id
        return JsonResponse({
            'status': 'Success',
            'result': userid
        })
    except:
        return JsonResponse({
            'status': 'Error',
            'result': 'Something went wrong'
        })


@csrf_exempt
@require_http_methods(['POST'])
def logoutv(request,tk):
    try:
        logout(request)
        token=Token.objects.get(key=tk)
        token.delete()
        return JsonResponse({
            'status': 'Success',
            'result': 'Log Out'
        })
    except:
        return JsonResponse({
            'status': 'Error',
            'result': 'Something went wrong'
        })

# @csrf_exempt


@require_http_methods(['POST'])
def log(request):
    body = JSONParser().parse(request)["data"]
    try:
        user = authenticate(email=body["email"], password=body["password"])
        if user is not None:
            token = Token.objects.get_or_create(user=user)[0]
            js = str(token)
            return JsonResponse({
                'status': 'Successful',
                'result': js
            })
        else:
            return JsonResponse({
                'status': 'Error',
                'result': 'Doesnt exist.'
            })
    except Exception as e:
        print(e)
        return JsonResponse({
            'status': 'Error',
            'result': 'Hubo un error al logear el usuario.'
        })

@csrf_exempt
@require_http_methods(['GET'])
def getUser(request,idC):
    try:
        id=Usuarios.objects.get(id=idC)
        name=str(id.name)
        lastname=str(id.lastname)
        email=str(id.email)
        return JsonResponse({
            'status': 'Success',
            'result': {'name': name, 'lastname': lastname, 'email': email}
        })
    except Exception as e:
        print(e)
        return JsonResponse({
            'status': 'Error',
            'result': 'Something went wrong'
        })