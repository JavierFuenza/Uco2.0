from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#Direccion

#producto
class producto(models.Model):
    id = models.AutoField(primary_key=True),
    nombre = models.CharField(max_length=100,null=False),
    precio = models.IntegerField(null=False,max_length=8),

#compra
class compra(models.Model):
    id = models.AutoField(primary_key=True),
    monto = models.IntegerField(null=False,max_length=9),
    productos = models.CharField(max_length=500,null=False),
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)