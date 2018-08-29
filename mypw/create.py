#!/user/bin/env python
#coding:utf-8

import mysql.connector


# 定义建表方法
def createTable(cursor):
	sql_create_table = "create table if not exists mypw (id int(4) not null primary key auto_increment,\
	client varchar(20) default null,\
	acc varchar(20) default null,\
	pw varchar(20) default null )"
	try:
		cursor.execute(sql_create_table)
	except mysql.connector.error as e:
		print('create table error')


# 连接
con = mysql.connector.connect(host='66.98.113.68',user='root',password='suiyi',database='database_test')

# 创建游标
cursor = con.cursor()

# 建表
createTable(cursor)

# 关闭连接 关闭游标
con.close()
cursor.close()












	