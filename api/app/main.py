from sqlalchemy import text
from fastapi import FastAPI
from routers import UsuariosRouter
from routers import TaskRouter
from routers import SecaoTaskRouter

app = FastAPI(title="Api notificação Discord Bot")

app.include_router(UsuariosRouter.router)
app.include_router(TaskRouter.router)
app.include_router(SecaoTaskRouter.router)

@app.get("/")
def home():
    return {"msg": "API rodando "}






# @app.get("/test-db")
# def test_db():
#     try:
#         db = sessionLocal()
#         db.execute(text("SELECT 1"))
#         return {"status": "Conectado ao banco com sucesso! "}
#     except Exception as e:
#         return {"status": "Erro ao conectar no banco", "detalhe": str(e)}
#     finally:
#         db.close()