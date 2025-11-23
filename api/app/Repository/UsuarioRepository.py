from fastapi import HTTPException
from models.Usuario import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:

    @staticmethod
    def criarUser(db: Session, usuario: Usuario): 
        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario
    
    @staticmethod
    def getEmailUser(db: Session, email: str):
        return db.query(Usuario).filter(Usuario.email == email).first()
    
    @staticmethod
    def getIdUser(db: Session, id: int):
        return db.query(Usuario).filter(Usuario.id == id).first()

    @staticmethod 
    def getMatriculaUser(db: Session, matricula: int):
        return db.query(Usuario).filter(Usuario.matricula == matricula).first()

    @staticmethod
    def listarUsuarios(db: Session):
        return db.query(Usuario).all()
    
    @staticmethod
    def getDiscordID(db: Session, discordId: str):
        return db.query(Usuario).filter(Usuario.discordId == discordId).first()

    @staticmethod
    def editarDadosUser(db: Session, id: int, newDados: dict):
        usuario = db.query(Usuario).filter(Usuario.id == id).first()
        if not usuario:
            return None
        for camp, valor in newDados.items():
            setattr(usuario, camp, valor)
        db.commit()
        db.refresh(usuario)
        return usuario

    @staticmethod
    def deleteUser(db: Session, id:int):
        usuario = db.query(Usuario).filter(Usuario.id == id).first()
        if not usuario:
            return None
        db.delete(usuario)
        db.commit()

        return True





    #Em processo , essa função foi feita pensando no buscar do front mas não é final
    # @staticmethod
    # def buscarUserFilter(db: Session, email: str | None = None, matricula: int | None = None):

    #     query = db.query(Usuario)

    #     if matricula is None and email is None:
    #         return None
        
    #     if email is not None and matricula is not None:
    #         raise HTTPException(status_code=400, detail="Envie apenas email OU matrícula")

    #     if email is not None:
    #         query = query.filter(Usuario.email == email).first()

    #     if  matricula is not None:
    #         query = query.filter(Usuario.matricula == matricula).first()

    #     return query