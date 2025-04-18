#include <Arduino.h>
#line 1 "/home/njadpi/Desktop/IR_remote_rcv/IR_remote_rcv.ino"
#include <IRremote.h>
#include <Servo.h>

#define IR_RECEIVE_PIN 13
#define pitchPin A0
#define yawPin A1

// IR REMOTE CONTROL BLOCK
#define MUL 5
uint8_t servo_mode = 0;   // servo1 or servo2
uint8_t servo_angle = 0;  // servo1 or servo2

// Create two servo objects
Servo pitchServo;
Servo yawServo;

// Variables to store the read angle values
uint8_t pitchAngle = 0;
uint8_t yawAngle = 0;

// Temporary storage for the received characters
String inputString = "";
bool stringComplete = false;
bool ir_mode = false;

#line 26 "/home/njadpi/Desktop/IR_remote_rcv/IR_remote_rcv.ino"
void setup();
#line 42 "/home/njadpi/Desktop/IR_remote_rcv/IR_remote_rcv.ino"
void loop();
#line 82 "/home/njadpi/Desktop/IR_remote_rcv/IR_remote_rcv.ino"
void process_cmd();
#line 108 "/home/njadpi/Desktop/IR_remote_rcv/IR_remote_rcv.ino"
void serialEvent();
#line 26 "/home/njadpi/Desktop/IR_remote_rcv/IR_remote_rcv.ino"
void setup() {
  Serial.begin(115200);
  IrReceiver.begin(IR_RECEIVE_PIN);

  // Connect the servos to the corresponding pins
  pitchServo.attach(pitchPin);
  yawServo.attach(yawPin);

  // Set the initial position of the servos to 90 degrees
  pitchServo.write(pitchAngle);
  yawServo.write(yawAngle);

  // Initialize the input string
  inputString.reserve(200);
}

void loop() {
  if (IrReceiver.decode()) {  // control servos with remote data

    process_cmd();

    IrReceiver.resume();

  } else if (!ir_mode){  // Control Servos from camera data
            // Process serial data
    serialEvent();

    if (stringComplete) {
      // Parse the received string
      int commaIndex = inputString.indexOf(',');
      if (commaIndex != -1) {
        pitchAngle = inputString.substring(0, commaIndex).toInt();
        yawAngle = inputString.substring(commaIndex + 1).toInt();

        // Ensure the angle values are within the acceptable range of the servo (0 - 180 degrees)
        pitchAngle = constrain(pitchAngle, 0, 180);
        yawAngle = constrain(yawAngle, 0, 180);

        // Set the servo angles
        pitchServo.write(pitchAngle);
        yawServo.write(yawAngle);

        // Output the read angle values
        Serial.print("Pitch Angle: ");
        Serial.print(pitchAngle);
        Serial.print(", Yaw Angle: ");
        Serial.println(yawAngle);
      }

      // Clear the input string and reset the flag
      inputString = "";
      stringComplete = false;
    }
  }
}

void process_cmd() {
  uint8_t cmd = IrReceiver.decodedIRData.command;

  switch (cmd) {
    case 69: servo_angle = 1 * MUL; break;
    case 70: servo_angle = 2 * MUL; break;
    case 71: servo_angle = 3 * MUL; break;
    case 68: servo_angle = 4 * MUL; break;
    case 64: servo_angle = 5 * MUL; break;
    case 67: servo_angle = 6 * MUL; break;
    case  7: servo_angle = 7 * MUL; break;
    case 21: servo_angle = 8 * MUL; break;
    case  9: servo_angle = 9 * MUL; break;
    case 25: servo_angle = 0;  break; // "0"

    case 22: pitchServo.write(servo_angle); break;        // "*" ===> IR mode (100)
    case 13: pitchServo.write(servo_angle); break;
    case 24: pitchAngle += MUL; break; // "UP"
    case 90: yawAngle += MUL;  break; // "RIGHT"
    case 82: pitchAngle -= MUL; break;  // "DOWN"
    case  8: yawAngle -= MUL;   // "LEFT": 90  to left
    case 28: ir_mode = !ir_mode; Serial.println("IR Mode: " + String(ir_mode));  // "OK"
    default: Serial.println("Unrecognized command...");
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      stringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}

