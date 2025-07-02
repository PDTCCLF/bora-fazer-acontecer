from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Participacao
from .forms import EventoForm, ParticipacaoForm
from django.contrib.auth.decorators import login_required

@login_required
# View para listar todos os eventos
def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista.html', {'eventos': eventos})

@login_required
# View para listar todas as participações
def lista_participacoes(request):
    participacoes = Participacao.objects.all()
    return render(request, 'eventos/participacoes.html', {'participacoes': participacoes})

@login_required
# Criar evento
def criar_evento(request):
    form = EventoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_eventos')
    return render(request, 'eventos/formulario.html', {'form': form, 'titulo': 'Criar Evento'})

@login_required
# Criar participação
def criar_participacao(request):
    form = ParticipacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_participacoes')
    return render(request, 'eventos/formulario_participacao.html', {'form': form, 'titulo': 'Criar Participação'})

@login_required
# Editar evento
def editar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    form = EventoForm(request.POST or None, instance=evento)
    if form.is_valid():
        form.save()
        return redirect('lista_eventos')
    return render(request, 'eventos/formulario.html', {'form': form, 'titulo': 'Editar Evento'})

@login_required
# Editar participação
def editar_participacao(request, pk):
    participacao = get_object_or_404(Participacao, pk=pk)
    form = ParticipacaoForm(request.POST or None, instance=participacao)
    if form.is_valid():
        form.save()
        return redirect('lista_participacoes')
    return render(request, 'eventos/formulario_participacao.html', {'form': form, 'titulo': 'Editar Participação'})

@login_required
# Deletar evento
def deletar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')
    return render(request, 'eventos/confirma_deletar.html', {'evento': evento})

@login_required
# Deletar participação
def deletar_participacao(request, pk):
    participacao = get_object_or_404(Participacao, pk=pk)
    if request.method == 'POST':
        participacao.delete()
        return redirect('lista_participacoes')
    return render(request, 'eventos/confirma_deletar_participacao.html', {'participacao': participacao})