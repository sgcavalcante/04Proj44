from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ConsultaForm
from .models import Consulta
from apps.CadastroUsuario.models import CadastroPacientes
from .forms import ConsultaForm


@login_required
def agendar_consulta(request, paciente_id):
    paciente = get_object_or_404(CadastroPacientes, id=paciente_id)

    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.paciente = paciente  # Associa o paciente à consulta
            consulta.save()
            return redirect('calendario_consultas')  # Redireciona para a lista de pacientes após o agendamento
    else:
        form = ConsultaForm()

    return render(request, 'agendar_consulta.html', {'form': form, 'paciente': paciente})

'''
@login_required
def consultas(request):
    consultas = Consulta.objects.filter()
    return render(request, 'lista_consultas.html', {'consultas': consultas})

'''
from django.http import JsonResponse
from django.shortcuts import render
from .models import Consulta
from apps.CadastroUsuario.models import CadastroPacientes
import datetime

@login_required
def calendario_consultas(request):
    return render(request, 'lista_consultas.html')  # Template com o calendário

@login_required
def eventos_consultas(request):
    consultas = Consulta.objects.all()
    eventos = []
    
    for consulta in consultas:
        eventos.append({
            'title': f'Consulta: {consulta.paciente.nome}',  # Exibe o nome do paciente
            'start': consulta.data_horario.isoformat(),  # Data e hora de início
            'description': consulta.descricao,  # Descrição da consulta
        })
    
    return JsonResponse(eventos, safe=False)  # Retorna os eventos em formato JSON
