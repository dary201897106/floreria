from django.contrib import admin
from django.urls import path
from .views import home,galeria,formulario,quienes,adm,eliminar_flor,login,carrito_compra,ubicacion,cerrar_sesion

urlpatterns = [
    path('',home,name='HOME'),
    path('galeria/',galeria,name='GALE'),
    path('formulario/',formulario,name='FORM'),
    path('quienes_somos/',quienes,name='QUIENES'),
    path('adm_flores/',adm,name='ADM'),
    path('eliminar_flor/<id>/',eliminar_flor,name='ELIMINAR'),
    path('login/',login,name='LOGIN'),
    path('carrito_compra/<id>/',carrito_compra,name='AGREGAR_CARRO'),
    path('ubicacion/',ubicacion,name='UBI'),
    path('cerrar_sesion/',cerrar_sesion,name='LOGOUT'),
]