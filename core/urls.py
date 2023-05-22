from django.urls import path

from .views import *


urlpatterns = [
    path("", home,name="home"),
    path("listar/<slug>", listar,name="listar"),
    path("template", template,name="template"),
    path("nuevo-producto", Productoform,name="Productoform"),
    path("Modificar-producto/<Barcode>", Mod_Producto,name="Mod_Producto"),
    path('agre-producto/<id>',delete_Producto, name="delete_Producto"),
    path("crud", crud,name="crud"),
    path("nueva-categoria", agreCategoria,name="agreCategoria"),
    path("nuevo-ingrediente", agreIngrediente,name="agreIngrediente"),
    path("asig-ingre", asigIngre,name="asigIngre"),
]

