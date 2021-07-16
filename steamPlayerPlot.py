import matplotlib.pyplot as plt
import csv
import pandas as pd
from textwrap import wrap
from pylab import mpl
x = [] # game title
y1 = [] # current player
y2= [] # peak player


with open('C:/github/steamtop10/steamPlayer.txt',"r",encoding="utf-8") as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
    for row in plots:
        x.append(row[0])
        y1.append(row[1])
        y2.append(row[2])
x.pop(0)
y1.pop(0)
y2.pop(0)
current = [int(c) for c in y1]
peak = [int(p) for p in y2]

df = pd.DataFrame({'今天遊戲在線人數': current,
                   '今天最高在線人數': peak}, index=x)
plt.rcParams.update({'font.size': 10, 'font.family': 'sans-serif'}) # 字體大小
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 解決中文亂碼
df.plot(kind='barh', figsize=(12,5))



plt.gca().invert_yaxis()
plt.tight_layout() # fit the x label in plot
plt.savefig('steamPlayer.png')


