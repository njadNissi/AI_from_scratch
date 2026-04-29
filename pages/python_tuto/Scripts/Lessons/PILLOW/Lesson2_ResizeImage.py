from PIL import Image

# Open imageObj
imageObj = Image.open("results/example.jpeg")

# Resize to 300x200 pixels
resized_imageObj = imageObj.resize((300, 200))

# Save the resized imageObj
resized_imageObj.save("results/resized_example.jpg")
resized_imageObj.show()

# Print image details
print(f"Format: {resized_imageObj.format}") # extension
print(f"Size: {resized_imageObj.size} (width x height)") # shape: rows x cols
print(f"Mode: {resized_imageObj.mode}")  # e.g., 'RGB' for color, 'L' for grayscale