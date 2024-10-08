"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from apps.OrcamentoPaciente import urls
from apps.CadastroUsuario import urls
from apps.CadastroProprietario import urls
from apps.consultas import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('apps.CadastroUsuario.urls')),
    path('',include('apps.CadastroProprietario.urls')),
    #path('',include('apps.OrcamentoPaciente.urls')),
    path('',include('apps.Orcamentos.urls')),
    path('',include('apps.consultas.urls')),
]
