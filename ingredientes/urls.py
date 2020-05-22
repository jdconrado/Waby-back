from django.urls import path

from . import views

urlpatterns = [
    path('crear', views.crear_ingrediente, name='crear_ingrediente'),
    path('getall', views.get_allIngredientes, name='get_allIngredientes'),
    path('actualizar/<pk>', views.actualizar_ingrediente, name='actualizar_ingrediente'),
    path('eliminar/<pk>', views.eliminar_ingrediente, name='eliminar_ingrediente'),
    path('getlista/<pedidoId>', views.get_allListPedido, name='get_allListPedido'),
    path('geting/<pk>',views.getIng, name='getIng')
]