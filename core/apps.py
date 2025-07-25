from django.apps import AppConfig

# Configuração do app 'core' com BigAutoField como campo padrão para chaves primárias
class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
