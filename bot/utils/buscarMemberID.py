from discord.utils import get

async def buscarMember(guild, nome=None, discordId= None):
    
    if discordId:
        return guild.get_member(discordId)
    
    elif nome:
        return get(guild.members, name=nome)
    
    return None