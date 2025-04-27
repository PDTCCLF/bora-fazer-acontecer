from django.db import models
from base.models import Base
from eventos.models import Evento

class Patrocinador(Base):
    """
    Representa uma empresa ou instituição que financia eventos.
    """
    CAMPO_ATIVIDADE_CHOICES = [
        ('EDUCAO', 'Educação e Treinamento'),
        ('ESPORTE', 'Esporte e Recreação'),
        ('ARTES', 'Artes e Cultura'),
        ('SAUDE', 'Saúde e Bem-estar'),
        ('COMUNIDADE', 'Desenvolvimento Comunitário'),
        ('MEIO_AMBIENTE', 'Meio Ambiente'),
        ('OUTRO', 'Outro'),
    ]

    nome = models.CharField(max_length=150)
    telefone_contato = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    documento_id = models.CharField(max_length=50, blank=True, null=True)  # CNPJ, registro etc.
    campo_atividade = models.CharField(max_length=20, choices=CAMPO_ATIVIDADE_CHOICES)

    class Meta:
        verbose_name = "Patrocinador"
        verbose_name_plural = "Patrocinadores"

    def __str__(self):
        return self.nome


class FinanciamentoEvento(Base):
    """
    Representa um financiamento de um patrocinador para um evento específico.
    """
    patrocinador = models.ForeignKey(Patrocinador, on_delete=models.CASCADE, related_name="financiamentos")
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="financiamentos")
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateField(auto_now_add=True)  # data do registro do financiamento

    class Meta:
        unique_together = ('patrocinador', 'evento')  # evita duplicar financiamentos
        verbose_name = "Financiamento de Evento"
        verbose_name_plural = "Financiamentos de Eventos"

    def __str__(self):
        return f"{self.patrocinador.nome} → {self.evento.nome} ({self.valor})"
