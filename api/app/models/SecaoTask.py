from sqlalchemy import Integer, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from config.database import Base

class SecaoTask(Base):
    __tablename__ = "secaoTask"

    id = Column(Integer, primary_key = True, index = True)
    taskId = Column(Integer, ForeignKey("tasks.id"), nullable = False)
    task = relationship("Task", foreign_keys = [taskId])
    userId = Column(Integer, ForeignKey("usuarios.id"), nullable = False)
    user = relationship("Usuario", foreign_keys = [userId]) 
    timeStart = Column(DateTime(timezone = True),default = lambda: datetime.now(timezone.utc), nullable = False )
    timeEnd = Column(DateTime(timezone = True), nullable = True)
    timeSessionS = Column(Integer, nullable = True)
