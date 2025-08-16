import pandas as pd
import numpy as np

# declarations

s1 = pd.Series([1, -2, 2.3, 'hq']) # build a series with default indices
s2 = pd.Series([1, -2, 2.3, 'hq'], index=['a', 'b', 'c', 'd']) # build series with custom indices
s3 = pd.Series((1, 2, 3, 4, 2, 0, 3, 0,'hq')) # build series with a tuple
s4 = pd.Series(np.array([1, 2, 4, 7.1])) # build series with array
s5 = pd.Series([1, -2, 2.3, 'hq', 'hq', 'he'])
s6 = pd.Series((1, 2, 3, 4, 2, 0, 3, 0))
s8 = pd.Series({'red':2000, 'bule':1000, 'yellow':500}) # build series with a dictionary
# 空值处理 
s7 = pd.Series([10, 'hq', 60, np.nan, 20])
# get non-null values
sn1 = s7[~s7.isnull()]
sn2 = s7[~s7.notnull()]
sn3 = s7.dropna()


sum = s6.sum()
mean = s6.mean()
std = s6.std()
max = s6.max()
min = s6.min()
SV = s6.var
# test

print('s1[3]=', s1[3], "s2['c']=", s2['c'])
print('s1 values=', s1.values, 's2 indices=', s2.index)
print('s5 values=', s5.values, 's5 unique=', s5.unique())
print('[0, he] exist in s5?=', s5.isin([0, 'he']))
print('value counts:\n', s3.value_counts())