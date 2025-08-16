from PIL import Image

# Open image
image = Image.open("results/cropped_example.jpg")

# Rotate 90 degrees clockwise
rotated_90 = image.rotate(-90)  # Negative = clockwise

# Rotate 180 degrees
rotated_180 = image.rotate(180)

# Save rotated images
rotated_90.save("results/rotated_90.jpg")
rotated_180.save("results/rotated_180.jpg")