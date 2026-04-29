from PIL import Image, ImageDraw
import numpy as np

# Open the image
image = Image.open('results/example.jpeg')

# Get the width and height of the image
width, height = image.size

# Create a new image for the distorted result
distorted_image = Image.new('RGB', (width, height))

# Define the distortion function (example: simple wave distortion)
def distort(x, y):
    new_x = x + 10 * np.sin(y / 20)
    new_y = y
    return new_x, new_y

# Iterate over each pixel in the original image
for x in range(width):
    for y in range(height):
        new_x, new_y = distort(x, y)
        if 0 <= new_x < width and 0 <= new_y < height:
            pixel = image.getpixel((int(new_x), int(new_y)))
            distorted_image.putpixel((x, y), pixel)

# Save and show the distorted image
distorted_image.save('results/distorted_example.jpg')
distorted_image.show()