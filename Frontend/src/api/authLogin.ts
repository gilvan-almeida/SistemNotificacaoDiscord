import axios from "axios";
import apiClient from "./clientApi";

interface userAuth {
    email: string,
    password: string;
}

interface dadosUserResponse{
    id: number;
    matricula: number;
    name: string;
    email: string;
    acesso: string;
    discorId: string;
    datauser: string;

}

const loginAuth = async({email, password}: userAuth) => {
    try{
        const reponse = await apiClient.post<dadosUserResponse>('/usuarios/auth', {
            email,
            password
        });


        return reponse.data;


    }catch (error){
        if(axios.isAxiosError(error) && error.response){
            if(error.response.status === 404){
                throw new Error("Email ou senha invalidos")
            }   
            if(error.response.status === 400){
                throw new Error("Dados invalidos, verifique o formato da escrita")
            }
            throw new Error(`Erro no servidor $({error.response})`);
        }

        throw new Error("Falha na conexão de rede. A API está offline?");
    }
}

export default loginAuth;