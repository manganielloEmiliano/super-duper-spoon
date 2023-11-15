from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

from apps.socio.models import Socio
from .models import Mesa


class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = '__all__'
        widgets = {
            'jugadores': FilteredSelectMultiple("Jugadores", is_stacked=False),
        }



class MesaCreateForm(forms.ModelForm):
    jugadores = forms.ModelMultipleChoiceField(
        queryset=Socio.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Mesa
        exclude = ['costo', 'costo_director'] 

class MesaUpdateForm(forms.ModelForm):
    jugadores = forms.ModelMultipleChoiceField(
        queryset=Socio.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Esto permite que el campo sea opcional
    )

    class Meta:
        model = Mesa
        exclude = ['costo', 'costo_director'] 