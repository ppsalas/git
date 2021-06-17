from django.contrib import admin
from .models import Cliente, Carro, Producto, Producto_Carro
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Carro)
admin.site.register(Producto)
admin.site.register(Producto_Carro)


