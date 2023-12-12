 
# OrcamentoPaciente/forms.py
# OrcamentoPaciente/forms.py
from django import forms
from .models import OrcamentoItem,Dentes

class OrcamentoItemForm(forms.ModelForm):
    class Meta:
        model = OrcamentoItem
        fields = ['dente', 'procedimentos']

class DentesForm(forms.ModelForm):
    class Meta:
        model = Dentes
        fields = ['nome_dente', 'imagem_dente']