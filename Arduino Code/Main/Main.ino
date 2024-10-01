#include <Servo.h>
Servo EyeV; //Eye, Horizontal, Vertical. Just wire the the servos on each eye together! Vertical R and L on the same pin! (just make sure the 0's are the same)
Servo EyeH;
int ValH = 0; // curent servo val. 50 is middle (check for all of them)
//int ValV = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  EyeH.attach(A0); //change these pins to pwm ones
  //EyeV.attach(A1);
  EyeH.write(50); //change this if it doesnt work. point of it is to make servos go to their max value so they can be not drifting.
  delay(15);
  //EyeV.write(50);
  //delay(15);
  EyeH.write(0);
  //delay(15);
  //EyeV.write(0);
  delay(1000);
  Serial.println("ready");
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    int input = Serial.parseInt();
    EyeV.write(ValH);
    //EyeH.write(ValH);
    Serial.println(1); // say we are done working
  }
}
