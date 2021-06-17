from django import forms
from django.forms import ModelForm
from .models import Producto



##crearemos nuestra clase para el formulario desde la base de datos

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields =["cod_producto", "nombre", "precio", "stock", "descripcion", "foto"]