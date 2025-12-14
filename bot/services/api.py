import httpx
from config.settings import URL_API
from utils.cache import taskCache, userCache, secaoTaskCache

async def getTaskUser(discordId: str):
    if discordId in taskCache:
        print(f"tem cache para task {discordId}")
        return taskCache[discordId]

    print("não tem cache, fazendo requisicao")

    try:  
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{URL_API}/task/{discordId}")
            if response.status_code == 404:
                taskCache[discordId] = None
                return None
            
            response.raise_for_status()
            dados = response.json()
            taskCache[discordId] = dados
            return dados
        
    except Exception as exc:
        print(f"Error ao buscar task {exc}")
        return None

async def getUserDiscordId(discordId: str):
    if discordId in userCache:
        print(f"tem cache de user {discordId}")
        return userCache[discordId]
    
    print("não tem cache, fazendo requisicao")
    try:
        async with httpx.AsyncClient() as client:
            reponse = await client.get(f"{URL_API}/usuarios/{discordId}")
            if reponse.status_code == 404:
                userCache[discordId] = None
                return None
            
            reponse.raise_for_status()
            dados = reponse.json()
            userCache[discordId] = dados
            return dados
    
    except Exception as exc:
        print(f"Error ao buscar user {exc}")
        return None


async def verifcarSecao(discordID: str):

    if discordID in secaoTaskCache:
        print(f"Existe cache para sesao {discordID}")
        return secaoTaskCache[discordID]
    print("não tem cache para seao id")
    
    user = await getUserDiscordId(discordID)
    if not user:
        return None
    idUser = user["id"]

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{URL_API}/secaoTask/status/{idUser}")
        dados = response.json()
        secaoTaskCache[discordID] = dados
        return dados


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

            taskCache.clear()
            userCache.clear()
            secaoTaskCache.clear()

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