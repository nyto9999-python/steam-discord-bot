import discord,time,datetime,fetchSteamSearch,csv
from discord.ext import commands
from core.classes import Cog_Extension



class Event(Cog_Extension):
    pass




def setup(bot):
    bot.add_cog(Event(bot))
