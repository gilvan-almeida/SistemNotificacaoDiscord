from datetime import datetime
from pydantic import BaseModel, EmailStr
from models.Enums import nivelAcesso

class UsuarioBase(BaseModel):
    id: int
    matricula: int
    name: str
    email: EmailStr
    acesso: nivelAcesso
    discordId: str
    dataCreateUser: datetime

    class Config():
        from_attributes = True 

class UsuarioCreate(BaseModel):
    matricula: int
    name: str
    senha: str
    email: str
    discordId: str
    acesso: nivelAcesso = nivelAcesso.USER    
    dataCreateUser: datetime

class UsuarioResponse(UsuarioBase):
    pass

