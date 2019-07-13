#!/usr/bin/python
# -*- coding: utf-8 -*-


from framework.mysql import mysql
from strategy.ma import ma
from strategy.singlek import singlek as singleK
import pandas as pd
from full_line_class.common import insert_fx

import os
class LineModel():
    """docstring for LineModel"""

    def __init__(self, code, table):

        self.code = code
        self.table = table
        self.get_TD()

    def get_TD(self):
        self.df = mysql.select_with_index(self.table, self.code)

class LineModel2():
    """docstring for LineModel"""

    def __init__(self, code, table):

        self.code = code
        self.table = table
        self.get_TD()

    def get_TD(self):
        self.df = mysql.select_with_index(self.table, self.code)

def run(code,times,gap=0):
	table = code+"_f365_"+times
    macd = LineModel(code, table).df[0:]

    table = code+"_all_stock_dayline_details_"+times
    k_data = LineModel(code, table).df[0:]

    df = []
    point = 0
    for i in range(1,len(macd)):
    	if macd.ix[i-1]['bar']:
    		# 红柱小于绿柱
    		if float(macd.ix[i-2]['bar']) < float(macd.ix[i-1]['bar']) and float(macd.ix[i-1]['bar']) > float(macd.ix[i]['bar']):
    			if point > 0 and float(macd.ix[i-1]['bar']) < 0 and (abs(float(macd.ix[i-1]['bar'])) - abs(point) > gap):
    				# 平仓
                	df.append([macd.ix[i].data, k_data.ix[i].bar, 'duo', code])
    			point = float(macd.ix[i-1]['bar'])
    		# 绿柱小于红柱
    		if float(macd.ix[i-2]['bar']) > float(macd.ix[i-1]['bar']) and float(macd.ix[i-1]['bar']) < float(macd.ix[i]['bar']):
    			if point < 0 and float(macd.ix[i-1]['bar']) > 0 and (abs(float(macd.ix[i-1]['bar'])) - abs(point) > gap):
    				# 平仓
                	df.append([macd.ix[i].data, k_data.ix[i].bar, 'kong', code])
    			point = float(macd.ix[i-1]['bar'])

    line_df = pd.DataFrame(df, columns=["date","bar", "type", "code"])

    line_df = line_df.set_index(line_df.date)
    line_df = line_df.drop(['date'], axis=1)

    insert_table=code+"_f365_close_"+times
    insert_fx(line_df,insert_table,code)


code_list = ['RB0']

times = 'm15'

for code in code_list:
	run(code,times)
