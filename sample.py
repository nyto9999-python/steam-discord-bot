import os



for Filename in os.listdir('steamtop10\cmds'):
    print(Filename)


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

    # if message.author.id == 697221038076985355 and message.author != self.bot.user:
    #     for i in emoji:
    #         await message.add_reaction(i)
    #     await self.bot.process_commands(message)#warning
    # search steam game


# from typing import Any
# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# num = 0

# def get_text(url):
#     try:
#          headers = {
#      "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/85.0.4183.102 Safari/537.36', 'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4' }
#     except: return "爬取网站失败！"
#     r = requests.get(url, headers=headers)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding
#     return r.text

# def run(game_info, jump_link, game_evaluation, text):
#     soup = BeautifulSoup(text, "html.parser")


#         # 遊戲評價
#     w = soup.find_all(class_ = "col search_reviewscore responsive_secondrow")[:10]
#     for u in w:
#         if u.span is not None:
#             game_evaluation.append(u.span["data-tooltip-html"].split("<br>"[0] + "," + u.span["data-tooltip-html"].split("<br")[-1]))
#         else:
#             game_evaluation.append("暫無評價")

#     # 遊戲頁面連接
#     link_text = soup.find_all("div", id="search_resultsRows")
#     for k in link_text:
#         b = k.find_all('a')
#     for j in b:
#         jump_link.append(j['href'])

#     # 遊戲名稱和價格
#     global num
#     name_text = soup.find_all('div', class_="responsive_search_name_combined")[:10]
#     for z in name_text:
#     # 每個遊戲的價格
#         name = z.find(class_="title").string.strip()
#         print(name)
#     # 判斷是否折扣為None, 提取價格
#         if z.find(class_="col search_discount responsive_secondrow").string is None:
#             price = z.find(class_="col search_price discounted responsive_secondrow").text.strip().split("NT$")
#             game_info.append([num + 1, name, price[2].strip(), game_evaluation[num], jump_link[num]])
#         else:
#             price = z.find(class_="col search_price responsive_secondrow").string.strip().split("NT$")
#             game_info.append([num + 1, name, price[1], game_evaluation[num], jump_link[num]])
#         num = num + 1




# def save_data(game_info):
#     save_path = "C:/github/steamtop10/Steam.txt"
#     df = pd.DataFrame(game_info, columns=['排行榜', '遊戲名稱', '當前遊戲價格', '遊戲評價', '遊戲頁面連接'])
#     df.to_csv(save_path, index=0)
#     print("文件保存成功！")

# if __name__ == "__main__":
#     Game_info = [] # 遊戲全部訊息
#     Turn_link = [] # 翻頁連結
#     Jump_link = [] # 遊戲詳情連結
#     Game_evaluation = [] # 遊戲好評率
#     for i in range(1):
#         Turn_link.append("https://store.steampowered.com/search/?filter=globaltopsellers&page=1&os=win")
#         run(Game_info, Jump_link, Game_evaluation, get_text(Turn_link[i-1]))
#         save_data(Game_info)


    # embedVar = discord.Embed(title="Steam",timestamp=datetime.datetime.utcnow(), url="https://steamcharts.com/top",description="玩家人數", color=0x808080)
    # # embedVar.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
    # with open('C:/github/steamtop10/Steamchart.txt',"r",encoding="utf-8") as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     # the specific rows we want
    #     interestingrows=[row for idx, row in enumerate(csv_reader) if idx in (1,2,3,4,5,6,7,8,9,10)]
    # for row in interestingrows:
    #     #row[0] game title, row[1] review, row[2] price, row[3] hyperlink
    #     embedVar.add_field(name=row[0], value=":thumbsup:當前人數"+row[1]+':moneybag:今日最高'+row[2], inline=False)

    # embedVar.set_footer(text="Real-time data from Steam charts")

    # await ctx.send(embed=embedVar)



#MARK: plot
# x = []
# y = []

# with open('C:/github/steamtop10/Steamchart.txt',"r",encoding="utf-8") as csvfile:
#     plots = csv.reader(csvfile, delimiter = ',')

#     for row in plots:
#         x.append(row[0])
#         y.append(row[1])

#     x.pop(0)
#     y.pop(0)



# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data

# y_pos = np.arange(len(x))
# currentplayer = y
# error = np.random.rand(len(x))

# ax.barh(y_pos, currentplayer, xerr=error, align='center')
# ax.set_yticks(y_pos)
# x.reverse()
# ax.set_yticklabels(x)
# currentplayer.reverse()
# ax.set_xticklabels(currentplayer)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Current player')
# ax.set_title('Steam chart')
# plt.gca().invert_yaxis()

# plt.show()






# # Steam今日玩家人數圖表 steam current player plot
# @bot.command()
# async def steamplayerImg(ctx):
#     fetchSteamchart # download player data from steamchart.com
#     steamChartPlot # create chart plot

#     with open('C:/github/steamtop10/steamchart.png', 'rb') as f:
#         picture = discord.File(f)
#         await ctx.send('Steam在線人數',file=picture)
