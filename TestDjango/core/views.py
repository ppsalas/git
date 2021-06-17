from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.


def coleccioncompleta(request):
    return render(request, 'core/coleccioncompleta.html')


def Contacto(request):
    return render(request, 'core/Contacto.html')


def cuadrosgrabados(request):
    return render(request, 'core/cuadrosgrabados.html')


def equipo(request):
    return render(request, 'core/equipo.html')


def formatopequeño(request):
    return render(request, 'core/formatopequeño.html')


def index(request):
    return render(request, 'core/index.html')


def iniciarsesion(request):
    return render(request, 'core/iniciarsesion.html')


def pinturadestacada1(request):
    # accediendo al objeto que contiene los datos de la base de datos
    # el metodo all traera todos los productos que estan en la tabla
    productos = Producto.objects.all()
    # ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'productos': productos
    }
    # ahora lo agregamos para que se envie al templateee
    return render(request, 'core/pinturadestacada1.html', datos)


def pinturadestacada2(request):
    return render(request, 'core/pinturadestacada2.html')


def pinturadestacada3(request):
    return render(request, 'core/pinturadestacada3.html')


def registrar(request):
    return render(request, 'core/registrar.html')


def form_producto(request):
    # el view sera el responsable de entregar el form al template
    datos = {'form': ProductoForm}
    # verificamos que peticion sean post y rescatamos los datos
    if request.method == 'POST':
        # con request recuperamos los datos del formulario
        formulario = ProductoForm(request.POST)
        # validamos el formulario
        if formulario.is_valid:
            # guardamos en la base de datos
            formulario.save()
            # y mostramos un mensaje
            datos['mensaje'] = "Guardado correctamente"
    return render(request, 'core/form_producto.html', datos)


def form_mod_producto(request, id):

    # el id es el identificador de la tabla productos
    # buscando los datos en la base de datos
    # buscamos por codigo que llega como dato en la url
    producto = Producto.objects.get(cod_producto=id)
    # ahora le entregamos los datos del producto al formulario
    datos = {'form': ProductoForm(instance=producto)}

    # verificamos que la peticion sean post y rescatamos los datos
    if request.method == 'POST':
        # con request recuperamos los datos del formulario y le agregamos el id modificar
        formulario = ProductoForm(data=request.POST, instance=producto)
        # validamos el formulario
        if formulario.is_valid:
            # ahora guardamosen la base datos
            formulario.save()
            # enviamos mensaje
            datos['mensaje'] = "Modificado Correctamente"

    return render(request, 'core/form_mod_producto.html', datos)


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        super().__init__()


def subirobra(request):

    lista = ["Lasaña", "Charquican", "Porotos Granados"]

    hijo = Persona("Fernando Rivera", "4")

    contexto = {"nombre": "Jose Salas", "comidas": lista, "hijo": hijo}

    return render(request, 'core/subirobra.html', contexto)


def form_del_producto(request,id):
    #el id es el identificador de la tabla productos
    #buscando los datos en la base de datos
    producto=Producto.objects.get(cod_producto=id)
    #eliminamos el producto del id buscado
    producto.delete()
    #ahora redirigmos a la pagina con el listado
    return redirect(to="pinturadestacada1")