
from asyncio.tasks import sleep
from os import name
from typing import Any
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import functools
import operator,time

def get_text():
    try:
         headers = {
     "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/85.0.4183.102 Safari/537.36', 'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4' }
    except: return "爬取網頁失敗！"
    r = requests.get("https://fast.com/zh/tw/", headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def run():
    sleep(6)
    text = get_text()
    soup = BeautifulSoup(text, "html.parser")

    result = soup.find('div',class_="speed-results-container succeeded").text
    return result
