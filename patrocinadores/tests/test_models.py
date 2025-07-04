from django.test import TestCase
from django.db import IntegrityError
from decimal import Decimal
from eventos.models import Evento
from patrocinadores.models import Patrocinador, FinanciamentoEvento
from datetime import date, time


class PatrocinadorModelTests(TestCase):
    """Testes para o modelo Patrocinador."""

    def setUp(self):
        self.patrocinador = Patrocinador.objects.create(
            documento_id="12.345.678/0001-90",
            nome="Empresa X",
            telefone_contato="123456789",
            email="contato@empresa.com",
            campo_atividade="EDUCACAO"
        )

    def test_str_method(self):
        """__str__ deve retornar o nome do patrocinador."""
        self.assertEqual(str(self.patrocinador), "Empresa X")

    def test_unique_documento_id(self):
        """Não deve permitir dois patrocinadores com o mesmo documento_id."""
        with self.assertRaises(IntegrityError):
            Patrocinador.objects.create(
                documento_id="12.345.678/0001-90",  # mesmo ID
                nome="Empresa Y",
                campo_atividade="ESPORTE"
            )


class FinanciamentoEventoModelTests(TestCase):
    """Testes para o modelo FinanciamentoEvento."""

    def setUp(self):
        self.patrocinador = Patrocinador.objects.create(
            documento_id="98.765.432/0001-10",
            nome="Instituição Y",
            campo_atividade="ESPORTE"
        )
        self.evento = Evento.objects.create(
            nome="Campeonato de Futebol",
            data=date.today(),
            hora_inicio=time(14, 0),
            local="Quadra da ONG"
        )

    def test_str_method(self):
        """__str__ deve retornar no formato 'Patrocinador → Evento (valor)'."""
        financiamento = FinanciamentoEvento.objects.create(
            patrocinador=self.patrocinador,
            evento=self.evento,
            valor=Decimal("1500.00")
        )
        esperado = f"{self.patrocinador.nome} → {self.evento.nome} (1500.00)"
        self.assertEqual(str(financiamento), esperado)

    def test_unique_constraint_patrocinador_evento(self):
        """Não deve permitir dois financiamentos iguais para o mesmo patrocinador e evento."""
        FinanciamentoEvento.objects.create(
            patrocinador=self.patrocinador,
            evento=self.evento,
            valor=Decimal("500.00")
        )
        with self.assertRaises(IntegrityError):
            FinanciamentoEvento.objects.create(
                patrocinador=self.patrocinador,
                evento=self.evento,
                valor=Decimal("1000.00")
            )

    def test_auto_date_field(self):
        """O campo data deve ser preenchido automaticamente na criação."""
        financiamento = FinanciamentoEvento.objects.create(
            patrocinador=self.patrocinador,
            evento=self.evento,
            valor=Decimal("750.00")
        )
        self.assertIsNotNone(financiamento.criado_em)
