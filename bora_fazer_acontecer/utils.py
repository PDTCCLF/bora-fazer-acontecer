import uuid
import coolname

#Criação de id único legível
def gerar_identificador_legivel():
    nome = '-'.join(coolname.generate(3))  # Ex: sleepy-mountain-wolf
    uid = str(uuid.uuid4())         # Ex: a1b2c3d4
    return f"{nome}-{uid}"