 
# OrcamentoPaciente/forms.py
# OrcamentoPaciente/forms.py
from django import forms
from .models import OrcamentoItem

class OrcamentoItemForm(forms.ModelForm):
    class Meta:
        model = OrcamentoItem
        fields = ['dente', 'procedimentos']

