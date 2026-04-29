import os
import random as rnd
import math
import datasets_generator as datasets
import pandas as pd
import matplotlib.pyplot as plt

EPSILON = .001 # epsilon
lr = .001 # learning rate
WEIGHTS_NO = 2
# example :OR gate
training_set = datasets.XOR_dataset()
history = []
file_dir = os.path.dirname(os.path.abspath(__file__)) + "/artifacts"


def mse(W, dataset=training_set): # Wnx1 and Xmxn => W^T . X
    cost = 0
    for x, y in zip(dataset[0], dataset[1]):
        y_pred = 0
        for i in range(WEIGHTS_NO):
            y_pred += W[i] * x[i]
        error = (y - sigmoid(y_pred)) **2 # the y value is either 0 or 1 bcz of sigmoid
        cost += error

    return cost / len(dataset)


def grad(W):
    
    global EPSILON # epsilon
    W_new = []
    for i in range(WEIGHTS_NO):
        m2e = mse(W) # cost(w0, w1) : deviation from current weights

        # dw0 = mse(w0 + e, w1), dw1 = mse(w0, w1 + e)
        Wi = W[:i] + [W[i] + EPSILON] + W[i+1:]

        # dw_0 = (mse(w0 + e, w1) - m2e) / e
        dw_i = (mse(Wi) - m2e) / EPSILON
        W_new.append(W[i] - lr * dw_i)
    
    return W_new # minimization on the opposite direction of the gradient


def sigmoid(x):
    """
        No matter the twiking of w1, w2 and bias we won't achieve the perfect learning.
        that's where activation functions comes in handy. 
        sigmoid function gives 0 for w <=0, and 1 elsewise;
    """
    return 1.0 / (1.0 + math.exp(-x))


def train(iters):

    W = [rnd.random() for _ in range(WEIGHTS_NO)] # start with a guess from 0-10
    print_interval = iters // 10 # then print 10 times
    for _ in range(iters):
        m2e = mse(W) # error related to the weights
        if _ % print_interval == 0:
            print(f'epoch={_}   W={W}       mse={m2e}')
        history.append((_, *W.copy(), m2e))
        W = grad(W)
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

    W, m2e = train(iters=500)
    df = pd.DataFrame(history, columns=["epoch", *[f'w{i}' for i in range(WEIGHTS_NO)], "mse"])
    df.to_csv(f"{file_dir}/XOR_challenge_train_history.csv", index=False)

    y = predict(model=W, testing_set=datasets.XOR_dataset()[0])
    print(f"Result: {y}")


    # ------------------------------------------------------
    # 1. Plot MSE on the left Y-axis
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.plot(df['epoch'], df['mse'], color='tab:red', linewidth=2)
    ax1.set_title('XOR Challenge | Training Loss (MSE)')
    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Error')
    ax1.grid(True, alpha=0.3)
    fig1.tight_layout()
    fig1.savefig(f"{file_dir}/XOR_challenge_mse.png")

    # --- FIGURE 2: WEIGHTS ---
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.plot(df['epoch'], df['w0'], label='Weight 0')
    ax2.plot(df['epoch'], df['w1'], label='Weight 1')
    ax2.set_title('XOR Challenge | Weight Evolution')
    ax2.set_xlabel('Epochs')
    ax2.set_ylabel('Value')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    fig2.tight_layout()
    fig2.savefig(f"{file_dir}/XOR_challenge_weights.png")
