#include <Servo.h>
/*
  Notes from aya on 2024-8-18:
    1. Do pid on the computer side, then send the result to here via serial.
*/
Servo servo1;
Servo servo2; 

String inputString_1, inputString_2;
String outputString_1, outputString_2;
double data_1, data_2;
String header;
byte RxedByte;
void update_servo_pos(float servo1Pos, float servo2Pos);
void receive_send_2_data_2();

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  servo1.attach(9);  // attaches the servo on pin 9 to the servo object
  servo2.attach(10); 
}


void  loop() {
    receive_send_2_data_2();
    update_servo_pos(data_1, data_2);
}


void update_servo_pos(float servo1Pos, float servo2Pos){
  servo1.write(servo1Pos);                  // sets the servo position according to the scaled value
  servo2.write(servo2Pos);
  delay(5);
}


void receive_send_2_data_2(){
    if (Serial.available()) {
        RxedByte = Serial.read();
       switch(RxedByte){
          case 'A':  
                digitalWrite(13,HIGH);
                Serial.println("LED is on");
                break;
          case 'B':
                digitalWrite(13,LOW);
                Serial.println("LED is off");
                break;
          case 'C': // save data 1
                inputString_1 = Serial.readStringUntil("\n");
                data_1 = inputString_1.toDouble();
//                Serial.println("Data 1 is received");
                break;
          case 'D': // save data 2
                inputString_2 = Serial.readStringUntil("\n");
                data_2 = inputString_2.toDouble();
//                Serial.println("Data 2 is received");
                break;
          case 'R': // Read data
                outputString_1 = (String)data_1;
                outputString_2 = (String)data_2;
                delay(20);
                Serial.print("Data 1: ");
                Serial.print(outputString_1);
                Serial.print(" Data2: ");
                Serial.println(outputString_2);
                break;
          default:
                break;
        }
    }
}
