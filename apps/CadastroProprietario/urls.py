from django.urls import path
from apps.CadastroProprietario.views import loginProprietario,registroProprietario


urlpatterns = [
        path('loginProprietario',loginProprietario,name='loginProprietario'),
        path('registroProprietario/',registroProprietario,name='registroProprietario')
]