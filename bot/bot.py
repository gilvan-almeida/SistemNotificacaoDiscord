import discord
from discord.ext import commands
from config.settings import TOKEN_BOT

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def loadCogs():
    print(f"BOT POCANDO : {bot.user}")
    await bot.load_extension("cogs.testeView")
    # await bot.load_extension("cogs.task")

@bot.event
async def on_ready():
    print("Aqui ta pocando tudooo papai")
    await loadCogs()

bot.run(TOKEN_BOT)