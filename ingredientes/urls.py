from django.urls import path

from . import views

urlpatterns = [
    path('crear', views.crear_ingrediente, name='crear_ingrediente')
]