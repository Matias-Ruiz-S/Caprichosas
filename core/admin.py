from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Ingrediente)
admin.site.register(tipoPago)
admin.site.register(Cliente)
admin.site.register(OrdenPedido)
admin.site.register(ListaOrdenPedido)
admin.site.register(Boleta)


