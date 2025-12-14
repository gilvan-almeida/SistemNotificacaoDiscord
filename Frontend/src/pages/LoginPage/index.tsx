import React, { use, type JSX } from "react";2
import { toast } from "react-toastify";
import { Label, TextInput, Button, Checkbox } from "flowbite-react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import loginAuth from "../../api/authLogin";

import "./Style.css"

function LoginPage() {


    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [errorMsg, setErrorMsg] = useState<string | JSX.Element | null>(null);

    const navigation = useNavigate();

    const subimitDados = async (e: any) =>{
        e.preventDefault();

        try{
            const userDados = await loginAuth({email, password});
            console.log("dados ai do elemento: ", userDados);
            toast.success("Login feito com sucesso")
            setTimeout(() => navigation("/home"), 2000);
        }catch (error) {
              if (error instanceof Error) {
                toast.error("Error email ou senha incorreto")
            } else {
                setErrorMsg("Erro inesperado!");
            }
        }
    }

    return (
        <div className="flex justify-center items-center min-h-screen bg-red-200">
            <form className="w-full max-w-sm flex flex-col gap-4 p-6 rounded-xl shadow-lg bg-white border border-gray-200" onSubmit={subimitDados}>
                <div className="boxInput">
                    <div className="mb-2 block">
                        <Label htmlFor="email1" className="textLabel">Email</Label>
                    </div>
                    <TextInput 
                        id="email1" 
                        type="email" 
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required />
                </div>

                <div className="boxInput">
                    <div className="mb-2 block">
                        <Label htmlFor="password1" className="textLabel">Senha</Label>
                    </div>
                    <TextInput 
                        id="password1" 
                        type="password" 
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required />
                </div>

                <div className="flex items-center gap-2 checkBoxInput">
                    <Checkbox id="remember" />
                    <Label htmlFor="remember">Lembrar Senha</Label>
                </div>
                {errorMsg && (
                    <p className="text-red-600 text-sm font-medium">{errorMsg}</p>
                    )}

                <Button type="submit">Submit</Button>
            </form>
        </div>
    );
}

export default LoginPage;
