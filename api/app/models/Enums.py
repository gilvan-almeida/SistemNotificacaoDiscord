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