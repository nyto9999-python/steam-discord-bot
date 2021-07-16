from os import name
import discord, time, os, json
from discord import member
from discord import channel
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import pandas as pd
from bs4 import BeautifulSoup


with open('setting.json', 'r', encoding="utf8") as jFile:
    discord_setting = json.load(jFile)
# intents = discord.Intents.default()
# intents.members = True
bot = commands.Bot(command_prefix='!')
slash = SlashCommand(bot, sync_commands= True)
@bot.event
async def on_ready():
    print(">>Bot is online<<")


#welcom message
@bot.event
async def on_member_join(member):
    guild = bot.get_guild(int(discord_setting['Guild_Channel']))                        #server id
    channel = guild.get_channel(int(discord_setting['Chat_Channel']))                     #channel id
    await channel.send(f'嗨 {member.mention}!\n !ask可查詢指令')

# load, unload, reload
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded{extension} done.')

@bot.command()
async def un(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Un-loaded{extension} done.')

@bot.command()
async def re(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re-loaded{extension} done.')



for Filename in os.listdir('cmds'):
    if Filename.endswith('.py'):
        print(Filename[:-3])
        bot.load_extension(f'cmds.{Filename[:-3]}')





bot.run(discord_setting['TOKEN'])



