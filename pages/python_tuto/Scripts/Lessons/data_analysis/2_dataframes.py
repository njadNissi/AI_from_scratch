import pandas as pd
import numpy as np


data = {
    'a':[2, 2, np.nan, 5, 6],
    'b':['kl', 'kl', 'kl', np.nan, 'kl'],
    'c':[4, 6, 5, np.nan, 6],
    'd':[7, 9, np.nan, 9, 8]
    }
df = pd.DataFrame(data=data)
cols = df.columns
ind = df.index
vals = df.values

df1 = df.dropna(0) # fill nulls with zeros
df2 = df.fillna({'a':0, 'b':'kl', 'c':0, 'd':0}) # fill whole series
df2 = df.fillna({'a':0, 'b':'kl'}) # fill part of series
