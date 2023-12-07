from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apps.OrcamentoPaciente.views import criar_orcamento

urlpatterns = [
                path('criar_orcamento/<int:paciente_id>/',criar_orcamento, name = 'criar_orcamento'),
              ]