from django.urls import path
from apps.CadastroUsuario.views import index,Clinica,login


urlpatterns = [
            path('',index,name= 'index'),
            path('Clinica',Clinica, name = 'Clinica'),
            path('login',login,name="login"),
]