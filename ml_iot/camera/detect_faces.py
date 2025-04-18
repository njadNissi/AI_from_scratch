import cv2
import sys

if len(sys.argv) < 2:
	print("python3 detect_faces.py <cam> or <image.extension>")
	exit(0)

arg = sys.argv[1]

def main():
    if arg == "cam":

        # Initialize the camera
        cap = cv2.VideoCapture(0)

        # Load the pre-trained Haar cascade classifier for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        while True:
            # Read a frame from the camera
            ret, frame = cap.read()

            if not ret:
                print("Failed to grab frame")
                break

            # Check if the frame has 3 channels (BGR)
            if len(frame.shape) == 3 and frame.shape[2] == 3:
                # Convert the frame to grayscale
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            else:
                # If the frame is already grayscale, use it as is
                gray = frame

            # Detect faces in the grayscale frame
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Draw rectangles around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the frame with detected faces
            cv2.imshow('Face Detection', frame)

            # Press 'q' to exit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

    else:
        # Load the pre-trained face cascade classifier
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Read the input image
        image = cv2.imread(arg)

        # Convert the image to grayscale (Haar cascade works better on grayscale images)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the output image
        cv2.imshow('Face Detection', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__=="__main__":
    
    main()
