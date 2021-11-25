from django.db import models

# Create your models here.


#MODELO USUARIO
class Usuario(models.Model):
    run=models.CharField(max_length=10, primary_key=True, verbose_name='Rut')
    nombre=models.CharField(max_length=20, verbose_name='Nombre')
    email=models.CharField(max_length=50, verbose_name='Email')
    contraseña=models.CharField(max_length=50, verbose_name='Contraseña')
    tipo=models.CharField(max_length=50, verbose_name='Tipousuario')
    def __str__(self):
        return self.run
    
#MODELO AGENDA_MEDICO
class Agenda(models.Model):
    idagenda=models.IntegerField(primary_key=True, verbose_name='Id Agenda')
    hora=models.CharField(max_length=50, verbose_name='Hora')
    medicoespecialidad=models.CharField(null=True, max_length=50, verbose_name='Medico y especialidad')
    run=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.run 
    
#MODELO CITAS_PACIENTE
class Citas(models.Model):
    run=models.CharField(max_length=10, verbose_name='Rut Cliente')  
    hora=models.CharField(max_length=50, verbose_name='Hora') 
    estado=models.CharField(max_length=50, verbose_name='Estado')
    idcita=models.IntegerField(primary_key=True, verbose_name='Id Cita') 
    
    def __str__(self):
        return self.idagenda 
    
#MODELO PAGO
class Pago(models.Model):
    idpago=models.IntegerField(primary_key=True, verbose_name='Id pago')
    run=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    comprobante=models.CharField(max_length=50, verbose_name='Comprobante')
    precio=models.IntegerField(verbose_name='Precio')
    
    def __str__(self):
        return self.run
    
#MODELO INFORME
class Informes(models.Model):
    idinforme=models.IntegerField(primary_key=True, verbose_name='Id informe')
    idpago=models.ForeignKey(Pago, on_delete=models.CASCADE)
    tipoinforme=models.CharField(max_length=50, verbose_name='tipo informe')
    
    def __str__(self):
        return self.idinforme           

#MODELO CLIENTE
class Cliente(models.Model):
    run=models.CharField(max_length=10, primary_key=True, verbose_name='Rut Cliente')
    nombre=models.CharField(max_length=20, verbose_name='Nombre Cliente')
    apellido=models.CharField(max_length=20, verbose_name='Apellido Cliente')
    email=models.CharField(max_length=50, verbose_name='Email')
    contraseña=models.CharField(max_length=50, verbose_name='Contraseña')
    
    def __str__(self):
        return self.run

#MODELO CARRO
class Carro(models.Model):
    cod_carro=models.IntegerField(primary_key=True, verbose_name='Codigo de Carro')
    fecha_creacion=models.DateField(auto_now=False, auto_now_add=False, verbose_name='Fecha de Creacion')
    run=models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.run    


#Modelo Producto
class Producto(models.Model):
    cod_producto=models.IntegerField(primary_key=True,verbose_name='Codigo de Producto')
    nombre=models.CharField(max_length=20, verbose_name='Nombre de Producto')
    precio=models.IntegerField(verbose_name='Precio')
    stock=models.IntegerField(verbose_name='Stock')
    descripcion=models.CharField(max_length=1000, verbose_name='Descripcion')
    foto=models.ImageField(null=True, blank=True, verbose_name='Foto Producto')
    
    def __int__(self):
        return self.cod_producto


    
#Modelo Pruducto Carro

class Producto_Carro(models.Model):
    cod_producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    cod_carro=models.ForeignKey(Carro, on_delete=models.CASCADE)
    precio_venta=models.IntegerField(verbose_name='Precio de Venta')
    cantidad=models.IntegerField(verbose_name='Cantidad')
    
    def __int__(self):
        return self.cantidad

    