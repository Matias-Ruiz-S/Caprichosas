from django.shortcuts import render
from .forms import *
from .models import Categoria,Producto,Ingrediente

def home(request):    
    return render(request, 'core/index.html')

def template(request):    
    return render(request, 'core/template.html')


def Productoform(request):
    datos = {'form': ProductoForm()}
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
            
    return render(request, 'core/agregarProducto.html', datos)


def crud (request):
    producto  = Producto.objects.all()
    ingrediente  = Ingrediente.objects.all()
    categoria  = Categoria.objects.all()
    contex = {'ingredientes' : ingrediente,'productos':producto,'categorias':categoria}
  

    return render(request,'core/crud.html',contex)


def agreCategoria (request): 
    datos = {'form': CategoriaForm()}
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
    return render(request,'core/agreCategoria.html',datos)


def agreIngrediente (request):
    datos = {'form': IngredienteForm()}
    if request.method == 'POST':
        formulario = IngredienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
    return render(request,'core/agreIngrediente.html',datos)


def SelecIngre(request):    
    return render(request, 'core/ingresarIngredientes.html')