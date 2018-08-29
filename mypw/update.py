#!/user/bin/env python
#coding:utf-8

import mysql.connector as mc
import sys


# update
def updateData(cursor):
	sql_update_data = "update mypw set acc = '"+sys.argv[1]+"',pw = '"+sys.argv[2]+"' where client = '"+sys.argv[3]+"'"
	try:
		cursor.execute(sql_update_data)
		print('Update OK!')
	except mc.Error as e:
		print('Update Data Error.{}'.format(e))




# 连接
con = mc.connect(host='66.98.113.68',user='root',password='suiyi',database='database_test')

# 创建游标
cursor = con.cursor()

# 调用查询方法
updateData(cursor)

# commit
con.commit()
# 释放游标
cursor.close()
# 释放连接
con.close()
