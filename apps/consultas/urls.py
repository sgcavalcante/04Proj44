from django.urls import path

from apps.consultas.views import agendar_consulta,consultas

urlpatterns = [
    path('agendar_consulta/<int:paciente_id>/', agendar_consulta, name='agendar_consulta'),
    path('consultas/', consultas, name='consultas'),
]
