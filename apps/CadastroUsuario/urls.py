from django.urls import path
from apps.CadastroUsuario.views import index,Clinica,erro,configuracao,cadastrar_paciente,listar_dados,remover#login,


urlpatterns = [
            path('',index,name= 'index'),
            path('Clinica',Clinica, name = 'Clinica'),
            path('configuracao',configuracao,name='configuracao'), 
            #path('login',login,name='login'),
            path('erro',erro,name='erro'),
            path('cadastrar_paciente',cadastrar_paciente,name='cadastrar_paciente'),
            path('listar_dados',listar_dados,name='listar_dados'),
            path('remover<int:id>',remover,name='remover'),
]