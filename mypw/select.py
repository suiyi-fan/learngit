#!/user/bin/env python
#coding:utf-8

import mysql.connector
import sys


# 接收终端参数
cli = sys.argv[1]
print('cli=='+cli)
# 查询方法
def selectData(cursor):
	sql_select_data = " select acc,pw from mypw where client = '"+str(sys.argv[1])+"'"
	try:
		cursor.execute(sql_select_data)
		print('sql_select_data=='+sql_select_data)
		for (acc,pw) in cursor:
			print('acc=',acc,'pw=',pw)
	except mysql.connector.Error as e:
		print("select data error:{}".format(e))


# 连接
con = mysql.connector.connect(host='66.98.113.68',user='root',password='suiyi',database='database_test')

# 创建游标
cursor = con.cursor()

# sql_select_data = "select acc,pw from mypw where client = tx"#+cli #+ sys.argv[1]
# cursor.execute(sql_select_data)
# 执行查询
selectData(cursor)

# commit
#con.commit()

# 关闭游标
cursor.close()
# 关闭连接
con.close()
