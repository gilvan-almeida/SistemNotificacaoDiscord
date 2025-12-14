from sqlalchemy import text
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import UsuariosRouter
from routers import TaskRouter
from routers import SecaoTaskRouter

app = FastAPI(title="Api notificação Discord Bot")

app.include_router(UsuariosRouter.router)
app.include_router(TaskRouter.router)
app.include_router(SecaoTaskRouter.router)

origin = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_credentials=True,
    allow_methods=["*"],     
    allow_headers=["*"]
)



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