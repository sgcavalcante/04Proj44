from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib import auth
from apps.CadastroUsuario.forms import LoginForm,CadastroPacientesForm,ImageAForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from apps.CadastroUsuario.models import CadastroPacientes,ImageA
from django.contrib.auth.decorators import login_required
from django.db.models import Q # para fazer filtro
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


@login_required
def cadastrar_paciente(request):
    if request.method=='POST':
        #form = CadastroPacientesForm(request.POST)
        novo_registro = CadastroPacientes(
            #['nome','telefone','email','data_nascimento','profissao','cep','estado','cidade','bairro','numero','complemento','alergia','doencas_conhecidas']  
            usuario = request.user,
            nome = request.POST['nome'],
            cpf = request.POST['cpf'],
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
     
    return render(request,'Cadastro/cadastropacientes.html',{'form':form}) #alterado a pasta Cadastro para configuracao e funcionou


#####
@login_required
def editar(request,id):
    dado = get_object_or_404(CadastroPacientes,pk=id)
    #dado = CadastroPacientes.objects.filter(usuario=request.user)
    if request.method =='GET':
        form = CadastroPacientesForm(initial={
            'nome':dado.nome,
            'cpf':dado.cpf,
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
        form = CadastroPacientesForm(request.POST,instance=dado)
        
        if form.is_valid():
             
            form.save()
            return redirect('listar_dados')
        else:
            form = CadastroPacientesForm(instance=dado)
               
    return render (request,'Cadastro/Editar_Dados.html',{"form":form,"id":id})



@login_required
def listar_dados(request):
    nome = request.GET.get('nome')
    pacientes = CadastroPacientes.objects.filter(usuario=request.user)
    if nome:
        pacientes = pacientes.filter(nome__icontains=nome)
    return render(request,'Cadastro/listar_dados_filtro.html',{'Pacientes':pacientes})


@login_required
def remover(request,id):
    paciente = CadastroPacientes.objects.filter(usuario=request.user)
    paciente = get_object_or_404(CadastroPacientes,pk=id)
    paciente.delete()
    return redirect('listar_dados')    


@login_required
def paciente_acoes(request,id):
     
    paciente = get_object_or_404(CadastroPacientes,pk=id)
    
    if request.method =='GET':
        form = CadastroPacientesForm(initial={
            
            'nome':paciente.nome,
            'cpf':paciente.cpf,
            'telefone':paciente.telefone,
            'email':paciente.email,
            'data_nascimento':paciente.data_nascimento,
            'profissao':paciente.profissao,
            'cep':paciente.cep,
            'estado':paciente.estado,
            'cidade':paciente.cidade,
            'bairro':paciente.bairro,
            'numero':paciente.numero,
            'complemento':paciente.complemento,
            'alergia':paciente.alergia,
            'doencas_conhecidas':paciente.doencas_conhecidas,
             
            })
    return render(request,'Cadastro/paciente_acoes.html',{'Pacientes':paciente,"id":id})
 


####
@login_required
def gallery(request, paciente_id):
    
    paciente = CadastroPacientes.objects.get(pk=paciente_id)
    
    if request.method == "POST":
        foto = request.FILES["foto"]
        imagem = ImageA(nome=paciente, name=foto.name, imagem=foto)
        imagem.save()
        #return redirect("cadastropacientes_list")
        return redirect('listar_dados')
    #return render(request, "cadastropacientes_adicionar_foto.html", {"paciente": paciente})
    return render(request,"Cadastro/gallery_img.html",{"paciente":paciente})
####
@login_required
def fotos_tratamento(request,paciente_id):
    paciente = get_object_or_404(CadastroPacientes, pk=paciente_id)
    
    Fotos = paciente.imagea_set.all()
    return render(request,'Cadastro/fotos.html',{'paciente':paciente,'Fotos':Fotos})    
