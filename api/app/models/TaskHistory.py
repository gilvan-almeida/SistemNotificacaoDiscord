from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from config.database import Base
from datetime import datetime, timezone
from models.Enums import statusHistory
from sqlalchemy.orm import relationship

class TaskHistory(Base):
    __tablename__ ="taskHistory"

    id = Column(Integer, primary_key = True, index = True)
    secaoTaskId = Column(Integer, ForeignKey("SecaoTask.id", ondelete = "CASCADE"), nullable = False)
    secaoTask = relationship("SecaoTask", back_populates = "history")
    action = Column(Enum(statusHistory), default = statusHistory.CRIADA, nullable = False )
    dateAction = Column(DateTime(timezone = True), default = lambda:datetime.now(timezone.utc), nullable = False)
    description = Column(String, nullable = False)
