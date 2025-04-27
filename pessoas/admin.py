from django.contrib import admin
from .models import Pessoa, Aluno, Voluntario

# Registra o modelo Pessoa no admin do Django
admin.site.register(Pessoa)

# Registra o modelo Aluno no admin do Django
admin.site.register(Aluno)

# Registra o modelo Voluntario no admin do Django
admin.site.register(Voluntario)