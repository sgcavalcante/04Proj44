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
            return redirect('consultas')  # Redireciona para a lista de pacientes após o agendamento
    else:
        form = ConsultaForm()

    return render(request, 'agendar_consulta.html', {'form': form, 'Pacientes': paciente})


@login_required
def consultas(request):
    consultas = Consulta.objects.filter()
    return render(request, 'lista_consultas.html', {'consultas': consultas})

