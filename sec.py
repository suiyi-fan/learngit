#!/user/bin/env python
#coding:utf-8

import mysql.connector


def select():
	data = []
	con = mysql.connector.connect(host='47.75.10.105',user='sel_er',password='1234',database='forex')
	#cursor = con.cursor()
	selectString = "select open,high,close,low from EUR_USD limit 10"
	cursor=con.cursor(buffered=True)

	cursor.execute(selectString)
	for (open,high,close,low) in cursor:
		data.append([open,high,close,low])
		#print("open=",open,"\thigh=",high,"\tclose=",close," \tlow=",low)

	for i in range(0,len(data)):
		print("data[",i,"]=",data[i])
	cursor.close()
	con.close()




if __name__ == '__main__':
	main()
	select()
# class A():
# 	'Common'
# 	def __init__(self,a,b):
# 		self.__a = a
# 		self.__b = b 

# 	def getA(self):
# 		#return self.__a
# 		print('a='+(str)(self.__a)+'  b='+(str)(self.__b))

# 	def setA(self,a1):
# 		self.__a = a1
# 		print('a after modify:'+(str)(self.__a))
# 	def __str__(self):
# 		return 'ver (%d,%d)' % (self.__a,self.__b)
# 	def __add__(self,other):
# 		return A(self.__a+other.__a , self.__b+other.__b)
# 	def __sub__(self,other):
# 		return A(self.__a-other.__a , self.__b-other.__b)

# def main():
# 	a1 = A(10,20)
# 	a2 = A(5,8)
# 	print(a1-a2)

# if __name__ == '__main__':
# 	main()


# aa = A(10,20)
# aa.c = 30
# if hasattr(aa,'c'):
# 	print(aa.c)
# print(hasattr(aa,'c'))
# print ("A.__doc__:", A.__doc__)
# 
# 
# aa.getA()
# aa.setA(15)

# if __name__ == '__main__':
# 	main()
# 	

# aaa['first'] = 1;

# print(aaa['first'])