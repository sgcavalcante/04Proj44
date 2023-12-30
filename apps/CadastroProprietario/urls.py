from django.urls import path
from apps.CadastroProprietario.views import loginProprietario,registroProprietario,listar_proprietarios


urlpatterns = [
        path('loginProprietario',loginProprietario,name='loginProprietario'),
        path('registroProprietario/',registroProprietario,name='registroProprietario'),
        path('listar_proprietarios/',listar_proprietarios,name='listar_proprietarios')
]