
from os import name
import discord
from discord.ext import commands
from core.classes import Cog_Extension
import fetchSteamtop10,fetchSteamPlayer,steamPlayerPlot,fetchSteamSearch
import time,datetime,csv
import re, json
import py_compile
with open('setting.json', 'r', encoding="utf8") as jFile:
    data = json.load(jFile)
 #https://store.steampowered.com/category/"類別"/#p=0&tab=TopSellers
    #https://store.steampowered.com/specials/#p=0&tab=TopSellers 特價
# category = {
#     "action" : 'action',
#     "action_rogue_like" : 'Rogue',
#     "action_tps" : 'tps',
#     "action_fps" : 'fps',
#     "multiplayer": '多人'
# }

# for en, ch in category.items():
#     if ch == "多人":
#         print('https://store.steampowered.com/category/'+en+'/#p=0&tab=TopSellers')

print(json.dumps(data['Category'], indent=4, sort_keys=True))



for key, value in data['Command'].items():
    embedVar.add_field(name = value, value= key, inline=False)