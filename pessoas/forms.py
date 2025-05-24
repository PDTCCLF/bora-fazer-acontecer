from django import forms
from .models import Aluno, Voluntario


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # garantir que o parsing também aceite o formato ISO vindo do <input type="date">
        for f in ('data_nascimento', 'data_saida'):
            self.fields[f].input_formats = ['%Y-%m-%d']

# Formulário para Voluntário
class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nome_completo', 'email', 'telefone', 'data_nascimento',  'data_saida', 'endereco']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': ISODateInput(attrs={'class': 'form-control'}),
            'data_saida': ISODateInput(attrs={'class': 'form-control'}),
            'endereco': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # garantir que o parsing também aceite o formato ISO vindo do <input type="date">
        for f in ('data_nascimento', 'data_saida'):
            self.fields[f].input_formats = ['%Y-%m-%d']