# -*- coding: gbk -*-
import pymssql


class MSSQL:
    def __init__(self):  # ��Ĺ��캯������ʼ�����ݿ�����ip�����������Լ��û��������룬Ҫ���ӵ����ݿ�����
        self.host ='DESKTOP-T4BRN52'
        self.user = 'sa'
        self.pwd = '8a7a2a'
        self.db = 'homework2'

    def __GetConnect(self):  # �õ����ݿ�������Ϣ������ ����: conn.cursor()
        if not self.db:
            print(NameError, "û���������ݿ���Ϣ")
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset='utf8')
        cur = self.conn.cursor()  # �����ݿ�������Ϣ����ֵ��cur��
        if not cur:
            raise (NameError, "�������ݿ�ʧ��")
        else:
            return cur

    def ExecQuery(self,sql):
        '''
       ִ�в�ѯ���
         ����һ������tuple��list��list��Ԫ�صļ�¼�У�tuple��¼ÿ�е��ֶ���ֵ
        '''
        cur = self.__GetConnect()
        cur.execute(sql) # ִ�в�ѯ���
        result = cur.fetchall() # fetchall()��ȡ��ѯ���
        # ��ѯ��Ϲر����ݿ�����
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
        cur.execute(sql)  # ִ�в�ѯ���
        result = cur.fetchone()  # fetchall()��ȡ��ѯ���
        # ��ѯ��Ϲر����ݿ�����
        self.conn.close()
        return result

if __name__ == '__main__':
    ms=MSSQL
    ms.print_s
    ms.clear
    ms.print_s



