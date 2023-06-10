from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CATEGORIA)
admin.site.register(PRODUCTO)
admin.site.register(INGREDIENTE)
admin.site.register(TIPO_PAGO)
admin.site.register(ORDEN_PEDIDO)
admin.site.register(PRODUCTO_ORDEN)



