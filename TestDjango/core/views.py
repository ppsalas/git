from django.shortcuts import render, redirect
from .models import Producto
from .models import Usuario
from .models import Citas
from .models import Agenda
from .models import Pago
from .models import Informes
from .forms import ProductoForm
from .forms import CitasForm


# Create your views here.




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

    return render(request, 'core/pinturadestacada1.html')


def pinturadestacada2(request):
    return render(request, 'core/pinturadestacada2.html')


def pinturadestacada3(request):
    return render(request, 'core/pinturadestacada3.html')


def registrar(request):
    return render(request, 'core/registrar.html')


def reservarhora(request):
    # accediendo al objeto que contiene los datos de la base de datos
    # el metodo all traera todas las horas que estan en la tabla
    agenda = Agenda.objects.all()
    # ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'agenda': agenda
    }
    # ahora lo agregamos para que se envie al templateee
    return render(request, 'core/reservarhora.html', datos)

def confirmarhoraa(request):
    # el view sera el responsable de entregar el form al template
    datos = {'form': CitasForm}
    # verificamos que peticion sean post y rescatamos los datos
    if request.method == 'POST':
        # con request recuperamos los datos del formulario
        formulario = CitasForm(request.POST)
        idagenda=request.POST.get("idagenda")
        # validamos el formulario
        if formulario.is_valid:
            if not validaAgenda(idagenda):
                # guardamos en la base de datos
                formulario.save()
                # y mostramos un mensaje
                datos['mensaje'] = "Hora Reservada correctamente"
            else:
                datos['mensaje']="Ya existe un registro asociado a ese codigo"    + cod_producto  
    return render(request, 'core/confirmarhoraa.html', datos)

def validaAgenda(idagenda):
    existe=Agenda.objects.filter(idagenda=idagenda).exists()
    return existe

def confirmarhora(request, id):

    # el id es el identificador de la tabla productos
    # buscando los datos en la base de datos
    # buscamos por codigo que llega como dato en la url
    agenda = Agenda.objects.get(idagenda=id)
    # ahora le entregamos los datos del producto al formulario
    datos = {'form': CitasForm(instance=agenda)}

    # verificamos que la peticion sean post y rescatamos los datos
    if request.method == 'POST':
        # con request recuperamos los datos del formulario y le agregamos el id modificar
        formulario = CitasForm(data=request.POST, instance=agenda)
        # validamos el formulario
        if formulario.is_valid:
            # ahora guardamosen la base datos
            formulario.save()
            # enviamos mensaje
            datos['mensaje'] = "Hora Tomada Correctamente "

    return render(request, 'core/confirmarhora.html', datos)

def form_del_agenda(request,id):
    #el id es el identificador de la tabla productos
    #buscando los datos en la base de datos
    productos=Producto.objects.get(cod_producto=id)
    #eliminamos el producto del id buscado
    productos.delete()
    #ahora redirigmos a la pagina con el listado
    return redirect(to="listado")

def listado(request):
    # accediendo al objeto que contiene los datos de la base de datos
    # el metodo all traera todos los productos que estan en la tabla
    productos = Producto.objects.all()
    # ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'productos': productos
    }
    # ahora lo agregamos para que se envie al templateee
    return render(request, 'core/listado.html', datos)


def form_producto(request):
    # el view sera el responsable de entregar el form al template
    datos = {'form': ProductoForm}
    # verificamos que peticion sean post y rescatamos los datos
    if request.method == 'POST':
        # con request recuperamos los datos del formulario
        formulario = ProductoForm(request.POST)
        cod_producto=request.POST.get("cod_producto")
        # validamos el formulario
        if formulario.is_valid:
            if not validaProducto(cod_producto):
                # guardamos en la base de datos
                formulario.save()
                # y mostramos un mensaje
                datos['mensaje'] = "Guardado correctamente"
            else:
                datos['mensaje']="Ya existe un registro asociado a ese codigo"    + cod_producto  
    return render(request, 'core/form_producto.html', datos)

def validaProducto(cod_producto):
    existe=Producto.objects.filter(cod_producto=cod_producto).exists()
    return existe

def form_mod_producto(request, id):

    # el id es el identificador de la tabla productos
    # buscando los datos en la base de datos
    # buscamos por codigo que llega como dato en la url
    productos = Producto.objects.get(cod_producto=id)
    # ahora le entregamos los datos del producto al formulario
    datos = {'form': ProductoForm(instance=productos)}

    # verificamos que la peticion sean post y rescatamos los datos
    if request.method == 'POST':
        # con request recuperamos los datos del formulario y le agregamos el id modificar
        formulario = ProductoForm(data=request.POST, instance=productos)
        # validamos el formulario
        if formulario.is_valid:
            # ahora guardamosen la base datos
            formulario.save()
            # enviamos mensaje
            datos['mensaje'] = "Modificado Correctamente"

    return render(request, 'core/form_mod_producto.html', datos)




def form_del_producto(request,id):
    #el id es el identificador de la tabla productos
    #buscando los datos en la base de datos
    productos=Producto.objects.get(cod_producto=id)
    #eliminamos el producto del id buscado
    productos.delete()
    #ahora redirigmos a la pagina con el listado
    return redirect(to="listado")


def consume_api(request):
    productos = Producto.objects.all()
    # ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'productos': productos
    }
    # ahora lo agregamos para que se envie al templateee
    return render(request, 'core/consume_api.html', datos)


def coleccioncompleta(request):
    productos = Producto.objects.all()
    # ahora crearemos una variable que le pase los datos del producto al template
    datos = {
        'productos': productos
    }
    # ahora lo agregamos para que se envie al templateee
    return render(request, 'core/coleccioncompleta.html', datos)
