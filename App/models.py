from django.db import models

# Create your models here.

class Emprendimiento(models.Model):

    nombre = models.CharField(max_length=30)
    cuit = models.IntegerField()
    rubro = models.CharField(max_length=20)


class Empleados(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    DNI = models.IntegerField()

class Proveedores(models.Model):

    razonsocial = models.CharField(max_length=30)
    productos = models.CharField(max_length=30)
    telefono = models.IntegerField()

class Clientes(models.Model):

    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField()
