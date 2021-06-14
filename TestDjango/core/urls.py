from django.urls import path
from .views import coleccioncompleta
from .views import Contacto
from .views import cuadrosgrabados
from .views import equipo
from .views import formatopequeño
from .views import index
from .views import iniciarsesion
from .views import pinturadestacada1
from .views import pinturadestacada2
from .views import pinturadestacada3
from .views import registrar
from .views import subirobra


urlpatterns = [
    path('', coleccioncompleta,name="coleccioncompleta"),
]

urlpatterns = [
    path('', Contacto,name="Contacto"),
]

urlpatterns = [
    path('', cuadrosgrabados,name="cuadrosgrabados"),
]

urlpatterns = [
    path('', equipo,name="equipo"),
]

urlpatterns = [
    path('', formatopequeño,name="formatopequeño"),
]

urlpatterns = [
    path('', index,name="index"),
]

urlpatterns = [
    path('', iniciarsesion,name="iniciarsesion"),
]

urlpatterns = [
    path('', pinturadestacada1,name="pinturadestacada1"),
]

urlpatterns = [
    path('', pinturadestacada2,name="pinturadestacada2"),
]

urlpatterns = [
    path('', pinturadestacada3,name="pinturadestacada3"),
]

urlpatterns = [
    path('', registrar,name="registrar"),
]

urlpatterns = [
    path('', subirobra,name="subirobra"),
]

