from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ConsultaForm
from .models import Consulta
from apps.CadastroUsuario.models import CadastroPacientes
from .forms import ConsultaForm
from datetime import datetime,timedelta
from django.http import JsonResponse
 
from django.utils.dateparse import parse_datetime        # <-- aqui
from .models import Consulta, CadastroPacientes
from django.views.decorators.cache import cache_page 

@login_required
def agendar_consulta(request, paciente_id):
    doutor = request.user
    paciente = get_object_or_404(CadastroPacientes, id=paciente_id, usuario=doutor)

    # GET → exibe a página com o FullCalendar
    if request.method == 'GET':
        return render(request, 'consulta/agendar_consulta.html', {
            'paciente': paciente,
            'doutor': doutor
        })

    # POST → recebimento via AJAX
    if request.method == 'POST':
        ds = request.POST.get('data_horario')
        de = request.POST.get('data_horario_end')
        desc = request.POST.get('descricao')

        # valida campos
        if not ds or not de or not desc:
            return JsonResponse({
                'error': 'Campos data_horario, data_horario_end e descricao são obrigatórios.'
            }, status=400)

        # parsing robusto
        def _parse(dt_str):
            for fmt in ('%Y-%m-%dT%H:%M:%S.%fZ','%Y-%m-%dT%H:%M:%S'):
                try:
                    return datetime.strptime(dt_str, fmt)
                except ValueError:
                    continue
            return None

        start = _parse(ds)
        end   = _parse(de)
        if not start or not end:
            return JsonResponse({'error': 'Formato de data inválido.'}, status=400)

        # zera minutos/segundos e garante +1h mínimo
        start = start.replace(minute=0, second=0, microsecond=0)
        if end <= start:
            end = start + timedelta(hours=1)

        # checa conflito de intervalo para este doutor
        conflict = Consulta.objects.filter(
            paciente__usuario=doutor,
            data_horario__lt=end,
            data_horario_end__gt=start
        ).exists()
        if conflict:
            return JsonResponse({'error': 'Já existe uma consulta nesse intervalo.'}, status=400)

        # salva
        Consulta.objects.create(
            paciente=paciente,
            descricao=desc,
            data_horario=start,
            data_horario_end=end
        )
        return JsonResponse({'message': 'Consulta agendada com sucesso!'}, status=200)

    # outros métodos não permitidos
    return HttpResponseNotAllowed(['GET','POST'])




 

@login_required
def calendario_consultas(request):
    #pacientes = CadastroPacientes.objects.filter(usuario=request.user) 
    usuario=request.user
    print(usuario)
    return render(request, 'consulta/lista_consultas.html',{'doutor':usuario})  # Template com o calendário

@login_required
@cache_page(30)   # cache de 30s
def eventos_consultas(request):
    # 1) Parse dos parâmetros de data
    start_str = request.GET.get('start')
    end_str   = request.GET.get('end')
    start_dt  = parse_datetime(start_str)
    end_dt    = parse_datetime(end_str)
    if not start_dt or not end_dt:
        return JsonResponse({'error': 'Parâmetros inválidos'}, status=400)

    user = request.user

    # 2) Consulta única ao banco para obter apenas os agendados no intervalo
    pacientes = CadastroPacientes.objects.filter(usuario=user)
    consultas = Consulta.objects.filter(
        paciente__in=pacientes,
        data_horario__lt=end_dt,
        data_horario_end__gt=start_dt
    )

    # 3) Inicializa a lista de eventos
    eventos = []

    # 4) Preenche os eventos “sólidos” (agendados)
    for c in consultas:
        eventos.append({
            'title':           f'Consulta: {c.paciente.nome}',
            'start':           c.data_horario.isoformat(),
            'end':             c.data_horario_end.isoformat(),
            'backgroundColor': '#dc3545',
            'borderColor':     '#dc3545',
            'extendedProps':   {'type': 'booked'},
        })

    # 5) Gera os slots livres (08–18) em memória
    work_start = 8
    work_end   = 18
    dia = start_dt.replace(hour=0, minute=0, second=0, microsecond=0)

    while dia < end_dt:
        for hora in range(work_start, work_end):
            slot_start = dia.replace(hour=hora)
            slot_end   = slot_start + timedelta(hours=1)

            if slot_start < start_dt or slot_end > end_dt:
                continue

            # checa se existe interseção com algum agendado
            ocupado = consultas.filter(
                data_horario__lt=slot_end,
                data_horario_end__gt=slot_start
            ).exists()

            if not ocupado:
                eventos.append({
                    'title':           'Livre',
                    'start':           slot_start.isoformat(),
                    'end':             slot_end.isoformat(),
                    'backgroundColor': '#198754',
                    'borderColor':     '#198754',
                    'textColor':       '#ffffff',
                    'extendedProps':   {'type': 'free'},
                })
        dia += timedelta(days=1)

    # 6) Retorna tudo em JSON
    return JsonResponse(eventos, safe=False)