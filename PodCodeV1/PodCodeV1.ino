/*
  Wireless Testing - Remote Control
  As user inputs commands into terminal -> xBee, c-controller (containing this code) will
  receive the commands, which are WASD and transmit relative hex values to the m-controller
*/
#include <Wire.h>
#include <stdio.h>

#define DEBUG

int ID = 0x3;   //ID of the pod - 1, 2, 3
uint32_t incomingMsg;      // a variable to read incoming serial data into
uint32_t outgoingValue;
uint32_t payload = 0x00000000; // upper byte should not be used - should be all 0's
const int frontSensor = 7; // front sensor
const int leftSensor = 5; // left sensor
const int rightSensor = 3; // right sensor
long front, left, right;  //used for output to serial - converted to inches
char incomingCharArray[11];
char outputBuff[11];

enum PODID{
  Pod1 = 0x1,
  Pod2 = 0x2,
  Pod3 = 0x3,
};

enum DIRECTION{
  FORWARD = 0x3,
  LEFT    = 0x2,
  RIGHT   = 0x1,
  STOP    = 0x0,
};

enum FRONTSPEED{
  SLOW = 0x11,
  FAST = 0x13,
  HALT = 0x00,
};

enum MESSAGETYPE{
  MainHub_Path_InitialPathMsg   = 0x00,
  Pod_Path_ConfirmPathMsg       = 0x01,
  MainHub_Path_GoPathMsg        = 0x02,
  Pod_Path_ConfirmGoMsg         = 0x03,
  MainHub_Status_RequestStatus  = 0x04,
  Pod_Status_StatusInfo         = 0x05,
  EmergencyShutDown             = 0x0F,
};

FRONTSPEED front_speed;
DIRECTION direction = STOP;
MESSAGETYPE message_type;

//===================== USER DEFINED SECTION =================
PODID PodID;
//=================== END USER DEFINED SECTION ===============

void setup(){
  /*
  This function gets executed once when the Arduino powers up/restarts.
  Serial communication is initialized to the xBee module mounted using
  (XBEE/USB) switch on the xBee shield mounted directly on the Arduino.
  Pins connected to the sensors are set up as inputs here.
  =====================================================================
  User MUST define the PodID here.
  If DEBUG at the top of the code is not commented out, the debug
  messages will show.
  */
  Serial.begin(9600);
  Wire.begin();
  pinMode(frontSensor, INPUT);
  pinMode(leftSensor, INPUT);
  pinMode(rightSensor, INPUT);
  Serial.write("\n\r============= Setup Initialized =============\n\r");
  PodID = Pod1;
  
  #ifdef DEBUG
    Serial.write("=============== Debug Mode On ===============\n\r");
    if (PodID == Pod1)
      Serial.write("PodID = 1\n\r");
    else if (PodID == Pod2)
      Serial.write("PodID = 1\n\r");
    else if (PodID == Pod3)
      Serial.write("PodID = 1\n\r");
    else
      Serial.write("PodID not Initialized");
  #endif
}

void updateMotors(){
  /*
   This function updates the motors. When there is a change in direction
   or sensor values, this function will decide what the motors will do.
   This section of code computes the right values to send to the motor
   controller via I2C interface.
  */
  front = (pulseIn(frontSensor, HIGH))/146;
  right = (pulseIn(rightSensor, HIGH))/146;
  left  = (pulseIn(leftSensor, HIGH))/146;
  
  if(direction == STOP){
    Wire.beginTransmission(4);
    Wire.write(0x00);
    Wire.endTransmission();
  }

  else if (direction == FORWARD){  
    if(front <12 || right < 8 || left < 8 ){ // if object in front is less than 1 feet, then STOP
        //STAHP
        front_speed = HALT;
      }
    else if(front < 24 && front > 12){ // if between 1-2 feet, then go at MEDIUM speed
      // Slow slow slow
        front_speed = SLOW;
      }
    else{
        //go full speed ahead - well not really full speed
        front_speed = FAST;
      }
    Wire.beginTransmission(4);
    Wire.write(front_speed);
    Wire.endTransmission();
  }

  else if(direction == LEFT){
    Wire.beginTransmission(4);
    Wire.write(0x14);
    Wire.endTransmission();
  }

  else if(direction == RIGHT){
    Wire.beginTransmission(4);
    Wire.write(0x15);
    Wire.endTransmission();
  }
  else
    Serial.print("ERROR\n");
}

