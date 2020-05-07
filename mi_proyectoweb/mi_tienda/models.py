from django.db import models

# Create your models here.
# Modelos de datos


#creamos clase que herada de models.
class Producto(models.Model):
    """Modelo de datos de mis productos"""

    nombre = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)
    precio = models.FloatField()

    # -- Usamos el nombre para identificar
    # -- el productol
    # -- método __str__(self), que un método reservado que usa python para
    # -- obtener una cadena que represente a ese objet0
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    """Modelo de datos para pedidos"""

    nombre = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)



    def __str__(self):
        return self.nombre
