import httpx
from config.settings import URL_API

async def getTaskUser(discordId: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{URL_API}/task/{discordId}")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                return None
            else:
                raise

async def getUserDiscordId(discordId: str):
    async with httpx.AsyncClient() as client:
        try:
            reponse = await client.get(f"{URL_API}/usuarios/{discordId}")
            reponse.raise_for_status()
            return reponse.json()
        
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 404:
                return None
            else:
                raise

async def verifcarSecao(discordID: str):
    user = await getUserDiscordId(discordID)
    if not user:
        return None
    idUser = user["id"]

    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{URL_API}/secaoTask/status/{idUser}")
        return resp.json()


async def iniciarTaskUser(discordId: str):
    user = await getUserDiscordId(discordId)

    if not user:
        return None
    
    task = await getTaskUser(discordId)

    if not task:
        return None
    
    dadesLoad = {
        "taskId" : task["id"],
        "userId" : user["id"] 
    }

    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{URL_API}/secaoTask/", json = dadesLoad)
        resp.raise_for_status()
        return resp.json()


async def pausarTaskUser(secaoId: int):
    try:
        url = f"{URL_API}/secaoTask/pausar/{secaoId}"
        async with httpx.AsyncClient() as client:
            resp = await client.put(url)
            resp.raise_for_status()
            return resp.json()
        
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 400:
            raise Exception("Sessão já está pausada ou não está ativa")
        elif e.response.status_code == 404:
            raise Exception("Sessão não encontrada")
        else:
            raise Exception(f"Erro na API: {e.response.status_code}")

async def retomarTaskUser(secaoId: int):
    try:
        url = f"{URL_API}/secaoTask/retomar/{secaoId}"
        async with httpx.AsyncClient() as client:
            resp = await client.put(url)
            resp.raise_for_status()
            return resp.json()
        
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 400:
            try:
                error_detail = e.response.json().get('detail', 'Sessão não pode ser retomada')
            except:
                error_detail = 'Sessão não pode ser retomada'
            raise Exception(error_detail)
        elif e.response.status_code == 404:
            raise Exception("Sessão não encontrada")
        else:
            raise Exception(f"Erro na API: {e.response.status_code}")
        
async def finalizarTaskUser(secaoId: int):
    try:
        url = f"{URL_API}/secaoTask/finalizar/{secaoId}"
        async with httpx.AsyncClient() as client:
            resp = await client.put(url)
            resp.raise_for_status()
            return resp.json()
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 400:
            try:
                error_detail = e.response.json().get('detail', 'Sessão não pode ser finalizada')
            except:
                error_detail = 'Sessão não pode ser finalizada'
            raise Exception(error_detail)
        elif e.response.status_code == 404:
            raise Exception("Sessão não encontrada")
        else:
            raise Exception(f"Erro na API: {e.response.status_code}")