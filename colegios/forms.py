from django import forms
from colegios.models import Regiones,Colegios

class ColegioForm(forms.ModelForm):
    class Meta:
        model = Colegios
        exclude = ('user',)