void checkForMessage(){
  /*
  This function simply checks for any messages that have been broadcasted.
  If the first two bits match the PodID, the incoming 32-bit number in
  string format will be then converted to an actual uint32_t and pass
  control over to checkAndSet_Msg().
  If the first two bits don't match, then the function does not do
  anything.
  */
  if (Serial.available() > 0) { // Receive Serial Message
    Serial.readBytes(incomingCharArray, 10);
    incomingMsg = 0;
    #ifdef DEBUG
    Serial.write("\r\nHit\r\n");
    #endif
  //This 'for' loop is to transform the incoming message from character array into a number.
    for (int i =0 ; i<11; i++){ //Buffer size = 11 bytes 
      if (incomingCharArray[i]==NULL)
        break;
      else
        incomingMsg = (incomingMsg*10)+(incomingCharArray[i] - '0');
    }
    for (int i = 0; i<11; i++){ //clear buffer that contains characters received from wireless broadcast
      incomingCharArray[i]=NULL;
    }
    if (((incomingMsg >> 28) & 0xF) == (PodID << 2)){  // check for receiver ID - if it matches PodID then execute.
      //Serial.write("Received Matching Code\n\r");
      checkAndSet_Msg(incomingMsg);
    }
  }
}

void checkAndSet_Msg(uint32_t incomingMsg){
  /*
  This function takes an incoming message and determines what to do with it.
  Since at this point we know the incoming message is meant for this
  particular pod, we need to see what kind of message it is by the type of
  message sent in that packet. These cases belong to dedicated 'conversations'
  stated in our Wireless Message Format document.
  */
  if(((incomingMsg >> 24) & 0x0F) == MainHub_Path_InitialPathMsg){  // initial path message coming from main hub
    #ifdef DEBUG
    Serial.write("Received MainHub_Path_InitialPathMsg\n\r");
    #endif
    message_type = Pod_Path_ConfirmPathMsg;
    payload = incomingMsg & 0x00FFFFFF;
    //outgoingValue = 285274352;
  }
  else if(((incomingMsg >> 24) & 0x0F) == MainHub_Path_GoPathMsg){       // "GO" path message coming from main hub
    #ifdef DEBUG
    Serial.write("Received MainHub_Path_GoPathMsg\n\r");
    #endif
    message_type = Pod_Path_ConfirmGoMsg;
  }
  else if(((incomingMsg >> 24) & 0x0F) == MainHub_Status_RequestStatus){ // "Request Status" message coming from main hub
    #ifdef DEBUG
    Serial.write("Received MainHub_Status_RequestStatus\n\r");
    #endif
    message_type = Pod_Status_StatusInfo;
  }
  else if(((incomingMsg >> 24) & 0x0F) == EmergencyShutDown){    // EmergencyShutDown
    #ifdef DEBUG
    Serial.write("Received Emergency Shut Down Code!\n\r");
    #endif
    direction = STOP;
  }
  else{
    Serial.write("Unknown\n\r");
  }
  packageAndSendMsg();  
}

void packageAndSendMsg(){
  /*
  By this point, the message_type and payload for the output should
  be already set. This function puts Receiver (main hub), Sender
  (PodID), message_type, and payloed together and broadcasts at the
  end.
  =================================================================
  byte array "sector" is used to assemble the 32-bit message into
  four 8-bit 'containers' before being combined into an integer,
  which is then transformed into a character array that is shipped
  out the broadcaster. Because of some limitations of the Arduino,
  this method proved to work for us. There is probably a better way
  of doing this.
  */
  byte sector[4];
  sector[0] = (PodID << 4) & 0xF0;  //(PodID<<4)& message_type;
  sector[0] |= (message_type & 0x0F); // set message Type
  sector[1] = (payload >> 16); 
  sector[2] = (payload >> 8) | 0x00; //(payload >> 8) & 0xFF;
  sector[3] = payload | 0x00; //| (payload & 0xFF);
    
  outgoingValue = 0x00000000; //clearing outgoingMsg
  outgoingValue |= sector[0];
  outgoingValue = outgoingValue<<8;
  outgoingValue |= sector[1];
  outgoingValue = outgoingValue<<8;
  outgoingValue |= sector[2];
  outgoingValue = outgoingValue<<8;
  outgoingValue |= sector[3];
  
  /* We really don't care about 'out' but we use it only to fill the outputBuff C-string */
  String out;
  out += outgoingValue;
  out.toCharArray(outputBuff,11);
  Serial.write(outputBuff);
}

void loop(){
  #ifdef DEBUG
    Serial.write("Loop!\n\r");
  #endif
  
  /*
  Note: if there is a disconnection from the pins and the sensors,
  updateMotors() will lag the entire system by 3-4 seconds. If
  they aren't connected, it is highly recommended to comment this
  function out before running.
  */
  //updateMotors(); 
  Serial.flush(); // Sittin' on the toilet!
  checkForMessage();
}