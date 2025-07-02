from django.test import TestCase
from django.contrib.auth.models import User
from pessoas.forms import AlunoForm, VoluntarioForm, ISODateInput
from pessoas.models import Aluno, Voluntario
from datetime import date

class AlunoFormTest(TestCase):
    def test_form_valid_data(self):
        """Testa criação de Aluno com dados válidos"""
        form_data = {
            'nome_completo': 'João da Silva',
            'email': 'joao@email.com',
            'telefone': '123456789',
            'data_nascimento': '2000-01-01',
            'endereco': 'Rua A, 123'
        }
        form = AlunoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_missing_required_field(self):
        """Testa que campo obrigatório ausente invalida o form"""
        form_data = {
            'email': 'joao@email.com',
            'telefone': '123456789',
            'data_nascimento': '2000-01-01',
            'endereco': 'Rua A, 123'
        }  # nome_completo faltando
        form = AlunoForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('nome_completo', form.errors)

    def test_iso_date_input(self):
        """Testa que o widget ISODateInput gera o tipo correto"""
        field = AlunoForm().fields['data_nascimento']
        self.assertIsInstance(field.widget, ISODateInput)
        self.assertEqual(field.widget.input_type, 'date')
        self.assertEqual(field.widget.format, '%Y-%m-%d')

    def test_edit_existing_instance_fields_disabled(self):
        """Campos não editáveis aparecem ao editar instância"""
        aluno = Aluno.objects.create(
            nome_completo='Maria',
            data_nascimento='2000-02-02',
            endereco='Rua B, 456'
        )
        form = AlunoForm(instance=aluno)
        self.assertTrue(form.fields['matricula_id'].disabled)
        self.assertTrue(form.fields['data_matricula'].disabled)
        self.assertTrue(form.fields['status_ativo'].disabled)


class VoluntarioFormTest(TestCase):
    def setUp(self):
        """Cria usuário e voluntário para testes"""
        self.user = User.objects.create_user(username='voluntario1', email='vol@teste.com', password='123456')
        self.voluntario = Voluntario.objects.create(
            nome_completo='Voluntário Teste',
            data_nascimento='1990-01-01',
            endereco='Rua Voluntário, 1',
            usuario=self.user
        )

    def test_form_valid_new_voluntario(self):
        """Testa criação de novo voluntário com senha e confirmação"""
        form_data = {
            'nome_completo': 'Novo Voluntario',
            'telefone': '999888777',
            'data_nascimento': '1995-05-05',
            'endereco': 'Rua Nova, 10',
            'usuario': 'novo_user',
            'email': 'novo@email.com',
            'senha': '12345678',
            'senha_conf': '12345678'
        }
        form = VoluntarioForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_password_mismatch(self):
        """Testa erro quando senha e confirmação não conferem"""
        form_data = {
            'nome_completo': 'Novo Voluntario',
            'telefone': '999888777',
            'data_nascimento': '1995-05-05',
            'endereco': 'Rua Nova, 10',
            'usuario': 'novo_user',
            'email': 'novo@email.com',
            'senha': '12345678',
            'senha_conf': '87654321'
        }
        form = VoluntarioForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('__all__', form.errors)  # clean() lança ValidationError global

    def test_existing_voluntario_fields_disabled(self):
        """Campos de usuário, email e senha estão desabilitados ao editar"""
        form = VoluntarioForm(instance=self.voluntario)
        self.assertEqual(form.fields['usuario'].initial, self.user.username)
        self.assertTrue(form.fields['usuario'].disabled)
        self.assertEqual(form.fields['email'].initial, self.user.email)
        self.assertTrue(form.fields['email'].disabled)
        self.assertEqual(form.fields['senha'].initial, '********')
        self.assertTrue(form.fields['senha'].disabled)
        self.assertNotIn('senha_conf', form.fields)  # campo removido

    def test_required_fields_new_voluntario(self):
        """Testa que username, email e senha são obrigatórios ao criar"""
        form_data = {
            'nome_completo': 'Sem Campos Obrigatórios'
        }
        form = VoluntarioForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('usuario', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('senha', form.errors)
        self.assertIn('senha_conf', form.errors)
