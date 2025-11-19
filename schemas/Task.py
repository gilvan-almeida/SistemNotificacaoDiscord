from datetime import datetime
from pydantic import BaseModel
from models.Enums import statusTask
from schemas.Usuario import UsuarioResponse

class TaskBase(BaseModel):
    id: int
    title: str
    description: str
    status: statusTask
    criadorTask: UsuarioResponse
    usuarioTask: UsuarioResponse
    dateTaskCreate: datetime
    dateTaskEnd: datetime

    class Config():
        from_attributes = True 

class TaskCreate(BaseModel):
    title: str
    description: str
    status: statusTask = statusTask.CRIADO
    criadorTaskId: int
    usuarioTaskId: int

class TaskResponse(TaskBase):
    pass    