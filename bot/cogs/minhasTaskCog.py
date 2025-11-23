import discord
from discord.ext import commands
from services.api import getTaskUser, getUserDiscordId , verifcarSecao
from views.painelView import PainelView
from datetime import datetime
from utils.formatDate import formatDate
from utils.formatHoras import formatHoras

class MinhasTasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name="minhaTask")
    async def minha_task(self, ctx):
        discordId = str(ctx.author.id)
        
        user = await getUserDiscordId(discordId)
        task = await getTaskUser(discordId)

        if not user:
            await ctx.send("❌ Usuário não cadastrado no banco, falar com Administrador para mais informações")
            return

        if not task:
            await ctx.send("❌ Você não tem nenhuma Task cadastrada no momento")
            return
        
        if task.get('status') in ['Finalizada', 'Concluída', 'Encerrada']:  # Adapte para seus status
            await ctx.send("❌ Você não tem nenhuma Task ativa no momento")
            return
        
        secao = await verifcarSecao(discordId)  
        
        taskId = task["id"]
        view = PainelView(taskId, discordId)
        await view.botCheckSession()

        # print(f" Task: {task}")
        # print(f" Secao: {secao}")

        mention = ctx.author.mention
        nameDisc = ctx.author.display_name

        await ctx.send(f"{mention}")


        embed = discord.Embed(
            title= task['title'],
            color=discord.Color.green(),
            description= task['description']
        )
        embed.set_author(name=f"Destinatario: {nameDisc}")

        embed.set_image(url="https://i.imgur.com/GxXx7qE.png")

        if secao and secao.get("secao"):
            status_secao = secao["secao"].get("statusSecao", "Nenhuma")
            tempo_sessao = secao["secao"].get("timeSessionS", 0)
            horaFormatada = formatHoras(tempo_sessao)
        else:
            status_secao = "Nenhuma sessão"
            horaFormatada = "00:00:00"

        embed.add_field(name="Status Secao: ", value = status_secao)

        dataInicio = formatDate(task['dateTaskCreate'])
        embed.add_field(name="Iniciada em", value = dataInicio)

        embed.add_field(name="Tempo de Secão: ", value = horaFormatada, inline = False)
       
        embed.set_thumbnail(url="https://scontent-for2-1.cdninstagram.com/v/t51.2885-19/501585496_17869588206372782_4866275767702682431_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-for2-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2QEVUGPfGvFmbPhH7reBM2Xl1hq79TgK6Lx-1JUOTnNQk3c82SDTFnhfFc95wB21tLc&_nc_ohc=PY8ZbuevTwwQ7kNvwEPOFA3&_nc_gid=rhl1IB8KzcP1kQl5wYjb-w&edm=APoiHPcBAAAA&ccb=7-5&oh=00_AfjrRfe3KULmEB0CDjacMut7gBudi2U-BAtE2M81rAf5Jw&oe=692622D2&_nc_sid=22de04")
        
        embed.timestamp = datetime.now()

        embed.set_footer(text="Sistema de Tasks • Gilvan Almeida")

        await ctx.send(embed=embed, view = view)

async def setup(bot):
    await bot.add_cog(MinhasTasks(bot))