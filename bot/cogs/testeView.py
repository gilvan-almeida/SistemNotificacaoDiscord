import discord
from discord.ext import commands

class PainelView(discord.ui.View):
    
    def __init__(self):
        super().__init__(timeout=None)
        self.iniciarTask.disabled = False
        self.pausarTask.disabled = True
        self.retomarTask.disabled = True
        self.finalizarTask.disabled = True


    @discord.ui.button(
        label = "Iniciar Task", 
        emoji = "🚀",
        style = discord.ButtonStyle.green,
        custom_id = "btn_inciar"
        )
    async def iniciarTask(self, interaction: discord.Interaction, button):

        button.disabled = True

        self.pausarTask.disabled = False
        self.finalizarTask.disabled = False

        await interaction.response.edit_message(content="Task Iniciada", view = self)
    
    @discord.ui.button(
        label = "Pausar",
        emoji = "⏸️",
        style = discord.ButtonStyle.grey,
        custom_id = "btn_pausar"
    )
    async def pausarTask(self, interaction:  discord.Interaction, button):
        button.disabled = True

        self.retomarTask.disabled = False

        await interaction.response.edit_message(content = "Task Pausada", view = self)


    @discord.ui.button(
        label="Retomar",
        emoji="▶️",
        style=discord.ButtonStyle.blurple,
        custom_id="btn_retomar"
    )
    async def retomarTask(self, interaction: discord.Interaction, button):
        button.disabled = True
        self.pausarTask.disabled = False

        await interaction.response.edit_message(content = "Task Retomada", view = self)

    @discord.ui.button(
        label="Finalizar",
        emoji="🛑",
        style=discord.ButtonStyle.red,
        custom_id="btn_finalizar"
    )
    async def finalizarTask(self, interaction: discord.Integration, button):

        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(content="Sessão finalizada!", view=self)


class TesteViewCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="testeview")
    async def teste_view(self, ctx):
        """Comando que envia a view."""
        view = PainelView()
        await ctx.send("Aqui está sua view:", view=view)


# OBRIGATÓRIO PARA FUNCIONAR !!
async def setup(bot):
    await bot.add_cog(TesteViewCog(bot))