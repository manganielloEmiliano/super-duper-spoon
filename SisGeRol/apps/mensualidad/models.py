from django.db import models
from apps.socio.models import Socio
from apps.mesa.models import Mesa
from django.utils import timezone

class Mensualidad(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name='mensualidades')
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name='mensualidades')
    mes = models.PositiveIntegerField()  
    pagada = models.BooleanField(default=False)
    costo_a_pagar = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    fecha = models.DateField(default=timezone.now)

    def calcular_costo_a_pagar(self):
        if self.socio == self.mesa.director:
            return self.mesa.costo_director
        else:
            return self.mesa.costo

    def save(self, *args, **kwargs):
        self.costo_a_pagar = self.calcular_costo_a_pagar()
        super(Mensualidad, self).save(*args, **kwargs)

    def __str__(self):
        return f"Mensualidad para {self.socio.nombre} {self.socio.apellido} (Mesa: {self.mesa.nombre}, Mes: {self.mes}, costo pagado: {self.costo_a_pagar})"
