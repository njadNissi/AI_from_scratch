#!usr/bin/venv/python3

import numpy as np
import matplotlib.pyplot as plt

MAX_ITER = 1000

def y_fnc(x):
    return x**2


def der_y(x):
    return  2*x

x = np.arange(-100, 100, .1)
y = y_fnc(x)

curr_pos = (80, y_fnc(80))

learning_rate = .01


for _ in range(MAX_ITER):
	plt.clf() # clear figure
	new_x = curr_pos[0] - learning_rate * der_y(curr_pos[0])
	new_y = y_fnc(new_x)
	curr_pos = (new_x, new_y)

	plt.plot(x, y)
	plt.scatter(curr_pos[0], curr_pos[1], color='red')
	plt.pause(.001)

plt.show()
