"""
	Simple Gradient Descent with Interactive Slider and Video Generation
	- Interactive Plot with Slider (1D Quadratic Function)
	- Video Generation of Full Gradient Descent Process (MP4)
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FFMpegWriter

# --------------------------
# Core Function & Gradient Descent Logic
# --------------------------
def y_fnc(x):
    """Quadratic function to minimize: y = x²"""
    return x ** 2

def der_y(x):
    """Derivative (gradient for 1D) of y_fnc: dy/dx = 2x"""
    return 2 * x

# Hyperparameters
EPOCHS = 710 # Number of gradient descent iterations
learning_rate = 0.01
initial_x = 80  # Starting position
x_range = np.arange(-100, 100, 0.1)  # For plotting the full function curve
y_full = y_fnc(x_range)

# Step 1: Run gradient descent and store ALL positions (for slider/video)
history = []
curr_pos = (initial_x, y_fnc(initial_x))
history.append(curr_pos)  # Save initial position

for epoch in range(EPOCHS):
    # Update position using gradient descent
    new_x = curr_pos[0] - learning_rate * der_y(curr_pos[0])
    new_y = y_fnc(new_x)
    curr_pos = (new_x, new_y)
    history.append(curr_pos)  # Save each iteration's position
    print(f"Iter {epoch}: x={curr_pos[0]:.4f}, y={curr_pos[1]:.4f}")


# --------------------------
# 1. Interactive Plot with Slider
# --------------------------
# Create figure and main axis (for function plot)
fig_slider, ax_slider = plt.subplots(figsize=(10, 8))
fig_slider.subplots_adjust(bottom=0.2)  # Reserve space for slider

# Plot the full quadratic function (static)
ax_slider.plot(x_range, y_full, 'b-', linewidth=2, label='$y = x^2$')
# Plot initial position (will update with slider)
point_slider, = ax_slider.plot([history[0][0]], [history[0][1]], 
                               'ro', markersize=8, label='Current Position')

# Configure plot limits and labels
ax_slider.set_xlim(-100, 100)
ax_slider.set_ylim(0, max(y_full) * 0.1)  # Zoom in on the minimum region
ax_slider.set_xlabel('x')
ax_slider.set_ylabel('y = x²')
ax_slider.set_title('Gradient Descent Demo: Minimizing $y = x^2$ (Iteration 0/{EPOCHS})')
ax_slider.grid(True, alpha=0.3)
ax_slider.legend()

# Create slider axis (bottom of the figure)
ax_slider_widget = fig_slider.add_axes([0.2, 0.05, 0.65, 0.03])
slider = Slider(
    ax=ax_slider_widget,
    label='Iteration',
    valmin=0,
    valmax=EPOCHS,
    valinit=0,
    valstep=1,  # Only integer iterations (no fractions)
    color='#ff7f0e'
)

# Update function: Runs when slider is dragged
def update_slider(val):
    iteration = int(slider.val)
    x, y = history[iteration]
    # Update the red dot's position
    point_slider.set_data([x], [y])
    # Update title to show current iteration
    ax_slider.set_title(f'Gradient Descent Demo: Minimizing $y = x^2$ (Iteration {iteration}/{EPOCHS})')
    fig_slider.canvas.draw_idle()  # Refresh the plot

# Link slider to update function
slider.on_changed(update_slider)


# --------------------------
# 2. Generate Video of the Full Animation
# --------------------------
def generate_video(history, filename:str):
    """Save the full gradient descent process as an MP4 video"""
    # Create a new figure for the video (separate from slider plot)
    fig_video, ax_video = plt.subplots(figsize=(10, 8))
    
    # Plot the static quadratic function
    ax_video.plot(x_range, y_full, 'b-', linewidth=2, label='$y = x^2$')
    # Plot the initial position (will update frame-by-frame)
    point_video, = ax_video.plot([history[0][0]], [history[0][1]], 
                                 'ro', markersize=8, label='Current Position')
    
    # Configure video plot (match slider plot for consistency)
    ax_video.set_xlim(-100, 100)
    ax_video.set_ylim(0, max(y_full) * 0.1)
    ax_video.set_xlabel('x')
    ax_video.set_ylabel('y = x²')
    title_video = ax_video.set_title(f'Gradient Descent Demo: Minimizing $y = x^2$ (Iteration 0/{EPOCHS})')
    ax_video.grid(True, alpha=0.3)
    ax_video.legend()
    
    # Configure video writer (FFmpeg required)
    metadata = dict(title='Gradient Descent: Minimizing y=x²', artist='Matplotlib')
    writer = FFMpegWriter(fps=30, metadata=metadata)  # 30 FPS = smooth playback
    
    # Save each frame to the video
    with writer.saving(fig_video, filename, dpi=150):  # dpi=150 = good quality
        for i in range(len(history)):
            x, y = history[i]
            # Update the red dot and title
            point_video.set_data([x], [y])
            title_video.set_text(f'Gradient Descent Demo: Minimizing $y = x^2$ (Iteration {i}/{EPOCHS})')
            # Capture the current frame
            writer.grab_frame()
    
    plt.close(fig_video)  # Close video figure to free memory
    print(f"Video saved successfully as: {filename}")



# Generate the video file
file_dir = os.path.dirname(os.path.abspath(__file__)) + "/artifacts"
os.makedirs(file_dir, exist_ok=True)
generate_video(history, filename=f"{file_dir}/gradient_descent-0.mp4")

# Show the interactive plot with slider
# plt.show()
    