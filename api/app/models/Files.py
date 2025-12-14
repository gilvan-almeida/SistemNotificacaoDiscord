from sqlalchemy import Column, String, Integer, ForeignKey
from config.database import Base
from sqlalchemy.orm import relationship

class Files(Base):

    __tablename__ = "files"

    id = Column(Integer, primary_key = True, index = True)
    fileLocate = Column(String, nullable = False)
    fileType = Column(String, nullable = False)
    taskId = Column(Integer, ForeignKey("tasks.id"), nullable = True)
    task = relationship("Task", back_populates="taskMedia")
    reportId = Column(Integer, ForeignKey("reportTask.id"), nullable=True)
    report = relationship("ReportTask", back_populates="reportMedia")
    

