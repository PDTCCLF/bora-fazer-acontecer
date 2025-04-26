from django.shortcuts import render
from .models import Pessoa

# View para listar todas as pessoas
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas/lista.html', {'pessoas': pessoas})
