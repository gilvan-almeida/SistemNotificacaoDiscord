import discord
from discord.ext import commands
from views.confirmView import confirmView
from services.api import getUserDiscordId, iniciarTaskUser, pausarTaskUser, verifcarSecao, retomarTaskUser, finalizarTaskUser

class PainelView(discord.ui.View):
    
    def __init__(self, taskId: int, discordId: str):
        super().__init__()  
        self.discordId = discordId
        self.taskId = taskId
        self.secaoId = None

        self.iniciarTask.disabled = False
        self.pausarTask.disabled = True
        self.retomarTask.disabled = True
        self.finalizarTask.disabled = True

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if str(interaction.user.id) != self.discordId:
            await interaction.response.send_message(
                "❌ Apenas o usuário que executou o comando pode interagir com estes botões.",
                ephemeral=True
            )
            return False
        return True



    async def botCheckSession(self):
        try:
            statusDados = await verifcarSecao(self.discordId)

            print(f"Dados retornados da API: {statusDados}")

            if not statusDados or statusDados["status"] == "NINGUEM":
                self.iniciarTask.disabled = False
                self.pausarTask.disabled = True
                self.finalizarTask.disabled = True
                return
            
            secao = statusDados.get("secao")
            if not secao:
                self.iniciarTask.disabled = False
                self.pausarTask.disabled = True
                self.retomarTask.disabled = True
                self.finalizarTask.disabled = True
                self.secaoId = None
                return
            
            secao = statusDados["secao"]
            status = statusDados["status"]
            self.secaoId = secao["id"] 

            if status == "Ativa":
                self.iniciarTask.disabled = True
                self.pausarTask.disabled = False
                self.finalizarTask.disabled = False

            elif status == "Pausada":
                self.iniciarTask.disabled = True
                self.pausarTask.disabled = True
                self.retomarTask.disabled = False
                self.finalizarTask.disabled = False

            elif status == "Finalizada":
                self.iniciarTask.disabled = True
                self.pausarTask.disabled = True
                self.retomarTask.disabled = True
                self.finalizarTask.disabled = True

            else:
                print(f"⚪ Status desconhecido: {status}")
                self.iniciarTask.disabled = False
                self.pausarTask.disabled = True
                self.retomarTask.disabled = True
                self.finalizarTask.disabled = True

        except Exception as e:
            print(f"Erro no botCheckSession: {e}")
            import traceback
            traceback.print_exc()
            self.iniciarTask.disabled = False
            self.pausarTask.disabled = True
            self.retomarTask.disabled = True
            self.finalizarTask.disabled = True
            self.secaoId = None

    @discord.ui.button(
        label="Iniciar Task", 
        emoji="🚀",
        style=discord.ButtonStyle.green,
        custom_id="btn_iniciar"
    )
    async def iniciarTask(self, interaction: discord.Interaction, button):
        discordId = str(interaction.user.id)

        user = await getUserDiscordId(discordId)

        if not user:
            await interaction.response.send_message(
                "❌ Você não está cadastrado no sistema.",
                ephemeral=True 
            )
            return
        
  
        secao = await iniciarTaskUser(discordId)

        self.secaoId = secao['id']

        button.disabled = True
        self.pausarTask.disabled = False
        self.finalizarTask.disabled = False

        await interaction.response.send_message(content=f"🚀 Task iniciada! Sessão ID: `{secao['id']}`")
        await interaction.message.delete()

    @discord.ui.button(
        label="Pausar",
        emoji="⏸️",
        style=discord.ButtonStyle.grey,
        custom_id="btn_pausar"
    )
    async def pausarTask(self, interaction: discord.Interaction, button):
        try:
            if not self.secaoId:
                await interaction.response.send_message(
                    "❌ Nenhuma sessão ativa.", 
                    ephemeral=True
                )
                return
            
            resultado = await pausarTaskUser(self.secaoId)
            
            self.iniciarTask.disabled = True
            self.pausarTask.disabled = True
            self.retomarTask.disabled = False
            self.finalizarTask.disabled = False

            await interaction.response.send_message(
                content=f"⏸️ Sessão pausada! Tempo total: {resultado['secao']['timeSessionS']} segundos", 
            )
            await interaction.message.delete()

        except Exception as e:
            print(f"Erro ao pausar sessão: {str(e)}")
            await interaction.response.send_message(
                f"❌ Erro ao pausar sessão: {str(e)}",
                ephemeral=True
            )

    @discord.ui.button(
        label="Retomar",
        emoji="▶️",
        style=discord.ButtonStyle.blurple,
        custom_id="btn_retomar"
    )
    async def retomarTask(self, interaction: discord.Interaction, button):
        try:
            if not self.secaoId:
                await interaction.response.send_message(
                    "❌ Nenhuma sessão para retomar.", 
                    ephemeral=True
                )
                return           
            
            resultado = await retomarTaskUser(self.secaoId)

            self.iniciarTask.disabled = True
            self.pausarTask.disabled = False
            self.retomarTask.disabled = True
            self.finalizarTask.disabled = False

            await interaction.response.send_message(
                content=f"▶️ Sessão retomada!", 
            )
            await interaction.message.delete()

        except Exception as e:
            print(f"Erro ao retomar sessão: {str(e)}")
            await interaction.response.send_message(
                f"❌ Erro ao retomar sessão: {str(e)}",
                ephemeral=True
            )

    @discord.ui.button(
        label="Finalizar",
        emoji="🛑",
        style=discord.ButtonStyle.red,
        custom_id="btn_finalizar"
    )
    async def finalizarTask(self, interaction: discord.Interaction, button):
        await interaction.response.send_modal(confirmView(self))