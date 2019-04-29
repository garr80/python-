#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json
import time
import requests
import time
import numpy as np
import matplotlib.pyplot as plt
import sql
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

list1=['A030101','A030102','A030103','A030302','A030303','A030304']
list2=['total','male','female','young','worker','old']
class data_read():

    def __init__(self,seq):
        self.seq=seq
        self.title=''
        self.dic={}
        self.year=['1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
        self.num=[]
    def read(self):
        for i in self.dic:
            self.year.append(i['code'][-4:])
            self.num.append(i['data']['data'])

        #年份i['code'][-4:-1]  数据 i['data']['data']
    def p_bar(self):
        plt.bar(self.year , self.num, 0.5, 0, color='IndianRed')
        plt.title("年末总数条形图")
        plt.xlabel("年份")
        plt.ylabel("万人")
        plt.show()
    def get(self):
        ms=sql.MSSQL()

        self.num=ms.pull(list2[self.seq])
        return  self.num

def homework1():
    #条形绘制
    a=data_read(0)
    a.get()
    a.p_bar()

    #折线绘制
    male=data_read(1)
    male.get()
    x1=[ male.num[i]/a.num[i] for i in range(20)]
    female = data_read(2)
    female.get()
    x2= [female.num[i] / a.num[i] for i in range(20)]

    plt.plot(a.year,x1,c='red',label='male')
    plt.plot(a.year,x2,c='blue',label='female')
    plt.legend()
    plt.title("性别比例变化")
    plt.xlabel("年份")
    plt.ylabel("性别比例")
    plt.show()

def homework2():

    a=data_read(3)
    a.get()
    b=data_read(4)
    b.get()
    c = data_read(5)
    c.get()
    data_2016=[a.num[-2],b.num[-2],c.num[-2]]
    colors = ['#4499ff', '#ff7799', '#7777aa']
    # 2016扇形图
    plt.pie(x=data_2016,  # 绘图数据
            labels=['0-14岁','15-64岁','65岁及以上'],
            colors=colors
            )

    plt.title("2016 年龄结构")
    plt.show()
    #折线图
    d=data_read(0)
    d.get()
    x1 = [a.num[i] / d.num[i] for i in range(19)]
    x2 = [b.num[i] / d.num[i] for i in range(19)]
    x3 = [c.num[i] / d.num[i] for i in range(19)]
    plt.plot(a.year[:-1], x1, c='red', label='0-14岁')
    plt.plot(a.year[:-1], x2, c='blue', label='15-64岁')
    plt.plot(a.year[:-1], x3, c='green', label='65岁及以上')
    plt.title("年龄结构变化")
    plt.xlabel("年份")
    plt.ylabel("比例")
    plt.legend()
    plt.show()



homework1()
homework2()

