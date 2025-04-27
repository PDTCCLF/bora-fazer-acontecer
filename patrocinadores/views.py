from django.shortcuts import render
from .models import Patrocinador, FinanciamentoEvento

# View para listar todos os patrocinadores
def lista_patrocinadores(request):
    patrocinadores = Patrocinador.objects.all()
    return render(request, 'patrocinadores/lista.html', {'patrocinadores': patrocinadores})

# View para listar todos os financiamentos de eventos
def lista_financiamentos(request):
    financiamentos = FinanciamentoEvento.objects.all()
    return render(request, 'patrocinadores/financiamentos.html', {'financiamentos': financiamentos})