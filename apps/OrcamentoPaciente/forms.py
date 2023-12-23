 
# OrcamentoPaciente/forms.py
# OrcamentoPaciente/forms.py
from django import forms
from .models import OrcamentoItem,Dentes,Procedimento,CriarOrcamento

class OrcamentoItemForm(forms.ModelForm):
    class Meta:
        model = OrcamentoItem
        fields = ['procedimentos']
        
class DentesForm(forms.ModelForm):
    class Meta:
        model = Dentes
        fields = ['nome_dente', 'imagem_dente']

 
#class EscolherProcedimentoForm(forms.Form):
    #procedimento = forms.ModelChoiceField(queryset=Procedimento.objects.all())

from django import forms
from .models import CriarOrcamento

class CadastrarItemForm(forms.ModelForm):
    paciente = forms.CharField(max_length=120)
    dente = forms.CharField(max_length=120)
    procedimento = forms.ModelChoiceField(queryset=Procedimento.objects.all())
    
    class Meta:
        model = CriarOrcamento
        fields = ['paciente', 'dente', 'procedimento', 'usuario']
        widgets = {
            'usuario': forms.HiddenInput(),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].initial = user
    