from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import sessionLocal
from typing import List
from schemas.Usuario import UsuarioCreate, UsuarioResponse
from service.UsuarioService import UsuarioService


router = APIRouter(prefix="/usuarios")

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model = UsuarioResponse)
def criarUsuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return UsuarioService.criarUsuario(usuario, db)


@router.get("/", response_model= List[UsuarioResponse])
def listarUsuario(db: Session = Depends(get_db)):
    return UsuarioService.listarUsuarios(db)

