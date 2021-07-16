
import requests
import pandas as pd
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

#done
def save_data(chart_info):
    save_path = "steamPlayer.txt"
    df = pd.DataFrame(chart_info, columns=['遊戲名稱','當前人數','高峰人數'])
    df.to_csv(save_path, index=0)
    print("文件保存成功！")


def run():
    chart_info = [] # top game by current players全部訊息
    currentPlayers = [] #當前玩家
    peakPlayers = [] #人數最高峰
    text = get_text("https://steamcharts.com/top")
    soup = BeautifulSoup(text, "html.parser")

    # 當前人數
    # 獲取完全一樣的tag名稱
    current_players_text = soup.find_all(lambda tag: tag.name == 'td' and tag.get('class') == ['num'])[:10]
    for cp in current_players_text:
        currentPlayers.append(cp.string.strip())


    # 高峰人數
    peak_players_text = soup.find_all('td', class_="num period-col peak-concurrent")[:10]
    for p in peak_players_text:
        peakPlayers.append(p.string.strip())

    num = 0
    # 遊戲名稱
    game_title = soup.find_all('td', class_="game-name left")[:10]
    for t in game_title:
        name = str(num+1)+". "+t.find('a').string.strip()
        chart_info.append([name, currentPlayers[num], peakPlayers[num]])
        # game_info.append([ name, review[num-1], str(price[1]), str(hyperlink[num-1])])
        num = num + 1
    num = 0
    save_data(chart_info)



# def save_data(chart_info):


