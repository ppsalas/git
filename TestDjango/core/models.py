from django.db import models

# Create your models here.


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
    
    def __str__(self):
        return self.cod_producto


    
#Modelo Pruducto Carro

class Producto_Carro(models.Model):
    cod_producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    cod_carro=models.ForeignKey(Carro, on_delete=models.CASCADE)
    precio_venta=models.IntegerField(verbose_name='Precio de Venta')
    cantidad=models.IntegerField(verbose_name='Cantidad')
    
    def __str__(self):
        return self.cantidad

    