from fastapi import HTTPException
from models.SecaoTask import SecaoTask
from models.Enums import statusSecaoEnum
from sqlalchemy.orm import Session

class SecaoTaskRepository:

    @staticmethod
    def criarSecao(db: Session, secaoDados: SecaoTask):
        db.add(secaoDados)
        db.commit()
        db.refresh(secaoDados)
        return secaoDados
    
    @staticmethod
    def getSecaoId(db: Session, id: int):
        return db.query(SecaoTask).filter(SecaoTask.id == id).first()

    @staticmethod
    def listarSecaoUser(db: Session):
        return db.query(SecaoTask).all()
    
    @staticmethod
    def deleteSecao(db: Session, id: int):
        secaoId = db.query(SecaoTask).filter(SecaoTask.id == id).first()
        if not secaoId:
            raise HTTPException(status_code = 404, detail = "Erro, Secão task não encontrada")
        db.delete(secaoId)
        db.commit()

        return True
    

    @staticmethod
    def getStatusSecaoUser(db: Session, userId: int):
        return db.query(SecaoTask).filter(
            SecaoTask.userId == userId, 
            SecaoTask.statusSecao.in_([statusSecaoEnum.ATIVA, statusSecaoEnum.PAUSADA])
            ).order_by(SecaoTask.id.desc()).first()

        

    @staticmethod
    def salvarObject(db: Session, secaoTask: SecaoTask):
        db.commit()
        db.refresh(secaoTask)
        return secaoTask

    @staticmethod
    def deletarSecao(db: Session, secaoId: int):
        user = db.query(SecaoTask).filter(SecaoTask.id == secaoId).first()
        if not user:
            return None
        
        db.delete(user)
        db.commit()
