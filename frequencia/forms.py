from django import forms
from .models import Frequencia, Materia


class FrequenciaForm(forms.ModelForm):

    class Meta:
        model = Frequencia
        fields = ('presente',)

