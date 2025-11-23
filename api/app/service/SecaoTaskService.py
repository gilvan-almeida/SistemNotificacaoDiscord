from schemas.SecaoTask import SecaoTaskBase, SecaoTaskCreate, SecaoTaskResponse
from models.SecaoTask import SecaoTask
from models.Enums import statusSecaoEnum, statusTask
from fastapi import HTTPException
from datetime import datetime, timezone, timedelta
from Repository.SecaoTaskRepository import SecaoTaskRepository
from Repository.TaskRepository import TaskRepository
from sqlalchemy.orm import Session

class SecaoTaskService:

    @staticmethod
    def criarSecao(db: Session, secao: SecaoTaskCreate):
        task =TaskRepository.getTaskId(db, secao.taskId)
        if not task:
            raise HTTPException(status_code=404, detail="Erro, Task não encontrada")
        
        if task.status == statusTask.ENCERRADO:  
            raise HTTPException(status_code=400, detail="Erro, Task já finalizada")
        
        secao_existente = SecaoTaskRepository.getStatusSecaoUser(db, secao.userId)
        if secao_existente:
            raise HTTPException(status_code=400, detail="Erro, já existe uma sessão ativa/pausada para este usuário")
        
        newSecao = SecaoTask(
            taskId=secao.taskId,
            userId=secao.userId,
            statusSecao=statusSecaoEnum.ATIVA,
            timeStart=datetime.now(timezone.utc),
            timeSessionS=0
        )

        return SecaoTaskRepository.criarSecao(db, newSecao)
    
    @staticmethod
    def pausarSecao(db: Session, secaoId: int):
        secao = SecaoTaskRepository.getSecaoId(db, secaoId)

        if not secao:
            raise HTTPException(404, "Sessão não encontrada")


        timeNow = datetime.now(timezone.utc)

        elapse = int((timeNow - secao.timeStart).total_seconds())


        if secao.timeSessionS is None:
            secao.timeSessionS = 0

        secao.timeSessionS += elapse
        secao.timeStart = None
        secao.statusSecao = statusSecaoEnum.PAUSADA

        return SecaoTaskRepository.salvarObject(db, secao)
    
    @staticmethod
    def retomarSecao(db: Session, secaoId: int):
        secao = SecaoTaskRepository.getSecaoId(db, secaoId)
        
        if not secao:
            raise HTTPException(404, "Sessão não encontrada")

        if secao.statusSecao == statusSecaoEnum.FINALIZADA:
            raise HTTPException(400, "Sessão já finalizada")

        if secao.statusSecao != statusSecaoEnum.PAUSADA:
            raise HTTPException(400, "Sessão não está pausada")        

        
        secao.timeStart = datetime.now(timezone.utc)
        secao.statusSecao = statusSecaoEnum.ATIVA

        return SecaoTaskRepository.salvarObject(db, secao)
    
    @staticmethod
    def finalizarSecao(db: Session, secaoId: int):
        secao = SecaoTaskRepository.getSecaoId(db, secaoId)
        task = TaskRepository.getTaskId(db, secao.taskId)

        if not secao:
            raise HTTPException(404, "Sessão não encontrada")    
        
        if secao.statusSecao == statusSecaoEnum.FINALIZADA:
            raise HTTPException(400, "secão ja finalizada")

        timeNow = datetime.now(timezone.utc)

        if secao.timeStart and secao.statusSecao == statusSecaoEnum.ATIVA:
            elapse = int((timeNow - secao.timeStart).total_seconds())
            if secao.timeSessionS is None:
                secao.timeSessionS = 0
            secao.timeSessionS += elapse

        secao.statusSecao = statusSecaoEnum.FINALIZADA
        secao.timeStart = None
        secao.timeEnd = timeNow


        if task:
            task.status = statusTask.ENCERRADO
        
        return SecaoTaskRepository.salvarObject(db, secao)


    @staticmethod
    def verificarTaskOn(db: Session, userId: int):
        secao = SecaoTaskRepository.getStatusSecaoUser(db, userId)
        return secao

    
    @staticmethod
    def deleteSecao(db: Session, secaoId: int):
        return SecaoTaskRepository.deletarSecao(db, secaoId)


    @staticmethod
    def listarSecao(db: Session):
        secao = SecaoTaskRepository.listarSecaoUser(db)
        return [SecaoTaskResponse.model_validate(i) for i in secao]
    
