#include <Servo.h>

// 创建两个舵机对象
Servo pitchServo;
Servo yawServo;

// 定义舵机控制引脚
const int pitchPin = A0;
const int yawPin = A1;

// 定义变量用于存储读取的角度值
int pitchAngle = 0;
int yawAngle = 0;

// 用于临时存储接收到的字符
String inputString = "";
bool stringComplete = false;

void setup() {
    // 初始化串口通信
    Serial.begin(115200);

    // 连接舵机到相应的引脚
    pitchServo.attach(pitchPin);
    yawServo.attach(yawPin);

    // 将舵机初始位置设置为90度
    pitchServo.write(pitchAngle);
    yawServo.write(yawAngle);

    // 初始化输入字符串
    inputString.reserve(200);
}

void loop() {
    // 处理串口数据
    serialEvent();

    if (stringComplete) {
        // 解析接收到的字符串
        int commaIndex = inputString.indexOf(',');
        if (commaIndex != -1) {
            pitchAngle = inputString.substring(0, commaIndex).toInt();
            yawAngle = inputString.substring(commaIndex + 1).toInt();

            // 确保角度值在舵机可接受的范围内（0 - 180度）
            pitchAngle = constrain(pitchAngle, 0, 180);
            yawAngle = constrain(yawAngle, 0, 180);

            // 设置舵机角度
            pitchServo.write(pitchAngle);
            yawServo.write(yawAngle);

            // 输出读取到的角度值
            Serial.print("Pitch Angle: ");
            Serial.print(pitchAngle);
            Serial.print(", Yaw Angle: ");
            Serial.println(yawAngle);
        }

        // 清空输入字符串并重置标志
        inputString = "";
        stringComplete = false;
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
