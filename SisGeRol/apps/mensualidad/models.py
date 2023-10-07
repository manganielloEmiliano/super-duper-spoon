from django.db import models
from apps.socio.models import Socio
from apps.mesa.models import Mesa


class Mensualidad(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField()
    pagada = models.BooleanField(default=False)

    def __str__(self):
        return f"Mensualidad para {self.socio.nombre} {self.socio.apellido} (Mesa: {self.mesa.nombre} valor: {self.mesa.costo})"
