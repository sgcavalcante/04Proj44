# orcamentos/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Paciente, Dente, Procedimento, Orcamento, ItemOrcamento
from .forms import OrcamentoForm,ProcedimentoForm
import pdfkit
import qrcode


def criar_orcamento(request):
    if request.method == 'POST':
        orcamento_form = OrcamentoForm(request.POST)
        procedimento_form = ProcedimentoForm(request.POST)
        if orcamento_form.is_valid() and procedimento_form.is_valid():
            paciente = orcamento_form.cleaned_data['paciente']
            orcamento = Orcamento.objects.create(paciente=paciente)
            for dente in Dente.objects.all():
                procedimentos_ids = procedimento_form.cleaned_data.get(f'dente_{dente.id}', [])
                for procedimento_id in procedimentos_ids:
                    procedimento = get_object_or_404(Procedimento, id=procedimento_id)
                    ItemOrcamento.objects.create(
                        orcamento=orcamento,
                        dente=dente,
                        procedimento=procedimento,
                        preco=procedimento.preco
                    )
            return redirect('gerar_html', orcamento_id=orcamento.numero)
    else:
        orcamento_form = OrcamentoForm()
        procedimento_form = ProcedimentoForm()
    return render(request, 'Orcamentos/criar_orcamento.html', {
        'orcamento_form': orcamento_form,
        'procedimento_form': procedimento_form
    })

def gerar_html(request, orcamento_id):
    orcamento = get_object_or_404(Orcamento, numero=orcamento_id)
    itens_orcamento = ItemOrcamento.objects.filter(orcamento=orcamento)

    total = sum(item.preco for item in itens_orcamento)

    context = {
        'orcamento': orcamento,
        'itens_orcamento': itens_orcamento,
        'total': total
    }
    return render(request, 'Orcamentos/relatorio.html', context)



def relatorio_geral(request):
    pacientes = Paciente.objects.all()
    return render(request, 'Orcamentos/relatorio_geral.html', {'pacientes': pacientes})

# views.py
 

# views.py


# views.py

'''
def gerar_html(request, orcamento_id):
    # Buscar o objeto Orcamento pelo UUID
    orcamento = get_object_or_404(Orcamento, numero=orcamento_id)
    # Buscar todos os itens relacionados a este orçamento
    itens_orcamento = ItemOrcamento.objects.filter(orcamento=orcamento)

    # Passar os objetos para o template
    context = {
        'orcamento': orcamento,
        'itens_orcamento': itens_orcamento
    }
    return render(request, 'Orcamentos/relatorio.html', context)

'''

def alista_orcamentos(request):
    orcamentos = Orcamento.objects.all()
    return render(request, 'Orcamentos/alista_orcamentos.html', {'orcamentos': orcamentos})