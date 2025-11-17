from fastapi import Depends, APIRouter, HTTPException
from config.database import sessionLocal
from typing import List
from sqlalchemy.orm import Session
from service.TaskService import TaskService
from schemas.Task import TaskCreate, TaskResponse, TaskBase

router = APIRouter(prefix="/task")

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model = TaskResponse)
def criarTask(task: TaskCreate, db: Session = Depends(get_db)):
    return TaskService.criarTask(db, task)

@router.get("/", response_model = List[TaskResponse])
def listarTasks(db: Session = Depends(get_db)):
    return TaskService.listarTask(db)