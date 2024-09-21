from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ConsultaForm
from .models import Consulta
from apps.CadastroUsuario.models import CadastroPacientes
from .forms import ConsultaForm
from datetime import datetime,timedelta
from django.http import JsonResponse
 

@login_required

def agendar_consulta(request, paciente_id):
    paciente = get_object_or_404(CadastroPacientes, id=paciente_id)

    # Tratamento do método GET para renderizar o formulário
    if request.method == 'GET':
        form = ConsultaForm()
        return render(request, 'agendar_consulta.html', {'form': form, 'paciente': paciente})

    # Lida com o envio do formulário via POST
    if request.method == 'POST':
        data_horario = request.POST.get('data_horario')
        descricao = request.POST.get('descricao')

        if data_horario:
            try:
                data_horario = datetime.strptime(data_horario, '%Y-%m-%dT%H:%M:%S.%fZ')
            except ValueError:
                data_horario = datetime.strptime(data_horario, '%Y-%m-%dT%H:%M:%S')
            data_horario = data_horario.replace(minute=0)

        if not data_horario:
            return JsonResponse({'error': 'Data e hora não foram fornecidas.'}, status=400)

        # Preenche o formulário com os dados recebidos via POST
        form = ConsultaForm({'descricao': descricao})

        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.paciente = paciente
            consulta.data_horario = data_horario

            # Verifica se já existe uma consulta marcada no mesmo horário
            if Consulta.objects.filter(data_horario=consulta.data_horario).exists():
                return JsonResponse({'error': 'Já existe uma consulta marcada para este horário.'}, status=400)
            else:
                consulta.save()
                return JsonResponse({'message': 'Consulta agendada com sucesso!'}, status=200)

    return JsonResponse({'error': 'Método inválido'}, status=405)
'''
@login_required
def consultas(request):
    consultas = Consulta.objects.filter()
    return render(request, 'lista_consultas.html', {'consultas': consultas})

'''

 

@login_required
def calendario_consultas(request):
    return render(request, 'lista_consultas.html')  # Template com o calendário

@login_required
def eventos_consultas(request):
    consultas = Consulta.objects.all()  # Busca todas as consultas agendadas
    eventos = []

    for consulta in consultas:
        eventos.append({
            'title': f'Consulta: {consulta.paciente.nome}',
            'start': consulta.data_horario.isoformat(),
            'end': (consulta.data_horario + timedelta(hours=1)).isoformat(),  # Define a duração de 1h
            'description': consulta.descricao,
            'backgroundColor': '#ff0000',  # Cor do evento
            'borderColor': '#ff0000',
        })

    return JsonResponse(eventos, safe=False)