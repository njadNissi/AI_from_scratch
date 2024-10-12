import matplotlib.pyplot as plt
import numpy as np

def fx(x1, x2):
  return (3.0/2) * x1**2 + (1.0/2) * x2**2 - x1*x2 - 2*x1

def gradient(x1, x2):
  return 3*x1 - x2 - 2, -x1 + x2


x1_points = np.arange(-3, 3, .1)
x2_points = np.arange(-3, 3, .1)
X1, X2 = np.meshgrid(x1_points, x2_points)

Y = fx(X1, X2)

cp = (-2, 4, fx(-2, 4)) # current pos
lr = .1
n_iters = 100
ax = plt.subplot(projection="3d", computed_zorder=False)

try:
  for _ in range(n_iters):
    dx1, dx2 = gradient(cp[0], cp[1])
    x1_new, x2_new = cp[0] - lr * dx1, cp[1] - lr * dx2
    cp = x1_new, x2_new, fx(x1_new, x2_new)

    ax.plot_surface(X1, X2, Y, cmap="viridis", zorder=0)
    ax.scatter(cp[0], cp[1], cp[2], color='yellow', zorder=1)
    plt.pause(.001)
    ax.clear()
except KeyboardInterrupt:
  print('execution stopped...')
  exit(0)
