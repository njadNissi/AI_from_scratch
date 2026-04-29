"""
	Simple Gradient Descent Animation using Matplotlib
	- Real-time animation of gradient descent on y = x^2
	- Red dot shows current position during optimization
	- Clear and simple visualization for educational purposes
"""
import numpy as np
import matplotlib.pyplot as plt

EPOCHS = 710

def y_fnc(x):
    return x**2


def der_y(x):
    return  2*x

x = np.arange(-100, 100, .1)
y = y_fnc(x)

curr_pos = (80, y_fnc(80))

learning_rate = .01


for iter in range(EPOCHS):
	plt.clf() # clear figure
	new_x = curr_pos[0] - learning_rate * der_y(curr_pos[0])
	new_y = y_fnc(new_x)
	curr_pos = (new_x, new_y)
	print(f"Iter {iter}: x={curr_pos[0]:.4f}, y={curr_pos[1]:.4f}")

	plt.plot(x, y)
	plt.scatter(curr_pos[0], curr_pos[1], color='red')
	# plt.pause(.001)

# plt.show()
