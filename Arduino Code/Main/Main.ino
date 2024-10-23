#include <Servo.h>
//Eye, Horizontal, Vertical. Just wire the the servos on each eye together! Vertical R and L on the same pin! (just make sure the 0's are the same)
Servo Eye;
int Val = 0; // curent servo val. 50 is middle (check for all of them)
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); //make serial run on baud 115200
  Eye.attach(A0); //attach the servo to pin A0
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) { //if we have new serial data, run the code in if statement
    int Val = Serial.parseInt(); //val is = to the new serial data parsed as an int.
    Eye.write(Val); //write the new val to the servo
    delay(100); //wait 100ms
    Serial.println(1); // say we are done working
  }
}
