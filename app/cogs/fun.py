from discord import Interaction
from discord.app_commands import command
from discord.ext.commands import Bot, Cog


class Fun(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @command(description="Responde com um pong!")
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message("Pong!")


async def setup(bot: Bot):
    await bot.add_cog(Fun(bot))
