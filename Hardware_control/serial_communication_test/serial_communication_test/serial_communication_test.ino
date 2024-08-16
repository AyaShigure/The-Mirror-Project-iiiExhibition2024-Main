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




String inputString;
float x;
void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void  loop() {
  if (Serial.available() > 0) {
    inputString = Serial.readStringUntil('\n');
    x = inputString.toFloat();
    Serial.print("Received Float: ");
    Serial.println(x + 1.);
  }
}
