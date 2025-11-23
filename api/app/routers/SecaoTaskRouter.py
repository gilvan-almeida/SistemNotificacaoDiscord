from fastapi import Depends, APIRouter, HTTPException
from config.database import sessionLocal
from typing import List
from sqlalchemy.orm import Session
from schemas.SecaoTask import SecaoTaskBase, SecaoTaskCreate, SecaoTaskResponse, StatusSecaoResponse
from service.SecaoTaskService import SecaoTaskService
import traceback

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

@router.post("/retomar", response_model = SecaoTaskResponse)
def retomarTask(secaoTask: SecaoTaskCreate, db: Session = Depends(get_db)):
    return SecaoTaskService.retomarSecao(db, secaoTask)

@router.post("/finalizar", response_model = SecaoTaskResponse)
def finalizarTask(secaoTask: SecaoTaskCreate, db: Session = Depends(get_db)):
    return SecaoTaskService.finalizarSecao(db, secaoTask)


@router.get("/status/{userId}", response_model = StatusSecaoResponse)
def verificarStatus(userId: int, db: Session = Depends(get_db)):
    userOn = SecaoTaskService.verificarTaskOn(db, userId)

    if not userOn:
        return StatusSecaoResponse(
            status="NENHUM",
            secao=None
        )
    return StatusSecaoResponse(
        status=userOn.statusSecao.value,
        secao=SecaoTaskResponse.model_validate(userOn)
    )

@router.put("/pausar/{secaoId}")
def pausar_secao(secaoId: int, db: Session = Depends(get_db)):
    try:
        secao_atualizada = SecaoTaskService.pausarSecao(db, secaoId)
        return {
            "message": "Sessão pausada com sucesso",
            "secao": {
                "id": secao_atualizada.id,
                "statusSecao": secao_atualizada.statusSecao.value,
                "timeSessionS": secao_atualizada.timeSessionS,
                "timeStart": secao_atualizada.timeStart.isoformat() if secao_atualizada.timeStart else None
            }
        }
    
    except HTTPException as e:
        print(f"HTTPException: {e.detail}")
        raise e
    
    except Exception as e:
        print(f"Erro interno: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")
    
@router.put("/retomar/{secaoId}")
def retomar_secao(secaoId: int, db: Session = Depends(get_db)):
    try:
        print(f"Recebida requisição para retomar sessão: {secaoId}")
        
        secao_atualizada = SecaoTaskService.retomarSecao(db, secaoId)
        
        print(f"Sessão {secaoId} retomada com sucesso")
        
        return {
            "message": "Sessão retomada com sucesso",
            "secao": {
                "id": secao_atualizada.id,
                "statusSecao": secao_atualizada.statusSecao.value,
                "timeStart": secao_atualizada.timeStart.isoformat(),
                "timeSessionS": secao_atualizada.timeSessionS
            }
        }
    except HTTPException as e:
        print(f"HTTPException: {e.detail}")
        raise e
    
    except Exception as e:
        print(f"Erro interno: {str(e)}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")  
 

@router.put("/finalizar/{secaoId}")
def finalizar_secao(secaoId: int, db: Session = Depends(get_db)):
    try:
        print(f"Recebida requisição para finalizar sessão: {secaoId}")
        
        secao_atualizada = SecaoTaskService.finalizarSecao(db, secaoId)
        
        print(f"Sessão {secaoId} finalizada com sucesso")
        
        return {
            "message": "Sessão finalizada com sucesso",
            "secao": {
                "id": secao_atualizada.id,
                "statusSecao": secao_atualizada.statusSecao.value,
                "timeSessionS": secao_atualizada.timeSessionS,
                "timeEnd": secao_atualizada.timeEnd.isoformat() if secao_atualizada.timeEnd else None
            }
        }
    except HTTPException as e:
        print(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        print(f"Erro interno: {str(e)}")

        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")




@router.delete("/{id}")
def deleteSecao(id: int, db: Session = Depends(get_db)):
    return SecaoTaskService.deleteSecao(db, id)


@router.get("/", response_model = List[SecaoTaskResponse])
def listarSecaoTask(db: Session = Depends(get_db)):
    return SecaoTaskService.listarSecao(db)

