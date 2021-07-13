from typing import Any
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import functools
import operator


def get_text(url):
    try:
         headers = {
     "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/85.0.4183.102 Safari/537.36', 'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4' }
    except: return "爬取網頁失敗！"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def run(Search_info, Price, Discount, Image, text):
    soup = BeautifulSoup(text, "html.parser")

    # 遊戲圖片
    image_text = soup.find('div', class_="col search_capsule")
    if image_text == None:
        print("no result")
        return False
    image = image_text.find("img")["src"]

    Image.append(image)
    # 遊戲價格
    price_text = soup.find('div',class_="col search_discount responsive_secondrow")

    #有打折
    if price_text.string is None:

        discountPercentage = price_text.find('span').string.strip()
        Discount.append(''.join(discountPercentage))
        discountPrice_text = soup.find(class_="col search_price discounted responsive_secondrow").text.strip().split("NT$")

        Price.append('原價: '+discountPrice_text[1]+' 特價:'+(discountPrice_text[2]))
    else:
    #沒打折
        price_text = soup.find('div',class_="col search_price responsive_secondrow").text.strip().split("NT$")

        try:
            if price_text[0] != "免費遊玩":
                Discount.append("無")
                Price.append(price_text[1])

            else:
                Discount.append("免費遊玩")
                Price.append(price_text[0])
        except:
            Discount.append("無")
            Price.append("沒有標示價錢")


    # 遊戲名稱
    search_name_ellipsis_text = soup.find('div', class_="col search_name ellipsis")
    gameTitle = search_name_ellipsis_text.find('span', class_="title").string.strip()

    Search_info.append([gameTitle, Price[-1], Discount[-1], Image[-1]])
    return True

def save_data(search_info):
    save_path = "C:/github/steamtop10/steamSearch.txt"
    df = pd.DataFrame(search_info, columns=['遊戲名稱','特價','價錢','圖片'])
    df.to_csv(save_path, index=0)
    print("文件保存成功！")




