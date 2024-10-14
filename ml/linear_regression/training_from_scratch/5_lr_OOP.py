import random as rnd
import math
import sys
import datasets_generator as datasets


class LinearRegression():

    def __init__(self) -> None:
            
        self.EPSILON = .001
        self.LEARNING_RATE = .001

        self.SAMPLES_NO = 0
        self.WEIGHTS_NO = 0
        self.X_train = []
        self.y_train = []
        self.X_test = []
        self.y_test = []
        self.WEIGTHS = []


    def mse(self, dataset:list, W:list, bias:float): # Wnx1 and Xmxn => W^T . X
        
        cost = 0

        for sample in range(self.SAMPLES_NO):

            x = dataset[sample]
            y = sum(W[i] * x[i] for i in range(self.WEIGHTS_NO)) + bias
 
 			# the y value is either 0 or 1 bcz of sigmoid
            error = (self.y_train[sample] - self.sigmoid(y + bias)) **2
            cost += error

        return cost / self.SAMPLES_NO


    def forward(self, W: list, b:float):
        
        SAMPLES = len
        global EPSILON # epsilon
        W_new = list.copy(W)
        b_new = b
            
        for i in range(self.WEIGHTS_NO): # n weights per sample

            m2e = self.mse(self.X_train, W, b) # cost(w0, w1) : deviation from current weights

            # dw0 = mse(w0 + e, w1), dw1 = mse(w0, w1 + e)
            Wi = W[:i] + [W[i] + self.EPSILON] + W[i+1:]

            # dw_0 = (mse(w0 + e, w1) - m2e) / e
            dw_i = (self.mse(self.X_train, Wi, b) - m2e) / self.EPSILON
            W_new[i] -= self.LEARNING_RATE * dw_i
        

        db = (self.mse(self.X_train, W, b + self.EPSILON) - m2e) / self.EPSILON

        return W_new, b - self.LEARNING_RATE * db # minimization on the opposite direction of the gradient


    def sigmoid(self, x):
        """
            No matter the twiking of w1, w2 and bias we won't achieve the perfect learning.
            that's where activation functions comes in handy. 
            sigmoid function gives 0 for w <=0, and 1 elsewise;
        """
        return 1.0 / (1.0 + math.exp(-x))


    def train(self, training_dataset, iters, show_process='3'): # X_train should inclue y_train
        """
			show_process:
				0 or np: No printing
				1 or yp: yield line printing
				2 or ap: auto line printing
				3 or fp: full printing
		"""
        self.X_train = training_dataset[0]
        self.SAMPLES_NO = len(self.X_train)
        self.WEIGHTS_NO = len(self.X_train[0])
        self.y_train = training_dataset[1]

        W = [rnd.random() for _ in range(self.WEIGHTS_NO)] # start with a guess from 0-10
        b = rnd.random() # start with a guess from 0-10

        try:
            for i in range(iters):

                m2e = self.mse(self.X_train, W, b) # error related to the weights

                if show_process == '3' or show_process == 'fp':
                    print(f'Rnd{i}>{W}\t{b}\t{m2e:.3f}')
                elif show_process == '2' or show_process == 'ap':
                    print(f'Rnd{i}>{W}\t{b}\t{m2e:.3f}', end='\r')
                elif show_process == '1' or show_process == 'yp':
                    input()
                    print(f'Rnd{i}>{W}\t{b}\t{m2e:.3f}', end='\r')

                W, b = self.forward(W, b)

        except Exception as e:

            print(e, "f{w:{W}}")
            
        return W, b, m2e


    def predict(self, model:tuple, testing_set:tuple[list, list]):# model = (Weights, Bias)
        
        W, b = model
        m2e = 0
        Y_predicted = []
        self.X_test=testing_set[0]
        self.y_test = testing_set[1]
        SIZE = len(self.X_test)
        
        for sample in range(SIZE):

            x = self.X_test[sample]
            y = sum(W[i] * x[i] for i in range(self.WEIGHTS_NO))
            Y_predicted.append(self.sigmoid(y + b))

        return Y_predicted, m2e


if __name__=="__main__":
    
    try:
        epochs  = int(sys.argv[1]) # 1000
        verbose = sys.argv[2]
        training_set = datasets.linear_dataset(w=(.5, -1), b=0, size=5_000)
        testing_set = datasets.linear_dataset(w=(.5, -1), b=0, size=10)

        print('\tWEIGHTS\t\t\t\t\t\\t\tt\t\t\t\t\tERROR', '\n', '-*-'*35)

        AI = LinearRegression()
        W, b, m2e = AI.train(training_set, iters=epochs, show_process=verbose) # [1]: -p (printing)
        y_pred, b = AI.predict(model=(W, b), testing_set=testing_set)

        size = len(y_pred)
        y = testing_set[1]
        print(f"Prediction for {size} samples with bias = {b}")
        for i in range(size): 
            print(f"{testing_set[0][i]} => {y_pred[i]} vs {y[i]}")
            
    except Exception as e:
        
        print("Run command: ===> python 05_lr_OOP.py [iterations or epochs] [verbose level]")
        print("verbose defines the amount of details in the training process:")
        print("\t0 or np: No printing")
        print("\t1 or yp: yield line printing")
        print("\t2 or ap: auto single line printing")
        print("\t3 or fp: full printing")