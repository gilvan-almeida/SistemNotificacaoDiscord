from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import sessionLocal
from typing import List
from schemas.Usuario import UsuarioCreate, UsuarioResponse, UsuarioUpdate, UsuarioAuthentic
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


@router.get("/{discordId}", response_model = UsuarioResponse)
def buscarUserDiscordId(discordId: str, db: Session = Depends(get_db)):
    return UsuarioService.buscarUserDiscordId(db, discordId)



@router.get("/", response_model= List[UsuarioResponse])
def listarUsuario(db: Session = Depends(get_db)):
    return UsuarioService.listarUsuarios(db)


@router.put("/{id}", response_model= UsuarioUpdate)
def editarUser(id: int, newdados: UsuarioUpdate, db: Session = Depends(get_db)):
    newdados_dict = newdados.model_dump(exclude_unset=True)
    return UsuarioService.editarDadosUser(db, id, newdados_dict)


@router.delete("/{id}")
def deleteUser(id: int, db: Session = Depends(get_db)):
    return UsuarioService.deleteDadosUser(db, id)