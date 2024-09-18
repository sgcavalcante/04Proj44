from django import forms
from .models import Consulta, CadastroPacientes  # Importe o modelo CadastroPacientes

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'data_horario', 'descricao']  # Inclua paciente aqui
        widgets = {
            'data_horario': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'descricao': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }

    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        #self.fields['paciente'].queryset = CadastroPacientes.objects.all()  # Listar os pacientes cadastrados
