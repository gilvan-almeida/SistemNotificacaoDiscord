from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from models.Enums import statusSecaoEnum
from schemas.Task import TaskResponse
from schemas.Usuario import UsuarioResponse


class SecaoTaskBase(BaseModel):
    id: int
    task: TaskResponse
    statusSecao: Optional[statusSecaoEnum]
    timeStart: Optional[datetime]
    timeEnd: Optional[datetime]
    timeSessionS: Optional[int]

    model_config = {
        "from_attributes": True
    }

class SecaoTaskCreate(BaseModel):
    taskId: int
    userId: int

# class SecaoTaskUpdate(BaseModel):
#     timeEnd: datetime

class SecaoTaskResponse(SecaoTaskBase):
    pass

class StatusSecaoResponse(BaseModel):
    status: str
    secao: SecaoTaskResponse | None