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
    #CRUD
    path("crud", crud,name="crud"),
    path("crud/Listado-categorias",Lcategorias,name="Lcategorias"),
    path("crud/Listado-productos",Lproductos,name="Lproductos"),
    path("crud/Listado-ingredientes",Lingredientes,name="Lingredientes"),
    #NUEVO-OBJETO CRUD
    path("agre/<int:producto_id>/", agregar_producto, name="agregar_producto"),
    path("nueva-categoria", agreCategoria,name="agreCategoria"),
    path("nuevo-ingrediente", agreIngrediente,name="agreIngrediente"),
    path("nuevo-producto", Productoform,name="Productoform"),
    path("asignar-ingredientes", asigIngre,name="asigIngre"),
    #MODIFICAR PRODUCTOS 
    path("Modificar-producto/<Barcode>", Mod_Producto,name="Mod_Producto"),
    #ELIMINAR OBJETO CRUD
    path("eliminar/<id>/", eliminar_producto, name="eliminar"),
    #Carrito
    path("restar/<int:producto_id>/", restar, name="restar"),
    path("limpiar/<id>/", limpiar_carro, name="limpiar"),
]

