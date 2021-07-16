from core.classes import Cog_Extension
import discord
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from discord.ext import commands
import json

with open('setting.json', 'r', encoding="utf8") as jFile:
    data = json.load(jFile)


class Main(Cog_Extension):

    @cog_ext.cog_slash(name="ping", description="Discord ping值", guild_ids=[int(data['Guild_Channel'])])
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')



def setup(bot):
    bot.add_cog(Main(bot))