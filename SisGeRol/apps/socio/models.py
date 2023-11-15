from django.db import models

class Socio(models.Model):
 nombre = models.CharField( max_length=50,default='')
 apellido = models.CharField( max_length=50,default='')
 dni = models.CharField( max_length=8,default='')
 fecha_nacimiento = models.DateField(null=True, blank=True)
 def __str__(self):
        return self.nombre + " " + self.apellido
 
 

