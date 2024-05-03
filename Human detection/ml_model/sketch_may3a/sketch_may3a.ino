#include <Servo.h>

Servo servo1;

void setup() {
  Serial.begin(9600);
  servo1.attach(3);
}

void loop() {
  if (Serial.available() > 0) {
    int peopleCount = Serial.readString().toInt();
    // Serial.println(peopleCount); 
    if(peopleCount > 2){
      servo1.write(45);
      delay(800);  // Add a delay after rotating the servo
    }
    else{
      servo1.write(225);
      // delay(1000);  // Add a delay after rotating the servo
    }
  }
}
