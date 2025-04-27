from django.shortcuts import render
from .models import Evento, Participacao

# View para listar todos os eventos
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista.html', {'eventos': eventos})

# View para listar todas as participações
def lista_participacoes(request):
    participacoes = Participacao.objects.all()
    return render(request, 'eventos/participacoes.html', {'participacoes': participacoes})