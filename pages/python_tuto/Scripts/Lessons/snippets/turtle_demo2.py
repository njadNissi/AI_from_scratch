import turtle
import tkinter as tk
from tkinter import ttk

# Setup main window
root = tk.Tk()
root.title("Turtle Spiral Generator")
root.geometry("350x250")  # Slightly larger for value displays

# Create Turtle screen and turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)  # Initial speed

# Global variables
current_angle = 90  # Default angle
current_speed = 0   # Default speed (0 = fastest)


def draw_spiral():
    """Draw the spiral based on current angle and speed"""
    t.clear()  # Clear previous drawing
    t.speed(current_speed)
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    
    for i in range(200):
        t.pencolor(colors[i % 6])
        t.circle(i)
        t.left(current_angle)


def update_angle(value):
    """Update angle when slider changes and show current value"""
    global current_angle
    current_angle = int(value)
    angle_value_label.config(text=f"Current: {current_angle}°")  # Update display
    draw_spiral()  # Redraw with new angle


def update_speed(value):
    """Update speed when slider changes and show current value"""
    global current_speed
    current_speed = int(value)
    speed_value_label.config(text=f"Current: {current_speed} (0=Fastest)")  # Update display
    t.speed(current_speed)  # Update turtle speed immediately


def reset_screen():
    """Reset turtle and screen"""
    t.clear()
    t.penup()
    t.home()  # Move turtle to origin
    t.pendown()
    draw_spiral()  # Redraw with current settings


# --------------------------
# GUI Widgets with Value Displays
# --------------------------

# Angle Slider + Value Display
tk.Label(root, text="Adjust Angle (0°-180°):", font=("Arial", 10)).pack(pady=5)
angle_frame = tk.Frame(root)  # Frame to group slider and value
angle_frame.pack(pady=2)

angle_slider = ttk.Scale(
    angle_frame, from_=0, to=180, orient="horizontal",
    command=update_angle, length=200
)
angle_slider.set(current_angle)  # Set default
angle_slider.pack(side=tk.LEFT, padx=5)

angle_value_label = tk.Label(
    angle_frame, text=f"Current: {current_angle}°", 
    font=("Arial", 10, "bold")
)
angle_value_label.pack(side=tk.LEFT)


# Speed Slider + Value Display
tk.Label(root, text="Adjust Speed:", font=("Arial", 10)).pack(pady=5)
speed_frame = tk.Frame(root)  # Frame to group slider and value
speed_frame.pack(pady=2)

speed_slider = ttk.Scale(
    speed_frame, from_=0, to=10, orient="horizontal",
    command=update_speed, length=200
)
speed_slider.set(current_speed)  # Set default
speed_slider.pack(side=tk.LEFT, padx=5)

speed_value_label = tk.Label(
    speed_frame, text=f"Current: {current_speed} (0=Fastest)", 
    font=("Arial", 10, "bold")
)
speed_value_label.pack(side=tk.LEFT)


# Reset Button
reset_btn = tk.Button(
    root, text="Reset Screen", command=reset_screen,
    font=("Arial", 10), bg="#f0f0f0", padx=10
)
reset_btn.pack(pady=15)


# Initial drawing
draw_spiral()

# Start Tkinter and Turtle main loops
root.mainloop()
turtle.done()