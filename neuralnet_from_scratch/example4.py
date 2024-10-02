import numpy as np

inputs = [
    [1, 2, 3, 2.5],
    [2, 5, -1, 2],
    [-1.5, 2.7, 3.3, -0.8]
] # 3X4 # sample

weights = [
    [0.2, 0.8, -0.5, 1.0], # neuron1
    [0.5, -0.91, 0.26, -0.5], # neuron2
    [-0.26, -0.27, 0.17, 0.87] # neuron3
] # 3X4

biases = [2, 3, 0.5]

# matrix A and its transpose have the same determinant, the main digonal doesn't change, the secondary are swapped.
layer_outputs = np.dot(inputs, np.array(weights).T) + biases 

print(layer_outputs)
