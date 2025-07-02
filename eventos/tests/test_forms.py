from django.test import TestCase
from eventos.forms import EventoForm, ParticipacaoForm
from eventos.models import Evento, Participacao
from pessoas.models import Aluno
from datetime import date, time


class EventoFormTests(TestCase):
    """Testes para o form EventoForm."""

    def setUp(self):
        self.valid_data = {
            "nome": "Feira Cultural",
            "data": "2025-09-03",
            "hora_inicio": "14:00",
            "duracao": "2 horas",
            "descricao": "Apresentação de trabalhos artísticos.",
            "local": "Praça Central"
        }

    def test_form_valido(self):
        form = EventoForm(data=self.valid_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_invalido_sem_nome(self):
        data = self.valid_data.copy()
        data.pop("nome")
        form = EventoForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn("nome", form.errors)

    def test_form_edit_evento_adiciona_codigo_evento(self):
        evento = Evento.objects.create(
            nome="Oficina de Teatro",
            data=date.today(),
            hora_inicio=time(10, 0),
            local="Auditório"
        )
        form = EventoForm(instance=evento)
        # Como está editando, o campo codigo_evento deve ser adicionado e desabilitado
        self.assertIn("codigo_evento", form.fields)
        self.assertTrue(form.fields["codigo_evento"].disabled)


class ParticipacaoFormTests(TestCase):
    """Testes para o form ParticipacaoForm."""

    def setUp(self):
        self.aluno = Aluno.objects.create(
            nome_completo="Carlos Pereira",
            data_nascimento=date(2000, 1, 1),
            endereco="Rua B, 45"
        )
        self.evento = Evento.objects.create(
            nome="Workshop de Música",
            data=date.today(),
            hora_inicio=time(15, 0),
            local="Sala de Música"
        )

    def test_form_valido(self):
        form = ParticipacaoForm(data={"aluno": self.aluno.id, "evento": self.evento.id})
        self.assertTrue(form.is_valid(), form.errors)

    def test_form_invalido_sem_aluno(self):
        form = ParticipacaoForm(data={"evento": self.evento.id})
        self.assertFalse(form.is_valid())
        self.assertIn("aluno", form.errors)

    def test_form_invalido_sem_evento(self):
        form = ParticipacaoForm(data={"aluno": self.aluno.id})
        self.assertFalse(form.is_valid())
        self.assertIn("evento", form.errors)
