from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['descricao']  # O campo 'data_horario' será preenchido na view
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }
    


    