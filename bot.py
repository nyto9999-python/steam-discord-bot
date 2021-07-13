import datetime
from os import name
import discord
from discord.ext import commands
import csv
import fetchSteamSearch,fetchSteamPlayer,fetchSteamtop10,steamPlayerPlot
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

Search_info = [] # 搜尋到的遊戲列表
Price = [] #價錢
Imgae = [] #圖片
Discount = [] #特價
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

# Steam top 10 games
@bot.command()
async def top10(ctx):
    start = time.time()
    fetchSteamtop10 # dowload steam data from steam website

    embedVar = discord.Embed(title="Steam熱門遊戲",timestamp=datetime.datetime.utcnow(), url="https://store.steampowered.com/search/?filter=globaltopsellers&page=1&os=win",description="排行", color=0x808080)
    with open('C:/github/steamtop10/steamtop10.txt',"r",encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # the specific rows we want
        interestingrows=[row for idx, row in enumerate(csv_reader) if idx in (1,2,3,4,5,6,7,8,9,10)]
    for row in interestingrows:
        #row[0] game title, row[1] review, row[2] price, row[3] hyperlink
        embedVar.add_field(name=row[0], value="[:thumbsup:    "+row[1]+'    :moneybag:    '+row[2]+']('+row[3]+')', inline=False)
    end = time.time()
    embedVar.set_footer(text="執行時間：%f 秒" % (end - start))
    await ctx.send(embed=embedVar)


# steam玩家人數 steam current players
@bot.command()
async def player(ctx):
    start = time.time()
    fetchSteamPlayer # download player data from steamchart.com
    steamPlayerPlot
    file = discord.File("C:/github/steamtop10/steamPlayer.png", filename="steamPlayer.png") # use this way for inserting img to thumbnail

    embedVar = discord.Embed(title="今日玩家人數",timestamp=datetime.datetime.utcnow(), url="https://steamcharts.com/top",description="^^", color=0x808080)
    embedVar.set_thumbnail(url="attachment://steamPlayer.png")

    with open('C:/github/steamtop10/steamPlayer.txt',"r",encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # the specific rows we want
        interestingrows=[row for idx, row in enumerate(csv_reader) if idx in (1,2,3,4,5,6,7,8,9,10)]
    for row in interestingrows:
        #row[0] game title, row[1] review, row[2] price, row[3] hyperlink
        embedVar.add_field(name=row[0], value=":family_mwbb:    當前人數    "+row[1]+'    :fire:    今日最高'+row[2], inline=False)
    end = time.time()
    embedVar.set_footer(text="執行時間：%f 秒" % (end - start))

    await ctx.send(file=file, embed=embedVar)






@bot.event
async def on_message(message):
    thumb_down = '👎'
    data = []
    if message.author.id == 697221038076985355:
        await message.channel.send(f"{message.author.mention} shup up")
        await message.add_reaction(thumb_down)
        await bot.process_commands(message)
    # search steam game
    if message.content.startswith("!f"):
        start = time.process_time()
        if True == fetchSteamSearch.run(Search_info,Price, Discount, Imgae, fetchSteamSearch.get_text("https://store.steampowered.com/search/?term="+ message.content[2:])):
            fetchSteamSearch.save_data(Search_info)

            with open('C:/github/steamtop10/steamSearch.txt',"r",encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                # the specific rows we want
                for row in csv_reader:
                    if row:
                        columns = [row[0], row[1], row[2], row[3]]
                        data.append(columns)

            url = "https://store.steampowered.com/search/?term="+message.content[2:].replace(" ",'%20')
            embedVar = discord.Embed(title=row[0], url= url, color=0xc27c0e)
            embedVar.set_thumbnail(url=data[-1][3])
            embedVar.add_field(name="\u200B", value= ':moneybag:'+data[-1][1 ]+ '    折扣::small_red_triangle_down:'+ data[-1][2], inline=False)
            end = time.process_time()
            embedVar.set_footer(text="執行時間：%.2f 秒" % (end - start))
            await message.channel.send( embed=embedVar)
        else:
            await message.channel.send("No result")


    else:
        await bot.process_commands(message)


bot.run('//bot token')
