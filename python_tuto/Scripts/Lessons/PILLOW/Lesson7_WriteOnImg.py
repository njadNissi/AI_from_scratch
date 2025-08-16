from PIL import Image, ImageDraw, ImageFont

# Open image
image = Image.open("results/example.jpeg")
draw = ImageDraw.Draw(image)

# Load a font (use a system font path or PIL's default)
try:
    font = ImageFont.truetype("arial.ttf", 72)  # Size 36
except IOError:
    font = ImageFont.load_default()  # Fallback

# Add text at (50, 50) with white color
draw.text(xy=(50, 50), text="Hello, Enstein!", font=font, fill="white")

# Save
image.save("results/image_with_text.jpg")
image.show()