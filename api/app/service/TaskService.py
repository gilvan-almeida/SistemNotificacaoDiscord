from Repository.TaskRepository import TaskRepository
from fastapi import HTTPException
from Repository.UsuarioRepository import UsuarioRepository
from models.Task import Task
from schemas.Task import TaskBase, TaskCreate, TaskResponse

from sqlalchemy.orm import Session

class TaskService:

    @staticmethod
    def criarTask(db: Session, task: TaskCreate):
        if  not UsuarioRepository.getIdUser(db, task.usuarioTaskId):
            raise HTTPException(status_code = 404, detail = "Usuário destino não encontrado")
        
        if not UsuarioRepository.getIdUser(db, task.criadorTaskId):
            raise HTTPException(status_code = 404, detail = "Criador da task Não encontrado")

        newTask = Task(
            title = task.title,
            description = task.description,
            status = task.status,
            criadorTaksId = task.criadorTaskId ,
            usuarioTaskId = task.usuarioTaskId,
        )

        return TaskRepository.criarTask(db, newTask)

    @staticmethod
    def listarTask(db: Session):
        tasks = TaskRepository.listarTasks(db)
        return [TaskResponse.model_validate(i) for i in tasks]
    
    # def deleteTask(db: Session, id: int):

    
