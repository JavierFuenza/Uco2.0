import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#categoria
class categoria(models.Model):
    id = models.AutoField(primary_key=True),
    nombre = models.CharField(max_length=100,null=False)

#imagenes
class imagen(models.Model):
    nombre = models.CharField(max_length=100, primary_key=True)
    imagen = models.ImageField(upload_to='pics')

#producto
class producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100,null=False, default="NULL")
    precio = models.IntegerField(null=False, default=0)
    idCategoria = models.ForeignKey(categoria, on_delete=models.CASCADE, null=True)
    imagen = models.ForeignKey(imagen, on_delete=models.CASCADE, null=True)

#compra
class compra(models.Model):
    id = models.AutoField(primary_key=True)
    monto = models.IntegerField(null=False, default=0)
    productos = models.ForeignKey(producto, on_delete=models.CASCADE, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

#carrito



class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total
    
    
      
    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity
    
class CartItem(models.Model):
    product = models.ForeignKey(producto, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.product.nombre
    
    @property
    def price(self):
        new_price = self.product.precio * self.quantity
        return new_price