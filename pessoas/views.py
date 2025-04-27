from django.shortcuts import render
from .models import Pessoa, Aluno, Voluntario

# View para listar todas as pessoas
def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoas/lista.html', {'pessoas': pessoas})

# View para listar todos os alunos
def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'pessoas/alunos.html', {'alunos': alunos})

# View para listar todos os voluntários
def lista_voluntarios(request):
    voluntarios = Voluntario.objects.all()
    return render(request, 'pessoas/voluntarios.html', {'voluntarios': voluntarios})
