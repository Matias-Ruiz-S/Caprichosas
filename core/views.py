from django.shortcuts import redirect, render
from  .carro  import Carro
from .forms import *
from .models import Categoria,Producto,Ingrediente
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.error.transbank_error import TransbankError


# INDEX funciones
#Muestra la pagina principal
def home(request):  
    cat  = Categoria.objects.filter(is_activo=True)  
    producto  = Producto.objects.filter(is_activo=True)
    contex = {'productos':producto,'categorias':cat}
    return render(request, 'core/index.html',contex)

# Muestra los productos filtrados por categorias
def listar(request,slug):  
    cat  = Categoria.objects.get(slug=slug)  
    categorias = Categoria.objects.filter(is_activo=True)  
    producto  = Producto.objects.filter(is_activo=True,categoria=cat)
    contex = {'productos':producto,'categorias':categorias}
    return render(request, 'core/list.html',contex)


def template(request):    
    return render(request, 'core/template.html')


def detalleProducto(request,id): 
    producto  = Producto.objects.filter(is_activo=True,Barcode=id)
    contex = {'detalle': producto}   

    return render(request, 'core/detalle.html',contex)



# CRUD funciones

# Render crud  y trae todos los productos y categorias
def crud (request):
    producto  = Producto.objects.all()
    ingrediente  = Ingrediente.objects.all()
    categoria  = Categoria.objects.all()
    contex = {'ingredientes' : ingrediente,'productos':producto,'categorias':categoria}
    return render(request,'core/crud.html',contex)

# Agrega un nuevo producto
def Productoform(request):
    datos = {'form': ProductoForm()}
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
            
    return render(request, 'core/agregarProducto.html', datos)

# Agrega una nueva categoria
def agreCategoria (request): 
    datos = {'form': CategoriaForm()}
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
    return render(request,'core/agreCategoria.html',datos)

# Agrega un nuevo ingrediente
def agreIngrediente (request):
    datos = {'form': IngredienteForm()}
    if request.method == 'POST':
        formulario = IngredienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
    return render(request,'core/agreIngrediente.html',datos)

# CRUD funciones modificar

def Mod_Producto(request, Barcode):
    producto = Producto.objects.get(Barcode=Barcode)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/modProducto.html', datos)



# CRUD funciones delete

def delete_Producto(request,id):
    producto = Producto.objects.get(Barcode=id)
    producto.delete()
    return redirect(to="crud")

def delete_ingrediente(id):
    producto = Ingrediente.objects.get(SKU=id)
    producto.delete()
    return redirect(to="crud")

def delete_categoria(slug):
    producto = Categoria.objects.get(slug=slug)
    producto.delete()
    return redirect(to="crud")

def asigIngre(request):
    datos = {'form': AsignarIngreForm}
    if request.method == 'POST':
        formulario = AsignarIngreForm(request.POST)
        if formulario.is_valid():
            pass

    return render(request,'core/asigIngre.html',datos)



# carroo

def agregar_producto(request, producto_id):
    carro=Carro(request)
    producto= Producto.objects.get(Barcode=producto_id)
    carro.agregar(producto)
    return redirect("home")

def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto)
    return redirect("home")

def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiar_carro()
    return redirect("home")

def restar(request, producto_id):
    carro=Carro(request)
    producto= Producto.objects.get(Barcode=producto_id)
    carro.restar_producto(producto)
    return redirect("home")


def pagar(request,total):
    total = total
    buy_order = str(1)
    session_id = str(1)
    return_url = 'http://127.0.0.1:8000/terminar/'

    amount = total
    total= str('{:,.0f}'.format(total).replace(",", "@").replace(".", ",").replace("@", "."))
    try:
        response = Transaction().create(buy_order, session_id, amount, return_url)
        context ={'total':total,"response":response}
        print(amount)

        return render(request, 'core/pagar.html', context) 
    except TransbankError as e:
        print(e.message)
        print(e.message)
        error =e.message
        context ={'total':total,"error":error,}
        return render(request, 'core/pagar.html', context)
    

def terminar(request):
    token = request.GET.get("token_ws")
    try:
        response = Transaction().commit(token) 
        return render(request, 'core/terminar.html',{"token": token,"response": response})
    except TransbankError as e:
        error =e.message
        print(e.message)
        print(token)
        return render(request, 'core/terminar.html', {"error":error})