from enum import Enum as PyEnum

class nivelAcesso(PyEnum):
    ADMIN = "admin"
    USER = "usuario"

class statusTask(PyEnum):
    CRIADO = "Criado"
    INICIADO = "Iniciado"
    PAUSA = "Pausado"
    ATRASADA = "Atrasada"
    ENCERRADO = "Encerrado"
    CANCELADO = "Cancelado"

class statusSecaoEnum(PyEnum):
    CRIADA = "Criada"
    ATIVA = "Ativa"
    PAUSADA = "Pausada"
    FINALIZADA = "Finalizada"

class statusHistory(PyEnum):
    CRIADA = "Criada"
    INICIADA = "Iniciada"
    PAUSADA = "Pausada"
    RETOMADA = "Retomada"
    FINALIZADA = "Finalizada"

class statusReport(PyEnum):
    SUBMETIDO = "Submetido"
    RETORNADO = "Retornado"
    APROVADO = "Aprovado"