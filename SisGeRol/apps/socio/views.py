from apps.socio.models import Socio

from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from apps.core.util import admin_required
# Create your views here.

@method_decorator(admin_required, name="dispatch")
class SocioView(DetailView):
    model = Socio
    template_name = "socio_detail.html"
    context_object_name = "socio"