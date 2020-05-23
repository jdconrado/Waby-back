from django.urls import path

from . import views

urlpatterns = [
    path('crear', views.crear_usuario, name='crear_usuario'),
    path('login', views.login, name='login'),
    path('logout', views.logoutv, name='logoutv')
]