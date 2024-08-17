//float thetaY;
//float thetaZ;
//enum RECEIVED_DATA_TYPE{
//  THETA_Y_DATA = 0,
//  THETA_Z_DATA = 1,
//  COMMUNICATION_STATUS_CHECK = 2
//} RECEIVED_DATA_TYPE;
//
//int receivedDataType;
//
//void setup() {
//  Serial.begin(115200);
//  Serial.setTimeout(1);
//}
//
//void  loop() {
//  while (!Serial.available());
//  
//  RECEIVED_DATA_TYPE = Serial.readString().toInt();
//  if (RECEIVED_DATA_TYPE == THETA_Y_DATA){
//    while (!Serial.available());
//    thetaY = Serial.parseFloat();
//    Serial.println("Received_y_data : theta_y = ");
//    Serial.println(thetaY);
//  }
//  else if(RECEIVED_DATA_TYPE == THETA_Z_DATA){
//    while (!Serial.available());
//
//    thetaZ = Serial.parseFloat();
//    Serial.print("Received_z_data : theta_z = ");
//    Serial.println(thetaZ);
//  }
//  else if(RECEIVED_DATA_TYPE == COMMUNICATION_STATUS_CHECK){
//    
//    Serial.print("ok");
//  }
//}

float t,data;
void send_some_data_serial(){
  for(int i=0; i < 100; i++){
    t = (float)i * 0.1;
    data = sin(t);
    Serial.print("Time: ");
    Serial.print(t);
    Serial.print(" Data: ");
    Serial.println(data);
    delay(100);
  }
}

//String inputString_1, inputString_2;
//float data_1, data_2;
//String header;
//byte RxedByte;
//void receive_send_2_data(){
////    while (!Serial.available());
////    header = Serial.readStringUntil("\n");
//    if (Serial.available()) {
//        RxedByte = Serial.read();
//       switch(RxedByte){
//          case 'A':  
//                digitalWrite(13,HIGH);
////                delay(1000);
////                digitalWrite(11,LOW);
//                Serial.println("LED is on");
//
//                break;
//          case 'B': //your code
//                digitalWrite(13,LOW);
//                Serial.println("LED is off");
//                break;
//          default:
//                break;
//        }//end of switch()
//      }//endof if 
//
////    if (header == "a"){
////      while (!Serial.available());
////      inputString_1 = Serial.readStringUntil("\n");
////      data_1 = inputString_1.toFloat();
////      Serial.print("Data1: ");
////      Serial.println((String)data_1);
////    }
////    else if (header == "b"){
////      while (!Serial.available());
////      inputString_2 = Serial.readStringUntil("\n");
////      data_2 = inputString_2.toFloat();
////      Serial.print(" Data2: ");
////      Serial.println((String)data_2);
////    }
////    else if (header == "r"){
////      Serial.println("Message received.");
////    }
//}

String inputString_1, inputString_2;
String outputString_1, outputString_2;
double data_1, data_2;
String header;
byte RxedByte;

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
//                inputString_1 = read();
                data_1 = inputString_1.toDouble();
                Serial.println("Data 1 is received");
                break;
          case 'D': // save data 2
                inputString_2 = Serial.readStringUntil("\n");
                data_2 = inputString_2.toDouble();
                Serial.println("Data 2 is received");
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

String inputString;
float x;
void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void  loop() {
    receive_send_2_data_2();
}
