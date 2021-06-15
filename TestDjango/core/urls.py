from django.urls import path
from .views import index, coleccioncompleta, Contacto, cuadrosgrabados, equipo, formatopequeño, iniciarsesion, pinturadestacada1, pinturadestacada2, pinturadestacada3, registrar, subirobra 



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
    path('subir_obra', subirobra,name="subirobra"),
]



