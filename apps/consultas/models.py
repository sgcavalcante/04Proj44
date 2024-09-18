# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from apps.CadastroUsuario.models import CadastroPacientes  # Importe seu modelo de pacientes
class Consulta(models.Model):
    paciente = models.ForeignKey(CadastroPacientes, on_delete=models.CASCADE)  # Use CadastroPacientes
    data_horario = models.DateTimeField()
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return f"Consulta de {self.paciente} em {self.data_horario}"
