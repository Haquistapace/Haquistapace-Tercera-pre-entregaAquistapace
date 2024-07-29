from django.db import models

class Deporte(models.Model):
    deporte = models.CharField(max_length=40)
    dia = models.CharField(max_length=40)
    

class Acreditacion(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, unique=True)

class Socio(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=40)
    
