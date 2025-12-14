from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
from config.database import Base

from sqlalchemy.orm import relationship

class ReportTask(Base):

    __tablename__ = "reportTask"

    id = Column(Integer, primary_key = True, index = True)
    taskId = Column(Integer, ForeignKey("tasks.id"), nullable = False)
    task = relationship("Task", foreign_keys = [taskId])
    userId = Column(Integer, ForeignKey("usuarios.id"), nullable = False)
    user = relationship("Usuario", foreign_keys = [userId])
    description = Column(String, nullable = False)
    reportMedia = relationship("Files", back_populates="report", cascade="all, delete-orphan")
