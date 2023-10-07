from django.db import models


# Create your models here.

class Socio(models.Model):
 nombre = models.CharField( max_length=50,default='')
 apellido = models.CharField( max_length=50,default='')
 dni = models.CharField( max_length=8,default='')
 fecha_nacimiento = models.DateField(default='1900-01-01')
 
 def __str__(self):
        return self.nombre + " " + self.apellido
 
 

