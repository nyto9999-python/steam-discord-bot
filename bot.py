import discord
from discord.ext import commands
import csv
import steamTop10
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

    execfile('steamTop10.py')

    f = open("C:/github/steamtop10/Steam.txt", "r", encoding="utf-8")



@bot.event
async def on_member_join(member):
    channel = bot.get_channel(861601242508951562)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(861601242508951562)
    await channel.send(f'{member} join!')


@bot.command()
async def steam(ctx):

    f = open("C:/github/steamtop10/Steam.txt", "r", encoding="utf-8")
    await ctx.send(f'{f.read()}')

bot.run('//bot token')
