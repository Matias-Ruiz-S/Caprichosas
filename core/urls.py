from django.urls import path

from .views import *


urlpatterns = [
    path("", home,name="home"),
    path("listar/<slug>", listar,name="listar"),
    path("template", template,name="template"),
    path("nuevo-producto", Productoform,name="Productoform"),
    path("crud", crud,name="crud"),
    path("nueva-categoria", agreCategoria,name="agreCategoria"),
    path("nuevo-ingrediente", agreIngrediente,name="agreIngrediente"),
]

