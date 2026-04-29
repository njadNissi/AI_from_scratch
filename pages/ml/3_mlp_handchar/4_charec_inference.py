import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv) < 2:
    print("use: python charec_inference.py <model.keras>")
    exit

# Load the MNIST test dataset
mnist = keras.datasets.mnist
(_, _), (test_images, test_labels) = mnist.load_data()

# Normalize the test image data
test_images = test_images / 255.0

# Load the previously saved .keras model
# Please modify the model path according to the actual situation
model_path = sys.argv[1]
model = keras.models.load_model(model_path)

# Set the size of the figure
plt.figure(figsize=(10, 20))

# Iterate through each digit from 0 to 9
for digit in range(10):
    # Find all indices of the current digit in the test set
    digit_indices = np.where(test_labels == digit)[0]
    # Randomly select 5 samples
    random_indices = np.random.choice(digit_indices, 5, replace=False)

    # Plot the 5 samples
    for i, index in enumerate(random_indices):
        plt.subplot(10, 5, digit * 5 + i + 1)
        plt.imshow(test_images[index], cmap='gray')
        plt.axis('off')

        # Make a prediction
        predictions = model.predict(np.expand_dims(test_images[index], axis=0))
        predicted_digit = np.argmax(predictions)

        # Display the prediction result
        if predicted_digit == digit:
            plt.title(f'Pred: {predicted_digit}', color='green')
        else:
            plt.title(f'Pred: {predicted_digit}', color='red')

plt.tight_layout()
plt.show()
