#include <Servo.h>
//Eye, Horizontal, Vertical. Just wire the the servos on each eye together! Vertical R and L on the same pin! (just make sure the 0's are the same)
Servo Eye;
int Val = 0; // curent servo val. 50 is middle (check for all of them)
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Eye.attach(A0); //change these pins to pwm ones
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    int Val = Serial.parseInt();
    Eye.write(Val);
    delay(100);
    Serial.println(1); // say we are done working
  }
}
