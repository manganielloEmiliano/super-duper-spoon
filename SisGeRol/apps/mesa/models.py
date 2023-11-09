from django.db import models
from apps.socio.models import Socio

class Mesa(models.Model):
    regularidad_choices = [
        ('semanal', 'Semanal'),
        ('quincenal', 'Quincenal'),
    ]
    
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField("descripcion", max_length=500, blank=True)
    sistema = models.CharField(max_length=50)
    jugadores = models.ManyToManyField(Socio, blank=True, related_name='mesas_jugadas')
    director = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name='mesas_dirigidas')
    regularidad = models.CharField(choices=regularidad_choices, max_length=50, default='semanal')
    
    costo = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    costo_director = models.DecimalField(max_digits=8, decimal_places=2, default=0)  # Agrega este campo
    
    def calcular_costo(self):
        if self.regularidad == 'semanal':
            return 2800
        elif self.regularidad == 'quincenal':
            return 2500
        else:
            return 0
    
    def save(self, *args, **kwargs):
        self.costo = self.calcular_costo()
        self.costo_director = self.costo - 500  # Calcula el costo del director
        super(Mesa, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre

