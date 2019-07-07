# @Time    : 2019-07-07 14:21
# @Author  : zhangliangdong
# @File    : AutoTest.py
# @Software: PyCharm

from faker import Faker
import random as r
import pymysql
import datetime


class Test:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost", port=3306, user='root', passwd='Zhang99215', db='test1')
        self.cur = self.conn.cursor()
        self.f = Faker(locale="zh_CN")
        self.passwdNumber = "0123456789"

    def fake_id(self):
        id = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ID1 = ""
        name = []
        for i in range(4):
            ID1 = r.choice(id)+ID1
        ID2 = ID1.rstrip()
        if ID2 not in name:
            name.append(ID2)
        return name

    def fake_name(self):
        User_name  = self.f.name()
        return User_name

    def fake_phone(self):

        Mobile_phone_number = self.f.phone_number()
        return Mobile_phone_number

    def fake_number(self):
        a=0
        ticket_number = ''
        n = []
        while (a <= 7):
            ticket_num = r.randint(1, 36)
            if ticket_num not in n:
                n.append(ticket_num)
                a = a + 1
            else:
                continue
            if ticket_num <= 9:
                ticket_num = '0' + str(ticket_num)
            ticket_number += str(ticket_num) + ' '
        return ticket_number

    def fake_amount(self):
        ticket_count = r.randint(1, 10)
        return ticket_count

    def fake_passwd(self):
        id = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        passwd = ''
        for j in range(8):
            passwd += r.choice(id)
        return passwd

    def fake_time(self):
        ticket_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return ticket_time

#主函数
autotest = Test()
for i in range(10):
    autotest.cur.execute(
        "insert into lottey(User_id,Password,Buy_number,ticket_count,ticket_time,User_name,Mobile_phone_number) values(%s,%s,%s,%s,%s,%s,%s)",
        (autotest.fake_name(), autotest.fake_passwd(), autotest.fake_number(), autotest.fake_amount(), autotest.fake_time(), autotest.fake_name(), autotest.fake_phone()))
    autotest.cur.execute('select * from lottey')
for s in autotest.cur.fetchall():
    print(s)
autotest.conn.commit()
autotest.cur.close()
autotest.conn.close()