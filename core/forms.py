import email
from msilib.schema import Class
from django import forms
from django.forms import ModelForm
from .models import Producto,Categoria,Ingrediente




class ProductoForm (ModelForm):
    class Meta :
        model = Producto
        fields= ['Barcode','nombre','precio','stock','categoria']
      

class CategoriaForm (ModelForm):
    class Meta :
        model = Categoria
        fields= '__all__'

class IngredienteForm (ModelForm):
    class Meta :
        model = Ingrediente
        fields= '__all__'

