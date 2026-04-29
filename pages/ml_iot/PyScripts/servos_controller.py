"""
    Written by NJAD Nissi on March 1str, 2025. NUIST, China.
    ===> This program is intended to run on a raspberry pi.
    It continually reads the first line of data formatted as: x,y,w,h
    ===> There are two Servo 180 degrees motors :
                1. the Upper one for Pitch a.k.a vertical rotation
                2. the bottom one for Roll a.k.a lateral rotation
"""
#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

file_path = '.face_location.log'
# Calculate the center of the frame
frame_height, frame_width = (480, 640)
frame_center_x = frame_width // 2
frame_center_y = frame_height // 2
# Define a ERR_THRESH for error
PITCH_MIN_ANGLE = 0
PITCH_MAX_ANGLE = 90
YAW_MIN_ANGLE = 0
YAW_MAX_ANGLE = 180
PWM_FREQ = 50
ERR_THRESH = 25
# Scaling factor for movements. adjust based on the speed wanted for movements.
SCALE_X = .1
SCALE_Y = .1
# Define the GPIO pins for the servos
pitch_servo_pin = 12
yaw_servo_pin = 13
last_angles = [90, 0] # pitch, yaw

GPIO.setmode(GPIO.BCM)
GPIO.setup(pitch_servo_pin, GPIO.OUT)
GPIO.setup(yaw_servo_pin, GPIO.OUT)

# Create PWM instances for each servo with a frequency of 50Hz (standard for servos)
pitch_pwm = GPIO.PWM(pitch_servo_pin, PWM_FREQ)
yaw_pwm = GPIO.PWM(yaw_servo_pin, PWM_FREQ)
# Start the PWM with a 0% duty cycle (servo at 0 degrees)
pitch_pwm.start(0)
yaw_pwm.start(0)


def set_angle(pwm, start_angle:int, end_angle:int, step=1, delay=0.05):
    """
    Move the servo from start_angle to end_angle in steps, with a delay between each step.

    :param pwm: The PWM instance of the servo
    :param start_angle: The starting angle of the servo
    :param end_angle: The target angle of the servo
    :param step: The increment or decrement value for each step. Default is 1 degree.
    :param delay: The time to wait between each step. Default is 0.05 seconds.
    """
    if start_angle < end_angle:
        for angle in range(start_angle, end_angle + 1, step):
            duty = angle / 18 + 2.5
            pwm.ChangeDutyCycle(duty)
            time.sleep(delay)
    else:
        for angle in range(start_angle, end_angle - 1, -step):
            duty = angle / 18 + 2.5
            pwm.ChangeDutyCycle(duty)
            time.sleep(delay)



def track_and_center_face(x, y, w, h):
    global yaw_servo_angle, pitch_servo_angle
    
    # Calculate the center of the face
    #face_center_x = x + w // 2
    #face_center_y = y + h // 2
    #print(f"Center = {face_center_x}, {face_center_y}")

    # Calculate the error in the x and y directions
    error_x = face_center_x - frame_center_x
    error_y = face_center_y - frame_center_y

    # Adjust the pitch servo
    if abs(error_y) > ERR_THRESH:
        # face is on the up/down, move to up/down
        pitch_angle = pitch_servo_angle + error_y * SCALE_Y
        pitch_angle = max(PITCH_MIN_ANGLE, min(PITCH_MAX_ANGLE, pitch_angle))
        set_angle(pitch_pwm, last_angles[0], pitch_angle)
        last_angles[0] = pitch_angle
        print(f"Pitch = {pitch_angle}°")
            
    # Adjust the yaw servo
    if abs(error_x) > ERR_THRESH:
        # face is on the right/left, move to right/left
        yaw_angle = yaw_servo_angle + error_x * SCALE_X
        yaw_angle = max(YAW_MIN_ANGLE, min(YAW_MAX_ANGLE, yaw_angle))
        set_angle(yaw_pwm, last_angles[1], yaw_angle)
        last_angles[1] = yaw_angle
        print(f"Yaw = {yaw_angle}°")

    print(f"==============================")
   
   
# Set initial servo positions
yaw_servo_angle = 90
pitch_servo_angle = 0
set_angle(pitch_pwm, 0, pitch_servo_angle)
time.sleep(1)
set_angle(yaw_pwm, 0, yaw_servo_angle)
time.sleep(1)
        
if __name__=="__main__":
    try:        
        while True:
            # Take the first detected face
            try:
                with open(file_path, 'r') as f:
                    #print(time.time())
                    (x, y, w, h) = map(int, f.readline().strip().split(',')) # read first line
                
                    # Update servos to center the face 
                    track_and_center_face(x, y, w, h)
                
                # Add delay to avoid excessive updates
                time.sleep(0.1)
                
            except Exception as e:
                print(e)
            
    except KeyboardInterrupt:
        print("Program interrupted by user")
        
    finally:
        # Stop the PWM signals
        pitch_pwm.stop()
        yaw_pwm.stop()
        # Clean up the GPIO settings
        GPIO.cleanup()

