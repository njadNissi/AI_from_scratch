import cv2
import sys
import serial


if len(sys.argv) < 2:
    print("python3 detect_faces.py <cam> or <image.extension>")
    exit(0)

arg = sys.argv[1]
file_path = '.face_location.log'
try:
    ser = serial.Serial(baudrate=115200, port="/dev/ttyUSB0")
except:
    ser = serial.Serial(baudrate=115200, port="/dev/ttyUSB1")
    
# Load the pre-trained Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Calculate the center of the frame
frame_height, frame_width = (480, 640)
frame_center_x = frame_width // 2
frame_center_y = frame_height // 2
face_size = (30, 30)
PITCH_MIN_ANGLE = 0
PITCH_MAX_ANGLE = 180
YAW_MIN_ANGLE = 0
YAW_MAX_ANGLE = 180
ERR_THRESH = 10
SCALE_X = .01
SCALE_Y = .01
last_angles = [0, 0]

def track_and_center_face(x, y, w, h):
    
    # Calculate the center of the face
    face_center_x = x + w // 2
    face_center_y = y + h // 2
    print(f"Face Size = {w} x {h}\n"
          f"Center = {face_center_x}, {face_center_y}")

    # Calculate the error in the x and y directions
    error_x = face_center_x - frame_center_x
    error_y = face_center_y - frame_center_y
     
    # Adjust the pitch servo
    if abs(error_y) > ERR_THRESH:
        # face is on the up/down, move to up/down
        pitch_angle = last_angles[0] + error_y * SCALE_Y
        pitch_angle = max(PITCH_MIN_ANGLE, min(PITCH_MAX_ANGLE, pitch_angle))
        last_angles[0] = pitch_angle
        print(f"Pitch = {pitch_angle}°")
            
    # Adjust the yaw servo
    if abs(error_x) > ERR_THRESH:
        # face is on the right/left, move to right/left
        yaw_angle = last_angles[1] - error_x * SCALE_X
        yaw_angle = max(YAW_MIN_ANGLE, min(YAW_MAX_ANGLE, yaw_angle))
        last_angles[1] = yaw_angle
        print(f"Yaw = {yaw_angle}°")

    print(f"==============================")

def send2serial(x, y):
    try:
        #line:str = f"{x},{y},{w},{h}\n"
        line:str = f"{x},{y}\n"
        ser.write(line.encode("UTF-8"))
        #print(line)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    if arg == "cam":

        # Initialize the camera
        cap = cv2.VideoCapture(0)

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
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=face_size)

            # Draw rectangles around the detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                track_and_center_face(x, y, w, h)
                send2serial(*last_angles)
            
            # Display the frame with detected faces
            cv2.imshow('Face Detection', frame)

            # Press 'q' to exit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

    else:

        # Read the input image
        image = cv2.imread(arg)

        # Convert the image to grayscale (Haar cascade works better on grayscale images)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=face_size)

        # Draw rectangles around the detected faces
        for (x, y, w, h) in faces:
             #write2buffer(x, y, w, h)
             cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                
        # Display the output image
        cv2.imshow('Face Detection', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__=="__main__":

    main()
