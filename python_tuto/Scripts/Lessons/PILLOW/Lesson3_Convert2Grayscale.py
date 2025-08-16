from PIL import Image

# Open color image
color_image = Image.open("results/resized_example.jpg")

# Convert to grayscale
grayscale_image = color_image.convert("L")  # 'L' mode for grayscale

# Save or display
grayscale_image.save("results/grayscale_example.jpg")
grayscale_image.show()

# Print image details
print(f"Format: {grayscale_image.format}") # extension
print(f"Size: {grayscale_image.size} (width x height)") # shape: rows x cols
print(f"Mode: {grayscale_image.mode}")  # e.g., 'RGB' for color, 'L' for grayscale