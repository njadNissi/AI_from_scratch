
import random as rnd
import math
import datasets_generator as datasets

EPSILON = .001 # epsilon
lr = .001 # learning rate
WEIGHTS_NO = 2
# example :OR gate
dataset = datasets.AND_dataset()


def mse(W, dataset:list[tuple]=dataset): # Wnx1 and Xmxn => W^T . X
    X, y = dataset
    cost = 0
    for x in X:
        y_pred = 0
        for i in range(WEIGHTS_NO):
            y_pred += W[i] * x[i]
        error = (y[i] - sigmoid(y_pred)) **2 # the y value is either 0 or 1 bcz of sigmoid
        cost += error

    return cost / len(dataset)


def grad(w, dataset:list[tuple]=dataset):
    
    global EPSILON # epsilon
    w_new = []
    for i in range(WEIGHTS_NO):
        m2e = mse(w) # cost(w0, w1) : deviation from current weights

        # dw0 = mse(w0 + e, w1), dw1 = mse(w0, w1 + e)
        Wi = w[:i] + [w[i] + EPSILON] + w[i+1:]

        # dw_0 = (mse(w0 + e, w1) - m2e) / e
        dw_i = (mse(Wi) - m2e) / EPSILON
        w_new.append(w[i] - lr * dw_i)
    
    return w_new # minimization on the opposite direction of the gradient


def sigmoid(x):
    """
        No matter the twiking of w1, w2 and bias we won't achieve the perfect learning.
        that's where activation functions comes in handy. 
        sigmoid function gives 0 for w <=0, and 1 elsewise;
    """
    return 1.0 / (1.0 + math.exp(-x))


def train(iters):

    w = [rnd.random() for _ in range(WEIGHTS_NO)] # start with a guess from 0-10

    for _ in range(iters):
        m2e = mse(w) # error related to the weights
        print(f'{w}       {m2e}')
        w = grad(w)
    print('\n')
    return w, m2e


def predict(model, testing_set:list[tuple]):# model = (Weights, Biases)

    X, y = testing_set
    Y_predicted = []
    for x in X:
        y_row = 0
        for i in range(WEIGHTS_NO):
            y_row += model[i] * x[i]
        
        Y_predicted.append(sigmoid(y_row))
    
    return Y_predicted


if __name__=="__main__":

    print('\tWEIGHTS\t\t\tERROR', '\n', '-*-'*20)

    w, m2e = train(iters=500000)
    y = predict(model=w, testing_set=dataset)
    
    print("Training Results", "\n", "-*-"*20)
    print(f"Weights: {w} with MSE = {m2e}")
    print("Truth Table:", '\n', '-*-'*20)
    X_test = dataset[0]
    for i in range(len(X_test)):
        x = X_test[i]
        print(f"{x[0]} | {x[1]} | {bool(y[i])}", '\n', '-'*12) 