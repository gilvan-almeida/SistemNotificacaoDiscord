from sqlalchemy import Integer, Column, String, Enum, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone, timedelta
from config.database import Base
from models.Enums import statusTask

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, nullable = False)
    description = Column(String, nullable = False)
    status = Column(Enum(statusTask), default = statusTask.CRIADO, nullable = False)

    projectId = Column(Integer, ForeignKey("projects.id", ondelete = "CASCADE"), nullable = False)
    project = relationship("Project")

    criadorTaksId = Column(Integer, ForeignKey("usuarios.id"))
    criadorTask = relationship("Usuario", foreign_keys = [criadorTaksId])
    usuarioTaskId = Column(Integer, ForeignKey("usuarios.id"))
    usuarioTask = relationship("Usuario", foreign_keys = [usuarioTaskId])
    
    taskMedia = relationship("Files", back_populates="task", cascade="all, delete-orphan")

    dateTaskCreate = Column(DateTime(timezone = True), default = lambda:datetime.now(timezone.utc), nullable = False)
    dateTaskEnd = Column(DateTime(timezone=True), default = lambda: datetime.now(timezone.utc) + timedelta(days = 7),nullable = False)  