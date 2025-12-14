import os
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from jose import jwt
from models.Usuario import Usuario
from Repository.UsuarioRepository import UsuarioRepository
from config.database import sessionLocal
from schemas.AuthSchemas import LoginRequest, TokenResponse
from passlib.context import CryptContext
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated = "auto")

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITMO = "HS256"
TIMEEXP = 60

class AuthService:

    @staticmethod
    def verificarPassword(password, hashPassword):
        return pwd_context.verify(password, hashPassword)
    
    @staticmethod
    def createToken(valorUser: dict):
        valorEncoder = valorUser.copy()
        exp = datetime.now(timezone.utc) + timedelta(minutes= TIMEEXP)
        valorEncoder.update({"expira": exp})
        return jwt.encode(valorEncoder, SECRET_KEY, algorithm= ALGORITMO)
    

    @staticmethod
    def login(db: Session, valoresUser: LoginRequest) -> TokenResponse:
        
        user = UsuarioRepository.getEmailUser(db, valoresUser.email)

        if not user:
            raise HTTPException(status_code = 404, detail = "Erro usuario não encontrado")

        if not AuthService.verificarPassword(valoresUser.password, user.senha):
            raise HTTPException(status_code = 401, detail = "dados invalidos")
        
        token = AuthService.createToken({"sub" :  str(user.id)})

        return TokenResponse(acessToken=token, typeToken= "bearer")