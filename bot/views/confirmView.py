import discord
from services.api import finalizarTaskUser
from utils.formatHoras import formatHoras

class confirmView(discord.ui.Modal, title="Confirmar Finalização"):

    def __init__(self, view_ref):
        super().__init__()
        self.view_ref = view_ref 

    confirmacao = discord.ui.TextInput(
        label="Digite CONFIRMAR para finalizar",
        placeholder="CONFIRMAR",
        required=True,
    )

    async def on_submit(self, interaction: discord.Interaction):
        try:
            if self.confirmacao.value.strip().lower() != "confirmar":
                await interaction.response.send_message(
                    "❌ Confirmação inválida.",
                    ephemeral=True
                )
                return
            
            await interaction.message.delete()

            resultado = await finalizarTaskUser(self.view_ref.secaoId)
   
            self.view_ref.iniciarTask.disabled = False
            self.view_ref.pausarTask.disabled = True
            self.view_ref.retomarTask.disabled = True
            self.view_ref.finalizarTask.disabled = True

            tempo_total = formatHoras(resultado['secao']['timeSessionS'])
        
            await interaction.response.send_message(
                content=f"✅ Sessão finalizada! Tempo: {tempo_total}",
            )

            # await asyncio.sleep(5)
            # await interaction.message.delete()

        except Exception as e:
            await interaction.response.send_message(
                f"❌ Erro: {str(e)}",
                ephemeral=True
            )

    async def on_error(self, interaction: discord.Interaction, error: Exception):
        await interaction.response.send_message(
            f"❌ Ocorreu um erro: {str(error)}",
            ephemeral=True
        )