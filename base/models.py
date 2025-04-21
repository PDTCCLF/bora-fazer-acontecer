from django.db import models

class Base(models.Model):
    """
    Base abstrata que fornece campos de timestamps criado_em e atualizado_em para todos os modelos que a herdam. 
    """
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    # Indica que esta é uma classe abstrata e não deve ser criada como uma tabela no banco de dados.
    class Meta:
        abstract = True
