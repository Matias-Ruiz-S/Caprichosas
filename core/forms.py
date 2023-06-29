import email
from msilib.schema import Class
from django import forms
from django.forms import ModelForm
from .models import PRODUCTO,CATEGORIA,INGREDIENTE,INGREDIENTE_PRODUCTO, BOLETA, ORDEN_PEDIDO




class ProductoForm (ModelForm):
    class Meta :
        model = PRODUCTO
        fields= ['Barcode','nombre','precio','stock','categoria','imgurl']
      

class CategoriaForm (ModelForm):
    class Meta :
        model = CATEGORIA
        fields= ['nombre']
        exclude = ['is_activo']

class IngredienteForm (ModelForm):
    class Meta :
        model = INGREDIENTE
        fields= '__all__'

class AsignarIngreForm (ModelForm):
    class Meta :
        model = INGREDIENTE_PRODUCTO
        fields= '__all__'

class BoletaForm (ModelForm):
    class Meta :
        model = BOLETA
        fields= '__all__'

class orderForm (ModelForm):
    class Meta :
        model = ORDEN_PEDIDO
        fields= '__all__'


class pagoForm (forms.Form):
    cliente = forms.CharField()
    total = forms.IntegerField()
    num_order = forms.IntegerField()
    ubicacion = forms.CharField()
    tipo_despacho = forms.CharField()
    tipo_pago = forms.CharField()
    status = forms.CharField()
    descripcion = forms.CharField()
  