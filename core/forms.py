import email
from msilib.schema import Class
from django import forms
from django.forms import ModelForm
from .models import Producto,Categoria,Ingrediente,asigIngrediente




class ProductoForm (ModelForm):
    class Meta :
        model = Producto
        fields= ['Barcode','nombre','precio','stock','categoria','imgurl']
      

class CategoriaForm (ModelForm):
    class Meta :
        model = Categoria
        fields= ['nombre']
        exclude = ['is_activo']

class IngredienteForm (ModelForm):
    class Meta :
        model = Ingrediente
        fields= '__all__'

class AsignarIngreForm (ModelForm):
    class Meta :
        model = asigIngrediente
        fields= '__all__'

