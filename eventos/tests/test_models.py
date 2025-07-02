from django.test import TestCase
from django.core.exceptions import ValidationError
from pessoas.models import Aluno
from eventos.models import Evento, Participacao
from datetime import date, time
from decimal import Decimal


class EventoModelTests(TestCase):
    """Testes para o model Evento."""

    def setUp(self):
        self.evento = Evento.objects.create(
            nome="Campeonato de Futebol",
            data=date.today(),
            hora_inicio=time(14, 0),
            local="Quadra da ONG"
        )

    def test_codigo_evento_gerado_automaticamente(self):
        self.assertIsNotNone(self.evento.codigo_evento)
        self.assertNotEqual(self.evento.codigo_evento, "")

    def test_codigo_evento_unico(self):
        # Forçar duplicação manual
        with self.assertRaises(ValidationError):
            evento2 = Evento(
                nome="Outro Evento",
                data=date.today(),
                hora_inicio=time(10, 0),
                local="Praça"
            )
            evento2.codigo_evento = self.evento.codigo_evento  # força duplicação
            evento2.full_clean()  # dispara validações

    def test_str_evento(self):
        esperado = f"{self.evento.nome} em {self.evento.data}"
        self.assertEqual(str(self.evento), esperado)


class ParticipacaoModelTests(TestCase):
    """Testes para o model Participacao."""

    def setUp(self):
        # Criar aluno
        self.aluno = Aluno.objects.create(
            nome_completo="Maria Silva",
            data_nascimento=date(2000, 1, 1),
            endereco="Rua A, 123"
        )
        # Criar evento
        self.evento = Evento.objects.create(
            nome="Oficina de Arte",
            data=date.today(),
            hora_inicio=time(9, 0),
            local="Sala 1"
        )
        # Criar participação
        self.participacao = Participacao.objects.create(
            aluno=self.aluno,
            evento=self.evento
        )

    def test_participacao_str(self):
        esperado = f"{self.aluno.nome_completo} inscrito em {self.evento.nome}"
        self.assertEqual(str(self.participacao), esperado)

    def test_participacao_unica(self):
        with self.assertRaises(Exception):  # IntegrityError ou ValidationError
            Participacao.objects.create(
                aluno=self.aluno,
                evento=self.evento
            )
