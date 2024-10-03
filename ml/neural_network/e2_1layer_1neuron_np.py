import numpy as np
# inputs that come from 3 neurons of previous layer to one neuron of current layer.
inputs = [1, 2, 3]
# each neuron has a link that has a weight
weights = [0.2, 0.8, -0.5]
# error estimation of each neuron
bias = 2

output = np.dot(inputs, weights) + bias

print(output)
