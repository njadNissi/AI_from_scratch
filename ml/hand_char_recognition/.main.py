import matplotlib.pyplot as plt
import numpy as np


def draw_neural_network(ax, input_nodes=784, hidden_nodes=[128, 64], output_nodes=10):
    # Scale the drawing
    layer_sizes = [input_nodes] + hidden_nodes + [output_nodes]
    layer_heights = [np.linspace(0.6, 0.8, n) for n in layer_sizes]
    node_size = 0.05

    # Draw input layer nodes
    for y in layer_heights[0]:
        ax.add_patch(plt.Circle((0.1, y), node_size, color='r'))

    # Draw hidden layer nodes
    for i, n in enumerate(hidden_nodes):
        for y in layer_heights[i + 1]:
            ax.add_patch(plt.Circle((0.3 + 0.2 * i, y), node_size, color='g'))

    # Draw output layer nodes
    for y in layer_heights[-1]:
        ax.add_patch(plt.Circle((0.7, y), node_size, color='b'))

    # Draw connections
    for i in range(len(layer_sizes) - 1):
        for y1 in layer_heights[i]:
            for y2 in layer_heights[i + 1]:
                ax.plot([0.1 + 0.2 * i, 0.3 + 0.2 * i], [y1, y2], 'k-')


fig = plt.figure(figsize=(8, 10))

# Create the subplot for the neural - network
ax1 = fig.add_subplot(2, 1, 1)
draw_neural_network(ax1)
ax1.axis('off')

# Create the subplot for the input board
board_size = 28
grid = np.zeros((board_size, board_size))
ax2 = fig.add_subplot(2, 1, 2)
ax2.imshow(grid, cmap='gray', extent=[0, board_size, 0, board_size])
ax2.set_xticks(np.arange(0, board_size + 1, 1))
ax2.set_yticks(np.arange(0, board_size + 1, 1))
ax2.grid(which='both', color='w', linewidth=1)
ax2.axis('off')

plt.show()
