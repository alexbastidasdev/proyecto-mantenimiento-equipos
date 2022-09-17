from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('equipos', EquipoViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('contacto/', contacto, name='contacto'),
    path('privacidad/', privacidad, name='privacidad'),
    path('equipos/', listar_equipos, name='listar_equipos'),
    path('agregar-equipo/', agregar_equipo, name='agregar_equipo'),
    path('editar-equipo/<id>/', editar_equipo, name='editar_equipo'),
    path('eliminar-equipo/<id>/', eliminar_equipo, name='eliminar_equipo'),
    path('tecnicos/', tecnicos, name='tecnicos'),
    path('mantenimientos/', mantenimientos, name='mantenimientos'),
    path('registro/', registro, name='registro'),
    path('api/', include(router.urls)),
]
