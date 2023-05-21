from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class Categoria(models.Model):
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

class Producto(models.Model):
    Barcode = models.CharField(max_length=6 ,primary_key=True ,verbose_name='Barcode')      
    nombre =  models.CharField(max_length=50 ,verbose_name='nombre')  
    slug = AutoSlugField(populate_from='nombre')    
    precio = models.IntegerField(verbose_name='precio')
    stock = models.IntegerField(verbose_name='stock')
    imgurl = models.CharField(max_length=600,verbose_name='url_img')
    descripcion = models.TextField(max_length=600,verbose_name='descripcion')
    is_activo = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre   
    
    def change_activo(self):
        if self.is_activo == True:
            self.is_activo == False
        else:
            if self.is_activo == False:
                self.is_activo == True

    

class Ingrediente(models.Model):
    id = models.IntegerField(primary_key=True,verbose_name='IdIngrediente')
    nombre = models.CharField(max_length=50, verbose_name='nombre')
    nomProducto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nombre


class tipoPago(models.Model):
    id = models.CharField(max_length=6 ,primary_key=True ,verbose_name='Barcode')      
    Tnombre =  models.CharField(max_length=50 ,verbose_name='nombre')     

class Cliente(models.Model):     
    nombre =  models.CharField(max_length=50 ,primary_key=True,verbose_name='nombre')     
    ubicacion =  models.CharField(max_length=50 ,verbose_name='ubicacion')     
 

class OrdenPedido(models.Model):     
    id =  models.IntegerField(primary_key=True,verbose_name='id')
    fecha =  models.CharField(max_length=50 ,verbose_name='apellido')
    nomCliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)    
    tipoPago = models.ForeignKey(tipoPago,on_delete=models.CASCADE)


class ListaOrdenPedido(models.Model):
    id_orden = models.ForeignKey(OrdenPedido,on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto,on_delete=models.CASCADE)


class Boleta(models.Model):     
    id =  models.IntegerField(primary_key=True,verbose_name='id')
    id_orden = models.ForeignKey(OrdenPedido,on_delete=models.CASCADE)
    fecha =  models.CharField(max_length=50 ,verbose_name='fecha')     
    descripcion =  models.CharField(max_length=150 ,verbose_name='descripcion')

  

     


