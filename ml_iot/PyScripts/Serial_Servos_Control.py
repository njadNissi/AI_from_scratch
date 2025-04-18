import serial
import json
import RPi.GPIO as GPIO
import time


# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define servo pins
pitch_servo_pin = 12
yaw_servo_pin = 13

# Set up servo pins as output
GPIO.setup(pitch_servo_pin, GPIO.OUT)
GPIO.setup(yaw_servo_pin, GPIO.OUT)

# Initialize PWM for servos
pitch_pwm = GPIO.PWM(pitch_servo_pin, 50)  # 50Hz frequency
yaw_pwm = GPIO.PWM(yaw_servo_pin, 50)

# Start PWM with 0% duty cycle
pitch_pwm.start(0)
yaw_pwm.start(0)


def set_servo_angle(pwm, angle):
    # Map the angle (0 - 180) to the duty cycle (2 - 12)
    duty = angle / 18 + 2
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.1)  # Wait for the servo to reach the position


# Open serial port
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8').strip()
        print(line)
        if line:
            try:
                # Parse the JSON data
                data = json.loads(line)
                # Check if 'pitch' and 'yaw' are in the JSON data
                if 'pitch' in data and 'yaw' in data:
                    pitch = int(data['pitch'])
                    yaw = int(data['yaw'])
                    # Make sure the values are within the valid range (0 - 180)
                    pitch = max(0, min(180, pitch))
                    yaw = max(0, min(180, yaw))
                    # Set servo angles
                    set_servo_angle(pitch_pwm, pitch)
                    #set_servo_angle(yaw_pwm, yaw)
            except json.JSONDecodeError:
                print("Failed to decode JSON data:", line)
except KeyboardInterrupt:
    print("Program interrupted by user")
finally:
    # Clean up
    pitch_pwm.stop()
    yaw_pwm.stop()
    GPIO.cleanup()
    ser.close()

