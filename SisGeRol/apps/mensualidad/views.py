from django import forms
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator


from apps.core.util import admin_required
from apps.mensualidad.models import Mensualidad
from apps.mensualidad.mensualidadForm import MensualidadForm

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

@method_decorator(admin_required, name="dispatch")
class MensualidadListView(ListView):
    model = Mensualidad
    template_name = 'mensualidad_list.html'
    context_object_name = 'mensualidades'  

    def get_queryset(self):
        
        return Mensualidad.objects.order_by('socio', 'mes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context

@method_decorator(admin_required, name="dispatch")
class mensualidadDetailView(DetailView):
    model = Mensualidad
    template_name = 'detail_mensualidad.html'
    context_object_name = 'mensualidad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
    
@method_decorator(admin_required, name="dispatch")
class MensualidadCreateView(CreateView):
    model = Mensualidad
    form_class = MensualidadForm  # Usa el formulario correcto
    template_name = 'create_mensualidad.html'
    
    def get_success_url(self):
        return reverse_lazy('mensualidad-list')
    
class MensualidadDeleteView(DeleteView):
    model = Mensualidad
    template_name = 'delete_mensualidad.html'
    success_url = reverse_lazy('mensualidad-list')

@method_decorator(admin_required, name="dispatch")
class MensualidadUpdateView(UpdateView):
    model = Mensualidad
    form_class = MensualidadForm
    template_name = 'update_mensualidad.html'
    def get_success_url(self):
        return reverse_lazy('mensualidad-detail', kwargs={'pk': self.object.pk}) 