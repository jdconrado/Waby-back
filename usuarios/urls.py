from django.urls import path
from . import views

urlpatterns = [
    path('crear', views.crear_usuario, name='crear_usuario'),
    path('login', views.log, name='log'),
    path('logout/<tk>', views.logoutv, name='logoutv'),
    path('getid/<token>', views.getid, name='getid'),
    path('getUser/<idC>', views.getUser, name='getUser'),
    path('update/<idU>', views.updateUser, name='updateUser')
]