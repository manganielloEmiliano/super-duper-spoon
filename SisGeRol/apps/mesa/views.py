
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from apps.mensualidad.models import Mensualidad
from apps.mesa.forms import MesaCreateForm, MesaUpdateForm
from apps.core.util import admin_required
from django.views.generic import DeleteView


from apps.mesa.models import Mesa
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView

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
        mesa = self.object
        jugadores = mesa.jugadores.all()

        context['jugadores'] = jugadores
        return context
    
@method_decorator(admin_required, name="dispatch")
class MesaCreateView(CreateView):
    model = Mesa
    form_class = MesaCreateForm
    template_name = "create_mesa.html"
    success_url = reverse_lazy('mesa_list')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Lógica para crear las mensualidades aquí
        mesa = form.instance
        for mes in range(1, mesa.duracion_meses + 1):
            # Crear mensualidades para jugadores
            for jugador in mesa.jugadores.all():
                Mensualidad.objects.create(mesa=mesa, socio=jugador, mes=mes)

            # Crear mensualidad para el director
            Mensualidad.objects.create(mesa=mesa, socio=mesa.director, mes=mes)

        return response

@method_decorator(admin_required, name="dispatch")
class MesaDeleteView(DeleteView):
    model = Mesa
    template_name = 'delete_mesa.html'  
    success_url = reverse_lazy('mesa_list') 

@method_decorator(admin_required, name="dispatch")
class MesaUpdateView(UpdateView):
    model = Mesa
    form_class = MesaUpdateForm
    template_name = 'update_mesa.html'
    context_object_name = 'mesa'

    def form_valid(self, form):
        # Obtenemos la instancia de la Mesa
        mesa = get_object_or_404(Mesa, pk=self.kwargs['pk'])

        # Limpiamos los jugadores actuales
        mesa.jugadores.clear()

        # Añadimos los nuevos jugadores seleccionados
        jugadores = form.cleaned_data['jugadores']
        mesa.jugadores.add(*jugadores)

        # Guardamos la Mesa
        mesa.save()

        return HttpResponseRedirect(self.get_success_url())

    
    def get_success_url(self):
        return reverse_lazy('mesa_detail', kwargs={'pk': self.object.pk})
    
    
    