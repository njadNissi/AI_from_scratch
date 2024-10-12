"""
This script is created by Njad Nissi 2024.02.28
Weight estiomation/approximation for linear data sets
y_pred = w . x
 Where:
 ->> y_pred is the predicted y to be tested agains the true y
 ->> w is the estimated weight that aims to minimize the 
 distance between the prediction and the exact value
 mean_squared_error d = (y - y_pred)^2, the lesser the better
"""

import random as rnd

# r = rnd.seed(t.CLOCK_REALTIME)
EPSILON = .001 # epsilon
lr = .001 # learning rate

dataset = [
    (0, 0),
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 8),
    (5, 10)
]

def mse(w, X=dataset):
    cost = 0
    for x in X:
        y_pred = x[0] * w
        se = (x[1] - y_pred) **2 # squared error
        cost += se

    return cost / len(X)

# back propagation: check influence of error for each sample and optimize
def grad(w):
    global EPSILON # epsilon
    dw = (mse(w + EPSILON) - mse(w)) / EPSILON 
    return w - lr * dw # minimization on the opposite direction of the gradient


def train(w0, iters, X=dataset):
    w = w0
    for _ in range(iters):
        m2e = mse(w, X)
        print(f'{w}       {m2e}')
        w = grad(w)
    
    return w, m2e



if __name__=="__main__":
    w = rnd.random() * 10 # start with a guess from 0-10
    print('\tWEIGHT\t\t\tERROR', '\n', '-*-'*15)
    w, m2e = train(w, 400)
