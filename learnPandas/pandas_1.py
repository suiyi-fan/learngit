#user/bin/env python
#coding:utf-8

import numpy as np
import pandas as pd


arr = {'a':[[1,2,3]],'b':[[4,5,6]],'c':[[3]]}

df = pd.DataFrame(arr)
df.index = ['A']
print(df['a']['A'][-1])
# print('---------')
# print(df.values)	
# print('---------')
# print(df.ix[0:,0:1])
# print('---------')
# print(df.iloc[0,1])
print('---------')
print(df)
print('=========')

arr1 = {'a':[[1],['x']],'b':[[4],['y']],'c':[[3],['z']]}

df1 = pd.DataFrame(arr1)
df1.index = ['A','B']
print(df1['a'][1][0])
# print('---------')
# print(df1.values)	
# print('---------')
# print(df1.ix[0:,0:1])
# print('---------')
# print(df1.iloc[0,1])
print('---------')
print(df1)

# dict0 = { 'android': [90, 80, 60], 'java': [99, 78, 89], 'python': [98, 82, 85], 'c': 80 } 
# df0 = pd.DataFrame(dict0) 
# print("df0===========================") 
# print(df0)
