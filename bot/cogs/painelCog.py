import discord
from discord.ext import commands
from discord.utils import get
from views.painelView import PainelView
from datetime import datetime
from utils.buscarMemberID import buscarMember

class painelCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="minhaTask")

    async def teste_view(self, ctx):
        """Comando que envia a view."""

        view = PainelView()

        discordId = "gilvanalmeida"

        member = await buscarMember(ctx.guild, nome=discordId)

        if member:
            mention = member.mention
        else:
            mention = discordId

        print(mention)

        embed = discord.Embed(
            title="Titulo com a Task Aqui",
            color=discord.Color.green()
        )

        teste = await ctx.send(f"{mention}")
        embed.set_image(url="https://i.imgur.com/GxXx7qE.png")
       
        embed.set_thumbnail(url="https://scontent-for2-1.cdninstagram.com/v/t51.2885-19/501585496_17869588206372782_4866275767702682431_n.jpg?stp=dst-jpg_s150x150_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-for2-1.cdninstagram.com&_nc_cat=102&_nc_oc=Q6cZ2QEVUGPfGvFmbPhH7reBM2Xl1hq79TgK6Lx-1JUOTnNQk3c82SDTFnhfFc95wB21tLc&_nc_ohc=PY8ZbuevTwwQ7kNvwEPOFA3&_nc_gid=rhl1IB8KzcP1kQl5wYjb-w&edm=APoiHPcBAAAA&ccb=7-5&oh=00_AfjrRfe3KULmEB0CDjacMut7gBudi2U-BAtE2M81rAf5Jw&oe=692622D2&_nc_sid=22de04")
        embed.set_author(name=f"Destinatario: {member}")
        embed.timestamp = datetime.now()

        embed.description="Use os botões abaixo para controlar sua task."

        embed.set_footer(text="Sistema de Tasks • Vortex")


        await ctx.send(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(painelCog(bot))