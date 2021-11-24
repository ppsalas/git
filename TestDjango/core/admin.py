from django.contrib import admin
from .models import Cliente, Carro, Producto, Producto_Carro, Usuario, Agenda, Citas, Pago, Informes
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Carro)
admin.site.register(Producto)
admin.site.register(Producto_Carro)
admin.site.register(Usuario)
admin.site.register(Agenda)
admin.site.register(Citas)
admin.site.register(Pago)
admin.site.register(Informes)

