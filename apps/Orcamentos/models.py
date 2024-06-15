# Create your models here.
# orcamentos/models.py
from django.db import models
from apps.CadastroUsuario.models import CadastroPacientes
import uuid

#class Paciente(models.Model):
    #nome = models.CharField(max_length=100)
    #cpf = models.CharField(max_length=11, unique=True)

    #def __str__(self):
        #return self.nome

class Dente(models.Model):
    numero = models.IntegerField(unique=True,blank=True,)
    descricao = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='Odontograma/')

    def __str__(self):
        return f"Dente {self.numero} - {self.descricao}"
    

    

   

class Procedimento(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Orcamento(models.Model):
    numero = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    paciente = models.ForeignKey(CadastroPacientes, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orçamento {self.numero} para {self.paciente.nome}"

class ItemOrcamento(models.Model):
    orcamento = models.ForeignKey(Orcamento, on_delete=models.CASCADE)
    dente = models.ForeignKey(Dente, on_delete=models.CASCADE)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.procedimento.nome} para {self.dente.numero}"
