

from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    # campo adicional para horário de término
    data_horario_end = forms.DateTimeField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Consulta
        fields = [
            'descricao',
            'data_horario',
            'data_horario_end',   # passa a aceitar o fim também
        ]
        widgets = {
            'data_horario': forms.HiddenInput(),
        }
    