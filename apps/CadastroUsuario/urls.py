from django.urls import path
from apps.CadastroUsuario.views import index,Clinica,erro,configuracao,cadastrar_paciente,listar_dados,remover,editar,gallery,paciente_acoes,fotos_tratamento#login,
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
            path('',index,name= 'index'),
            path('Clinica',Clinica, name = 'Clinica'),
            path('configuracao',configuracao,name='configuracao'), 
            #path('login',login,name='login'),
            path('erro',erro,name='erro'),
            path('cadastrar_paciente',cadastrar_paciente,name='cadastrar_paciente'),
            path('listar_dados',listar_dados,name='listar_dados'),
            path('remover<int:id>',remover,name='remover'),
            path('editar/<int:id>',editar,name='editar'),
            path('gallery/<int:paciente_id>',gallery,name='gallery'),
            path('paciente_acoes/<int:id>',paciente_acoes,name='paciente_acoes'),
            path('fotos_tratamento/<int:paciente_id>',fotos_tratamento,name='fotos_tratamento'),
            
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)