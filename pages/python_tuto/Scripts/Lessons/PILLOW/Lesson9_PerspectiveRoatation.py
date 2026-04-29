import cv2
import numpy as np

# Callback function for the slider (updates distortion strength)
def update_distortion(val):
    global distortion_strength
    distortion_strength = val  # Get value from slider

# Read the image
image = cv2.imread('results/example.jpeg')
if image is None:
    print("Error: Could not read the image.")
    exit()

h, w = image.shape[:2]
distortion_strength = 50  # Initial distortion strength

# Create a window to display results
cv2.namedWindow('Distorted Image')

# Add a slider bar (range: 0 to 200, initial value: 50)
cv2.createTrackbar('Distortion Strength', 'Distorted Image', 50, 200, update_distortion)

while True:
    # Define source and destination points (distortion depends on slider value)
    src = np.float32([[0, 0], [w-1, 0], [0, h-1], [w-1, h-1]])
    dst = np.float32([
        [distortion_strength, distortion_strength//2],  # Top-left
        [w - distortion_strength, distortion_strength//2],  # Top-right
        [distortion_strength//2, h - distortion_strength],  # Bottom-left
        [w - distortion_strength//2, h - distortion_strength]  # Bottom-right
    ])

    # Calculate perspective transformation matrix
    M = cv2.getPerspectiveTransform(src, dst)
    distorted = cv2.warpPerspective(image, M, (w, h))

    # Display the distorted image
    cv2.imshow('Distorted Image', distorted)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()