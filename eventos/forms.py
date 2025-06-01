from django import forms
from .models import Evento, Participacao


# Widget customizado para datas no formato ISO (YYYY-MM-DD)
class ISODateInput(forms.DateInput):
    input_type = 'date'           # gera <input type="date">
    format = '%Y-%m-%d'           # formato que o browser entende

    def __init__(self, **kwargs):
        kwargs.setdefault('format', self.format)
        super().__init__(**kwargs)

# Formulário para Evento
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'data', 'hora_inicio', 'duracao', 'descricao', 'local']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome do evento'}),
            'data': ISODateInput(attrs={'class': 'form-control'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'duracao': forms.TextInput(attrs={'placeholder': 'Formato: 2 horas'}),
            'descricao': forms.Textarea(attrs={'rows': 4}),
            'local': forms.TextInput(attrs={'placeholder': 'Endereço do evento'}),
        }
        exclude = ['codigo_evento']
        labels = {
            'nome': 'Nome do Evento',
            'data': 'Data',
            'hora_inicio': 'Hora de Início',
            'duracao': 'Duração',
            'descricao': 'Descrição',
            'local': 'Local',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # garantir que o parsing também aceite o formato ISO vindo do <input type="date">
        for f in ('data',):
            self.fields[f].input_formats = ['%Y-%m-%d']
        # Campos só para visualização
        if self.instance and self.instance.pk:
            self.fields['codigo_evento'] = forms.CharField(
                initial=self.instance.codigo_evento,
                disabled=True,
                label="Código do Evento"
            )

# Formulário para Participação
class ParticipacaoForm(forms.ModelForm):
    class Meta:
        model = Participacao
        fields = ['aluno', 'evento']
        widgets = {
            'aluno': forms.Select(),
            'evento': forms.Select(),
        }
        labels = {
            'aluno': 'Aluno(a)',
            'evento': 'Evento',
        }