from fastapi import HTTPException
from models.Task import Task
from sqlalchemy.orm import Session

class TaskRepository:

    @staticmethod
    def criarTask(db: Session, task: Task):
        db.add(task)
        db.commit()
        db.refresh(task)
        return task
    
    @staticmethod
    def getTaskId(db: Session, id: int):
        return db.query(Task).filter(Task.id == id).first()
    
    @staticmethod
    def listarTasks(db: Session):
        return db.query(Task).all()
    
    @staticmethod
    def deleteTask(db: Session, id: int):
        task = db.query(Task).filter(Task.id == id).first()
        if not task:
            raise None
        
        db.delete(task)
        db.commit()

