from django import forms
from .models import Orcamento, Procedimento
from apps.CadastroUsuario.models import CadastroPacientes

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ['paciente', 'procedimentos']

    def __init__(self, *args, **kwargs):
        super(OrcamentoForm, self).__init__(*args, **kwargs)
        self.fields['paciente'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['procedimentos'].widget = forms.CheckboxSelectMultiple()

    paciente = forms.ModelChoiceField(
        queryset=CadastroPacientes.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    procedimentos = forms.ModelMultipleChoiceField(
        queryset=Procedimento.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )