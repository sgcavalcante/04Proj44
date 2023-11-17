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

@login_required
def listar_dados(request):
    pacientes = CadastroPacientes.objects.all()
    
    return render(request,'configuracao/listar_dados.html',{'Pacientes':pacientes})
@login_required
def remover(request,id):
    paciente = get_object_or_404(CadastroPacientes,pk=id)
    paciente.delete()
    return redirect('listar_dados')    