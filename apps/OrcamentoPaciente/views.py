from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import Procedimento,Orcamento,Dentes  

from apps.CadastroUsuario.models import CadastroPacientes
from django.contrib.auth.models import User
from django.db.models import QuerySet
from .forms import OrcamentoItemForm

def criar_orcamento(request, paciente_id,dente_id):
    paciente = CadastroPacientes.objects.get(id=paciente_id)
    dente = Dentes.objects.get(id=dente_id) 
     
    ####### 
    if request.method == 'POST':
        if 'selecionar_dente' in request.POST:
            form_dente = OrcamentoItemForm(request.POST)
            if form_dente.is_valid():
                orcamento_item = form_dente.save(commit=False)
                orcamento_item.orcamento = Orcamento.objects.create(paciente=paciente)
                orcamento_item.save()
                return redirect('criar_orcamento', paciente_id=paciente_id)
        elif 'finalizar_orcamento' in request.POST:
            # Lógica para finalizar o orçamento, gerar relatório, etc.
            return redirect('sucesso')
    else:
        form_dente = OrcamentoItemForm()

    return render(request, 'orcamento/orcamento_form.html', {'form_dente': form_dente, 'paciente': paciente,'dente':dente})

 
def sucesso(request):
    return render(request, 'orcamento/sucesso.html')


def orcamento(request, paciente_id):
    paciente = CadastroPacientes.objects.get(id=paciente_id)
    dentes_fotos = Dentes.objects.all()
    print(dentes_fotos)
    procedimentos = Procedimento.objects.all()
     

    return render(request, 'orcamento/orcamento.html',{'paciente':paciente,'procedimentos':procedimentos,'dentes_fotos':dentes_fotos})

def orcamento_dente(request):
    procedimentos = Procedimento.objects.all()
     
    return render(request,'orcamento/orcamento_dente.html',{'procedimentos':procedimentos})

def teste(request,dente_id):
    imagens = get_object_or_404(Dentes,pk=dente_id)
    fotos_dentes = imagens.Dente_set.all()
    return render(request,'orcamento/orcamento_dente.html',{'fotos_dentes':fotos_dentes})


 