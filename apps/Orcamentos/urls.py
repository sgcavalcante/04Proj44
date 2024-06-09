# apps/orcamentos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('criar_orcamento/', views.criar_orcamento, name='criar_orcamento'),
    #path('gerar_pdf/<int:orcamento_id>/', views.gerar_pdf, name='gerar_pdf'),
    path('relatorio_geral/', views.relatorio_geral, name='relatorio_geral'),
    path('gerar_html/<uuid:orcamento_id>/', views.gerar_html, name='gerar_html'),
    path('alista_orcamentos/', views.alista_orcamentos, name='alista_orcamentos'),
     
]