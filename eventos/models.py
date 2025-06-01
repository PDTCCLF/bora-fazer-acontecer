from django.db import models
from base.models import Base
from pessoas.models import Aluno
from datetime import date
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from bora_fazer_acontecer.utils import gerar_identificador_legivel


class Evento(Base):
    """
    Representa um evento cultural ou esportivo organizado pela ONG.
    """
    codigo_evento = models.CharField(max_length=100, unique=True, editable=False) # ID próprio do evento
    nome = models.CharField(max_length=150)
    data = models.DateField()
    hora_inicio = models.TimeField()
    duracao = models.TextField(blank=True, null=True) # opcional
    descricao = models.TextField(blank=True, null=True) # opcional
    local = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        # Gera codigo_evento apenas na criação
        if not self.codigo_evento:
            codigo = gerar_identificador_legivel()

            # Verifica unicidade
            if Evento.objects.filter(codigo_evento=codigo).exists():
                raise ValidationError(f"O código ID do evento {codigo} já existe, tente novamente.")

            self.codigo_evento = codigo

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} em {self.data}"


class Participacao(Base):
    """
    Representa a inscrição de um aluno em um evento.
    A inscrição pode ser removida para cancelar a participação.
    """
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name="participacoes")
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="participacoes")

    class Meta:
        unique_together = ('aluno', 'evento')  # evita duplicar inscrições
        verbose_name = "Participação"
        verbose_name_plural = "Participações"

    def __str__(self):
        return f"{self.aluno.nome_completo} inscrito em {self.evento.nome}"
