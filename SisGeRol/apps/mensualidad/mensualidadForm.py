from django import forms
from .models import Mensualidad

class MensualidadForm(forms.ModelForm):
    class Meta:
        model = Mensualidad
        fields = ['mesa', 'socio', 'mes', 'pagada']