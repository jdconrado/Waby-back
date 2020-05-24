from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Pedido
from .serializers import PedidoSerializer
import json
from django.utils import timezone
from ingredientes.serializers import ListaIgnSerializer, IngredienteSerializer
from ingredientes.models import Ingrediente

# Create your views here.


@csrf_exempt
@require_http_methods(['POST'])
def crear_pedido(request):

    body = JSONParser().parse(request)["data"]
    i = PedidoSerializer(data={
        "especificaciones": body["especificaciones"],
        "precioTotal": body["precioTotal"],
        "estado": body["estado"],
        "userId": body["userId"],
        "fecha_creado": timezone.now()
    })
    try:
        if i.is_valid():
            i.save()
            for relIgn in body["receta"]:
                try:
                    li = ListaIgnSerializer(data={
                        "pedidoId": i.data["id"],
                        "ingred": relIgn["ingId"],
                        "cantidad": relIgn["cantidad"]
                    })
                    if li.is_valid():
                        li.save()
                    else:
                        return JsonResponse({
                            'status': 'No es valido',
                            'valid': li.is_valid(),
                            'result': i.data
                        })
                except:
                    return JsonResponse({
                        'status': 'Error',
                        'result': 'Error al encontrar el ingrediente',
                    })
            return JsonResponse({
                'status': 'Succesful',
                'result': 'Orden creada.'
            })
        else:
            return JsonResponse({
                'status': 'Error',
                'result': 'Los campos no son validos.',
            })
    except:
        return JsonResponse({
            'status': 'Error',
            'result': 'Hubo un error al crear el pedido.'
        })


@csrf_exempt
@require_http_methods(['GET'])
def get_pedidos(request):
    try:
        pedidos = Pedido.objects.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return JsonResponse({
            'status': 'Succesful',
            'result': serializer.data
        })
    except:
        return JsonResponse({
            'status': 'Error',
            'result': 'Error al extraer la lista de pedidos.'
        })


@csrf_exempt
@require_http_methods(['GET'])
def get_userPedidos(request, id2):
    try:
        pedidos = Pedido.objects.filter(userId=id2)
        serializer = PedidoSerializer(pedidos, many=True)
        return JsonResponse({
            'status': 'Succesful',
            'result': serializer.data
        })
    except Exception as e:
        print(e)
        return JsonResponse({
            'status': 'Error',
            'result': 'Error al extraer la lista de pedidos.'
        })