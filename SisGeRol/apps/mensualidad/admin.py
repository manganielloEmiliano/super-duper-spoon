from django.contrib import admin
from django.db.models import Q
from .models import Mensualidad
from apps.socio.models import Socio
from apps.mesa.models import Mesa  # Asegúrate de que esta línea esté presente y sea correcta

class MensualidadAdmin(admin.ModelAdmin):
    list_display = ('mes', 'socio', 'pagada', 'costo_a_pagar')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'socio':
            # Obtén la mesa asociada a la mensualidad
            mensualidad_id = request.resolver_match.kwargs.get('object_id')
            if mensualidad_id:
                mensualidad = Mensualidad.objects.get(pk=mensualidad_id)
                mesa = mensualidad.mesa
                # Filtra los socios según la mesa asociada a la mensualidad
                kwargs['queryset'] = Socio.objects.filter(
                    Q(mesas_jugadas=mesa) | Q(mesas_dirigidas=mesa)
                )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Mensualidad, MensualidadAdmin)
