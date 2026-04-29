"""
    Rastrigin Function (Complex 2D Function with Many Local Minima)
    - Interactive Plot with Slider (2D Contour + 3D Surface)
    - Video Generation of Full Gradient Descent Process (MP4)
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FFMpegWriter

# --------------------------
# 1. Define the Complex 2D Function: Rastrigin Function
# --------------------------
def rastrigin(x1, x2, A=10):
    """
    Rastrigin function (non-convex, many local minima):
    f(x1,x2) = A*2 + (x1² - A*cos(2πx1)) + (x2² - A*cos(2πx2))
    Global minimum at (0,0) with f=0.
    """
    return A * 2 + (x1**2 - A * np.cos(2 * np.pi * x1)) + (x2**2 - A * np.cos(2 * np.pi * x2))

def rastrigin_gradient(x1, x2, A=10):
    """Gradient of the Rastrigin function (for gradient descent)"""
    dx1 = 2 * x1 + 2 * np.pi * A * np.sin(2 * np.pi * x1)  # dF/dx1
    dx2 = 2 * x2 + 2 * np.pi * A * np.sin(2 * np.pi * x2)  # dF/dx2
    return dx1, dx2

# --------------------------
# 2. Initialize Parameters & Precompute Gradient Descent History
# --------------------------
# Challenge: Hyperparameters
EPOCHS = 200                # Number of iterations
learning_rate = 0.003       # Smaller LR (avoids overshooting local minima)
initial_pos = (2.5, 2.5)    # Starting position (far from global minimum)
A = 10                      # Rastrigin function parameter


# Add "momentum" (critical for escaping local minima!)
momentum = 0.85               # 3. Momentum: carries past small barriers
prev_dx1, prev_dx2 = 0.0, 0.0# Tracks previous gradient step


# Generate grid for function visualization (2D contour + 3D surface)
x1_range = np.linspace(-5, 5, 100)  # x1 from -5 to 5
x2_range = np.linspace(-5, 5, 100)  # x2 from -5 to 5
X1, X2 = np.meshgrid(x1_range, x2_range)
Z = rastrigin(X1, X2, A)

# Precompute gradient descent path (store all positions in history)
history = []
curr_x1, curr_x2 = initial_pos
curr_z = rastrigin(curr_x1, curr_x2, A)
history.append((curr_x1, curr_x2, curr_z))  # (x1, x2, f(x1,x2))

for _ in range(EPOCHS):
    # Update position using gradient descent (minimize the function)
    dx1, dx2 = rastrigin_gradient(curr_x1, curr_x2, A)

    # Add momentum: combine current gradient with previous step
    # Momentum = (momentum * previous step) + (learning rate * current gradient)
    step_x1 = momentum * prev_dx1 - learning_rate * dx1
    step_x2 = momentum * prev_dx2 - learning_rate * dx2
    
    # Update position (using momentum step)
    new_x1 = curr_x1 + step_x1
    new_x2 = curr_x2 + step_x2
    new_z = rastrigin(new_x1, new_x2, A)
    
    # Update state
    curr_x1, curr_x2, curr_z = new_x1, new_x2, new_z
    prev_dx1, prev_dx2 = step_x1, step_x2  # Save step for next iteration's momentum
    history.append((curr_x1, curr_x2, curr_z))
    
    # Optional: Print progress every 100 iterations
    if (_ + 1) % 10 == 0:
        print(f"Iter {_+1}: x1={curr_x1:.4f}, x2={curr_x2:.4f}, f={curr_z:.4f}")

# --------------------------
# 3. Interactive Plot: 2D Contour + 3D Surface + Slider
# --------------------------
# Create a 2-subplot figure (2D contour on top, 3D surface below)
fig_slider = plt.figure(figsize=(12, 10))
fig_slider.subplots_adjust(bottom=0.2, hspace=0.4)  # Space for slider and subplots

# Subplot 1: 2D Contour Plot (top)
ax_contour = fig_slider.add_subplot(121)
# Plot contour lines (darker = lower function value; white = global minimum)
contour = ax_contour.contourf(X1, X2, Z, levels=50, cmap='viridis', alpha=0.8)
fig_slider.colorbar(contour, ax=ax_contour, label='f(x1, x2)')
# Initial position (red dot) – updates with slider
point_contour, = ax_contour.plot(
    [history[0][0]], [history[0][1]], 
    'ro', markersize=8, label='Current Position'
)
# Plot path (optional: shows full trajectory)
path_contour, = ax_contour.plot(
    [h[0] for h in history[:1]], [h[1] for h in history[:1]], 
    'r--', alpha=0.5, label='Trajectory'
)
# Configure contour plot
ax_contour.set_xlabel('x1')
ax_contour.set_ylabel('x2')
ax_contour.set_title('2D Contour: Rastrigin Function')
ax_contour.legend()
ax_contour.grid(True, alpha=0.3)

# Subplot 2: 3D Surface Plot (bottom)
ax_3d = fig_slider.add_subplot(122, projection='3d', computed_zorder=False)
# Plot 3D surface (alpha=0.7 to see the red dot behind)
surface = ax_3d.plot_surface(X1, X2, Z, cmap='viridis', alpha=0.7, zorder=0)
# Initial position (red dot) – updates with slider
point_3d, = ax_3d.plot(
    [history[0][0]], [history[0][1]], [history[0][2]], 
    'ro', markersize=8, zorder=1, label='Current Position'
)
# Configure 3D plot
ax_3d.set_xlabel('x1')
ax_3d.set_ylabel('x2')
ax_3d.set_zlabel('f(x1, x2)')
ax_3d.set_title('3D Surface: Rastrigin Function')
ax_3d.legend()
ax_3d.set_zlim(0, 100)  # Zoom in on relevant z-range

# Add Slider (bottom of the figure)
slider_ax = fig_slider.add_axes([0.2, 0.05, 0.65, 0.03])
iteration_slider = Slider(
    ax=slider_ax,
    label='Iteration',
    valmin=0,
    valmax=EPOCHS,
    valinit=0,
    valstep=1,
    color='#ff7f0e'
)

# Update Function (runs when slider is dragged)
def update_slider(val):
    current_iter = int(iteration_slider.val)
    x1, x2, z = history[current_iter]
    
    # Update 2D contour plot
    point_contour.set_data([x1], [x2])
    path_contour.set_data([h[0] for h in history[:current_iter+1]], 
                          [h[1] for h in history[:current_iter+1]])
    
    # Update 3D surface plot
    point_3d.set_data_3d([x1], [x2], [z])
    
    # Update main title
    fig_slider.suptitle(
        f'Gradient Descent on Rastrigin Function (Iteration {current_iter}/{EPOCHS}) | f(x1,x2) = {z:.2f}',
        fontsize=14
    )
    
    fig_slider.canvas.draw_idle()

# Link slider to update function
iteration_slider.on_changed(update_slider)
# Set initial title
fig_slider.suptitle(
    f'Gradient Descent on Rastrigin Function (Iteration 0/{EPOCHS}) | f(x1,x2) = {history[0][2]:.2f}',
    fontsize=14
)


# --------------------------
# 4. Generate Video of the Full Animation
# --------------------------
def generate_video(history, output_filename:str):
    """Save 2D contour + 3D surface animation as MP4."""
    fig_video = plt.figure(figsize=(10, 8))
    fig_video.subplots_adjust(hspace=0.4)
    
    # Video Subplot 1: 2D Contour
    ax_contour_vid = fig_video.add_subplot(121)
    contour_vid = ax_contour_vid.contourf(X1, X2, Z, levels=50, cmap='viridis', alpha=0.8)
    fig_video.colorbar(contour_vid, ax=ax_contour_vid, label='f(x1, x2)')
    point_contour_vid, = ax_contour_vid.plot([], [], 'ro', markersize=8)
    path_contour_vid, = ax_contour_vid.plot([], [], 'r--', alpha=0.5)
    ax_contour_vid.set_xlabel('x1')
    ax_contour_vid.set_ylabel('x2')
    ax_contour_vid.set_title('2D Contour: Rastrigin Function')
    ax_contour_vid.grid(True, alpha=0.3)

    # Video Subplot 2: 3D Surface
    ax_3d_vid = fig_video.add_subplot(122, projection='3d', computed_zorder=False)
    surface_vid = ax_3d_vid.plot_surface(X1, X2, Z, cmap='viridis', alpha=0.7, zorder=0)
    point_3d_vid, = ax_3d_vid.plot([], [], [], 'ro', markersize=8, zorder=1)
    ax_3d_vid.set_xlabel('x1')
    ax_3d_vid.set_ylabel('x2')
    ax_3d_vid.set_zlabel('f(x1, x2)')
    ax_3d_vid.set_title('3D Surface: Rastrigin Function')
    ax_3d_vid.set_zlim(0, 100)

    # Video Writer Configuration
    writer = FFMpegWriter(
        fps=20,  # Smooth playback (slower than real-time for clarity)
        metadata=dict(title='Gradient Descent on Rastrigin Function', artist='Matplotlib'),
        bitrate=2000  # Higher quality
    )

    # Save Frames to Video
    with writer.saving(fig_video, output_filename, dpi=150):
        for i in range(len(history)):
            x1, x2, z = history[i]
            
            # Update 2D Contour
            point_contour_vid.set_data([x1], [x2])
            path_contour_vid.set_data([h[0] for h in history[:i+1]], 
                                     [h[1] for h in history[:i+1]])
            
            # Update 3D Surface
            point_3d_vid.set_data_3d([x1], [x2], [z])
            
            # Update Title
            fig_video.suptitle(
                f'Gradient Descent on Rastrigin Function (Iteration {i}/{EPOCHS}) | f(x1,x2) = {z:.2f}',
                fontsize=14
            )
            
            # Capture Frame
            writer.grab_frame()

    plt.close(fig_video)
    print(f"Video saved as: {output_filename}")

# Run Video Generation
file_dir = os.path.dirname(os.path.abspath(__file__)) + "/artifacts"
os.makedirs(file_dir, exist_ok=True)
generate_video(history, output_filename=f"{file_dir}/gradient_descent-3.mp4")


# --------------------------
# Show Interactive Slider Plot
# --------------------------
# plt.show()