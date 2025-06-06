from django import forms
from .models import Aluno, Voluntario
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Widget customizado para datas no formato ISO (YYYY-MM-DD)
class ISODateInput(forms.DateInput):
    input_type = 'date'           # gera <input type="date">
    format = '%Y-%m-%d'           # formato que o browser entende

    def __init__(self, **kwargs):
        kwargs.setdefault('format', self.format)
        super().__init__(**kwargs)

# Formulário para Aluno
class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome_completo', 'email', 'telefone', 'data_nascimento', 'data_saida', 'endereco']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': ISODateInput(attrs={'class': 'form-control'}),
            'data_saida': ISODateInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        exclude = ['matricula_id', 'data_matricula', 'status_ativo']
        labels = {
            'nome_completo': 'Nome Completo',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'data_nascimento': 'Data de Nascimento',
            'data_saida': 'Data de Saída',
            'endereco': 'Endereço',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # garantir que o parsing também aceite o formato ISO vindo do <input type="date">
        for f in ('data_nascimento', 'data_saida'):
            self.fields[f].input_formats = ['%Y-%m-%d']
        # Campos só para visualização
        if self.instance and self.instance.pk:
            self.fields['matricula_id'] = forms.CharField(
                initial=self.instance.matricula_id,
                disabled=True,
                label="Matrícula"
            )
            self.fields['data_matricula'] = forms.DateField(
                initial=self.instance.data_matricula,
                disabled=True,
                label="Data de Matrícula"
            )
            self.fields['status_ativo'] = forms.BooleanField(
                initial=self.instance.status_ativo,
                disabled=True,
                required=False,
                label="Status Ativo"
            )

# Formulário para Voluntário
class VoluntarioForm(forms.ModelForm):
    usuario = forms.CharField(label="Nome de Usuário", max_length=150, required=False)
    email = forms.EmailField(label="E-mail", required=False)
    senha = forms.CharField(label="Senha", widget=forms.PasswordInput, required=False)
    senha_conf = forms.CharField(label="Confirmar Senha", widget=forms.PasswordInput, required=False)

    class Meta:
        model = Voluntario
        fields = ['nome_completo', 'telefone', 'data_nascimento', 'data_saida', 'endereco']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': ISODateInput(attrs={'class': 'form-control'}),
            'data_saida': ISODateInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        exclude = ['matricula_id', 'data_matricula', 'status_ativo', 'usuario']
        labels = {
            'nome_completo': 'Nome Completo',
            'telefone': 'Telefone',
            'data_nascimento': 'Data de Nascimento',
            'data_saida': 'Data de Saída',
            'endereco': 'Endereço',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # garantir que o parsing também aceite o formato ISO vindo do <input type="date">
        for f in ('data_nascimento', 'data_saida'):
            self.fields[f].input_formats = ['%Y-%m-%d']
        # Campos só para visualização
        if self.instance and self.instance.pk:
            self.fields['matricula_id'] = forms.CharField(
                initial=self.instance.matricula_id,
                disabled=True,
                label="Matrícula"
            )
            self.fields['data_matricula'] = forms.DateField(
                initial=self.instance.data_matricula,
                disabled=True,
                label="Data de Matrícula"
            )
            self.fields['status_ativo'] = forms.BooleanField(
                initial=self.instance.status_ativo,
                disabled=True,
                required=False,
                label="Status Ativo"
            )
            # Voluntário já existe → mostrar dados do usuário admin vinculados
            user = self.instance.usuario
            self.fields['usuario'].initial = user.username
            self.fields['usuario'].disabled = True

            self.fields['email'].initial = user.email
            self.fields['email'].disabled = True

            self.fields['senha'].widget = forms.PasswordInput(render_value=True)
            self.fields['senha'].initial = "********"
            self.fields['senha'].disabled = True

            # Voluntário já existe, então esconde-se a confirmação de senha
            self.fields.pop('senha_conf', None)
        else:
            # Novo voluntário → username, email e senha obrigatórios
            self.fields['usuario'].required = True
            self.fields['email'].required = True
            self.fields['senha'].required = True
            self.fields['senha_conf'].required = True

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.pk:  # validação só na criação
            senha = cleaned_data.get("senha")
            senha_conf = cleaned_data.get("senha_conf")

            if senha and senha_conf and senha != senha_conf:
                raise ValidationError("As senhas não conferem.")
        return cleaned_data