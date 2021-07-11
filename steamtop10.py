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

from typing import Any
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import functools
import operator
num = 1

def get_text(url):
    try:
         headers = {
     "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/85.0.4183.102 Safari/537.36', 'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4' }
    except: return "爬取網頁失敗！"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def listToString(list):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in list:
        str1 = ''.join(ele)

    # return string
    return str1

def save_data(game_info):
    save_path = "C:/github/steamtop10/Steam.txt"
    df = pd.DataFrame(game_info, columns=['Steam遊戲排行','遊戲評價','價格'])
    df.to_csv(save_path, index=0)
    print("文件保存成功！")

def run(game_info,review, price, text):

    soup = BeautifulSoup(text, "html.parser")

    # 遊戲評價
    w = soup.find_all(class_ = "col search_reviewscore responsive_secondrow")[:10]
    for u in w:
        if u.span is not None:
            substring = u.span["data-tooltip-html"]
            reviewInfo = " "+substring.replace('<br>', '  ')
            list = re.findall(r'(\d+(\.\d+)?%)',reviewInfo)
            reviewRate = listToString(list)
            review.append(":thumbsup:"+reviewRate+" ")

        else:
            review.append(" 暫無評價")



    global num
    # 遊戲名稱
    name_text = soup.find_all('div', class_="responsive_search_name_combined")[:10]
    for z in name_text:
        name = str(num) + ". " + z.find(class_="title").string.strip() + "  "
        # game.append([name,review[num-1]])
        if z.find(class_="col search_discount responsive_secondrow").string is None:
            price = z.find(class_="col search_price discounted responsive_secondrow").text.strip().split("NT$")

            game_info.append([ name, review[num-1], " :dollar:"+str(price[2].strip())])
        else:
            price = z.find(class_="col search_price responsive_secondrow").string.strip().split("NT$")

            game_info.append([ name, review[num-1], " :dollar:"+str(price[1])])
        num = num + 1


if __name__ == "__main__":
    game_info = [] # 遊戲全部訊息
    review = [] #遊戲評價
    price = []
    run(game_info,review, price, get_text("https://store.steampowered.com/search/?filter=globaltopsellers&page=1&os=win"))
    save_data(game_info)
