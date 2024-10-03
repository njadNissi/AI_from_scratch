import pandas as pd
import numpy as np
import random as rd
import pandas as pd


lb = -100
rb = 100
SAMPLES_NO = 50000

x1 = [rd.randint(lb, rb) for _ in range(SAMPLES_NO)]
x2 = [rd.randint(lb, rb) for _ in range(SAMPLES_NO)]
x3 = [rd.randint(lb, rb) for _ in range(SAMPLES_NO)]

# Coefficients (weights) for linear combination
coefs = np.array([1, -2, 3])

X = pd.DataFrame({'x1':x1, 'x2':x2, 'x3':x3})
# X.head()

Y = (X[['x1', 'x2', 'x3']] * coefs).sum(axis=1)
# Y.head()
Y = Y.rename('Y')

dataset = pd.concat([X, Y], axis=1)
print(dataset.head())

dataset.to_csv('3fFormulaRegressor.csv', index=False)

