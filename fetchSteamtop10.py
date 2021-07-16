from typing import Any
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup



def get_text(url):
    try:
         headers = {
     "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/85.0.4183.102 Safari/537.36', 'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4' }
    except: return "爬取網頁失敗！"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
# re.findall return a list of tuples
def listToString(list):
    str1 = ""

    # tuple in the list
    for ele in list:
        # tuple convert to string
        str1 = ''.join(ele)
    return str1

# save data to local
def save_data(game_info):
    save_path = "steamtop10.txt"
    df = pd.DataFrame(game_info, columns=['Steam遊戲排行','遊戲評價','價格','鏈接'])
    df.to_csv(save_path, index=0)
    print("文件保存成功！")

def run():
    game_info = [] # 遊戲全部訊息
    review = [] #遊戲評價
    price = [] #遊戲價格
    hyperlink = [] #遊戲鏈接
    text = get_text("https://store.steampowered.com/search/?filter=globaltopsellers&page=1&os=win")
    soup = BeautifulSoup(text, "html.parser")
    # 遊戲評價
    w = soup.find_all(class_ = "col search_reviewscore responsive_secondrow")
    for u in w:
        if u.span is not None:
            substring = u.span["data-tooltip-html"]
            reviewInfo = " "+substring.replace('<br>', '  ')
            list = re.findall(r'(\d+(\.\d+)?%)',reviewInfo)
            reviewRate = listToString(list)
            review.append(reviewRate)

        else:
            review.append(" 暫無評價")

    # 遊戲頁面連接
    link_text = soup.find_all("div", id="search_resultsRows")
    for k in link_text:
        b = k.find_all('a')
    for j in b:
        hyperlink.append(j['href'])

    num = 1
    # 遊戲名稱
    name_text = soup.find_all('div', class_="responsive_search_name_combined")
    for z in name_text:
        name = str(num) + ". " + z.find(class_="title").string.strip() + "  "

        # 判斷是否特價
        if z.find(class_="col search_discount responsive_secondrow").string is None:
            price = z.find(class_="col search_price discounted responsive_secondrow").text.strip().split("NT$")

            game_info.append([ name, review[num-1], str(price[2].strip()), str(hyperlink[num-1])])
        else:
            price = z.find(class_="col search_price responsive_secondrow").string.strip().split("NT$")

            game_info.append([ name, review[num-1], str(price[1]), str(hyperlink[num-1])])
        num = num + 1
    num = 1
    save_data(game_info)

