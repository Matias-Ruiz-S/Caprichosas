from django.shortcuts import redirect, render
from  .carro  import Carro
from .forms import *
from .models import CATEGORIA,PRODUCTO,INGREDIENTE, BOLETA, ORDEN_PEDIDO, PRODUCTO_ORDEN, TIPO_PAGO, STATUS, TIPO_DESPACHO
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.error.transbank_error import TransbankError
from django.core.paginator import Paginator
from datetime import datetime


# INDEX funciones
#Muestra la pagina principal
def home(request):
    cat = CATEGORIA.objects.exclude(nombre='Arma Tu')  # TODAS las categorias menos Arma tu
    catArma = CATEGORIA.objects.get(nombre='Arma Tu')  # trae solo cat armatu
    producto = PRODUCTO.objects.filter(is_activo=True)
    productoArma = PRODUCTO.objects.filter(is_activo=True, categoria=catArma)
    contex = {'productos': producto,
              'categorias': cat,
              'Arma': catArma,
              'armalist': productoArma}
    return render(request, 'core/Web/list.html', contex)

# Muestra los productos filtrados por categorias
def listar(request,slug):  
  
    categorias = CATEGORIA.objects.exclude(nombre = 'Arma Tu') # TODAS las categorias menos Arma tu 
    catArma = CATEGORIA.objects.get(nombre = 'Arma Tu') # trae solo cat armatu 
    productoArma  = PRODUCTO.objects.filter(is_activo=True,categoria=catArma)
    #filtra los productos en la categoria
    cat  = CATEGORIA.objects.get(slug=slug)
    producto  = PRODUCTO.objects.filter(is_activo=True,categoria=cat)

    contex = {'productos':producto,'categorias':categorias, 'Arma':catArma,
              'armalist':productoArma}
    
    return render(request, 'core/Web/list.html',contex)


def template(request):    
    return render(request, 'core/template.html')


def detalleProducto(request,id): 
    producto  = PRODUCTO.objects.filter(is_activo=True,Barcode=id)
    contex = {'detalle': producto}   

    return render(request, 'core/detalle.html',contex)

# CRUD funciones

# LISTAS 
def Lcategorias(request):
    categoria  = CATEGORIA.objects.all() 
    context = { 'categorias' : categoria}
    return render(request,'core/Crud/Listas/Lcategorias.html',context)

def Lproductos(request):
    productos = PRODUCTO.objects.all()
    paginator = Paginator(productos, 15)  # 15 productos por página

    page_number = request.GET.get('page')
    productos = paginator.get_page(page_number)

    context = {'productos': productos}
    return render(request, 'core/Crud/Listas/Lproductos.html', context)

def Lingredientes(request):
    ingredientes = INGREDIENTE.objects.all()
    paginator = Paginator(ingredientes, 10)  # 15 ingredientes por página

    page_number = request.GET.get('page')
    ingredientes = paginator.get_page(page_number)

    context = {'ingredientes': ingredientes}
    return render(request, 'core/Crud/Listas/Lingredientes.html', context)




def agregar_boleta(request):
    datos = {'form': BoletaForm()}
    if request.method == 'POST':
        request.POST = request.POST.copy()
        request.POST['nombre_cliente'] = request.POST['cliente']

        #modificar
        current_datetime = datetime.now()
        number = int(current_datetime.strftime('%Y%m%d%H%M%S'))
        request.POST['id'] = number
        request.POST['status'] = 1

        formulario = BoletaForm(request.POST)

        


        formulario = orderForm(request.POST)
        if(formulario.is_valid()):
            print("VALID")
        else:
            print(formulario.errors)
    

    cat = CATEGORIA.objects.exclude(nombre='Arma Tu')  # TODAS las categorias menos Arma tu
    catArma = CATEGORIA.objects.get(nombre='Arma Tu')  # trae solo cat armatu
    producto = PRODUCTO.objects.filter(is_activo=True)
    productoArma = PRODUCTO.objects.filter(is_activo=True, categoria=catArma)
    contex = {'productos': producto,
              'categorias': cat,
              'Arma': catArma,
              'armalist': productoArma}
    return render(request, 'core/Web/index.html', contex)



# Agrega un nuevo producto
def Productoform(request):
    datos = {'form': ProductoForm()}
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
            return redirect('Lproductos')
    return render(request, 'core/Crud/agregarProducto.html', datos)

# Agrega una nueva categoria
def agreCategoria (request): 
    datos = {'form': CategoriaForm()}
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
            return redirect('Lcategorias')
    return render(request,'core/Crud/agreCategoria.html',datos)

# Agrega un nuevo ingrediente
def agreIngrediente (request):
    datos = {'form': IngredienteForm()}
    if request.method == 'POST':
        formulario = IngredienteForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados correctamente"
        return redirect('Lingredientes')
    return render(request,'core/Crud/agreIngrediente.html',datos)

# CRUD funciones modificar

def Mod_Producto(request, Barcode):
    producto = PRODUCTO.objects.get(Barcode=Barcode)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados correctamente"
    return render(request, 'core/Crud/modProducto.html', datos)



# CRUD funciones delete

def delete_Producto(request,id):
    producto = PRODUCTO.objects.get(Barcode=id)
    producto.delete()
    return redirect(to="crud")

def delete_ingrediente(id):
    producto = INGREDIENTE.objects.get(SKU=id)
    producto.delete()
    return redirect(to="crud") 
   

def delete_categoria(slug):
    producto = CATEGORIA.objects.get(slug=slug)
    producto.delete()
    return redirect(to="crud")


def asigIngre(request):
    datos = {'form': AsignarIngreForm}
    if request.method == 'POST':
        formulario = AsignarIngreForm(request.POST)
        if formulario.is_valid():
            pass

    return render(request,'core/Crud/asigIngre.html',datos)



# carroo
 
def agregar_producto(request,producto_id):
    carro=Carro(request)
    producto= PRODUCTO.objects.get(Barcode=producto_id)
    a = request.path
    print(a)
    carro.agregar(producto)
    print(carro)
    
    return redirect('listar' , producto.categoria.slug)



def eliminar_producto(request, producto_id):
    carro=Carro(request)
    producto=PRODUCTO.objects.get(Barcode=producto_id)
    carro.eliminar(producto)
    return redirect('listar' , producto.categoria.slug)

def limpiar_carro(request, producto_id):
    carro=Carro(request)
    carro.limpiar_carro()
    producto= PRODUCTO.objects.get(Barcode=producto_id)
    return redirect('listar' , producto.categoria.slug)

def restar(request, producto_id):
    carro=Carro(request)
    producto= PRODUCTO.objects.get(Barcode=producto_id)
    carro.restar_producto(producto)
    return redirect('listar' , producto.categoria.slug)


def pagar(request,total):
    print(total)
    total = total
    buy_order = str(1)
    session_id = str(1)
    return_url = 'http://127.0.0.1:8000/terminar/'

    tipo_pago = TIPO_PAGO.objects.filter()
    tipo_despacho = TIPO_DESPACHO.objects.filter()
    status = STATUS.objects.filter()

    print(tipo_despacho)
    
    amount = total
    total= str('{:,.0f}'.format(total).replace(",", "@").replace(".", ",").replace("@", "."))
    try:
        response = Transaction().create(buy_order, session_id, amount, return_url)
        context = {'total':total,"response":response, 'tipo_pago': tipo_pago, 'tipo_despacho': tipo_despacho, 'status': status}
       

        return render(request, 'core/Carrito/pagar.html', context) 
    except TransbankError as e:
        print(e.message)
        print(e.message)
        error =e.message
        context ={'total':total,"error":error,  'tipo_pago': tipo_pago, 'tipo_despacho': tipo_despacho , 'status': status}
        return render(request, 'core/Carrito/pagar.html', context)
    

def terminar(request):
    token = request.GET.get("token_ws")
    try:
        response = Transaction().commit(token) 
        return render(request, 'core/Carrito/terminar.html',{"token": token,"response": response})
    except TransbankError as e:
        error =e.message
        print(e.message)
        print(token)
        return render(request, 'core/Carrito/terminar.html', {"error":error})
    
from django.utils import timezone

def agregar_boleta(request):
    if request.method == 'POST':

        try:
            id = int(timezone.now().strftime('%Y%m%d%H%M%S'))
            orden = generar_orden(request.POST, id)
            orden.save()

            boleta = generar_boleta(request.POST, id)
            boleta.save()
            
        except KeyError as e:
            print(f"Falta un valor necesario en los datos POST: {e}")

    cat = CATEGORIA.objects.exclude(nombre='Arma Tu')  # TODAS las categorias menos Arma tu
    catArma = CATEGORIA.objects.get(nombre='Arma Tu')  # trae solo cat armatu
    producto = PRODUCTO.objects.filter(is_activo=True)
    productoArma = PRODUCTO.objects.filter(is_activo=True, categoria=catArma)
    contex = {'productos': producto,
            'categorias': cat,
            'Arma': catArma,
            'armalist': productoArma}
    return render(request, 'core/Web/index.html', contex)

def generar_orden(data, id):
    orden = ORDEN_PEDIDO()
    orden.id = id
    orden.nombre_cliente = data['cliente']
    orden.ubicacion = data['ubicacion']
    
    tipo_pago_id = int(data['tipo_pago'])
    tipo_pago = TIPO_PAGO.objects.get(id=tipo_pago_id)
    orden.tipo_pago = tipo_pago

    tipo_despacho_id = int(data['tipo_despacho'])
    tipo_despacho = TIPO_DESPACHO.objects.get(id=tipo_despacho_id)
    orden.tipo_despacho = tipo_despacho

    status_id = int(data['status'])
    status = STATUS.objects.get(id=status_id)
    orden.status = status

    return orden

def generar_boleta(data, id):
    boleta = BOLETA()
    boleta.id = id
    boleta.cliente = data['cliente']
    boleta.descripcion = data['descripcion']

    num_order =  ORDEN_PEDIDO.objects.get(id=id)
    boleta.num_order = num_order
    
    total_str = data['total']
    total_no_point = total_str.replace(".", "")
    boleta.total = int(total_no_point)

    return boleta


def viewVendedor(request):
    ordenes = ORDEN_PEDIDO.objects.exclude(status = 1)
    context = {
        'orders': ordenes
    }
    return render(request,'core/Crud/Vendedor/VenView.html',context)


def detalleOrder(request,num):
    ordenes = ORDEN_PEDIDO.objects.exclude(status = 1)
    detalle = PRODUCTO_ORDEN.objects.filter(id_orden= num)

    context = {
        'orders': ordenes,
        'detalle':detalle
    }
    return render(request,'core/Crud/Vendedor/detallePedido.html',context)
