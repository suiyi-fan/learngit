#!/user/bin/env python
#coding:utf-8

import requests
import json
import time


# s = requests.Session()

# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get("http://httpbin.org/cookies")

# print(r.text)

def getData(sym,per,count):
	closeMid = []
	r = requests.get("https://api-fxtrade.oanda.com/v1/candles?instrument="+sym+"&count="+count+"&candleFormat=midpoint&granularity="+per+"&dailyAlignment=0&alignmentTimezone=America%2FNew_York")
	# print(r.text)

	shuju_p = json.loads(r.text)
	# print(shuju_p)

	# print('----------')

	# print(shuju_p['candles'][:])
	for i in shuju_p['candles'][:]:
		# print(i['time'],i['highMid'],i['lowMid'])
		closeMid.append(i['closeMid'])
	return closeMid




# print(shuju_p['candles'][:][2])

def MA(period):
	data = getData('EUR_USD','H1','100')
	# print(data)
	# print(type(data))
	print('-'*100)
	MA = []
	# print(data[0:5])
	for x in range(0,len(data)):
		if x >= period:
			MA.append(round(sum(data[x-period:x]),6))
		else:
			MA.append(0)
	print(MA)
	print(len(MA))

'''
@type:无限循环定时任务
'''
# a = 0
# while True:
# 	a += 1
# 	print(a)
# 	getData()
# 	time.sleep(60)
# 	

# getData('EUR_USD','H1','10')
# MA(5)
# print(round(sum([1.13695,1.136885,1.136525,1.13666,1.13646]),6))
# getData('EUR_USD','H1','5001')
# 


if __name__ == '__main__':
	getData('EUR_USD','H1','50')