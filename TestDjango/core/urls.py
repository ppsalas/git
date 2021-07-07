from django.urls import path
from .views import index, coleccioncompleta, Contacto, cuadrosgrabados, equipo, formatopequeño, iniciarsesion, pinturadestacada1, pinturadestacada2, pinturadestacada3, registrar, listado, form_producto, form_mod_producto, form_del_producto, lista_productos, detalle_producto



urlpatterns = [
    path('', index,name="index"),
    path('coleccion_completa', coleccioncompleta,name="coleccioncompleta"),
    path('contacto', Contacto,name="Contacto"),
    path('cuadros_grabados', cuadrosgrabados,name="cuadrosgrabados"),
    path('equipos', equipo,name="equipo"),
    path('formato_pequeño', formatopequeño,name="formatopequeño"),
    path('iniciar_sesion', iniciarsesion,name="iniciarsesion"),
    path('pintura_destacada1', pinturadestacada1,name="pinturadestacada1"),
    path('pintura_destacada2', pinturadestacada2,name="pinturadestacada2"),
    path('pintura_destacada3', pinturadestacada3,name="pinturadestacada3"),
    path('registrarse', registrar,name="registrar"),
    path('listado', listado,name="listado"),
    path('form-producto', form_producto, name="form_producto"),
    path('form-mod-producto/<id>', form_mod_producto, name="form_mod_producto"),
    path('form-del-producto/<id>', form_del_producto, name="form_del_producto"),
    path('lista_productos', lista_productos, name="lista_productos"),
    path('detalle_producto/<id>', detalle_producto, name="detalle_producto"),  
]



