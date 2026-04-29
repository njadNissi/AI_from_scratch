from PIL import Image

# Open image
image = Image.open("results/grayscale_example.jpg")

# Define crop coordinates: (left, top, right, bottom)
# Example: crop a 200x200 square starting at (50, 50)
crop_box = (80, 0, 300, 200)  # (left, top, right, bottom)
cropped_image = image.crop(crop_box)

# Save result
cropped_image.save("results/cropped_example.jpg")
cropped_image.show()
