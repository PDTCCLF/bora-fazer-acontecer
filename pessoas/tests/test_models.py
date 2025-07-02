from django.test import TestCase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date
from pessoas.models import Pessoa, Aluno, Voluntario
from bora_fazer_acontecer.utils import gerar_identificador_legivel

class PessoaModelTest(TestCase):
    """Testes para o model Pessoa"""

    def test_criar_pessoa_gera_matricula_e_data_matricula(self):
        """Verifica se Pessoa nova gera matricula_id e data_matricula automaticamente"""
        p = Pessoa.objects.create(
            nome_completo="Maria Silva",
            data_nascimento=date(1990, 5, 10),
            endereco="Rua A, 123"
        )
        self.assertIsNotNone(p.matricula_id, "matricula_id deve ser gerado")
        self.assertIsNotNone(p.data_matricula, "data_matricula deve ser definida")
        self.assertTrue(p.status_ativo, "Pessoa sem data_saida deve estar ativa")

    def test_status_ativo_ajustado_por_data_saida(self):
        """Verifica se status_ativo é False quando data_saida é definida"""
        p = Pessoa.objects.create(
            nome_completo="João",
            data_nascimento=date(1985, 1, 1),
            endereco="Rua B, 456",
            data_saida=date.today()
        )
        self.assertFalse(p.status_ativo)

    def test_matricula_id_unica(self):
        """Verifica se criar Pessoa com matricula_id duplicada gera ValidationError"""
        codigo = gerar_identificador_legivel()
        Pessoa.objects.create(
            nome_completo="Pessoa 1",
            data_nascimento=date(2000, 1, 1),
            endereco="Endereço 1",
            matricula_id=codigo
        )
        p2 = Pessoa(
            nome_completo="Pessoa 2",
            data_nascimento=date(2001, 2, 2),
            endereco="Endereço 2",
            matricula_id=codigo
        )
        with self.assertRaises(ValidationError):
            p2.save()

    def test_str_retorna_nome_e_matricula(self):
        """Verifica __str__ de Pessoa"""
        p = Pessoa.objects.create(
            nome_completo="Ana",
            data_nascimento=date(1995, 7, 7),
            endereco="Rua C, 789"
        )
        self.assertIn("Ana", str(p))
        self.assertIn(p.matricula_id, str(p))

class AlunoModelTest(TestCase):
    """Testes para o model Aluno, subclasse de Pessoa"""

    def test_criar_aluno_herda_campos_pessoa(self):
        aluno = Aluno.objects.create(
            nome_completo="Carlos",
            data_nascimento=date(2005, 3, 15),
            endereco="Rua D, 321"
        )
        self.assertIsInstance(aluno, Aluno)
        self.assertIsNotNone(aluno.matricula_id)
        self.assertEqual(str(aluno), f"Aluno: {aluno.nome_completo}")

class VoluntarioModelTest(TestCase):
    """Testes para o model Voluntario, subclasse de Pessoa"""

    def setUp(self):
        """Cria um usuário Django e Voluntário para testes"""
        self.user = User.objects.create_user(
            username="voluntario1",
            email="voluntario1@example.com",
            password="123456",
            is_staff=True,
            is_superuser=True
        )
        self.voluntario = Voluntario.objects.create(
            nome_completo="Voluntário Teste",
            data_nascimento=date(1992, 4, 4),
            endereco="Rua E, 654",
            usuario=self.user
        )

    def test_voluntario_criado_com_usuario(self):
        """Verifica se o voluntário está vinculado ao usuário Django"""
        self.assertEqual(self.voluntario.usuario.username, "voluntario1")
        self.assertTrue(self.voluntario.status_ativo)
        self.assertIsNotNone(self.voluntario.matricula_id)

    def test_str_retorna_nome(self):
        """Verifica __str__ do voluntário"""
        self.assertIn("Voluntario", str(self.voluntario))
        self.assertIn(self.voluntario.nome_completo, str(self.voluntario))

    def test_delete_deleta_usuario_associado(self):
        """Ao deletar o voluntário, o usuário Django também é deletado"""
        user_id = self.user.id
        self.voluntario.delete()
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=user_id)
