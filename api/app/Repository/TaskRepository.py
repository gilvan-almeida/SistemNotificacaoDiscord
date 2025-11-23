from fastapi import HTTPException
from models.Task import Task
from models.Usuario import Usuario
from models.Enums import statusTask
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
    def getTaskDiscrodId(db: Session, discordId: str):
        return db.query(Task).join(Task.usuarioTask).filter(Usuario.discordId == discordId).filter(Task.status == statusTask.CRIADO).first()
    
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

