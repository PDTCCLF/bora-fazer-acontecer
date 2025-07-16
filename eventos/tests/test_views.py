# eventos/tests/test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from eventos.models import Evento, Participacao
from pessoas.models import Aluno
from datetime import date, time


class EventoViewTests(TestCase):
    """Testes para as views relacionadas a Evento e a Participacao."""

    def setUp(self):
        super().setUp()
        # Cliente de teste
        self.client = Client()

        # Usuário para autenticação
        self.user = User.objects.create_user(username='admin', password='123456')
        self.user.is_staff = True
        self.user.save()

        # Login do cliente
        self.client.login(username='admin', password='123456')

        self.aluno = Aluno.objects.create(
            nome_completo="Ana Paula",
            data_nascimento=date(2001, 1, 1),
            endereco="Rua A, 123"
        )
        self.evento = Evento.objects.create(
            nome="Festival de Dança",
            data=date.today(),
            hora_inicio=time(19, 0),
            local="Ginásio"
        )
        self.participacao = Participacao.objects.create(
            aluno=self.aluno, evento=self.evento
        )

    def test_lista_eventos(self):
        url = reverse("lista_eventos")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Festival de Dança")

    def test_criar_evento(self):
        url = reverse("criar_evento")
        data = {
            "nome": "Campeonato de Xadrez",
            "data": "2025-09-03",
            "hora_inicio": "10:00",
            "duracao": "3 horas",
            "descricao": "Competição regional",
            "local": "Biblioteca"
        }
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse("lista_eventos"))
        self.assertTrue(Evento.objects.filter(nome="Campeonato de Xadrez").exists())

    def test_editar_evento(self):
        url = reverse("editar_evento", args=[self.evento.pk])
        response = self.client.post(url, {
            "nome": "Festival de Dança Atualizado",
            "data": "2025-09-04",
            "hora_inicio": "20:00",
            "local": "Arena"
        })
        self.assertRedirects(response, reverse("lista_eventos"))
        self.evento.refresh_from_db()
        self.assertEqual(self.evento.nome, "Festival de Dança Atualizado")

    def test_deletar_evento(self):
        url = reverse("deletar_evento", args=[self.evento.pk])
        response = self.client.post(url)
        self.assertRedirects(response, reverse("lista_eventos"))
        self.assertFalse(Evento.objects.filter(pk=self.evento.pk).exists())

    def test_lista_participacoes(self):
        url = reverse("lista_participacoes")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ana Paula")

    def test_criar_participacao(self):
        novo_evento = Evento.objects.create(
            nome="Oficina de Teatro",
            data=date.today(),
            hora_inicio=time(16, 0),
            local="Auditório"
        )
        url = reverse("criar_participacao")
        response = self.client.post(url, {
            "aluno": self.aluno.pk,
            "evento": novo_evento.pk
        })
        self.assertRedirects(response, reverse("lista_participacoes"))
        self.assertTrue(Participacao.objects.filter(aluno=self.aluno, evento=novo_evento).exists())

    def test_editar_participacao(self):
        novo_evento = Evento.objects.create(
            nome="Feira de Ciências",
            data=date.today(),
            hora_inicio=time(9, 0),
            local="Escola"
        )
        url = reverse("editar_participacao", args=[self.participacao.pk])
        response = self.client.post(url, {
            "aluno": self.aluno.pk,
            "evento": novo_evento.pk
        })
        self.assertRedirects(response, reverse("lista_participacoes"))
        self.participacao.refresh_from_db()
        self.assertEqual(self.participacao.evento, novo_evento)

    def test_deletar_participacao(self):
        url = reverse("deletar_participacao", args=[self.participacao.pk])
        response = self.client.post(url)
        self.assertRedirects(response, reverse("lista_participacoes"))
        self.assertFalse(Participacao.objects.filter(pk=self.participacao.pk).exists())
