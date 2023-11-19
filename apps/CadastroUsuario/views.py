from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
from apps.CadastroUsuario.forms import LoginForm,CadastroPacientesForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from apps.CadastroUsuario.models import CadastroPacientes 
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'index/index.html')

def Clinica(request):
    return render(request,'main/clinica1.html')

def erro(request):
    return render(request,'erro.html') 

@login_required
def configuracao(request):
    return render(request,'configuracao/configuracao.html')

'''
def login(request):

    formulario = LoginForm()

    if request.method == 'POST':
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            nome = formulario['nome_login'].value()
            senha = formulario['senha'].value()

        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha
        )    
        if usuario is not None:
            auth.login(request,usuario)
            return redirect('configuracao')
        
        else:
            return redirect('erro')
    return render(request,'CadastroProprietario/cadastroProprietario.html',{'form':formulario})

'''
'''

def cadastrar_paciente(request):
    if request.method=='POST':
        form = CadastroPacientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_dados')
    else:
        form = CadastroPacientesForm()
     
    return render(request,'Cadastro/cadastrar_pacientes.html')
'''
@login_required
def cadastrar_paciente(request):
    if request.method=='POST':
        #form = CadastroPacientesForm(request.POST)
        novo_registro = CadastroPacientes(
            #['nome','telefone','email','data_nascimento','profissao','cep','estado','cidade','bairro','numero','complemento','alergia','doencas_conhecidas']  
            nome = request.POST['nome'],
            telefone = request.POST['telefone'],
            email = request.POST['email'],
            data_nascimento = request.POST['data_nascimento'],
            profissao = request.POST['profissao'],
            cep = request.POST['cep'],
            estado = request.POST['estado'],
            cidade = request.POST['cidade'],
            bairro = request.POST['bairro'],
            numero = request.POST['numero'],
            complemento = request.POST['complemento'],
            alergia = request.POST['alergia'],
            doencas_conhecidas = request.POST['doencas_conhecidas'],
            
        )    
        
        novo_registro.save()
        return redirect('listar_dados')
    else:
        form = CadastroPacientesForm()
     
    return render(request,'configuracao/cp.html',{'form':form}) #alterado a pasta Cadastro para configuracao e funcionou


#####
@login_required
def editar(request,id):
    dado = get_object_or_404(CadastroPacientes,pk=id)
    if request.method =='GET':
        form = CadastroPacientesForm(initial={
            'nome':dado.nome,
            'telefone':dado.telefone,
            'email':dado.email,
            'data_nascimento':dado.data_nascimento,
            'profissao':dado.profissao,
            'cep':dado.cep,
            'estado':dado.estado,
            'cidade':dado.cidade,
            'bairro':dado.bairro,
            'numero':dado.numero,
            'complemento':dado.complemento,
            'alergia':dado.alergia,
            'doencas_conhecidas':dado.doencas_conhecidas,
             
            })
    elif request.method =='POST':
        form = CadastroPacientesForm(request.POST)
        if form.is_valid():
            dado.nome = form.cleaned_data['nome']
            dado.telefone = form.cleaned_data['telefone']
            dado.email = form.cleaned_data['email']
            dado.data_nascimento = form.cleaned_data['data_nascimento']
            dado.profissao = form.cleaned_data['profissao']
            dado.cep = form.cleaned_data['cep']
            dado.estado = form.cleaned_data['estado']
            dado.cidade = form.cleaned_data['cidade']
            dado.bairro = form.cleaned_data['bairro']
            dado.numero = form.cleaned_data['numero']
            dado.complemento = form.cleaned_data['complemento']
            dado.alergia = form.cleaned_data['alergia']
            dado.doencas_conhecidas = form.cleaned_data['doencas_conhecidas']
            dado.save()
            return redirect('listar_dados')
                
    return render (request,'configuracao/Editar_Dados.html',{"form":form,"id":id})


###


@login_required
def listar_dados(request):
    pacientes = CadastroPacientes.objects.all()
    
    return render(request,'configuracao/listar_dados.html',{'Pacientes':pacientes})
@login_required
def remover(request,id):
    paciente = get_object_or_404(CadastroPacientes,pk=id)
    paciente.delete()
    return redirect('listar_dados')    

