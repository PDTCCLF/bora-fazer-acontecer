from django import forms
from .models import Patrocinador, FinanciamentoEvento


# Formulário para Patrocinador
class PatrocinadorForm(forms.ModelForm):
    class Meta:
        model = Patrocinador
        fields = ['nome', 'telefone_contato', 'email', 'documento_id', 'campo_atividade']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone_contato': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'documento_id': forms.TextInput(attrs={'class': 'form-control'}),
            'campo_atividade': forms.Select(attrs={'class': 'form-control'}),
        }

# Formulário para Financiamento de Evento
class FinanciamentoEventoForm(forms.ModelForm):
    class Meta:
        model = FinanciamentoEvento
        fields = ['patrocinador', 'evento', 'valor']
        widgets = {
            'patrocinador': forms.Select(attrs={'class': 'form-control'}),
            'evento': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona validação para garantir que o valor seja positivo
        self.fields['valor'].validators.append(self.validate_positive)

    def validate_positive(self, value):
        if value <= 0:
            raise forms.ValidationError("O valor deve ser positivo.")