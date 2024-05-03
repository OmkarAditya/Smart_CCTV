#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

void setup() {
  Serial.begin(9600);
  servo1.attach(3);
  servo2.attach(5); 
  servo3.attach(6); 
  servo4.attach(9); 
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    int servoNumber = command.substring(0, 1).toInt();
    int joystickValue = command.substring(2).toInt(); 
    int servoAngle = map(joystickValue, 0, 180, 0, 180);

    switch (servoNumber) {
      case 1:
        servo1.write(servoAngle);
        break;
      case 2:
        servo2.write(servoAngle);
        break;
      case 3:
        servo3.write(servoAngle);
        break;
      case 4:
        servo4.write(servoAngle);
        break;
    }
  }
}
