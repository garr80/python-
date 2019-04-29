# -*- coding: gbk -*-
import pymssql


class MSSQL:
    def __init__(self):  # 类的构造函数，初始化数据库连接ip或者域名，以及用户名，密码，要连接的数据库名称
        self.host ='DESKTOP-T4BRN52'
        self.user = 'sa'
        self.pwd = '8a7a2a'
        self.db = 'homework2'

    def __GetConnect(self):  # 得到数据库连接信息函数， 返回: conn.cursor()
        if not self.db:
            print(NameError, "没有设置数据库信息")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset='utf8')
        cur = self.conn.cursor()  # 将数据库连接信息，赋值给cur。
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            return cur

    def ExecQuery(self,sql):
        '''
       执行查询语句
         返回一个包含tuple的list，list是元素的记录行，tuple记录每行的字段数值
        '''
        cur = self.__GetConnect()
        cur.execute(sql) # 执行查询语句
        result = cur.fetchall() # fetchall()获取查询结果
        # 查询完毕关闭数据库连接
        self.conn.close()
        return result

    def ExecNonQuery(self, sql):
        cur2 = self.__GetConnect()
        cur2.execute(sql)
        self.conn.commit()
        self.conn.close()

    def print_s(self):

        reslist = self.ExecQuery( "select * from total")

        return reslist


    def clear(self):
        reslist = self.ExecNonQuery(
        "truncate table  total;")

    def test(self):
        temp = [str(i) for i in range(20)]
        a = ','.join(temp)
        reslist = self.ExecNonQuery("INSERT into young    VALUES  ( " + '{}'.format(a) + ")")
    def put(self,table,x):
        x= [str(i) for i in x]
        a = ','.join((x[::-1]))
        reslist = self.ExecNonQuery("INSERT into "+'{}'.format(table)+"    VALUES  ( " + '{}'.format(a) + ")")
    def pull(self,table):
        l=[]
        sql='select * from '+table+';'
        cur = self.__GetConnect()
        cur.execute(sql)  # 执行查询语句
        result = cur.fetchone()  # fetchall()获取查询结果
        # 查询完毕关闭数据库连接
        self.conn.close()
        return result

if __name__ == '__main__':
    ms=MSSQL
    ms.print_s
    ms.clear
    ms.print_s



