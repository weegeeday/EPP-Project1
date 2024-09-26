#include <Servo.h>

Servo EyeL_H; //Eye, L for left, H is horizontal.
Servo EyeL_V;
Servo EyeR_H;
Servo EyeR_V;
//servos go from 0 to 180.
int StepsPerSignal = 1; //when we get told to move let or right, etc how much should the motor value change?
int ValH = 90; // curent servo val. starts at 90 because of ServoPrep()
int ValV = 90;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  EyeR_H.attach(8); //change these pins to pwm ones
  EyeR_V.attach(9);
  EyeL_H.attach(10);
  EyeL_V.attach(11);
  ServoPrep();
}

void ServoPrep() {
  EyeR_H.write(0); //change this if it doesnt work. point of it is to make servos go to their max value so they can be not drifting.
  EyeR_V.write(0);
  EyeL_H.write(0);
  EyeL_V.write(0);
  delay(100);
  EyeR_H.write(90); //center servos
  EyeR_V.write(90);
  EyeL_H.write(90);
  EyeL_V.write(90);
}
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()){
    if (Serial.readString() == "L"){
      //move left
      Serial.println(0); //say we recived signal
      ValH = ValH + StepsPerSignal; // change from + to - if its doing the inverse movement. Do the same for move right and other ones in testing.
      EyeR_H.write(ValH);
      EyeL_H.write(ValH);
      delay(10);
      Serial.println(1); //say we are done working
    }
    if (Serial.readString() == "R"){
      //move right
      Serial.println(0);
      ValH = ValH - StepsPerSignal;
      EyeR_H.write(ValH);
      EyeL_H.write(ValH);
      delay(10);
      Serial.println(1);
    }
    if (Serial.readString() == "U"){
      //move up
      Serial.println(0);
      ValV = ValV + StepsPerSignal;
      EyeR_V.write(ValV);
      EyeL_V.write(ValV);
      delay(10);
      Serial.println(1);
    }
    if (Serial.readString() == "D"){
      //move down
      Serial.println(0);
      ValV = ValV - StepsPerSignal;
      EyeR_V.write(ValV);
      EyeL_V.write(ValV);
      delay(10);
      Serial.println(1);
    }
  }
}