from django.db import models
from base.models import Base
from pessoas.models import Aluno


class Evento(Base):
    """
    Representa um evento cultural ou esportivo organizado pela ONG.
    """
    codigo_evento = models.CharField(max_length=20, unique=True) # ID próprio da ONG
    nome = models.CharField(max_length=150)
    data = models.DateField()
    hora_inicio = models.TimeField()
    duracao = models.DurationField(blank=True, null=True) # opcional
    descricao = models.TextField(blank=True, null=True) # opcional
    local = models.CharField(max_length=200)

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

    def __str__(self):
        return f"{self.aluno.nome_completo} inscrito em {self.evento.nome}"
