from django.db import models

# Create your models here.


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='nombre de la categoria')
    def __str__(self) -> str:
        return self.nombreCategoria

class Producto(models.Model):
    Barcode = models.CharField(max_length=6 ,primary_key=True ,verbose_name='Barcode')      
    nombre =  models.CharField(max_length=50 ,verbose_name='nombre')      
    precio = models.IntegerField(verbose_name='precio')
    stock = models.IntegerField(verbose_name='stock')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre   
    

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

     


