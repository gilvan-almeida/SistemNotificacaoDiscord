from sqlalchemy import Column, Integer, String, DateTime, Enum
from datetime import datetime, timezone
from config.database import Base
from models.Enums import nivelAcesso

class Usuarios(Base):
    
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key = True, index = True)
    name =  Column(String, nullable = False)
    senha = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    acesso = Column(Enum(nivelAcesso), default= nivelAcesso.USER, nullable = False)
    discordId = Column(String, nullable = False, unique = True)
    dataCreateUser = Column(DateTime(timezone = True), default = lambda:datetime.now(timezone.utc), nullable= False)

