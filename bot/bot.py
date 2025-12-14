import discord
from discord.ext import commands
from services.api import getTaskUser
from config.settings import TOKEN_BOT

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def loadCogs():
    print(f"BOT POCANDO : {bot.user}")
    # await bot.load_extension("cogs.painelCog")
    # await bot.load_extension("cogs.secaoCog")
    await bot.load_extension("cogs.minhasTaskCog")



@bot.event
async def on_ready():
    print("Aqui ta pocando tudooo papai")
    await loadCogs()



bot.run(TOKEN_BOT)