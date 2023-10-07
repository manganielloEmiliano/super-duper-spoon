from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from .models import Mesa


class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = '__all__'
        widgets = {
            'jugadores': FilteredSelectMultiple("Jugadores", is_stacked=False),
        }
