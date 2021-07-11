import discord
from discord.ext import commands
import csv
import steamtop10
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

# @bot.event
# async def on_member_join(member):
#     channel = bot.get_channel(861601242508951562)
#     await channel.send(f'{member} join!')

# @bot.event
# async def on_member_remove(member):
#     channel = bot.get_channel(861601242508951562)
#     await channel.send(f'{member} join!')


# @bot.command()
# async def stedddam(ctx):

#     # f = open("C:/github/steamtop10/Steam.txt", "r", encoding="utf-8")
#     # await ctx.send(f'{f.read()}')
#     execfile('steamTop10.py')
#     temp = []
#     with open('C:/github/steamtop10/Steam.txt',"r",encoding="utf-8") as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             else:
#                 embedVar = discord.Embed(title=row[0], description=row[1], color=0x00ff00)
#                 embedVar.add_field(name="Price", value=row[2], inline=False)
#                 line_count += 1
#                 await ctx.send(embed=embedVar)
#         for i in temp:


@bot.command()
async def steam(ctx):
    steamtop10
    embedVar = discord.Embed(title="Steam熱門遊戲", url="https://store.steampowered.com/search/?filter=globaltopsellers&page=1&os=win",description="排行", color=0x00ff00)
    with open('C:/github/steamtop10/Steam.txt',"r",encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        interestingrows=[row for idx, row in enumerate(csv_reader) if idx in (1,2,3,4,5,6,7,8,9,10)]
        for row in interestingrows:

            embedVar.add_field(name=row[0], value="評分"+row[1]+"價格"+row[2], inline=False)

    await ctx.send(embed=embedVar)





<<<<<<< HEAD
bot.run('discord token')
=======
bot.run('//bot token')
>>>>>>> 89097300e47474333dbc042f37444bf09bfd026f
