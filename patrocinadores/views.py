from django.shortcuts import render, get_object_or_404, redirect
from .models import Patrocinador, FinanciamentoEvento
from .forms import PatrocinadorForm, FinanciamentoEventoForm
from django.contrib.auth.decorators import login_required

@login_required
# View para listar todos os patrocinadores
def lista_patrocinadores(request):
    patrocinadores = Patrocinador.objects.all()
    return render(request, 'patrocinadores/lista.html', {'patrocinadores': patrocinadores})

@login_required
# View para listar todos os financiamentos de eventos
def lista_financiamentos(request):
    financiamentos = FinanciamentoEvento.objects.all()
    return render(request, 'patrocinadores/financiamentos.html', {'financiamentos': financiamentos})

@login_required
# Criar patrocinador
def criar_patrocinador(request):
    form = PatrocinadorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_patrocinadores')
    return render(request, 'patrocinadores/formulario.html', {'form': form, 'titulo': 'Criar Patrocinador'})

@login_required
# Criar financiamento de evento
def criar_financiamento(request):
    form = FinanciamentoEventoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_financiamentos')
    return render(request, 'patrocinadores/formulario_financiamento.html', {'form': form, 'titulo': 'Criar Financiamento de Evento'})

@login_required
# Editar patrocinador
def editar_patrocinador(request, pk):
    patrocinador = get_object_or_404(Patrocinador, pk=pk)
    form = PatrocinadorForm(request.POST or None, instance=patrocinador)
    if form.is_valid():
        form.save()
        return redirect('lista_patrocinadores')
    return render(request, 'patrocinadores/formulario.html', {'form': form, 'titulo': 'Editar Patrocinador'})

@login_required
# Editar financiamento de evento
def editar_financiamento(request, pk):
    financiamento = get_object_or_404(FinanciamentoEvento, pk=pk)
    form = FinanciamentoEventoForm(request.POST or None, instance=financiamento)
    if form.is_valid():
        form.save()
        return redirect('lista_financiamentos')
    return render(request, 'patrocinadores/formulario_financiamento.html', {'form': form, 'titulo': 'Editar Financiamento de Evento'})

@login_required
# Deletar patrocinador
def deletar_patrocinador(request, pk):
    patrocinador = get_object_or_404(Patrocinador, pk=pk)
    if request.method == 'POST':
        patrocinador.delete()
        return redirect('lista_patrocinadores')
    return render(request, 'patrocinadores/confirma_deletar.html', {'patrocinador': patrocinador})

@login_required
# Deletar financiamento de evento
def deletar_financiamento(request, pk):
    financiamento = get_object_or_404(FinanciamentoEvento, pk=pk)
    if request.method == 'POST':
        financiamento.delete()
        return redirect('lista_financiamentos')
    return render(request, 'patrocinadores/confirma_deletar_financiamento.html', {'financiamento': financiamento})