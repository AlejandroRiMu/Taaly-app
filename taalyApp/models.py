from django.db import models

# Create your models here.

class Planta(models.Model):
    nombre = models.CharField(max_length = 30)
    region = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length = 30)
    efectos = models.CharField(max_length = 30)
    usos = models.CharField(max_length = 30)