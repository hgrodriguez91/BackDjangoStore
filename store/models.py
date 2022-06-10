from django.db import models

# Create your models here.

class Category(models.Model):
    nombre= models.CharField(max_length=50, null= True)
    def __str__(self):
        return self.nombre

class Producto (models.Model):
    codigo = models.IntegerField(null= True)
    nombre = models.CharField(max_length=50, null= True)
    descripcion= models.CharField(max_length=255,null= True)    
    category= models.ForeignKey(Category, null= True, on_delete= models.SET_NULL)
    def __str__(self):
        return self.nombre
    
class Store (models.Model):
    nombre= models.CharField(max_length= 50, null= True) 
    def __str__(self):
        return self.nombre   
    
class Producto_store (models.Model):
    producto_id= models.ForeignKey( Producto,null= True,on_delete=models.CASCADE)
    store_id= models.ForeignKey(Store, null= True,on_delete=models.CASCADE)
    precio= models.FloatField(null= True)
    created_at= models.DateField(null= True)
    def __str__(self):
        return "Tienda: " + str(self.store_id)+" -- "+" Producto: "+str(self.producto_id)+ " -- "+" Precio: "+"$"+str(self.precio)   
    