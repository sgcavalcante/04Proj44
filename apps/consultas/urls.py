from django.urls import path

from apps.consultas.views import agendar_consulta,calendario_consultas,eventos_consultas#consultas

urlpatterns = [
    path('agendar_consulta/<int:paciente_id>/', agendar_consulta, name='agendar_consulta'),
    #path('consultas/', consultas, name='consultas'),
    path('calendario_consultas/', calendario_consultas, name='calendario_consultas'),  # Página do calendário
    path('eventos_consultas/', eventos_consultas, name='eventos_consultas'),  # Endpoint para os dados do calendário
]
