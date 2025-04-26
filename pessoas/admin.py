from django.contrib import admin
from .models import Pessoa

# Registra o modelo Pessoa no admin do Django
admin.site.register(Pessoa)