from django.urls import path

from .views import *


urlpatterns = [
    path("", home,name="home"),
    path("lista/<slug>", listar,name="listar"),
    path("template", template,name="template"),
    path("nuevo-producto", Productoform,name="Productoform"),
    path("Modificar-producto/<Barcode>", Mod_Producto,name="Mod_Producto"),
    path('agre-producto/<id>',delete_Producto, name="delete_Producto"),
    path("crud", crud,name="crud"),
    path("nueva-categoria", agreCategoria,name="agreCategoria"),
    path("nuevo-ingrediente", agreIngrediente,name="agreIngrediente"),
    path("asig-ingre", asigIngre,name="asigIngre"),
    path("detalle/<id>", detalleProducto,name="detalleProducto"),
    path("agre/<int:producto_id>/", agregar_producto, name="agregar_producto"),
    path("eliminar/<id>/", eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/", restar, name="restar"),
    path("limpiar/<id>/", limpiar_carro, name="limpiar"),
]

