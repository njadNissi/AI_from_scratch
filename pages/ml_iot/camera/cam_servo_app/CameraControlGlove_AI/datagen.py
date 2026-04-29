import random as r
import csv

frame_height, frame_width = (480, 640)
frame_center_x = frame_width // 2
frame_center_y = frame_height // 2
PITCH_MIN_ANGLE = 0
PITCH_MAX_ANGLE = 180
YAW_MIN_ANGLE = 0
YAW_MAX_ANGLE = 180
ERR_THRESH = 5
SCALE_X = .01
SCALE_Y = .01
last_angles = [0, 0]

def track_and_center_face(x, y, w, h):
    
    # Calculate the center of the face
    face_center_x = x + w // 2
    face_center_y = y + h // 2
    print(f"Center = {face_center_x}, {face_center_y}")

    # Calculate the error in the x and y directions
    error_x = face_center_x - frame_center_x
    error_y = face_center_y - frame_center_y
     
    # Adjust the pitch servo
    if abs(error_y) > ERR_THRESH:
        # face is on the up/down, move to up/down
        pitch_angle = last_angles[0] + error_y * SCALE_Y
        pitch_angle = max(PITCH_MIN_ANGLE, min(PITCH_MAX_ANGLE, pitch_angle))
        last_angles[0] = pitch_angle
            
    # Adjust the yaw servo
    if abs(error_x) > ERR_THRESH:        # face is on the right/left, move to right/left
        yaw_angle = last_angles[1] - error_x * SCALE_X
        yaw_angle = max(YAW_MIN_ANGLE, min(YAW_MAX_ANGLE, yaw_angle))
        last_angles[1] = yaw_angle
        

DS_SIZE = 20_000
if __name__=="__main__":

    faceX = [r.randint(0, frame_width) for _ in range(DS_SIZE)]    
    faceY = [r.randint(0, frame_height) for _ in range(DS_SIZE)]    
    faceW = [r.randint(30, 400) for _ in range(DS_SIZE)]    
    faceH = [r.randint(30, 400) for _ in range(DS_SIZE)]    
    servoPitch = []
    servoYaw = []
    
    for (x, y, w, h) in zip(faceX, faceY, faceW, faceH):

        track_and_center_face(x, y, w, h)
        pitch, yaw = last_angles
        servoPitch.append(pitch)
        servoYaw.append(yaw)
    
    try:
        with open("DATASET.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Table header
            writer.writerow(['faceX', 'faceY', 'faceW', 'faceH', 'servoPitch', 'servoYaw'])
            # Table data
            for vals in zip(faceX, faceY, faceW, faceH, servoPitch, servoYaw):
                writer.writerow([*vals])
        print(f"CSV file created at successfully")
    except Exception as e:
        print(f"Error in creating the file: {e}")
