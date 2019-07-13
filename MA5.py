#!/user/bin/env python
#coding:utf-8

import pymysql
import sec
import numpy as np
import pandas as pd
import sys

connection = pymysql.connect(host = '47.75.10.105',
	user = 'xxx',
	password = '123456',
	db = 'ea-my',
	charset = 'utf8mb4')



def getshuju(table_name):
	try:
		with connection.cursor() as cursor:
			select_sql = "select * from "+ table_name +" limit 100"
			select_sql_c = "select count(*) from "+table_name+""
			#print(select_sql)
			result = cursor.execute(select_sql)
			#result2 = cursor.execute(select_sql_c)
			#print(cursor.fetchall())
			return cursor.fetchall()
			connection.commit()
	except Exception as e:
		raise
	else:
		pass
	finally:
		connection.close()

def MA(period):
	close = []
	index = [[]]
	try:
		shuju = getshuju('AUD_USD_dayline_details_M10')
		# print(shuju)
		shuju_list = list(shuju)
		df = pd.DataFrame(shuju_list)
		print(len(df))
		for i in range(len(shuju_list)):
			close.append(df[5][i])
		# return close
		# print(close)
		# print(len(close))
		arr = []
		for x in range(len(close)):
			# print("x=",x)
			arr2 = []
			if x >= period:
				all_point = 0
				for y in range(x-period,x):
					# print("y=",y)
					arr2.append(close[y])
					all_point += close[y]
					# all_point = all_point.__iadd__(y)
				# print(all_point)
				avg_point = all_point/period
				# print(avg_point)
				# print(arr2)
				arr.append(arr2)
				arrdf = pd.DataFrame(arr)
		# print(arrdf)
		# print(arrdf[:][:])
		# for x in range(len(arrdf)):
		# 	print(len(arrdf[0]))
			# for y in range(5):
			# 	print('x=',x,'y=',y)
			# 	print(arrdf[y][x])
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass

def KDJ(period):
	close = []
	high = []
	low = []

	try:
		shuju = getshuju("AUD_USD_dayline_details_M10")
		shuju_list = list(shuju)
		df = pd.DataFrame(shuju_list)
		for i in range(len(df)):
			close.append(df[5][i])
			high.append(df[4][i])
			low.append(df[3][i])
		arr_close = []
		arr_high = []
		arr_low = []
		arr = []
		for x in range(len(close)):
			close_period = []
			high_period = []
			low_period = []
			if x >= period:
				for y in range(x-period,x):
					close_period.append(close[y])
					high_period.append(high[y])
					low_period.append(low[y])
				arr_close.append(close_period)
				arr_high.append(high_period)
				arr_low.append(low_period)
				# print('c=',close_period)
				# print('h=',high_period)
				# print('l=',low_period)
				# arr.append(arr_high)
				# arr.append(arr_low)
				arrdf_close = pd.DataFrame(arr_close)
				arrdf_high = pd.DataFrame(arr_high)
				arrdf_low = pd.DataFrame(arr_low)
				arr.append(close_period)
				# print(arr_close)
		# print(arr)
		# print(arrdf_close[:])
		# print(arr_close[0])
		# print(len(arr_close),len(arr_high),len(arr_low))
		k_list = []
		d_list = []
		for x in range(len(arr_close)):
			'''
			RSV、K、D、J
			'''
			# print(arr_close[x][period-1],'min(arr_low)=',min(arr_low[x][:]),'max(arr_high)=',max(arr_high[x][:]))
			rsv = (arr_close[x][period-1]-min(arr_low[x][:]))/(max(arr_high[x][:])-min(arr_low[x][:]))*100
			if k_list:
				k = 2/3*k_list[-1] + 1/3*rsv
				d = 2/3*d_list[-1] + 1/3*rsv
				j = 3*k - 2*d
				k_list.append(k)
				d_list.append(d)
			else:
				k = (2/3*50) + (1/3*rsv)
				d = (2/3*50) + (1/3*rsv)
				j = 3*k - 2*d
				k_list.append(k)
				d_list.append(d)
				# print('11 rsv==',rsv,'k==',k,'d==',d,'j==',j)

			# print('x=',x,'rsv==',rsv,'k==',k,'d==',d,'j==',j)


	except Exception as e:
		raise e

def MACD(small,big):
	close = []

	try:
		shuju = getshuju("AUD_USD_dayline_details_M10")
		shuju_list = list(shuju)
		# print(shuju_list)
		# print('---------')
		# print(shuju_list[0][5])

		for i in range(len(shuju_list)):
			close.append(shuju_list[i][5])

		print(close)
	except Exception as e:
		raise e



if __name__ == '__main__':
	#shuju = getshuju('AUD_USD_dayline_details_M10')
	#print(shuju)
	# print(sys.argv)
	# MA(int(sys.argv[1]))
	# KDJ(9)
	MACD(12,26)

