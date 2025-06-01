from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from base.models import Base
from bora_fazer_acontecer.utils import gerar_identificador_legivel


class Pessoa(Base):
    """
    Representa uma pessoa no sistema.
    Pode ser especializada como Aluno ou Voluntario.
    """
    matricula_id = models.CharField(max_length=100, unique=True, editable=False) # matricula na ong
    nome_completo = models.CharField(max_length=100)
    id_nacional = models.CharField(max_length=20, blank=True, null=True) # opcional
    telefone = models.CharField(max_length=20, blank=True, null=True) # opcional
    email = models.EmailField(blank=True, null=True) # opcional
    endereco = models.TextField()
    data_matricula = models.DateField(editable=False) # data de entrada na ong
    data_nascimento = models.DateField()
    data_saida = models.DateField(blank=True, null=True) # data de saída da ong, opcional
    status_ativo = models.BooleanField(default=True, editable=False) # se a pessoa está ativa na ong

    def save(self, *args, **kwargs):
        # Se for novo registro, define data_matricula
        if not self.pk:
            self.data_matricula = date.today()

        # Gera matricula_id apenas na criação
        if not self.matricula_id:
            codigo = gerar_identificador_legivel()

            # Verifica unicidade
            if Pessoa.objects.filter(matricula_id=codigo).exists():
                raise ValidationError(f"A matrícula {codigo} já existe, tente novamente.")

            self.matricula_id = codigo

        # Ajusta status conforme data_saida
        self.status_ativo = False if self.data_saida else True

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_completo} ({self.matricula_id})"


class Aluno(Pessoa):
    """
    Alunos são pessoas matriculadas em classes e eventos.
    """
    #
    
    def __str__(self):
        return f"Aluno: {self.nome_completo}"


class Voluntario(Pessoa):
    """
    Voluntarios são pessoas que também possuem contas de usuário Django para acesso administrativo.
    """
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Voluntário"
        verbose_name_plural = "Voluntários"

    def __str__(self):
        return f"Voluntario: {self.nome_completo}"
