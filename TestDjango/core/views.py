from django.shortcuts import render

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
    return render(request, 'core/pinturadestacada1.html')

def pinturadestacada2(request):
    return render(request, 'core/pinturadestacada2.html')

def pinturadestacada3(request):
    return render(request, 'core/pinturadestacada3.html')

def registrar(request):
    return render(request, 'core/registrar.html')




class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()
        


def subirobra(request):
    
    lista=["Lasaña","Charquican","Porotos Granados"]
    
    hijo=Persona("Fernando Rivera", "4")
    
    contexto={"nombre":"Jose Salas", "comidas":lista, "hijo":hijo}
    
    return render(request, 'core/subirobra.html', contexto)




