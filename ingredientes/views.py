from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Ingrediente,ListaIngredientes
from .serializers import IngredienteSerializer,ListaIgnSerializer
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

@csrf_exempt
@require_http_methods(['GET'])
def get_allIngredientes(request):
    try:
        ingredientes = Ingrediente.objects.all()
        serializer = IngredienteSerializer(ingredientes, many=True)
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
        ingrediente = Ingrediente.objects.get(pk=pk)
        serializer = IngredienteSerializer(ingrediente, data=body["data"] )
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

@csrf_exempt
@require_http_methods(['DELETE'])
def eliminar_ingrediente(request, pk):
    try:
        ingrediente = Ingrediente.objects.get(pk=pk)
        ingrediente.delete()
        return JsonResponse({
            'status':'Succesful',
            'result': 'Ingrediente eliminado.'
        })
    except:
        return JsonResponse({
            'status':'Error',
            'result':'Hubo un error al eliminar el ingrediente.'
        })


@csrf_exempt
@require_http_methods(['GET'])
def get_allListPedido(request, pedidoId):
    try:
        li = ListaIngredientes.objects.filter(pedidoId=pedidoId)
        serializer = ListaIgnSerializer(li, many=True)
        return JsonResponse({
                'status':'Succesful',
                'result': serializer.data
            })
    except:
        return JsonResponse({
                'status':'Error',
                'result':'Error al extraer la lista de ingredientes.'
            })

@csrf_exempt
@require_http_methods(['GET'])
def getIng(request,pk):
    try:
        ing = Ingrediente.objects.get(pk=pk)
        serializer=IngredienteSerializer(ing)
        return JsonResponse({
            'status': 'Succesful',
            'result': serializer.data
        })
    except:
        return JsonResponse({
            'status': 'Error',
            'result': None
        })
