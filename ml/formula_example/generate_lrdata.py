import pandas as pd
import numpy as np
import random as rd
import pandas as pd


lb = -100
rb = 100
SAMPLES_NO = 50000

def nfeatures(features:int):
    
    x1 = [rd.randint(lb, rb) for _ in range(SAMPLES_NO)]
    x2 = [rd.randint(lb, rb) for _ in range(SAMPLES_NO)]
    x3 = [rd.randint(lb, rb) for _ in range(SAMPLES_NO)]

    # Coefficients (weights) for linear combination
    coefs = np.array([1, -2, 3])

    X = pd.DataFrame({'x1':x1, 'x2':x2, 'x3':x3})
    # X.head()

    y = (X[['x1', 'x2', 'x3']] * coefs).sum(axis=1)
    # Y.head()
    y = y.rename('y')

    dataset = pd.concat([X, y], axis=1)
    print(dataset.head())

    dataset.to_csv('3fFormulaRegressor.csv', index=False)


def maths_magic(digits:int):

    X = [rd.randint(10**(digits-1), 10**digits - 1) for _ in range(SAMPLES_NO)]
    y = []
    for x in X:
        y.append(x + 200000 - 2)
  
    X = pd.DataFrame({'x': X})
    y = pd.DataFrame({'y': y})
    dataset = pd.concat([X, y], axis=1)
    print(dataset.head())
    dataset.to_csv('mathsMagicRegressor.csv', index=False)

    
if __name__=="__main__":
    
    # nfeatures(features=3)
    maths_magic(digits=5)