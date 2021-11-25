from django import forms
from django.forms import ModelForm
from .models import Producto
from .models import Usuario
from .models import Agenda
from .models import Citas
from .models import Pago



##crearemos nuestra clase para el formulario desde la base de datos

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields =["cod_producto", "nombre", "precio", "stock", "descripcion", "foto"]
        
class CitasForm(ModelForm):
    class Meta:
        model = Citas
        fields =["idagenda", "run", "hora", "estado"]
                