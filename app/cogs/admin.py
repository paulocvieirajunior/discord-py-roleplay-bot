from typing import Literal

from discord import HTTPException, Object
from discord.ext.commands import Bot, Cog, Context, Greedy, command, is_owner

SYNC_SCOPE = Literal["^", "~", "*"]


class Admin(Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @command(description="Syncronize commands")
    @is_owner()
    async def sync(
        self, ctx: Context, guilds: Greedy[Object], scope: SYNC_SCOPE | None = None
    ):
        if guilds:
            ret = 0

            for guild in guilds:
                try:
                    await self.bot.tree.sync(guild=guild)
                    ret += 1
                except HTTPException:
                    pass
            await ctx.reply(f"Commands synced to {ret} guild(s)!")
            return

        match scope:
            case "*":
                self.bot.tree.copy_global_to(guild=ctx.guild)
                synced = await self.bot.tree.sync()
                await ctx.reply(f"{len(synced)} commands synced globally!")

            case "~":
                synced = await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply(f"{len(synced)} commands synced locally!")

            case "^":
                self.bot.tree.clear_commands(guild=ctx.guild)
                synced = await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply(f"{len(synced)} commands removed locally!")

            case _:
                synced = await self.bot.tree.sync()
                await ctx.reply(f"{len(synced)} commands synced globally!")


async def setup(bot: Bot):
    await bot.add_cog(Admin(bot))
