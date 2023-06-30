from django.db import models

# Create your models here.
#usuario
class user(models.Model):
    #genero
    MASCULINO = "M"
    FEMENINO = "F"
    OTRO = "X"
    GENERO_CHOICES = [(MASCULINO,"Masculino"),(FEMENINO,"Femenino"),(OTRO,"Otro")]

    id = models.AutoField(primary_key=True),
    nombre = models.CharField(max_length=100,null=False),
    apellido = models.CharField(max_length=100,null=False)
    fecnac = models.DateField(null=False)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, null=False)
    email =models.CharField(max_length=30,null=False)
    telefono = models.CharField(max_length=12,null=False)
    direccion = models.CharField(max_length=50,null=False)

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
    usuario = models.ForeignKey(user, on_delete=models.CASCADE)