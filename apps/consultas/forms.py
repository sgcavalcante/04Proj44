from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['data_horario', 'descricao']
        widgets = {
            'data_horario': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'descricao': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }

    def clean_data_horario(self):
        data_horario = self.cleaned_data['data_horario']

        # Verifica se já existe uma consulta no mesmo horário
        if Consulta.objects.filter(data_horario=data_horario).exists():
            raise forms.ValidationError('Já existe uma consulta marcada para esse horário.')

        return data_horario