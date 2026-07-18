from django.forms import ModelForm
from .models import DireccionEnvio


class DireccionesEnviosForm(ModelForm):
    class Meta:
        model = DireccionEnvio
        fields = [
            'line1', 'line2', 'city', 'state', 'country', 'postal_code', 'reference'
        ]
