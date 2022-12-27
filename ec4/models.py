from django.db import models

class Curso(models.Model):
    codigo = models.CharField(max_length = 150)
    nombre = models.CharField(max_length = 150)
    horas = models.IntegerField()
    creditos = models.IntegerField()
    estado = models.CharField(max_length = 1)

class Carreras(models.Model):
    nombre = models.CharField(max_length = 150)
    nombre_corto = models.CharField(max_length = 150)
    estado = models.CharField(max_length = 1)    
