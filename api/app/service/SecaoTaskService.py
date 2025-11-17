from schemas.SecaoTask import SecaoTaskBase, SecaoTaskCreate, SecaoTaskResponse
from models.SecaoTask import SecaoTask
from fastapi import HTTPException
from Repository.SecaoTaskRepository import SecaoTaskRepository
from Repository.TaskRepository import TaskRepository
from sqlalchemy.orm import Session

class SecaoTaskService:

    @staticmethod
    def criarSecao(db: Session, secao: SecaoTaskCreate):
        if not TaskRepository.getTaskId(db, secao.taskId):
            raise HTTPException(status_code = 404, detail = "Erro, Task não encontrada")
        
        newSecao = SecaoTask(
            taskId = secao.taskId,
            userId = secao.userId,
            timeStart = secao.timeStart
        )

        return SecaoTaskRepository.criarSecao(db, newSecao)
    
    @staticmethod
    def listarSecao(db: Session):
        secao = SecaoTaskRepository.listarSecaoUser(db)
        return [SecaoTaskResponse.model_validate(i) for i in secao]