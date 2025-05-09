from django.db import models
from django.contrib.auth.models import User
from base.models import Base


class Pessoa(Base):
    """
    Representa uma pessoa no sistema.
    Pode ser especializada como Aluno ou Voluntario.
    """
    matricula_id = models.CharField(max_length=20, unique=True) # matricula na ong
    nome_completo = models.CharField(max_length=100)
    id_nacional = models.CharField(max_length=20, blank=True, null=True) # opcional
    telefone = models.CharField(max_length=20, blank=True, null=True) # opcional
    email = models.EmailField(blank=True, null=True) # opcional
    endereco = models.TextField()
    data_matricula = models.DateField() # data de entrada na ong
    data_nascimento = models.DateField()
    data_saida = models.DateField(blank=True, null=True) # data de saída da ong, opcional
    status_ativo = models.BooleanField(default=True) # se a pessoa está ativa na ong

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
