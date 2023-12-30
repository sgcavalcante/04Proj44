from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from apps.CadastroProprietario.forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

# Create your views here.

#Fazer novo Acesso
#@login_required
def loginProprietario(request):
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
            return redirect('loginProprietario')
    
    return render(request,'CadastroProprietario/loginProprietario.html',{'form':formulario})

#Registrar Novo Usuário no Sistema
#@login_required
def registroProprietario(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username,email=email,password=password)
            user = authenticate(username=username,password=password)
            #login(request)
            return redirect('loginProprietario')
    else:
        form = RegistrationForm()
    return render(request,'CadastroProprietario/registroProprietario.html',{'form':form})

@login_required
def listar_proprietarios(request):
    nome = request.GET.get('nome')
    usuarios = User.objects.all()
     
    return render(request,'CadastroProprietario/proprietarios.html',{'usuarios':usuarios})