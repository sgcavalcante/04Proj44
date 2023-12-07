from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.CadastroUsuario.models import CadastroPacientes
# Create your models here.

class Procedimento(models.Model):

    descricao = models.CharField(
        max_length=120,
        null=False,
        blank=False,
        unique=True,
        )

    valor_procedimento = models.DecimalField(
        max_digits=8,
        decimal_places=2,
         
        null=False,
        blank=False,
        )

    faces = models.IntegerField(
        
        default = 3
        )

    outros = models.CharField(
        max_length=120,
        null=True,
        blank=True,
        )    
    
    def __str__(self):
        return self.descricao


class Orcamento(models.Model):
    paciente = models.ForeignKey(CadastroPacientes, on_delete=models.CASCADE)
    procedimentos = models.ManyToManyField(Procedimento)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def calcular_total(self):
        return sum(procedimento.valor for procedimento in self.procedimentos.all())

    def __str__(self):
        return f'Orcamento para {self.paciente.nome} em {self.data_criacao}'
    
