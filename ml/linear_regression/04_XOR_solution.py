"""
    Multi-layer Perceptron, a simple neuralnet proposed by Marvin Minsky and  in 1969
    Author: Ndombasi Diakusala Joao Andre
    Date  : October 3rd, 2024 
"""
import math
import random as rnd
import datasets_generator as datasets



class MLP():
    
    def __init__(self, randomize=True) -> None:
        
        self.dataset = None
        
        # Layer 1: 2 neurons
        self.or_w1 = 0.0
        self.or_w2 = 0.0
        self.or_b = 0.0

        self.nand_w1 = 0.0
        self.nand_w2 = 0.0
        self.nand_b = 0.0
        
        # Layer 2: 1 neuron
        self.and_w1 = 0.0
        self.and_w2 = 0.0
        self.and_b = 0.0

        # HyperParameters
        self.eps = .1 # little increment
        self.lr  = .1 # alpha or stepsize
        
        if randomize: self.initParams();


    def fit(self, dataset:tuple[list]):
        
        self.X_train = dataset[0]
        self.y_train = dataset[1]
        
    
    def checkParams(self):
        
        for attribute in dir(self):
                
            if not attribute.startswith('__'):
                value = getattr(self, attribute) 
                if type(value) is float:
                    print(f"{attribute}: {value}")
                    pass
    

    def initParams(self):
        # Iterate through attributes of my_object
        for attribute in dir(self):
            
            if not attribute.startswith('__'):
                value = getattr(self, attribute)
                
                if type(value) is float:
                    setattr(self, attribute, rnd.random())
                    

    def sigmoid(self, x):
        """
            No matter the twiking of w1, w2 and bias we won't achieve the perfect learning.
            that's where activation functions comes in handy. 
            sigmoid function gives 0 for w <=0, and 1 elsewise;
        """
        return 1.0 / (1.0 + math.exp(-x))


    def forward(self, input:tuple[float, float]) -> float:
        x1, x2 = input
        y_or = self.sigmoid(self.or_w1 * x1 + self.or_w2 * x2 + self.or_b)
        y_nand = self.sigmoid(self.nand_w1 * x1 + self.nand_w2 * x2 + self.nand_b)
        return self.sigmoid(y_or * self.and_w1 + y_nand + self.and_w2 + self.and_b)

        
    def mse(self):
        
        cost = 0.0
        for sample in range(len(self.y_train)):
            x = self.X_train[sample]
            y_pred = self.forward(input=x)
            error = (self.y_train[sample] - y_pred) **2
            cost += error

        return cost / len(self.y_train)

        
    def grad(self):
        
        temp = MLP(randomize=False)
        c = self.mse()

        saved = self.or_w1
        self.or_w1 += self.eps
        temp.or_w1 = (self.mse() - c) / self.eps
        self.or_w1 = saved
        
        saved = self.or_w2
        self.or_w2 += self.eps
        temp.or_w2 = (self.mse() - c) / self.eps
        self.or_w2 = saved
        
        saved = self.or_b
        self.or_b += self.eps
        temp.or_b = (self.mse() - c) / self.eps
        self.or_b = saved
        
        saved = self.nand_w1
        self.nand_w1 += self.eps
        temp.nand_w1 = (self.mse() - c) / self.eps
        self.nand_w1 = saved
        
        saved = self.nand_w2
        self.nand_w2 += self.eps
        temp.nand_w2 = (self.mse() - c) / self.eps
        self.nand_w2 = saved
        
        saved = self.nand_b
        self.nand_b += self.eps
        temp.nand_b = (self.mse() - c) / self.eps
        self.nand_b = saved
        
        saved = self.and_w1
        self.and_w1 += self.eps
        temp.and_w1 = (self.mse() - c) / self.eps
        self.and_w1 = saved
        
        saved = self.and_w2
        self.and_w2 += self.eps
        temp.and_w2 = (self.mse() - c) / self.eps
        self.and_w2 = saved
        
        saved = self.and_b
        self.and_b += self.eps
        temp.and_b = (self.mse() - c) / self.eps
        self.and_b = saved
        
        return temp


    def train(self, iters:int, lr:float, eps:float):
        self.eps = eps
        self.lr = lr
        for i in range(iters):
            print(f"--------------- ITER {i+1} ----------------------")
        
            t = model.grad()
            self.or_w1 -= lr * t.or_w1
            self.or_w2 -= lr * t.or_w2
            self.or_b -= lr * t.or_b

            self.nand_w1 -= lr * t.nand_w1
            self.nand_w2 -= lr * t.nand_w2
            self.nand_b -= lr * t.nand_b

            self.and_w1 -= lr * t.and_w1
            self.and_w2 -= lr * t.and_w2
            self.and_b -= lr * t.and_b

            self.checkParams()
            print("Cost: " + str(self.mse()))
    
    
    def predict(self, x):
        
        return self.forward(x)
        

if __name__=="__main__": 
    
    # model 
    model = MLP(randomize=True)
    model.checkParams()
    model.fit(dataset=datasets.AND_dataset())
    model.train(iters=100_000, lr=.1, eps=.1)
   
    print("==================== TEST =======================")
    for i in range(2):
       for j in range(2):
           print(f"{i} | {j} = {round(model.predict((i, j)))}") 
     