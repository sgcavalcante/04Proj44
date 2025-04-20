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
def eventos_consultas(request):
    """
    Retorna lista de consultas do médico autenticado no formato JSON para o FullCalendar.
    Cada evento inclui título, início, término e cores.
    """
    doutor = request.user
    pacientes = CadastroPacientes.objects.filter(usuario=doutor)
    consultas = Consulta.objects.filter(paciente__in=pacientes)

    eventos = []
    for consulta in consultas:
        start = consulta.data_horario
        # Usa data_horario_end salvo; se for None, assume 1h de duração
        if consulta.data_horario_end:
            end = consulta.data_horario_end
        else:
            end = start + timedelta(hours=1)

        eventos.append({
            'title': f'Consulta: {consulta.paciente.nome}',
            'start': start.isoformat(),
            'end':   end.isoformat(),
            'description': consulta.descricao,
            'backgroundColor': '#ff0000',
            'borderColor': '#ff0000',
        })

    return JsonResponse(eventos, safe=False)
