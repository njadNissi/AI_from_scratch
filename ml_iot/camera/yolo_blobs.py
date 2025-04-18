import cv2
import numpy as np
import time

# Read the image
img = cv2.imread('images/horse.jpg')
if img is None:
    print("Failed to read the image. Please check the image path.")
else:
    # Display the original image
    cv2.imshow('Original Image', img)
    cv2.waitKey(1)

    # Load the YOLO model
    net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    # net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

    # Get the names of the model's layers
    ln = net.getLayerNames()
    print(f"Number of model layers: {len(ln)}")
    print("List of model layer names:", ln)

    # Construct a blob from the image
    blob = cv2.dnn.blobFromImage(img, 1 / 255.0, (416, 416), swapRB=True, crop=False)

    # Extract the three channels
    channel_0 = blob[0, 0, :, :]
    channel_1 = blob[0, 1, :, :]
    channel_2 = blob[0, 2, :, :]

    # Display the three channel blobs
    cv2.imshow('Blob Channel 0', channel_0)
    cv2.displayOverlay('Blob Channel 0', f'Blob Channel 0 shape={channel_0.shape}')
    cv2.imshow('Blob Channel 1', channel_1)
    cv2.displayOverlay('Blob Channel 1', f'Blob Channel 1 shape={channel_1.shape}')
    cv2.imshow('Blob Channel 2', channel_2)
    cv2.displayOverlay('Blob Channel 2', f'Blob Channel 2 shape={channel_2.shape}')

    cv2.waitKey(1)

    # Set the input and perform forward propagation
    net.setInput(blob)
    t0 = time.time()
    outputs = net.forward(ln)
    t = time.time()

    # Display the forward propagation time
    cv2.displayOverlay('Original Image', f'Forward propagation time={t - t0} seconds')

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
