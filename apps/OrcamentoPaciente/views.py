from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import User
from django.db.models import QuerySet
from apps.CadastroUsuario.models import CadastroPacientes
from .models import Procedimento,Orcamento,Dentes, OrcamentoItem,CriarOrcamento  
from .forms import OrcamentoItemForm,DentesForm,OrcamentoItemForm,CadastrarItemForm
from django.contrib.auth.decorators import login_required

@login_required
def cadastrar_item(request):
    if request.method == 'POST':
        form = CadastrarItemForm(request.user, request.POST)
        if form.is_valid():
            orcamento = form.save(commit=False)
            orcamento.usuario = request.user
            orcamento.save()
            return redirect('listar_orcamento')
    else:
        # Certifique-se de passar o formulário com o usuário para a renderização do template
        form = CadastrarItemForm(request.user)

     
            
    return redirect('erro_orcamento')
    

 
@login_required
def listar_orcamento(request):
    orcamentos_do_usuario = CriarOrcamento.objects.filter(usuario=request.user)
     
    return render(request, 'orcamento/listar_orcamento.html', {'orcamentos': orcamentos_do_usuario})
    



@login_required
def criar_orcamento(request, paciente_id,dente_id):
    paciente = CadastroPacientes.objects.get(id=paciente_id)
    dente = Dentes.objects.get(id=dente_id) 
    orcamentos = Orcamento.objects.all() 
    orcamentos_items = OrcamentoItem.objects.all()
    procedimentos = Procedimento.objects.all() 
    ####### 
    if request.method == 'POST':
        if 'selecionar_dente' in request.POST:
            form_dente = OrcamentoItemForm(request.POST)
            procedimentoForm = OrcamentoItemForm(request.POST)
            if form_dente.is_valid():
                orcamento_item = form_dente.save(commit=False)
                orcamento_item.orcamento = Orcamento.objects.create(paciente=paciente)
                orcamento_item.save()
                return redirect('criar_orcamento', paciente_id=paciente_id,dente_id=dente_id)
        elif 'finalizar_orcamento' in request.POST:
            # Lógica para finalizar o orçamento, gerar relatório, etc.
            return redirect('sucesso')
    else:
        form_dente = OrcamentoItemForm()
        procedimentoForm = OrcamentoItemForm()
    return render(request, 'orcamento/orcamento_form.html', {'procedimentos':procedimentos,'form_dente': form_dente, 'paciente': paciente,'dente':dente,'orcamentos':orcamentos,'orcamentos_items':orcamentos_items,'procedimentoForm':procedimentoForm})

 
def sucesso(request):
    return render(request, 'orcamento/sucesso.html')

 
def erro_orcamento(request):
    return render(request, 'orcamento/erro_orcamento.html')

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



def inserir_fotos_dentes(request):
    fotos_dentes = Dentes.objects.all() # apenas para pegar a models Dentes e mostrar no template de inserir fotos de dentes
    if request.method == 'POST':
        form = DentesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inserir_fotos_dentes')  # Redirecionar para a lista de dentes após o upload
    else:
        form = DentesForm()

    return render(request, 'configuracao/inserir_fotos_dentes.html', {'form': form,'fotos_dentes':fotos_dentes})
