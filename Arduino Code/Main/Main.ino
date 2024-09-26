#include <Servo.h>
//One arduino on horizontal, one on vertical.
Servo EyeL_H; //Eye, L for left, H is horizontal.
//Servo EyeL_V;
Servo EyeR_H;
//Servo EyeR_V;
//servos go from 0 to 180.
int ValH = 50; // curent servo val. 50 is middle
int ValV = 50; 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  EyeR_H.attach(A0); //change these pins to pwm ones
  //EyeR_V.attach(A1);
  EyeL_H.attach(A2);
  //EyeL_V.attach(A3);
  EyeR_H.write(0); //change this if it doesnt work. point of it is to make servos go to their max value so they can be not drifting.
  delay(15);
  //EyeR_V.write(0); //its like kinda calibration but not really.
  //delay(15);
  EyeL_H.write(0);
  //delay(15);
  //EyeL_V.write(0);
  delay(1000);
  EyeR_H.write(50); //center servos
  delay(15);
  //EyeR_V.write(50);
  //delay(15);
  EyeL_H.write(50);
  //delay(15);
  //EyeL_V.write(50);
  delay(1000);
  Serial.println("ready");
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    int input = Serial.parseInt();
    ValH = input;
    //ValV = input;
    EyeR_H.write(ValH);
    EyeL_H.write(ValH);
    //EyeR_V.write(ValV);
    //EyeL_V.write(ValV);
    Serial.println(1); // say we are done working
  }
}
