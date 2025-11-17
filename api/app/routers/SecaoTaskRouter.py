from fastapi import Depends, APIRouter
from config.database import sessionLocal
from typing import List
from sqlalchemy.orm import Session
from schemas.SecaoTask import SecaoTaskBase, SecaoTaskCreate, SecaoTaskResponse, SecaoTaskUpdate
from service.SecaoTaskService import SecaoTaskService

router = APIRouter(prefix = "/secaoTask")

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model = SecaoTaskResponse)
def criarSecaoTask(secaoTask: SecaoTaskCreate, db: Session = Depends(get_db)):
    return SecaoTaskService.criarSecao(db, secaoTask)

@router.get("/", response_model = List[SecaoTaskResponse])
def listarSecaoTask(db: Session = Depends(get_db)):
    return SecaoTaskService.listarSecao(db)