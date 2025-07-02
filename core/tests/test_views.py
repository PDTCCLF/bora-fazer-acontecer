from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class HomeViewTests(TestCase):
    """Testes para a view home do app core."""

    def setUp(self):
        # Cria um usuário para testar login_required
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="password123"
        )
        self.url = reverse("home")

    def test_home_redirect_if_not_logged_in(self):
        """
        Se o usuário não estiver logado, deve ser redirecionado para a página de login.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)  # URL de login configurada em urls.py

    def test_home_status_code_logged_in(self):
        """
        Usuário logado deve acessar a home com sucesso.
        """
        self.client.login(username="testuser", password="password123")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/home.html")

    def test_home_context_contains_debug(self):
        """
        A view home deve enviar a variável 'debug' no contexto.
        """
        self.client.login(username="testuser", password="password123")
        response = self.client.get(self.url)
        self.assertIn("debug", response.context)
        self.assertEqual(response.context["debug"], True)  # ou False se DEBUG=False
