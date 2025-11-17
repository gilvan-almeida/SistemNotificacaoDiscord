from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "Deu certo, amoooor!"}


@app.get("/teste1")
def teste1():
    return {"mesg":"Guygames game play e resenhas futebol club"}