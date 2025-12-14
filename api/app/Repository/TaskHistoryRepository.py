from fastapi import HTTPException
from models.TaskHistory import TaskHistory
from sqlalchemy.orm import Session


class TaskHistoryRepository:

    @staticmethod
    def criarTaskHistory(db:Session, taskHistory: TaskHistory):
        db.add(taskHistory)
        db.commit()
        db.refresh(taskHistory)
        return taskHistory
    
    @staticmethod
    def getTaskHistoryID(db: Session, id: int):
        user = db.query(TaskHistory).filter(TaskHistory.id == id).first()        
        return user

    @staticmethod
    def getTaskHistoryList(db: Session, taskId: int):
        user = db.query(TaskHistory).filter(TaskHistory.taskId == taskId).order_by(TaskHistory.dateAction).all()
        return user
    