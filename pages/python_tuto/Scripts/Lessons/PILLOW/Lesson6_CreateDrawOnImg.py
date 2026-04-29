from PIL import Image, ImageDraw

# Create a new 400x400 red image
new_image = Image.new(mode="RGB", size=(400, 400), color="red")

# # Get a drawing context
draw = ImageDraw.Draw(new_image)

# # Draw a blue rectangle (left, top, right, bottom)
draw.rectangle(xy=[(100, 100), (300, 300)], fill="blue")

draw.text(xy=(150, 120), text="This is beautiful!", stroke_fill="black", stroke_width=6)

# # Draw a yellow circle (ellipse with equal width/height)
draw.ellipse([(150, 150), (250, 250)], fill="yellow")

# # Save the image
new_image.save("results/drawn_image.jpg")
new_image.show()