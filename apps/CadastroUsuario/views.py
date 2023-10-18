from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import auth
from apps.CadastroUsuario.forms import LoginForm,CadastroPacientesForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from apps.CadastroUsuario.models import CadastroPacientes 
# Create your views here.

def index(request):
    return render(request,'index/index.html')

def Clinica(request):
    return render(request,'main/clinica1.html')

def erro(request):
    return render(request,'erro.html') 


def configuracao(request):
    return render(request,'configuracao/configuracao.html')

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
    return render(request,'Login/login.html',{'form':formulario})


def cadastrar_paciente(request):
    if request.method=='POST':
        form = CadastroPacientesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_dados')
    else:
        form = CadastroPacientesForm()
     
    return render(request,'Cadastro/cadastrar_pacientes.html')

def listar_dados(request):
    pacientes = CadastroPacientes.objects.all()
    return render(request,'Cadastro/listar_dados.html',{'Pacientes':pacientes})

def remover(request,id):
    paciente = get_object_or_404(CadastroPacientes,pk=id)
    paciente.delete()
    return redirect('listar_dados')    