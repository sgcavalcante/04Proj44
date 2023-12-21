from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.CadastroUsuario.models import CadastroPacientes
# Create your models here.

class Procedimento(models.Model):
    descricao = models.CharField(max_length=120,null=False,blank=False,unique=True,)
    valor_procedimento = models.DecimalField(max_digits=8,decimal_places=2,null=False,blank=False,)
    faces = models.IntegerField(default = 3)
    outros = models.CharField(max_length=120,null=True,blank=True,)    
    def __str__(self):
        return self.descricao

class Dentes(models.Model):
    nome_dente = models.CharField(max_length=120,null=False,blank=False,unique=True,)
    imagem_dente = models.ImageField(upload_to='Odontograma/',default=None)
    #procedimentos = models.ManyToManyField(Procedimento)
    def __str__(self):
            return self.nome_dente

class Orcamento(models.Model):
    paciente = models.ForeignKey(CadastroPacientes, on_delete=models.CASCADE)
    calcular_total = models.BooleanField(default=False)

class OrcamentoItem(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)
    dente = models.ForeignKey(Dentes, on_delete=models.CASCADE)
    procedimentos = models.ManyToManyField(Procedimento)
    def calcular_total(self):
        return sum(procedimento.valor for procedimento in self.procedimentos.all())

    def __str__(self):
        return f'Orcamento para {self.paciente.nome} em {self.data_criacao}'
    


class CriarOrcamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,default=5)  
    paciente = models.CharField(max_length=120,null=False,blank=False,unique=False,)
    dente = models.CharField(max_length=120,null=False,blank=False,unique=False,)
    procedimento = models.CharField(max_length=120,null=False,blank=False)
     
    #calcular_total = models.BooleanField(default=False)