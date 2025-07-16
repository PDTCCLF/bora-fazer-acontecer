from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from patrocinadores.models import Patrocinador, FinanciamentoEvento
from eventos.models import Evento
from decimal import Decimal
from datetime import date, time


class PatrocinadoresViewsTests(TestCase):
    """Testes para as views de Patrocinador e FinanciamentoEvento."""

    def setUp(self):
        # Cria usuário autenticado para acessar as views
        self.user = User.objects.create_user(username="testador", password="12345")
        self.client = Client()
        self.client.login(username="testador", password="12345")

        # Dados iniciais
        self.patrocinador = Patrocinador.objects.create(
            documento_id="11.111.111/0001-11",
            nome="Empresa Teste",
            campo_atividade="EDUCAO"
        )
        self.evento = Evento.objects.create(
            nome="Evento X",
            data=date.today(),
            hora_inicio=time(18, 0),
            local="Centro Comunitário"
        )
        self.financiamento = FinanciamentoEvento.objects.create(
            patrocinador=self.patrocinador,
            evento=self.evento,
            valor=Decimal("1000.00")
        )

    # -----------------------------
    # Testes de CRIAÇÃO
    # -----------------------------
    def test_criar_patrocinador(self):
        response = self.client.post(reverse("criar_patrocinador"), {
            "documento_id": "22.222.222/0001-22",
            "nome": "Novo Patrocinador",
            "campo_atividade": "ESPORTE"
        })
        self.assertRedirects(response, reverse("lista_patrocinadores"))
        self.assertTrue(Patrocinador.objects.filter(nome="Novo Patrocinador").exists())

    def test_criar_financiamento(self):
        self.patrocinador = Patrocinador.objects.create(
            documento_id="22.222.222/0001-22",
            nome="Novo Patrocinador",
            campo_atividade="ESPORTE"
        )
        self.evento = Evento.objects.create(
            nome="Evento Y",
            data=date.today(),
            hora_inicio=time(15, 0),
            local="Centro Comunitário"
        )
        response = self.client.post(reverse("criar_financiamento"), {
            "patrocinador": self.patrocinador.id,
            "evento": self.evento.id,
            "valor": "500.00"
        })
        self.assertRedirects(response, reverse("lista_financiamentos"))
        self.assertTrue(FinanciamentoEvento.objects.filter(valor="500.00").exists())

    # -----------------------------
    # Testes de LISTAGEM
    # -----------------------------
    def test_lista_patrocinadores(self):
        response = self.client.get(reverse("lista_patrocinadores"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Empresa Teste")

    def test_lista_financiamentos(self):
        response = self.client.get(reverse("lista_financiamentos"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "1000")

    # -----------------------------
    # Testes de EDIÇÃO
    # -----------------------------
    def test_editar_patrocinador(self):
        response = self.client.post(reverse("editar_patrocinador", args=[self.patrocinador.id]), {
            "documento_id": "11.111.111/0001-11",
            "nome": "Empresa Editada",
            "campo_atividade": "ARTES"
        })
        self.assertRedirects(response, reverse("lista_patrocinadores"))
        self.patrocinador.refresh_from_db()
        self.assertEqual(self.patrocinador.nome, "Empresa Editada")

    def test_editar_financiamento(self):
        response = self.client.post(reverse("editar_financiamento", args=[self.financiamento.id]), {
            "patrocinador": self.patrocinador.id,
            "evento": self.evento.id,
            "valor": "2000.00"
        })
        self.assertRedirects(response, reverse("lista_financiamentos"))
        self.financiamento.refresh_from_db()
        self.assertEqual(self.financiamento.valor, Decimal("2000.00"))

    # -----------------------------
    # Testes de DELETE
    # -----------------------------
    def test_deletar_patrocinador(self):
        response = self.client.post(reverse("deletar_patrocinador", args=[self.patrocinador.id]))
        self.assertRedirects(response, reverse("lista_patrocinadores"))
        self.assertFalse(Patrocinador.objects.filter(id=self.patrocinador.id).exists())

    def test_deletar_financiamento(self):
        response = self.client.post(reverse("deletar_financiamento", args=[self.financiamento.id]))
        self.assertRedirects(response, reverse("lista_financiamentos"))
        self.assertFalse(FinanciamentoEvento.objects.filter(id=self.financiamento.id).exists())
