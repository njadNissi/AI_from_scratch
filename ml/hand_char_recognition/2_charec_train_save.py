import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Load the MNIST dataset
mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalize the image data
train_images = train_images / 255.0
test_images = test_images / 255.0

# Build the model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.summary()

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=5)

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Test accuracy:', test_acc)

# Generate the model name containing accuracy and loss values
model_name = f"Artifacts/chrec_acc{test_acc:.4f}_loss{test_loss:.4f}"

# Save the model in Keras format
keras_model_path = f"{model_name}.keras"
model.save(keras_model_path)
print(f"Model saved as Keras format at {keras_model_path}")

# Save the model in .h5 format
h5_model_path = f"{model_name}.h5"
model.save(h5_model_path)
print(f"Model saved as {h5_model_path}")

# Convert the model to TFLite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

tflite_model_path = f"{model_name}.tflite"
with open(tflite_model_path, 'wb') as f:
    f.write(tflite_model)
print(f"Model converted and saved as {tflite_model_path}")
    
