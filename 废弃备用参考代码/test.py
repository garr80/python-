import requests
from  bs4 import BeautifulSoup
import lxml
import json
import execjs
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import sys

# 初始化变量


class report:
    def __init__(self, hot,againest):
        self.hot = hot
        self.againest = againest
    def show(self):
        print(self.hot)
        print(self.againest)
    def put(self):

        for i in range(9):
            print( self.hot[str(i+1)]["used_rate"])


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

report1 = report(b[list1[0]], b[list1[1]])
report1.put()