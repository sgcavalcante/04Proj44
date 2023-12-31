from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import User
from django.db.models import QuerySet
from apps.CadastroUsuario.models import CadastroPacientes
from .models import Procedimento,Orcamento,Dentes, OrcamentoItem,CriarOrcamento,TB_Orcamento 
from .forms import OrcamentoItemForm,DentesForm,OrcamentoItemForm,CadastrarItemForm
from django.contrib.auth.decorators import login_required
paciente_aux=''


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
    orcamentos_do_usuario = CriarOrcamento.objects.filter(usuario=request.user,paciente=paciente_aux)
     
     
    print(CriarOrcamento) 
    return render(request, 'orcamento/listar_orcamento.html', {'orcamentos': orcamentos_do_usuario})
    


@login_required
def abir_novo_orcamento(request,paciente_id):
    #via chat
     
    cont= request.session.get('cont', 1)
    cont += 1
    request.session['cont'] = cont
    ### 
    paciente = get_object_or_404(CadastroPacientes,pk=paciente_id)
    if request.method=='GET':
        
         
        TB_Orcamento.objects.create(paciente_id=paciente_id,numero_orcamento = cont,calcular_total = "False" )  
        orcamentos = TB_Orcamento.objects.filter(paciente_id=paciente_id) 
        
        return render(request,'orcamento/abrir_novo_orcamento.html',{'orcamentos': orcamentos,'paciente':paciente} )
        #return redirect('listar_orcamento')
    else:
        orcamentos = TB_Orcamento.objects.all()
         
        return redirect('erro_orcamento')

    
    return render(request,'orcamento/abrir_novo_orcamento.html',{'orcamentos': orcamentos} )



@login_required
def criar_orcamento(request, paciente_id,dente_id):
    global paciente_aux
    paciente = CadastroPacientes.objects.get(id=paciente_id)
    dente = Dentes.objects.get(id=dente_id) 
    orcamentos = Orcamento.objects.all() 
    orcamentos_items = OrcamentoItem.objects.all()
    procedimentos = Procedimento.objects.all() 
    informacao1 = request.session.get('cont', '')  
    paciente_aux =  CadastroPacientes.objects.get(id=paciente_id)
    print(f'teste >>>> {paciente_aux}') 
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
    return render(request, 'orcamento/orcamento_form.html', {'procedimentos':procedimentos,'form_dente': form_dente, 'paciente': paciente,'dente':dente,'orcamentos':orcamentos,'orcamentos_items':orcamentos_items,'procedimentoForm':procedimentoForm,'informacao1':informacao1})

 
def sucesso(request):
    return render(request, 'orcamento/sucesso.html')

 
def erro_orcamento(request):
    return render(request, 'orcamento/erro_orcamento.html')

def orcamento(request, paciente_id):
    paciente = CadastroPacientes.objects.get(id=paciente_id)
    informacao = request.session.get('cont', '')  
    dentes_fotos = Dentes.objects.all()
    procedimentos = Procedimento.objects.all()
     
    return render(request, 'orcamento/orcamento.html',{'paciente':paciente,'procedimentos':procedimentos,'dentes_fotos':dentes_fotos,'informacao':informacao})

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
