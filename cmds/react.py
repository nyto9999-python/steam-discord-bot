from asyncio.tasks import sleep
from os import name
import discord
from discord.ext import commands
from discord.ext.commands.core import command
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option
from core.classes import Cog_Extension
import fetchSteamtop10,fetchSteamPlayer,steamPlayerPlot,fetchSteamSearch,fetchSteamGameType
import time,datetime,csv
import re, json

# Steam top 10 games
with open('setting.json', 'r', encoding="utf8") as jFile:
    data = json.load(jFile)

class React(Cog_Extension):

    #type可用指令
    @cog_ext.cog_slash(name="typeask", description="type指令: 可用的遊戲類型", guild_ids=[int(data['Guild_Channel'])])
    async def _typeask(self, ctx):
        embedVar = discord.Embed(title="已開放: action,rogue, fps, tps, 多人")

        await ctx.send(content = "typeask", embed= embedVar)

    #Steam遊戲排行
    @cog_ext.cog_slash(name="Steam遊戲排行",
                       description="查詢Steam上熱銷遊戲,評價,價格",
                       guild_ids=[int(data['Guild_Channel'])],
                        options=[
                            create_option(
                            name = "enter",
                            description="請輸入1~25",
                            required= True,
                            option_type=3,
                        )])
    async def _Steamchart(self, ctx: SlashContext, enter:str):
        await ctx.defer()
        start = time.time()
        input = re.sub('\D', '', enter) # number only
        fetchSteamtop10.run() # fetch steam chart
        embedVar = discord.Embed(title="Steam熱門遊戲",timestamp=datetime.datetime.utcnow(), url="https://store.steampowered.com/search/?filter=globaltopsellers&page=1&os=win",description="排行", color=0x00ffff)
        with open('steamtop10.txt',"r",encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            interestingrows=[row for idx, row in enumerate(csv_reader) if idx in (range(1,int(input)+1))] # the specific rows we want
        for row in interestingrows:
            #row[0] game title, row[1] review, row[2] price, row[3] hyperlink
            embedVar.add_field(name=row[0], value="[:thumbsup:"+row[1]+':moneybag:'+row[2]+']('+row[3]+')', inline=False)
        end = time.time()
        embedVar.set_footer(text="執行時間：%f 秒" % (end - start))
        await ctx.send(embed=embedVar)

    # steam玩家人數 steam current players
    @cog_ext.cog_slash(name="player", description="Steam遊戲在線人數", guild_ids=[int(data['Guild_Channel'])])
    async def _player(self, ctx):
        await ctx.defer()
        start = time.time()
        fetchSteamPlayer.run()
        steamPlayerPlot
        file = discord.File("steamPlayer.png", filename="steamPlayer.png") # use this way for inserting img to thumbnail

        embedVar = discord.Embed(title="今日玩家人數",timestamp=datetime.datetime.utcnow(), url="https://steamcharts.com/top",description="^^", color=0x00ffff)
        embedVar.set_thumbnail(url="attachment://steamPlayer.png")
        with open('steamPlayer.txt',"r",encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            interestingrows=[row for idx, row in enumerate(csv_reader) if idx in (range(1,11))]
        for row in interestingrows:
            #row[0] game title, row[1] review, row[2] price, row[3] hyperlink
            embedVar.add_field(name=row[0], value=":family_mwbb:當前人數"+row[1]+':fire:今日最高'+row[2], inline=False)
        end = time.time()
        embedVar.set_footer(text="執行時間：%f 秒" % (end - start))
        await ctx.send(file=file, embed=embedVar)

    #sear type 搜尋遊戲by種類
    @cog_ext.cog_slash(name="Steam遊戲搜尋byType",
                       description="查詢特定遊戲,評價,價格",
                       guild_ids=[int(data['Guild_Channel'])],
                        options=[
                            create_option(
                            name = "enter",
                            description="action, tps, fps, rogue, etc. 更多資訊請查typeask",
                            required= True,
                            option_type=3,
                        )])
    async def _type(self, ctx: SlashContext, enter:str):
        await ctx.defer()
        start = time.time()
        type = search_jcategory(enter)
        if type != "Not found":
            fetchSteamGameType.run('https://store.steampowered.com/category/'+str(type)+'/#p=0&tab=TopSellers')
            embedVar = discord.Embed(title="Steam",timestamp=datetime.datetime.utcnow(),description= "Type: "+enter.capitalize(), color=0x00ffff)
            with open('steamtype.txt',"r",encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                interestingrows=[row for idx, row in enumerate(csv_reader) if idx in (range(1,16))]
                for row in interestingrows:
                    #Steam遊戲類別,圖片,價格,鏈接
                    embedVar.add_field(name=row[0], value='[Price:'+row[2]+']('+row[3]+')', inline=False)
            end = time.time()
            embedVar.set_footer(text="執行時間：%f 秒" % (end - start))
            await ctx.send(embed=embedVar)
        else:
            end = time.process_time()
            embedVar = discord.Embed(title="No result", color=0x00ffff)
            embedVar.set_footer(text="執行時間：%.2f 秒" % (end - start))
            await ctx.send(embed=embedVar)

    #steam 遊戲搜尋
    @cog_ext.cog_slash(name="Steam遊戲搜尋",
                       description="查詢特定遊戲,評價,價格",
                       guild_ids=[int(data['Guild_Channel'])],
                        options=[
                            create_option(
                            name = "enter",
                            description="請輸入遊戲名稱",
                            required= True,
                            option_type=3, #string
                        )])
    async def _Steamseaerch(self, ctx: SlashContext, enter:str):
        await ctx.defer()
        data = []
        start = time.process_time()
        if fetchSteamSearch.run("https://store.steampowered.com/search/?term="+ enter): #有抓到
            with open('steamSearch.txt',"r",encoding="utf-8") as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                # the specific rows we want
                for row in csv_reader:
                    if row:
                        columns = [row[0], row[1], row[2], row[3]]
                        data.append(columns)

            url = "https://store.steampowered.com/search/?term="+enter.replace(" ",'%20')
            embedVar = discord.Embed(title=row[0], url= url, color=0x00ffff)
            embedVar.set_thumbnail(url=data[-1][3])
            embedVar.add_field(name="\u200B", value= ':moneybag::    '+data[-1][1 ]+ '    折扣::small_red_triangle_down:'+ data[-1][2], inline=False)
            end = time.process_time()
            embedVar.set_footer(text="執行時間：%.2f 秒" % (end - start))
            await ctx.send(embed=embedVar)
        else: #沒抓到
            end = time.process_time()
            embedVar = discord.Embed(title="No result", color=0x00ffff)
            embedVar.set_footer(text="執行時間：%.2f 秒" % (end - start))
            await ctx.send(embed=embedVar)

def setup(bot):
    bot.add_cog(React(bot))

def search_jcategory(ctx):
    if ctx.strip() in data['Category']:
        return data['Category'][ctx.strip()]
    else:
        return "Not found"




