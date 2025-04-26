from django.contrib import admin
from .models import Patrocinador, FinanciamentoEvento

# Registra o modelo Patrocinador no admin
admin.site.register(Patrocinador)

# Registra o modelo FinanciamentoEvento no admin
admin.site.register(FinanciamentoEvento)