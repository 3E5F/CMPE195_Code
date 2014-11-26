/*
  Wireless Testing - Remote Control
  As user inputs commands into terminal -> xBee, c-controller (containing this code) will
  receive the commands, which are WASD and transmit relative hex values to the m-controller
*/

#include <Wire.h>
#include <stdio.h>

int ID = 0x3;   //ID of the pod - 1, 2, 3
uint32_t incomingMsg;      // a variable to read incoming serial data into
const int frontSensor = 7; // front sensor
const int leftSensor = 5; // left sensor
const int rightSensor = 3; // right sensor
long front, left, right;  //used for output to serial - converted to inches
char bytes[11];


enum PODID{
  Pod1 = 0x01,
  Pod2 = 0x02,
  Pod3 = 0x03,
};

enum DIRECTION{
  FORWARD = 'w',
  LEFT    = 'a',
  RIGHT   = 'd',
  STOP    = 's',
};

enum FRONTSPEED{
  SLOW = 0x11,
  FAST = 0x13,
  HALT = 0x00,
};

enum RIGHTSPEED{
  R_STOP = 0x14,
  R_SLOW = 0x16,
  R_FAST = 0x18,
};

enum LEFTSPEED{
  L_STOP = 0x15,
  L_SLOW = 0x17,
  L_FAST = 0x19,
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
RIGHTSPEED right_speed;
LEFTSPEED left_speed;
DIRECTION direction = STOP;
MESSAGETYPE message_type;
PODID PodID;

DIRECTION commands[7] = {FORWARD, RIGHT, LEFT, RIGHT, LEFT, FORWARD, STOP};
int instruction=0;

int R_HALL = 8;
int L_HALL = 9;
int rHall = 0;
int lHall = 0;
int set = 0;

void setup()
{
  Serial.begin(9600);
  Wire.begin();
  pinMode(frontSensor, INPUT);
  pinMode(leftSensor, INPUT);
  pinMode(rightSensor, INPUT);
  pinMode(R_HALL, INPUT);
  pinMode(L_HALL, INPUT);
  PodID = Pod1;
}

void updateMotors(){
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
    if(front <12 || right < 8 || left < 8 )
      left_speed = L_STOP;
    else
      left_speed = L_SLOW;

    Wire.beginTransmission(4);
    Wire.write(left_speed);
    Wire.endTransmission();  
  }

  else if(direction == RIGHT){
    if(front <12 || right < 8 || left < 8 )
      right_speed = R_STOP;
    else
      right_speed = R_SLOW;
    Wire.beginTransmission(4);
    Wire.write(right_speed);
    Wire.endTransmission();
  }
  else
    Serial.print("ERROR\n");
}

void checkHalls(){
  rHall = digitalRead(R_HALL);
  lHall = digitalRead(L_HALL);

  if (rHall == 0 || lHall == 0){
    if (set == 0){
      direction = commands[instruction];
      set = 1;
    }
  }
  else if(rHall == 1 && lHall ==1){
    if(set == 1){
      set = 0;
      instruction++;
    }
  }
}

void loop()
{
  updateMotors();
  checkHalls();
}