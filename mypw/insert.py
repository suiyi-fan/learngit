#!/user/bin/env python
#coding:utf-8

import mysql.connector
import sys

# 接收终端传入的参数
mid = sys.argv[1]
client = sys.argv[2]
acc = sys.argv[3]
pw = sys.argv[4]


def insertData(cursor,mid,client,acc,pw):
	sql_insert_data = "insert into mypw (id,client,acc,pw) values (%s,%s,%s,%s)"
	try:
		cursor.execute(sql_insert_data,(mid,client,acc,pw))
	except mysql.connector.Error as e:
		print('Insert Data error:{}'.format(e))
	


# 连接
con = mysql.connector.connect(host='66.98.113.68',user='root',password='suiyi',database='database_test')

# 创建游标
cursor = con.cursor()

# 插入终端传入数据
insertData(cursor,mid,client,acc,pw)

# commit提交
con.commit()

# 关闭连接 关闭游标
con.close()
cursor.close()
