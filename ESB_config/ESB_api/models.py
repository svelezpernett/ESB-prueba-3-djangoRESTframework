from django.db import models
from rest_framework import serializers

# Create your models here.

class Clientes(models.Model):
    cedula = models.CharField(primary_key=True, max_length=15, unique=True)
    nombre = models.CharField(max_length=30, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    telefono = models.CharField(max_length=15, blank=False, null=False)
    correo = models.EmailField(max_length=254, blank=False, null=False)
    
    def __str__(self):
        return self.nombre + ", CC " + self.cedula


class prueba(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    
    def __str__(self):
        return str(self.id)

class documento(models.Model):
    tipo = models.CharField(max_length=30, blank=False, null=False)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo
        