# Copyright (c) 2019 by 张良栋
import random as r
import pymysql
import datetime
from faker import Faker

f=Faker(locale="zh_CN")

id = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
name = []
passwdNumber = "0123456789"
for i in range(100000):
    ID1=r.choice(id)+r.choice(id)+r.choice(id)+r.choice(id)
    ID2=ID1.rstrip()
    if ID2 not in name:
        name.append(ID2)
conn = pymysql.connect(host = "localhost", port=3306, user='root', passwd='Zhang99215',db='test1')
cur = conn.cursor()
for i in range(len(name)):
    passwd = ''
    ticket_number=''
    ticket_count=r.randint(1,10)
    a = 0
    n = []
    User_name=f.name()
    Mobile_phone_number=f.phone_number()
    while( a <= 7):
        ticket_num = r.randint(1,36)
        if ticket_num not in n:
            n.append(ticket_num)
            a = a+1
        else:
            continue
        if ticket_num <= 9:
            ticket_num = '0' + str(ticket_num)
        ticket_number += str(ticket_num) + ' '
    for j in range(8):
        passwd += r.choice(id)
    ticket_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute("insert into lottey(User_id,Password,Buy_number,ticket_count,ticket_time,User_name,Mobile_phone_number) values(%s,%s,%s,%s,%s,%s,%s)",(name[i],passwd, ticket_number,ticket_count,ticket_time,User_name,Mobile_phone_number))
cur.execute('select * from lottey')
for s in cur.fetchall():
    print(s)
conn.commit()
cur.close()
conn.close()