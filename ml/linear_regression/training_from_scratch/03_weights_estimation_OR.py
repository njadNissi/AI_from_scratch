import math
import random as rnd

EPSILON = .001
lr = .001
WEIGHTS_NO = 2
# example :OR gate
dataset = [
    #w1 w2 y
    (0, 0, 0),
    (0, 1, 1),
    (1, 0, 1),
    (1, 1, 1)
]

def mse(W, dataset): # Wnx1 and Xmxn => W^T . X
    cost = 0
    for x in dataset:
        y = 0
        for i in range(WEIGHTS_NO):
            y += W[i] * x[i]
        error = (x[WEIGHTS_NO] - y) **2
        cost += error

    return cost / len(dataset)


def grad(W, dataset:list[tuple]):
    
    global EPSILON # epsilon
    W_new = []
    for i in range(WEIGHTS_NO):
        m2e = mse(W, dataset) # cost(w0, w1) : deviation from current weights

        # dw0 = mse(w0 + e, w1), dw1 = mse(w0, w1 + e)
        Wi = W[:i] + [W[i] + EPSILON] + W[i+1:]

        # dw_0 = (mse(w0 + e, w1) - m2e) / e
        dw_i = (mse(Wi, dataset) - m2e) / EPSILON
        W_new.append(W[i] - lr * dw_i)
    
    return W_new # minimization on the opposite direction of the gradient


def train(iters, training_set):
    W = [rnd.random() for _ in range(WEIGHTS_NO)] # start with a guess from 0-10
    for _ in range(iters):
        m2e = mse(W, training_set) # error related to the weights
        print(f'{W}       {m2e}')
        W = grad(W, training_set)
    print('\n')
    return W, m2e

def sigmoid(x):
    """
        No matter the twiking of w1, w2 and bias we won't achieve the perfect learning.
        that's where activation functions comes in handy. 
        sigmoid function gives 0 for w <=0, and 1 elsewise;
    """
    return 1.0 / (1.0 + math.exp(-x))


def predict(model:list[float], test_set:list[tuple]):# model = (Weights, Biases)

    Y_predicted = []
    for x in test_set:
        y_row = 0
        for i in range(WEIGHTS_NO):
            y_row += model[i] * x[i]
        
        Y_predicted.append(sigmoid(y_row))
    
    return Y_predicted


if __name__=="__main__":

    print('\tWEIGHTS\t\t\tERROR', '\n', '-*-'*20)
    w, m2e = train(iters=5000, training_set=dataset)
    y = predict(model=w, test_set=dataset)

    print(f"Weights: {w}")
    print(f"Pred y: {y} with MSE = {m2e}")
    y = [x>.5 for x in y]
    print(f"Pred y: {y} with MSE = {m2e}")
