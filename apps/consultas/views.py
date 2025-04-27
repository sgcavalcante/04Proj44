from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotAllowed
from datetime import datetime, timedelta
from .models import Consulta
from apps.CadastroUsuario.models import CadastroPacientes
from django.utils.dateparse import parse_datetime
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_POST

  
@login_required
def agendar_consulta(request, paciente_id):
    user = request.user
    paciente = get_object_or_404(CadastroPacientes, id=paciente_id, usuario=user)

    if request.method == 'GET':
        return render(request, 'consulta/agendar_consulta.html', {
            'paciente': paciente,
            'doutor': user
        })

    if request.method == 'POST':
        data_inicio = request.POST.get('data_horario')
        data_fim = request.POST.get('data_horario_end')
        descricao = request.POST.get('descricao')

        # Função auxiliar para parse de data
        def parse_dt(d):
            for fmt in ('%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%dT%H:%M:%S'):
                try:
                    return datetime.strptime(d, fmt)
                except ValueError:
                    continue
            return None

        inicio = parse_dt(data_inicio)
        fim = parse_dt(data_fim)
        if not inicio or not fim or not descricao:
            return JsonResponse({'error': 'Dados incompletos ou inválidos.'}, status=400)

        # Ajusta horas cheias
        inicio = inicio.replace(minute=0, second=0, microsecond=0)
        fim = fim.replace(minute=0, second=0, microsecond=0)
        if fim <= inicio:
            fim = inicio + timedelta(hours=1)

        # Verifica conflit
        conflito = Consulta.objects.filter(
            paciente__usuario=user,
            data_horario__lt=fim,
            data_horario_end__gt=inicio
        ).exists()
        if conflito:
            return JsonResponse({'error': 'Já existe uma consulta nesse horário.'}, status=400)

        # Cria consulta e retorna ID
        consulta = Consulta.objects.create(
            paciente=paciente,
            data_horario=inicio,
            data_horario_end=fim,
            descricao=descricao
        )
        return JsonResponse({'id': consulta.id, 'message': 'Consulta agendada com sucesso.'})

    return HttpResponseNotAllowed(['GET', 'POST'])



@login_required
def eventos_consultas(request):
    start_str = request.GET.get('start')
    end_str = request.GET.get('end')
    start_dt = parse_datetime(start_str)
    end_dt = parse_datetime(end_str)
    if not start_dt or not end_dt:
        return JsonResponse({'error': 'Parâmetros inválidos'}, status=400)

    doutor = request.user
    pacientes = CadastroPacientes.objects.filter(usuario=doutor)

    consultas = Consulta.objects.filter(
        paciente__in=pacientes,
        data_horario__lt=end_dt,
        data_horario_end__gt=start_dt
    )

    eventos = []
    for consulta in consultas:
        eventos.append({
            'id': consulta.id,
            'title': consulta.paciente.nome,
            'start': consulta.data_horario.isoformat(),
            'end': consulta.data_horario_end.isoformat(),
            'backgroundColor': '#dc3545',
            'borderColor': '#dc3545',
            'textColor': '#ffffff',
            'extendedProps': {'type': 'booked', 'consultaId': consulta.id},
        })
    return JsonResponse(eventos, safe=False)


@login_required
def calendario_consultas(request):
    consultas = Consulta.objects.all().order_by('data_horario')
    #
    #procedimentos = Procedimento.objects.all()
    return render(request, 'consulta/calendario_consultas.html',{'consultas':consultas})



@require_POST
@login_required
def remover_consulta(request, paciente_id):
    
    consulta_id = request.POST.get('consulta_id')
    if not consulta_id:
        return JsonResponse({'error':'ID não fornecido.'}, status=400)
    consulta = get_object_or_404(
        Consulta,
        id=consulta_id,
        paciente__id=paciente_id,
        paciente__usuario=request.user
    )
    consulta.delete()
    return JsonResponse({'success':True})
