from django.contrib import admin
from .models import Dente,Procedimento,Orcamento,ItemOrcamento
# Register your models here.
admin.site.register(Dente)
admin.site.register(Procedimento)
admin.site.register(Orcamento)
admin.site.register(ItemOrcamento)