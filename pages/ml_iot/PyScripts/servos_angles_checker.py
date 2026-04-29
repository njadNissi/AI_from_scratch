import RPi.GPIO as GPIO
import time
import sys

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the servos
upper_servo_pin = 12
lower_servo_pin = 13     
angle = 0
direction = 0 # 0=ascending 0r 1=descending
controlled_servos = sys.argv[1] if len(sys.argv) > 1 else "y" # p:pitch, y:yaw
servo_time = .05 #<========================
last_angles = [90, 0] # pitch, yaw

# Set up the GPIO pins as output
GPIO.setup(upper_servo_pin, GPIO.OUT)
GPIO.setup(lower_servo_pin, GPIO.OUT)

# Create PWM instances for each servo with a frequency of 50Hz (standard for servos)
pitch_pwm = GPIO.PWM(upper_servo_pin, 50)
yaw_pwm = GPIO.PWM(lower_servo_pin, 50)

# Start the PWM with a duty cycle of 0 (servo at 0 degrees)
pitch_pwm.start(90)
yaw_pwm.start(90)


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


def control_servo(servos="py", min_angle=0, max_angle=180, inc=45):
    """
        Move the pitch servo from min to max angle in degrees in both directions.
        p = pitch servo
        y = yaw servo
    """
    global direction
    
    if "p" in servos:
        print("Controlling Pitch servo")
        for angle in range(min_angle, max_angle+1, inc):
            angle = abs(angle - direction * max_angle)
            print(f"{angle}°")
            set_angle(pitch_pwm, start_angle=last_angles[0], end_angle=angle)
            last_angles[0] = angle
        
    if "y" in servos:
        print("Controlling Yaw servo")
        for angle in range(min_angle, max_angle+1, inc):
            angle = abs(angle - direction * max_angle)
            print(f"{angle}°")
            set_angle(yaw_pwm, start_angle=last_angles[1], end_angle=angle)
            last_angles[1] = angle
        
    print("=======================")
    direction = 1 if  direction == 0 else 0


try:
    # Recenter the servos
    set_angle(pitch_pwm, 0, 0)
    time.sleep(1)
    set_angle(yaw_pwm, 0, 90)
    time.sleep(1)
    while True:
        control_servo(servos=controlled_servos, min_angle=0, max_angle=180, inc=15)

except KeyboardInterrupt:
    print("Program interrupted by user")
finally:
    # Stop the PWM signals
    pitch_pwm.stop()
    yaw_pwm.stop()
    # Clean up the GPIO settings
    GPIO.cleanup()
