from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from apps.core.util import admin_required
from apps.mensualidad.models import Mensualidad
from apps.socio.models import Socio
from apps.mesa.models import Mesa
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class MensualidadListView(ListView):
    model = Mensualidad
    template_name = 'mensualidad_list.html'
    context_object_name = 'mensualidades'  # Nombre de la variable de contexto en la plantilla

    def get_queryset(self):
        # Ordenar las mensualidades por socio y mes
        return Mensualidad.objects.order_by('socio', 'mes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Aquí puedes agregar más información al contexto si es necesario
        # Ejemplo: context['otra_variable'] = valor

        return context
    

class MensualidadDetailView(DetailView):
    model = Mensualidad
    template_name = 'mensualidad_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fechas'] = self.object.fechas.all()
        return context

class MensualidadCreateView(CreateView):
    model = Mensualidad
    template_name = 'mensualidad/mensualidad_form.html'
    fields = ['mes', 'pagada']  # Ajusta los campos según tus necesidades

    def form_valid(self, form):
        form.instance.mesa = Mesa.objects.get(pk=self.kwargs['mesa_pk'])
        form.instance.socio = Socio.objects.get(pk=self.kwargs['socio_pk'])
        return super().form_valid(form)

class MensualidadUpdateView(UpdateView):
    model = Mensualidad
    template_name = 'mensualidad/mensualidad_form.html'
    fields = ['mes', 'pagada']  # Ajusta los campos según tus necesidades

class MensualidadDeleteView(DeleteView):
    model = Mensualidad
    template_name = 'mensualidad/mensualidad_confirm_delete.html'
    success_url = reverse_lazy('mensualidad-list')