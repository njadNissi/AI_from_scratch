from PIL import Image

# Open an image file
# Scripts/Lessons/PILLOW/results/example.jpeg
# variable:Object    # Class
image = Image.open("results/example.jpeg")

# Display the image
image.show() # function >> method

# Print image details
print(f"Format: {image.format}") # extension
print(f"Size: {image.size} (width x height)") # shape: rows x cols
print(f"Mode: {image.mode}")  # e.g., 'RGB' for color, 'L' for grayscale