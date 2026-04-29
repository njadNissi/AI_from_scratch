"""
  Simple Gradient Descent Animation using Matplotlib
  - Real-time animation of gradient descent on y = x^2
  - Red dot shows current position during optimization
  - Clear and simple visualization for educational purposes
"""
import matplotlib.pyplot as plt
import numpy as np

def fx(x1, x2):
  return np.sin(5 * x1) * np.cos(5 * x2) / 5


def gradient(x1, x2):
  return np.cos(5 * x1) * np.cos(5 * x2), -np.sin(5 * x1) * np.sin(5 * x2)


x1_points = np.arange(-1, 1, .05)
x2_points = np.arange(-1, 1, .05)
X1, X2 = np.meshgrid(x1_points, x2_points)

Y = fx(X1, X2)

cp = (.7, .4, fx(.7, .4)) # current position ==> x1, x2, f(x1, x2)
lr = .01 # learning rate (alpha)
n_iters = 1000
ax = plt.subplot(projection="3d", computed_zorder=False)

for epoch in range(n_iters):
  dx1, dx2 = gradient(cp[0], cp[1])
  x1_new, x2_new = cp[0] - lr * dx1, cp[1] - lr * dx2
  cp = x1_new, x2_new, fx(x1_new, x2_new)
  print(f"Iter {epoch}: x1={cp[0]:.4f}, x2={cp[1]:.4f}, f={cp[2]:.4f}")
  
  
  ax.plot_surface(X1, X2, Y, cmap="viridis", zorder=0) # plot current vals
  ax.scatter(cp[0], cp[1], cp[2], color='magenta', zorder=1)
  # plt.pause(.001)
  ax.clear()