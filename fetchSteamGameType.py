from os import name
from typing import Any
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import functools
import operator,time
def get_text(url):
    try:
         headers = {
     "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/85.0.4183.102 Safari/537.36', 'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4' }
    except: return "爬取網頁失敗！"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
# save data to local
def save_data(game_info):
    save_path = "steamtype.txt"
    df = pd.DataFrame(game_info, columns=['Steam遊戲類別','圖片','價格','鏈接'])
    df.to_csv(save_path, index=0)
    print("文件保存成功！")

def run(url):
    # game type
    game_info = []
    game = [] #遊戲
    img = [] #圖片
    price = [] #價格
    hyperlink = [] #鏈接

    text = get_text(url)
    soup = BeautifulSoup(text, "html.parser")


    top_seller = soup.find('div', id="TopSellersRows")
    #圖片
    if top_seller is None:
        return False
    for pic in top_seller.findAll("img"):
        img.append(pic["src"])
    #遊戲鏈接
    for link in top_seller.findAll('a')[0:]:
        hyperlink.append(link['href'])

    #遊戲價格
    for a in top_seller.findAll('a'):
        no_price = a.find('div', class_="discount_block empty tab_item_discount")

        if no_price is not None: #空標籤
            price.append("無")
        else:
            hasPrice = a.find('div',class_="discount_final_price")
            price.append(hasPrice.text)

    #遊戲名稱
    num = 1
    for g in top_seller.findAll('div', class_="tab_item_name"):
        name = str(num)+". "+g.text
        game.append(name)
        game_info.append([game[num-1], img[num-1], price[num-1], hyperlink[num-1]])
        num = num + 1
    num = 1
    save_data(game_info)
    return True

