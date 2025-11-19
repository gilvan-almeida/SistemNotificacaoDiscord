from datetime import datetime
from pydantic import BaseModel
from schemas.Task import TaskResponse
from schemas.Usuario import UsuarioResponse


class SecaoTaskBase(BaseModel):
    id: int
    task: TaskResponse
    user: UsuarioResponse
    timeStart: datetime
    timeEnd: datetime
    timeSession: int

    class Config():
        from_attributes = True

class SecaoTaskCreate(BaseModel):
    taskId: int
    userId: int
    timeStart: datetime

class SecaoTaskUpdate(BaseModel):
    timeEnd: datetime

class SecaoTaskResponse(SecaoTaskBase):
    pass