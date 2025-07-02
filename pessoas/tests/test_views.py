from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from pessoas.models import Aluno, Voluntario
from datetime import date

class PessoaViewsTest(TestCase):

    def setUp(self):
        # Cliente de teste
        self.client = Client()

        # Usuário para autenticação
        self.user = User.objects.create_user(username='admin', password='123456')
        self.user.is_staff = True
        self.user.save()

        # Login do cliente
        self.client.login(username='admin', password='123456')

        # Instâncias de teste
        self.aluno = Aluno.objects.create(
            nome_completo='Aluno Teste',
            data_nascimento='2000-01-01',
            endereco='Rua A, 123'
        )
        self.vol_user = User.objects.create_user(username='voluntario1', password='123456')
        self.vol_user.is_staff = True
        self.vol_user.is_superuser = True
        self.vol_user.save()
        self.voluntario = Voluntario.objects.create(
            nome_completo='Voluntário Teste',
            data_nascimento='1990-01-01',
            endereco='Rua Voluntário, 1',
            usuario=self.vol_user
        )

    # -------- LISTAGEM --------
    def test_lista_alunos_view(self):
        url = reverse('lista_alunos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pessoas/alunos/lista.html')
        self.assertContains(response, self.aluno.nome_completo)

    def test_lista_voluntarios_view(self):
        url = reverse('lista_voluntarios')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pessoas/voluntarios/lista.html')
        self.assertContains(response, self.voluntario.nome_completo)

    # -------- CRIAÇÃO --------
    def test_criar_aluno_get(self):
        url = reverse('criar_aluno')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pessoas/alunos/formulario.html')

    def test_criar_aluno_post(self):
        url = reverse('criar_aluno')
        data = {
            'nome_completo': 'Novo Aluno',
            'data_nascimento': '2001-02-02',
            'endereco': 'Rua Nova, 10'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)  # Redireciona após salvar
        self.assertTrue(Aluno.objects.filter(nome_completo='Novo Aluno').exists())

    def test_criar_voluntario_post(self):
        url = reverse('criar_voluntario')
        data = {
            'nome_completo': 'Novo Voluntario',
            'telefone': '999888777',
            'data_nascimento': '1995-05-05',
            'endereco': 'Rua Nova, 10',
            'usuario': 'novo_user',
            'email': 'novo@email.com',
            'senha': '12345678',
            'senha_conf': '12345678'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Voluntario.objects.filter(nome_completo='Novo Voluntario').exists())
        vol = Voluntario.objects.get(nome_completo='Novo Voluntario')
        self.assertEqual(vol.usuario.username, 'novo_user')
        self.assertTrue(vol.usuario.is_superuser)

    # -------- EDIÇÃO --------
    def test_editar_aluno_post(self):
        url = reverse('editar_aluno', args=[self.aluno.pk])
        data = {
            'nome_completo': 'Aluno Editado',
            'data_nascimento': '2000-01-01',
            'endereco': 'Rua A, 123'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.aluno.refresh_from_db()
        self.assertEqual(self.aluno.nome_completo, 'Aluno Editado')

    def test_editar_voluntario_post(self):
        url = reverse('editar_voluntario', args=[self.voluntario.pk])
        data = {
            'nome_completo': 'Voluntario Editado',
            'telefone': '111222333',
            'data_nascimento': '1990-01-01',
            'endereco': 'Rua Voluntário, 1'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.voluntario.refresh_from_db()
        self.assertEqual(self.voluntario.nome_completo, 'Voluntario Editado')

    # -------- DELEÇÃO --------
    def test_deletar_aluno_post(self):
        url = reverse('deletar_aluno', args=[self.aluno.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Aluno.objects.filter(pk=self.aluno.pk).exists())

    def test_deletar_voluntario_post(self):
        url = reverse('deletar_voluntario', args=[self.voluntario.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Voluntario.objects.filter(pk=self.voluntario.pk).exists())
        self.assertFalse(User.objects.filter(pk=self.vol_user.pk).exists())  # usuário também deletado

    # -------- LOGIN OBRIGATÓRIO --------
    def test_redirect_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(reverse('lista_alunos'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)
