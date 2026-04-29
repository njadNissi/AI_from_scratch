import os
import cv2
import sys

file_dir = os.path.dirname(os.path.abspath(__file__)) + "/artifacts"
os.makedirs(file_dir, exist_ok=True)

def main(arg:str):
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
            cv2.imwrite(f'{file_dir}/detected_faces.jpg', frame)

            # Press 'q' to exit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

    else:
        # 2. Check if file exists
        if not os.path.exists(arg):
            print(f"❌ Error: The file '{arg}' was not found.")
            return

        # Load the classifier
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Read the input image
        image = cv2.imread(arg)

        # 3. Handle the 'empty' check manually to avoid the Assertion Error
        if image is None:
            print(f"❌ Error: Could not decode the image at {arg}. Is it a valid image format?")
            return

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # 4. Save the result to Artifacts instead of using cv2.imshow
        # (Since cv2.imshow doesn't work well on a web server/Streamlit)
        cv2.imwrite(file_dir + "/detected_faces.jpg", image)
        print(f"✅ Success! View the result in the Artifacts pane: {output_path}")


if __name__=="__main__":
    # if len(sys.argv) < 2:
        # 	print("python3 detect_faces.py <cam> or <image.extension>")
        # 	exit(0)
        # arg = sys.argv[1]

    print("Enter one of the two args: \n\t'cam': to use the camera \n\t <the path to an image file>:")
    arg = input('')
    if arg == '': arg = "cam";
        
    main(arg)
