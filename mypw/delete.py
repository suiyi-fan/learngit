#!/user/bin/env python
#coding:utf-8


import mysql.connector as mc
import sys




def delete_Data(cursor):
	sql_delete_data = "delete from mypw where client = '"+str(sys.argv[1])+"'"
	# sql_delete_data = "delete from mypw where id = 3"
	try:
		# print(sql_delete_data)
		cursor.execute(sql_delete_data)
		# print(type(sys.argv[1]),type(sys.argv[2]))
		#print(cursor)
	except mc.Errno as e:
		Print('Delete Data Error:{}'.format())



con = mc.connect(host='66.98.113.68',user='root',password='suiyi',database='database_test')
#print(con)


# 游标
cursor = con.cursor()
#print(cursor)

# 执行方法
delete_Data(cursor)

# commit 提交
con.commit()

# 释放游标、连接
con.close()
cursor.close()
