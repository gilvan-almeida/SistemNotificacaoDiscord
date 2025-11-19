from fastapi import HTTPException
from models.Usuario import Usuario
from schemas.Usuario import UsuarioResponse
from Repository.UsuarioRepository import UsuarioRepository

class UsuarioService:
    @staticmethod
    def criarUsuario(usuario, db):
        if UsuarioRepository.getEmailUser(db, usuario.email):
            raise HTTPException(status_code=400, detail  ="Email ja cadastrado")
        
        if UsuarioRepository.getMatriculaUser(db, usuario.matricula):
            raise HTTPException(status_code = 400, detail = "Matricula ja Cadastrada")
        
        newUsuario = Usuario(
            name = usuario.name,
            email = usuario.email,
            senha = usuario.senha,
            matricula = usuario.matricula,
            acesso = usuario.acesso,
            discordId=  usuario.discordId
        )

        return UsuarioRepository.criarUser(db, newUsuario)

    @staticmethod
    def listarUsuarios(db):
       users = UsuarioRepository.listarUsuarios(db)
       return [UsuarioResponse.model_validate(i) for i in users]

    

    
 

