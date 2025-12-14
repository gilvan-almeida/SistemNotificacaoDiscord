from datetime import datetime
from pydantic import BaseModel
from models.Enums import statusHistory
from typing import Optional

class TaskHistoryBase(BaseModel):
    id: int
    taskId: int
    userId: int
    action: statusHistory
    description: str
    dateAction: datetime

    model_config = {
        "from_attributes": True
    }

class TaskHistoryCreate(BaseModel):
    taskId: int
    userId: int
    description: Optional[str] = None

class TaskHistoryResponse(TaskHistoryBase):
    pass
