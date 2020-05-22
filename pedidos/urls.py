from django.urls import path

from . import views

urlpatterns = [
    path('crear', views.crear_pedido, name='crear_pedido'),
    path('getall', views.get_pedidos, name='get_pedidos')
]