import requests
from  bs4 import BeautifulSoup
import lxml
import json
import execjs
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import sys



class report:
    def __init__(self, hot,againest,table1,table2):
        self.hot = hot
        self.againest = againest
        self.table1 = table1
        self.table2 = table2
    def show(self):
        print(self.hot)
        print(self.againest)
    def put(self):
        for i in range(9):

            self.table1.setItem(i,0, QTableWidgetItem('{:.2%}'.format(self.hot[str(i+1)]["used_rate"])))
            self.table1.setItem(i, 1, QTableWidgetItem('{:.2%}'.format(self.hot[str(i + 1)]["win_rate"])))
        for i in range(9):
             for j in range(9):
                self.table2.setItem(i, j, QTableWidgetItem('{:.2%}'.format(self.againest[str(i+1)][str(j+1)])))

#读取需要
ladder_hot_wild='data1'
ladder_againest_wild='data2'
ladder_hot_standard='data3'
ladder_againest_standard ='data4'

# 主体部分 数据获取
html = requests.get("http://lushi.163.com/bigdata/")
soup=BeautifulSoup(html.text)

a=soup.find_all('script', {'type': 'text/javascript'})

for i in a:
    try:
        if 'tianti' in i['src']:
            data=i['src']
            break
    except:
        pass

# 字符串处理
a=requests.get(data).text
b=a.split('\n')
b=b[0:-1]
b=','.join(b)
b=b.replace('=',':')
b='{'+b+'}'
b=b.replace('var','')
b=eval(b)
list1=[i for i in b]

