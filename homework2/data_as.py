import requests
from bs4 import BeautifulSoup
import json
import time
import requests
import time
import numpy as np
import matplotlib.pyplot as plt
import sql

list1=['A030101','A030102','A030103','A030302','A030303','A030304']
list2=['total','male','female','young','worker','old']

# 用来获取 时间戳
def gettime():
    return int(round(time.time() * 1000))
class data():

    def __init__(self,seq):
        self.seq=seq
        self.title=''
        self.dic={}
        self.year=[]
        self.num=[]
    def getinform (self):
        title = list1[self.seq]
        title='"'+str(title)+'"'

        # 用来自定义头部的
        headers = {}
        # 用来传递参数的
        keyvalue = {}
        # 目标网址(问号前面的东西)
        url = 'http://data.stats.gov.cn/easyquery.htm'

        # 头部的填充
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) ' \
                                'AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                                'Version/12.0 Safari/605.1.15'

        # 下面是参数的填充，参考图10
        keyvalue['m'] = 'QueryData'
        keyvalue['dbcode'] = 'hgnd'
        keyvalue['rowcode'] = 'zb'
        keyvalue['colcode'] = 'sj'
        keyvalue['wds'] = '[]'
        keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":'+'{}'.format(title)+'}]'
        keyvalue['k1'] = str(gettime())

        # 发出请求，使用get方法，这里使用我们自定义的头部和参数
        # r = requests.get(url, headers=headers, params=keyvalue)
        # 建立一个Session
        s = requests.session()
        # 在Session基础上进行一次请求
        r = s.get(url, params=keyvalue, headers=headers)
        # 打印返回过来的状态码
        print
        r.status_code
        # 修改dfwds字段内容
        keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
        # 再次进行请求
        r = s.get(url, params=keyvalue, headers=headers)
        # 此时我们就能获取到我们搜索到的数据了
        text = json.loads(r.text)
        self.dic=text['returndata']['datanodes']

    def read(self):
        for i in self.dic:
            self.year.append(i['code'][-4:])
            self.num.append(i['data']['data'])

        #年份i['code'][-4:-1]  数据 i['data']['data']
    def p_bar(self):
        plt.bar(self.year , self.num, 0.5, 0, color='IndianRed')
        plt.show()
    def put(self):
        ms=sql.MSSQL()
        print(self.num)
        ms.put(list2[self.seq],self.num)

    def clear(self):
        ms = sql.MSSQL()
        ms.clear()
# 数据存入数据库
# for i in range(6):
#
#     a = data(i)
#     a.getinform()
#     a.read()
#     a.put()
#

