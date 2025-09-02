from django.core.management.base import BaseCommand
from pessoas.models import Aluno, Voluntario
from eventos.models import Evento, Participacao
from patrocinadores.models import Patrocinador, FinanciamentoEvento

class Command(BaseCommand):
    help = "Apaga dados de uso, mantendo superusuários e configuração."

    def handle(self, *args, **kwargs):
        FinanciamentoEvento.objects.all().delete()
        Patrocinador.objects.all().delete()
        Participacao.objects.all().delete()
        Evento.objects.all().delete()
        Aluno.objects.all().delete()
        Voluntario.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Dados resetados, superusuários preservados."))
