"""
    Simple Gradient Descent with Interactive Slider and Video Generation
    - Interactive Plot with Slider (3D Surface)
    - Video Generation of Full Gradient Descent Process (MP4)
"""
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from matplotlib.animation import FFMpegWriter

# Define the function and gradient
def fx(x1, x2):
    return np.sin(5 * x1) * np.cos(5 * x2) / 5

def gradient(x1, x2):
    return np.cos(5 * x1) * np.cos(5 * x2), -np.sin(5 * x1) * np.sin(5 * x2)

# Create grid and run gradient descent
x1_points = np.arange(-1, 1, .05)
x2_points = np.arange(-1, 1, .05)
X1, X2 = np.meshgrid(x1_points, x2_points)
Y = fx(X1, X2)

# Gradient descent parameters and history collection
cp = (.7, .4, fx(.7, .4))
lr = .01
n_iters = 100
history = [cp]
current = cp

for iter in range(n_iters):
    dx1, dx2 = gradient(current[0], current[1])
    x1_new = current[0] - lr * dx1
    x2_new = current[1] - lr * dx2
    current = (x1_new, x2_new, fx(x1_new, x2_new))
    history.append(current)
    print(f"Iter {iter}: x1={current[0]:.4f}, x2={current[1]:.4f}, f={current[2]:.4f}")

# --------------------------
# 1. Create interactive plot with slider
# --------------------------
fig_slider = plt.figure(figsize=(10, 8))
ax_slider = fig_slider.add_subplot(111, projection="3d", computed_zorder=False)
fig_slider.subplots_adjust(bottom=0.2)

# Plot surface and initial point
surface_slider = ax_slider.plot_surface(X1, X2, Y, cmap="viridis", zorder=0, alpha=0.7)
point_slider, = ax_slider.plot([history[0][0]], [history[0][1]], [history[0][2]], 
                              'mo', markersize=10, zorder=1)

# Configure plot
ax_slider.set_xlim(-1, 1)
ax_slider.set_ylim(-1, 1)
ax_slider.set_zlim(-0.2, 0.2)
ax_slider.set_xlabel('X1')
ax_slider.set_ylabel('X2')
ax_slider.set_zlabel('f(X1, X2)')
title_slider = ax_slider.set_title(f'Gradient Descent (Iteration 0/{n_iters})')
fig_slider.colorbar(surface_slider, ax=ax_slider, shrink=0.5, aspect=5)

# Add slider
ax_slider_widget = fig_slider.add_axes([0.2, 0.05, 0.65, 0.03])
slider = Slider(
    ax=ax_slider_widget,
    label='Iteration',
    valmin=0,
    valmax=n_iters,
    valinit=0,
    valstep=1
)

def update_slider(val):
    iteration = int(slider.val)
    x1, x2, z = history[iteration]
    point_slider.set_data_3d([x1], [x2], [z])
    title_slider.set_text(f'Gradient Descent (Iteration {iteration}/{n_iters})')
    fig_slider.canvas.draw_idle()

slider.on_changed(update_slider)

# --------------------------
# 2. Generate video
# --------------------------
def generate_video(history, filename:str):
    """Generate a video from the history"""
    fig_video = plt.figure(figsize=(10, 8))
    ax_video = fig_video.add_subplot(111, projection="3d", computed_zorder=False)
    
    # Plot surface once
    surface_video = ax_video.plot_surface(X1, X2, Y, cmap="viridis", zorder=0, alpha=0.7)
    point_video, = ax_video.plot([history[0][0]], [history[0][1]], [history[0][2]], 
                                'mo', markersize=10, zorder=1)
    
    # Configure plot
    ax_video.set_xlim(-1, 1)
    ax_video.set_ylim(-1, 1)
    ax_video.set_zlim(-0.2, 0.2)
    ax_video.set_xlabel('X1')
    ax_video.set_ylabel('X2')
    ax_video.set_zlabel('f(X1, X2)')
    title_video = ax_video.set_title(f'Gradient Descent (Iteration 0/{n_iters})')
    fig_video.colorbar(surface_video, ax=ax_video, shrink=0.5, aspect=5)
    
    # Configure video writer
    metadata = dict(title='Gradient Descent', artist='Matplotlib')
    writer = FFMpegWriter(fps=10, metadata=metadata)
    
    # Save video
    with writer.saving(fig_video, f"{file_dir}/gradient_descent-1.mp4", dpi=150):
        for i in range(len(history)):
            x1, x2, z = history[i]
            point_video.set_data_3d([x1], [x2], [z])
            title_video.set_text(f'Gradient Descent (Iteration {i}/{n_iters})')
            writer.grab_frame()
    
    plt.close(fig_video)
    print(f"Video saved as: {filename}")

# Generate video when the script runs
file_dir = os.path.dirname(os.path.abspath(__file__)) + "/artifacts"
os.makedirs(file_dir, exist_ok=True)
generate_video(history, filename=f"{file_dir}/gradient_descent-2.mp4")

# Show interactive plot
# plt.show()
    