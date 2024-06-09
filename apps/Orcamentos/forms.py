from django import forms
from .models import Paciente, Dente, Procedimento

class OrcamentoForm(forms.Form):
    paciente = forms.ModelChoiceField(queryset=Paciente.objects.all(), label="Paciente")

class ProcedimentoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ProcedimentoForm, self).__init__(*args, **kwargs)
        for dente in Dente.objects.all():
            self.fields[f'dente_{dente.id}'] = forms.MultipleChoiceField(
                choices=[(proc.id, proc.nome) for proc in Procedimento.objects.all()],
                widget=forms.CheckboxSelectMultiple,
                label=f'Dente {dente.numero} - {dente.descricao}',
                required=False
            )
