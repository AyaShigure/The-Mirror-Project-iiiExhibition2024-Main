#include <Arduino.h>
#include <Servo.h>

const int SERVO_HORIZONTAL_MIN_ANG = 0;
const int SERVO_HORIZONTAL_MAX_ANG = 180;
const int SERVO_VERTICAL_MIN_ANG = 0;
const int SERVO_VERTICAL_MAX_ANG = 100;

/*
  Notes from aya on 20234-7-7

  Servo control of the mirror camera platfrom.

  Angle limit of :
    1.  Horizontal servo : 0 - 180
    2.  Vertical servo : 0 - 100
*/


Servo servoHorizontal;  // create servo object to control a servo
Servo servoVertical;
// twelve servo objects can be created on most boards


void HorizontalSweep()
{
  int delayTime = 10;
  int MIDDLE_POS = (int)((SERVO_HORIZONTAL_MAX_ANG - SERVO_HORIZONTAL_MIN_ANG)/2);

  // Middle pos to min
  for(int i = MIDDLE_POS; i >= SERVO_HORIZONTAL_MIN_ANG; i--)
  {
    servoHorizontal.write(i);
    delay(delayTime);
  }

  for(int i = SERVO_HORIZONTAL_MIN_ANG; i <= SERVO_HORIZONTAL_MAX_ANG; i++)
  {
    servoHorizontal.write(i);
    delay(delayTime);
  }

  for(int i = SERVO_HORIZONTAL_MAX_ANG; i >= SERVO_HORIZONTAL_MIN_ANG; i--)
  {
    servoHorizontal.write(i);
    delay(delayTime);
  }

  // Return to middle pos
  for(int i = SERVO_HORIZONTAL_MIN_ANG; i <= MIDDLE_POS; i++)
  {
    servoHorizontal.write(i);
    delay(delayTime);
  }
}

void VerticalSweep()
{
  int delayTime = 10;
  int MIDDLE_POS = (int)((SERVO_VERTICAL_MAX_ANG-SERVO_VERTICAL_MIN_ANG)/2);

  // Middle pos to min
  for(int i = MIDDLE_POS; i >= SERVO_VERTICAL_MIN_ANG; i--)
  {
    servoVertical.write(i);
    delay(delayTime);
  }


  for(int i = SERVO_VERTICAL_MIN_ANG; i <= SERVO_VERTICAL_MAX_ANG; i++)
  {
    servoVertical.write(i);
    delay(delayTime);
  }
  for(int i = SERVO_VERTICAL_MAX_ANG; i >= SERVO_VERTICAL_MIN_ANG; i--)
  {
    servoVertical.write(i);
    delay(delayTime);
  }

  // Return to middle pos
  for(int i = SERVO_VERTICAL_MIN_ANG; i <= MIDDLE_POS; i++)
  {
    servoVertical.write(i);
    delay(delayTime);
  }

  
}

void setup() {
  servoHorizontal.attach(9);  // attaches the servo on pin 9 to the servo object
  servoVertical.attach(10);
}

void loop() {
  // int min_angle = 0;
  // int max_angle = 100;

  // for (pos = min_angle; pos <= max_angle; pos += 1) { // goes from 0 degrees to 180 degrees
  //   // in steps of 1 degree
  //   servoHorizontal.write(pos);              // tell servo to go to position in variable 'pos'
  //   servoVertical.write(pos);
  //   delay(10);                       // waits 15ms for the servo to reach the position
  // }
  // for (pos = max_angle; pos >= min_angle; pos -= 1) { // goes from 180 degrees to 0 degrees
  //   servoHorizontal.write(pos);              // tell servo to go to position in variable 'pos'
  //   servoVertical.write(pos);
  //   delay(10);                       // waits 15ms for the servo to reach the position
  // }


  while(1)
  {
    HorizontalSweep();
    delay(500);
    VerticalSweep();
    delay(500);

  }

}
