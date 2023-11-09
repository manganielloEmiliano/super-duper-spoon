from django.contrib import admin
from .models import Mesa
from .forms import MesaForm


class MesaAdmin(admin.ModelAdmin):
    form = MesaForm
    list_display = ('nombre', 'sistema', 'director')

admin.site.register(Mesa, MesaAdmin)

