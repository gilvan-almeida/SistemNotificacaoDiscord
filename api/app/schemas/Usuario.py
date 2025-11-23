from datetime import datetime
from pydantic import BaseModel, EmailStr
from models.Enums import nivelAcesso
from typing import Optional

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
    dataCreateUser: Optional[datetime] = datetime.now()

class UsuarioUpdate(BaseModel):
    matricula: Optional[int] = None
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    acesso: Optional[int] = None
    discordId: Optional[str] = None

class UsuarioResponse(UsuarioBase):
    pass

