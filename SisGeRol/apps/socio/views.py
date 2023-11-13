from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404
from apps.core.util import admin_required
from .models import Socio
from django.utils.decorators import method_decorator


@method_decorator(admin_required, name="dispatch")
class SocioListView(ListView):
    model = Socio
    template_name = "list_socio.html"
    context_object_name = "socios"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar información sobre las mesas jugadas por cada socio
        socios = context['socios']
        mesas_por_socio = {socio.id: socio.mesas_jugadas.all() for socio in socios}
        context['mesas_por_socio'] = mesas_por_socio
        return context

@method_decorator(admin_required, name="dispatch")
class SocioView(DetailView):
    model = Socio
    template_name = "detalle_socio.html"
    context_object_name = "socio"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        socio = self.object
        sistemas_jugados = obtener_sistemas_jugados(socio)
        sistemas_dirigidos = obtener_sistemas_dirigidos(socio)
        context['sistemas_jugados'] = sistemas_jugados
        context['sistemas_dirigidos'] = sistemas_dirigidos
        return context

def obtener_sistemas_jugados(socio):
    return list(set(mesa.sistema for mesa in socio.mesas_jugadas.all()))

def obtener_sistemas_dirigidos(socio):
    return list(set(mesa.sistema for mesa in socio.mesas_dirigidas.all()))
