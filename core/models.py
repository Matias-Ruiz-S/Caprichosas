from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class CATEGORIA(models.Model):
    nombre = models.CharField(max_length=50,primary_key=True, verbose_name='nombre de la categoria')
    slug = AutoSlugField(populate_from='nombre')
    is_activo = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.nombre
    
    def change_activo(self):
        if self.is_activo == True:
            self.is_activo == False
        else:
            if self.is_activo == False:
                self.is_activo == True

class PRODUCTO(models.Model):
    Barcode = models.CharField(max_length=50 ,primary_key=True ,verbose_name='Barcode')      
    nombre =  models.CharField(max_length=50 ,verbose_name='nombre')  
    slug = AutoSlugField(populate_from='nombre')    
    precio = models.IntegerField(verbose_name='precio')
    stock = models.IntegerField(verbose_name='stock')
    imgurl = models.CharField(max_length=600,verbose_name='url_img')
    descripcion = models.TextField(max_length=600,verbose_name='descripcion',null=True)
    is_activo = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False)
    categoria = models.ForeignKey(CATEGORIA,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre   
    
    def change_activo(self):
        if self.is_activo == True:
            self.is_activo == False
        else:
            if self.is_activo == False:
                self.is_activo == True

    
class HISTORICO(models.Model):
    producto = models.ForeignKey(PRODUCTO,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.IntegerField()
    fecha= models.DateTimeField(auto_now_add=True)

class INGREDIENTE(models.Model):
    nombre = models.CharField(max_length=50,primary_key=True, verbose_name='nombre')
    slug = AutoSlugField(populate_from='nombre')  
    stock = models.IntegerField(verbose_name='stock')

    def __str__(self) -> str:
        return self.nombre

class INGREDIENTE_PRODUCTO(models.Model):
    union = models.CharField(max_length=100,primary_key=True)
    producto = models.ForeignKey(PRODUCTO,on_delete=models.CASCADE)
    Ingrediente = models.ForeignKey(INGREDIENTE,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.producto, self.Ingrediente

class TIPO_PAGO(models.Model):
    id = models.CharField(max_length=6 ,primary_key=True )      
    nombre =  models.CharField(max_length=50 ,verbose_name='nombre')     

class TIPO_DESPACHO(models.Model):
    id = models.CharField(max_length=6 ,primary_key=True )      
    Tnombre =  models.CharField(max_length=50 ,verbose_name='nombre')     


class STATUS(models.Model):
    id = models.IntegerField( primary_key=True )      
    tipo_estado =  models.CharField( max_length=50 )     


class ORDEN_PEDIDO(models.Model):     
    id =  models.IntegerField( primary_key=True )
    fecha = models.DateTimeField( auto_now_add=True )
    nombre_cliente = models.CharField( max_length=100 )  
    ubicacion = models.CharField( max_length=100 )
    tipo_pago =  models.ForeignKey( TIPO_PAGO,on_delete=models.CASCADE )
    tipo_despacho = models.ForeignKey( TIPO_DESPACHO,on_delete=models.CASCADE )
    status = models.ForeignKey( STATUS,on_delete=models.CASCADE )


class PRODUCTO_ORDEN(models.Model):
    id_orden = models.ForeignKey( ORDEN_PEDIDO,on_delete=models.CASCADE )
    id_producto = models.ForeignKey(PRODUCTO,on_delete=models.CASCADE)


class BOLETA(models.Model):     
    id = models.AutoField( primary_key=True )
    cliente = models.CharField(max_length=100) 
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=150 )
    num_order = models.ForeignKey(ORDEN_PEDIDO, on_delete=models.CASCADE, related_name='boletas')     
    total = models.IntegerField()