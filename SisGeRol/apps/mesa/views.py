from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from apps.core.util import admin_required

from apps.mesa.models import Mesa

@method_decorator(admin_required, name="dispatch")
class MesaListView(ListView):
    model = Mesa
    template_name = "list.html"
    context_object_name = "mesas"

@method_decorator(admin_required, name="dispatch")
class MesaDetailView(DetailView):
    model = Mesa
    template_name = "detail.html"
    context_object_name = "mesa"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mesa = self.object  # Obtiene la instancia de Mesa
        jugadores = mesa.jugadores.all()
        context['jugadores'] = jugadores
        return context
    
    
