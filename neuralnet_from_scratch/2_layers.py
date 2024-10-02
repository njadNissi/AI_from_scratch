import numpy as np

inputs = [
    [1, 2, 3, 2.5],
    [2, 5, -1, 2],
    [-1.5, 2.7, 3.3, -0.8]
] # sample

weights1 = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
] # loayer1 : 3 neuron

weights2 = [
    [0.1, -0.14, 0.5],
    [-0.5, 0.12, -0.33],
    [-0.44, 0.73, -0.13]
] # loayer2 : 3 neuron


biases1 = [2, 3, 0.5]
biases2 = [-1, 2, -0.5]

# matrix A and its transpose have the same determinant
layer_outputs1 = np.dot(inputs, np.array(weights1).T) + biases1 # sample is input of fisrt layer
layer_outputs2 = np.dot(layer_outputs1, np.array(weights2).T) + biases2 # output of layer1 is input for layer2

print(layer_outputs1)
print(layer_outputs2)
