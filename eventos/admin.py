from django.contrib import admin
from .models import Evento, Participacao

# Registra o modelo Evento no admin
admin.site.register(Evento)

# Registra o modelo Participacao no admin
admin.site.register(Participacao)