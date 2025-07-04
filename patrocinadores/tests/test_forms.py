from django.test import TestCase
from django.core.exceptions import ValidationError
from eventos.models import Evento
from patrocinadores.models import Patrocinador, FinanciamentoEvento
from patrocinadores.forms import PatrocinadorForm, FinanciamentoEventoForm
from datetime import date, time


class PatrocinadorFormTests(TestCase):
    """Testes para o formulário de Patrocinador."""

    def test_form_valid_data(self):
        """Formulário deve ser válido quando todos os campos são preenchidos corretamente."""
        form_data = {
            'nome': 'Empresa X',
            'telefone_contato': '123456789',
            'email': 'contato@empresa.com',
            'documento_id': '12.345.678/0001-90',
            'campo_atividade': 'MEIO_AMBIENTE',
        }
        form = PatrocinadorForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_missing_required_field(self):
        """Formulário inválido quando algum campo obrigatório não é preenchido."""
        form_data = {
            'nome': '',
            'telefone_contato': '123456789',
            'email': 'contato@empresa.com',
            'documento_id': '12.345.678/0001-90',
            'campo_atividade': 'Tecnologia',
        }
        form = PatrocinadorForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)


class FinanciamentoEventoFormTests(TestCase):
    """Testes para o formulário de Financiamento de Evento."""

    def setUp(self):
        # Criar objeto Patrocinador e Evento para relacionamentos
        self.patrocinador = Patrocinador.objects.create(
            nome='Empresa X',
            telefone_contato='123456789',
            email='contato@empresa.com',
            documento_id='12.345.678/0001-90',
            campo_atividade='Tecnologia'
        )
        self.evento = Evento.objects.create(
            nome='Evento Teste',
            data=date.today(),
            hora_inicio=time(8, 45),
            local='Auditório'
        )

    def test_form_valid_data(self):
        """Formulário deve ser válido quando valor é positivo."""
        form_data = {
            'patrocinador': self.patrocinador.id,
            'evento': self.evento.id,
            'valor': 1000.00
        }
        form = FinanciamentoEventoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_negative_value(self):
        """Formulário deve ser inválido quando o valor é negativo."""
        form_data = {
            'patrocinador': self.patrocinador.id,
            'evento': self.evento.id,
            'valor': -50
        }
        form = FinanciamentoEventoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('valor', form.errors)
        self.assertEqual(form.errors['valor'][0], 'O valor deve ser positivo.')

    def test_form_missing_required_field(self):
        """Formulário deve ser inválido se algum campo obrigatório não for preenchido."""
        form_data = {
            'patrocinador': self.patrocinador.id,
            'evento': '',
            'valor': 100
        }
        form = FinanciamentoEventoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('evento', form.errors)
