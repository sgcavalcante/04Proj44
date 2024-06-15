# orcamentos/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Dente, Procedimento, Orcamento, ItemOrcamento
from .forms import OrcamentoForm,ProcedimentoForm,DenteForm
from apps.CadastroUsuario.models import CadastroPacientes
import pdfkit
import qrcode


def criar_orcamento(request,id):
    #id = id
    pacientes = get_object_or_404(CadastroPacientes,id = id)
    paciente_id = id
    print(id,pacientes)  
    if request.method == 'POST':
        orcamento_form = OrcamentoForm(request.POST)
        procedimento_form = ProcedimentoForm(request.POST)
        if orcamento_form.is_valid() and procedimento_form.is_valid():
            #paciente = orcamento_form.cleaned_data['paciente']
            
            orcamento = Orcamento.objects.create(paciente_id=paciente_id)
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
        'procedimento_form': procedimento_form,
        'pacientes':pacientes,
         
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
    pacientes = CadastroPacientes.objects.all()
    return render(request, 'Orcamentos/relatorio_geral.html', {'pacientes': pacientes})

def todosospacientes(request):
    pacientes = CadastroPacientes.objects.all()
    return render(request, 'Orcamentos/todosospacientes.html', {'pacientes': pacientes})

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


def inserir_fotos_dentes(request):
    fotos_dentes = Dente.objects.all() # apenas para pegar a models Dentes e mostrar no template de inserir fotos de dentes
    if request.method == 'POST':
        form = DenteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inserir_fotos_dentes')  # Redirecionar para a lista de dentes após o upload
    else:
        form = DenteForm()

    return render(request, 'configuracao/inserir_fotos_dentes.html', {'form': form,'fotos_dentes':fotos_dentes})
'''
def orcamento(request, paciente_id):
    paciente = CadastroPacientes.objects.get(id=paciente_id)
    informacao = request.session.get('cont', '')  
    dentes_fotos = Dente.objects.all()
    procedimentos = Procedimento.objects.all()
     
    return render(request, 'orcamento/orcamento.html',{'paciente':paciente,'procedimentos':procedimentos,'dentes_fotos':dentes_fotos,'informacao':informacao})
'''
