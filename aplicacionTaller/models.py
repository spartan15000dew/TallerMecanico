from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.IntegerField()
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.CharField(max_length=50)
    direccion = models.CharField(max_length=40)