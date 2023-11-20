from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class CadastroPacientes(models.Model):

     

    nome=models.CharField(
        max_length=120,
        null=False,
        blank=False
    )

    telefone=models.CharField(
        max_length=15,
        null=False,
        blank=False
    )

    email=models.EmailField(
        max_length=40,
        null=False,
        blank=False
    )
    data_nascimento=models.DateField(
        null=False,
        blank=False,
        
    )
    profissao=models.CharField(
        max_length=40,
        null=False,
        blank=False
    )

    cep = models.CharField(
        max_length=9,
        null=True,
        blank=True
    )

    estado = models.CharField(
        max_length=2,
        null=True,
        blank=True
    )

    cidade = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    bairro = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    rua = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )

    numero = models.IntegerField(
        
        null=True,
        blank=True
    )

    complemento = models.TextField(
        max_length=400,
        null=True,
        blank=True
    )

    alergia = models.CharField(
        max_length=400,
        null=False,
        blank=False
    )

     
    doencas_conhecidas = models.CharField(
        max_length=400,
        null=False,
        blank=False
    )
    
class Image(models.Model):

    name = models.CharField(max_length=50,default=None)
    imagem = models.ImageField(upload_to='images/',default=None)
    
