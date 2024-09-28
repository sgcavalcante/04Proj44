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
    # Tenta buscar o paciente relacionado ao doutor (usuário autenticado)
    doutor = request.user
    
    # Filtra os pacientes cadastrados pelo doutor logado
    paciente = get_object_or_404(CadastroPacientes, id=paciente_id, usuario=doutor)

    # Tratamento do método GET para renderizar o formulário
    if request.method == 'GET':
        form = ConsultaForm()
        return render(request, 'consulta/agendar_consulta.html', {'form': form, 'paciente': paciente, 'doutor': doutor})

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


 

@login_required
def calendario_consultas(request):
    #pacientes = CadastroPacientes.objects.filter(usuario=request.user) 
    usuario=request.user
    print(usuario)
    return render(request, 'consulta/lista_consultas.html',{'doutor':usuario})  # Template com o calendário

@login_required
def eventos_consultas(request):
# Obtém o doutor (usuário logado)
    doutor = request.user

    # Filtra os pacientes cadastrados pelo doutor logado
    pacientes = CadastroPacientes.objects.filter(usuario=doutor)

    # Filtra as consultas apenas dos pacientes cadastrados pelo doutor logado
    consultas = Consulta.objects.filter(paciente__in=pacientes)

    # Prepara os eventos para o FullCalendar
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