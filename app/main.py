from os import listdir

from core import settings
from discord import Intents
from discord.ext.commands import Bot


class Client(Bot):
    async def setup_hook(self) -> None:
        # Load bot cogs
        for dir in listdir("app/cogs"):
            if dir.endswith(".py"):
                await self.load_extension(f"cogs.{dir[:-3]}")

    async def on_ready(self) -> None:
        print(f"Logged in as {self.user}")


client = Client(
    command_prefix="$",
    intents=Intents.all(),
)


if __name__ == "__main__":
    client.run(settings.BOT_TOKEN)
