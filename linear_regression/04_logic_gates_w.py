
import random as rnd
import math
import datasets_generator as datasets

EPSILON = .001 # epsilon
lr = .001 # learning rate
WEIGHTS_NO = 2
# example :OR gate
dataset = datasets.AND_dataset()

def mse(W, dataset:list[tuple]): # Wnx1 and Xmxn => W^T . X
    cost = 0
    for x in dataset:
        y = 0
        for i in range(WEIGHTS_NO):
            y += W[i] * x[i]
        error = (x[WEIGHTS_NO] - sigmoid(y)) **2 # the y value is either 0 or 1 bcz of sigmoid
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


def sigmoid(x):
    """
        No matter the twiking of w1, w2 and bias we won't achieve the perfect learning.
        that's where activation functions comes in handy. 
        sigmoid function gives 0 for w <=0, and 1 elsewise;
    """
    return 1.0 / (1.0 + math.exp(-x))


def train(iters, dataset:list[tuple]):

    W = [rnd.random() for _ in range(WEIGHTS_NO)] # start with a guess from 0-10

    for _ in range(iters):
        m2e = mse(W, dataset) # error related to the weights
        print(f'{W}       {m2e}')
        W = grad(W, dataset)
    print('\n')
    return W, m2e


def predict(model, testing_set=None):# model = (Weights, Biases)

    Y_predicted = []
    for x in testing_set:
        y_row = 0
        for i in range(WEIGHTS_NO):
            y_row += model[i] * x[i]
        
        Y_predicted.append(sigmoid(y_row))
    
    return Y_predicted


if __name__=="__main__":

    print('\tWEIGHTS\t\t\tERROR', '\n', '-*-'*20)

    W, m2e = train(iters=10_000, dataset=dataset)

    y = predict(model=W, testing_set=dataset)
    print(y)