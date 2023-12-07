from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrcamentoForm
from .models import Procedimento  
from apps.CadastroUsuario.models import CadastroPacientes
def criar_orcamento(request, paciente_id):
    paciente = get_object_or_404(CadastroPacientes, id=paciente_id)

    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            orcamento = form.save(commit=False)
            procedimentos = form.cleaned_data['procedimentos']
            valor_total = sum(procedimento.valor_procedimento for procedimento in procedimentos)
            orcamento.valor_total = valor_total
            orcamento.paciente = paciente
            orcamento.save()
            return redirect('teste.html')  # Redirecione para uma página de sucesso
    else:
        form = OrcamentoForm(initial={'paciente': paciente})

    return render(request, 'orcamento/orcamento.html', {'form': form, 'paciente': paciente})