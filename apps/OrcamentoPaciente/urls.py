from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apps.OrcamentoPaciente.views import orcamento,orcamento_dente,teste,criar_orcamento,sucesso,inserir_fotos_dentes
urlpatterns = [
                path('orcamento/<int:paciente_id>/',orcamento, name = 'orcamento'),
                path('orcamento_dente/',orcamento_dente, name = 'orcamento_dente'),
                path('teste/<int:paciente_id>',teste, name = 'teste'),
                path('criar_orcamento/<int:paciente_id>/<int:dente_id>/',criar_orcamento, name = 'criar_orcamento'),
                path('orcamento_dente',orcamento_dente, name = 'orcamento_dente'),
                path('sucesso',sucesso, name = 'sucesso'),
                path('inserir_fotos_dentes',inserir_fotos_dentes, name = 'inserir_fotos_dentes'),
                 
              ]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)