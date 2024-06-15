from django import forms
from .models import Dente, Procedimento #Paciente, 
from apps.CadastroUsuario.models import CadastroPacientes
class OrcamentoForm(forms.Form):
    pacientes = forms.ModelChoiceField(queryset=CadastroPacientes.objects.all(),required=False)
    #pacientes = forms.Field(required=False)
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


class DenteForm(forms.ModelForm):
    class Meta:
        model = Dente
        fields = ['numero','descricao', 'imagem']