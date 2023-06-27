from django.urls import path

from .views import *


urlpatterns = [
    #WEB
    path("", home, name="home"),
    path("lista/<slug>", listar,name="listar"),
    path("detalle/<id>", detalleProducto,name="detalleProducto"),
    path('agre-producto/<id>',delete_Producto, name="delete_Producto"),
    path("pagar/<int:total>/", pagar,name="pagar"),
    path("terminar/", terminar,name="terminar"),
    path('agregar_boleta/', agregar_boleta, name='agregar_boleta'),
    #CRUD
    path("crud", Lcategorias,name="crud"),
    path("crud/Listado-categorias",Lcategorias,name="Lcategorias"),
    path("crud/Listado-productos",Lproductos,name="Lproductos"),
    path("crud/Listado-ingredientes",Lingredientes,name="Lingredientes"),
    #NUEVO-OBJETO CRUD
    path("nueva-categoria", agreCategoria,name="agreCategoria"),
    path("nuevo-ingrediente", agreIngrediente,name="agreIngrediente"),
    path("nuevo-producto", Productoform,name="Productoform"),
    path("asignar-ingredientes", asigIngre,name="asigIngre"),
    #MODIFICAR PRODUCTOS 
    path("Modificar-producto/<Barcode>", Mod_Producto,name="Mod_Producto"),
    #Carrito
    path("agre/<int:producto_id>", agregar_producto, name="agregar_producto"),
    path("restar/<int:producto_id>/", restar, name="restar"),
    path("limpiar/<int:producto_id>/", limpiar_carro, name="limpiar"),
    path("eliminar/<int:producto_id>/", eliminar_producto, name="eliminar"),
]

