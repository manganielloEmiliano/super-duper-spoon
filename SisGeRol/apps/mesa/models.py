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
    duracion_meses = models.PositiveIntegerField(default=3)
    
    costo = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    costo_director = models.DecimalField(max_digits=8, decimal_places=2, default=0) 
    
    def calcular_costo(self):
        if self.regularidad == 'semanal':
            return 6000
        elif self.regularidad == 'quincenal':
            return 3000
        else:
            return 0
    def duracion_meses_range(self):
        return range(1, self.duracion_meses + 1)
    def mensualidades_socio(self, socio):
        return self.mensualidad_set.filter(socio=socio)
    
    def save(self, *args, **kwargs):
        self.costo = self.calcular_costo()
        self.costo_director = self.costo / 2
        super(Mesa, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.nombre