from django.urls import path

from .views import *


urlpatterns = [
    path("", home,name="home"),
    path("template", template,name="template"),
    path("nuevo-producto", Productoform,name="Productoform"),
    path("crud", crud,name="crud"),
    path("nueva-categoria", agreCategoria,name="agreCategoria"),
    path("nuevo-ingrediente", agreIngrediente,name="agreIngrediente"),
    path("Seleccion-de-ingredientes", SelecIngre,name="SelecIngre"),
    path("armapizza", armapizza,name="armapizza"),
    path("armapan", armapan,name="armapan"),
]

