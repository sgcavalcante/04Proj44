from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apps.OrcamentoPaciente.views import orcamento,orcamento_dente,teste,criar_orcamento,sucesso,inserir_fotos_dentes,cadastrar_item,erro_orcamento,listar_orcamento,abir_novo_orcamento
 
urlpatterns = [
                path('orcamento/<int:paciente_id>/',orcamento, name = 'orcamento'),
                path('orcamento_dente/',orcamento_dente, name = 'orcamento_dente'),
                path('teste/<int:paciente_id>',teste, name = 'teste'),
                path('criar_orcamento/<int:paciente_id>/<int:dente_id>/',criar_orcamento, name = 'criar_orcamento'),
                path('orcamento_dente',orcamento_dente, name = 'orcamento_dente'),
                path('sucesso',sucesso, name = 'sucesso'),
                path('erro_orcamento',erro_orcamento, name = 'erro_orcamento'),
                path('inserir_fotos_dentes',inserir_fotos_dentes, name = 'inserir_fotos_dentes'),
                path('cadastrar_item',cadastrar_item, name = 'cadastrar_item'),
                path('listar_orcamento',listar_orcamento, name = 'listar_orcamento'),
                path('abir_novo_orcamento/<int:paciente_id>',abir_novo_orcamento, name = 'abir_novo_orcamento'),
                
              ]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)