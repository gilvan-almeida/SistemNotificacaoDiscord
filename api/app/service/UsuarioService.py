from fastapi import HTTPException
from models.Usuario import Usuario
from schemas.Usuario import UsuarioResponse
from Repository.UsuarioRepository import UsuarioRepository

class UsuarioService:
    @staticmethod
    def criarUsuario(usuario: Usuario, db):
        if UsuarioRepository.getEmailUser(db, usuario.email):
            raise HTTPException(status_code=400, detail  ="Email ja cadastrado")
        
        if UsuarioRepository.getMatriculaUser(db, usuario.matricula):
            raise HTTPException(status_code = 400, detail = "Matricula ja Cadastrada")
        
        if UsuarioRepository.getDiscordID(db, usuario.discordId):
            raise HTTPException(status_code = 400, detail = "DiscordId ja cadastrado")
        
        newUsuario = Usuario(
            name = usuario.name,
            email = usuario.email,
            senha = usuario.senha,
            matricula = usuario.matricula,
            acesso = usuario.acesso,
            discordId =  usuario.discordId
        )

        return UsuarioRepository.criarUser(db, newUsuario)
    
    @staticmethod
    def buscarUserDiscordId(db, discordId: str):
        result = UsuarioRepository.getDiscordID(db, discordId)
        if not result:
            raise HTTPException(status_code = 404, detail =  "Error, usuario com discord Id não foi encontrado")
        return result

    @staticmethod
    def listarUsuarios(db):
       users = UsuarioRepository.listarUsuarios(db)
       return [UsuarioResponse.model_validate(i) for i in users]

    @staticmethod
    def editarDadosUser(db, id: int, newDados: dict):
        resultUser = UsuarioRepository.getIdUser(db, id)

        if not resultUser: 
            raise HTTPException(status_code = 404, detail = "Error, Usuario não encontrado")
    
        return UsuarioRepository.editarDadosUser(db, id, newDados)

    
    @staticmethod
    def deleteDadosUser(db, id: int):
        usuario = UsuarioRepository.getIdUser(db, id)
        if not usuario:
            raise HTTPException(status_code = 404, detail = "Erro id não encontrado")
        
        UsuarioRepository.deleteUser(db, id)
        
        return {"message": "Usuário deletado com sucesso"}
    

