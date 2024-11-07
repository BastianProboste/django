
from django.urls import path

from .views import *

urlpatterns = [
    path('', listar_usuarios, name='listar_usuarios'),
    path('nuevo/', crear_usuario, name='crear_usuario'),
    path('editar_usuario/<int:id_usuario>/', editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:id_usuario>/', eliminar_usuario, name='eliminar_usuario'),
]
