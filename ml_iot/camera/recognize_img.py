import cv2
import numpy as np
import sys

if len(sys.argv) < 2:
        print("python3 recogniz.py <image_path.extension>")

       
# Load the YOLO model
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

# Load the class names
classes = []
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Read an image
image = cv2.imread(sys.argv[1])
height, width, _ = image.shape

# Prepare the input blob for the neural network
blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)

# Get the output layer names
output_layer_names = net.getUnconnectedOutLayersNames()
layer_outputs = net.forward(output_layer_names)

# Process the outputs to detect objects
boxes = []
confidences = []
class_ids = []

for output in layer_outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Apply non - maximum suppression to remove overlapping boxes
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

# Draw rectangles and labels around the detected objects
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(len(classes), 3))
if len(indexes) > 0:
    for i in indexes.flatten():
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = str(round(confidences[i], 2))
        color = colors[class_ids[i]]
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        cv2.putText(image, label + " " + confidence, (x, y + 20), font, 2, color, 2)

# Display the image with detected objects
cv2.imshow('Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

