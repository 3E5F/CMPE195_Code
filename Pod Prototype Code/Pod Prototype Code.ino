/*
  Wireless Testing - Remote Control
  As user inputs commands into terminal -> xBee, c-controller (containing this code) will
  receive the commands, which are WASD and transmit relative hex values to the m-controller
*/

#include <Wire.h>

int incomingByte;      // a variable to read incoming serial data into
int ID;   //ID of the pod - 1, 2, 3
const int frontSensor = 7; // front sensor
const int leftSensor = 5; // left sensor
const int rightSensor = 3; // right sensor
long front, left, right;  //used for output to serial - converted to inches



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

enum MESSAGETYPE{
  MainHub_Path_InitialPathMsg   = 0x0,
  Pod_Path_ConfirmPathMsg       = 0x1,
  MainHub_Path_GoPathMsg        = 0x2,
  Pod_Path_ConfirmGoMsg         = 0x3,
  MainHub_Status_RequestStatus  = 0x4,
  Pod_Status_StatusInfo         = 0x5,
};





void setup()
{
  Serial.begin(9600);
  Wire.begin();
  pinMode(frontSensor, INPUT);
  pinMode(leftSensor, INPUT);
  pinMode(rightSensor, INPUT);

  FRONTSPEED front_speed;
  DIRECTION direction;
  MESSAGETYPE message_type;
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
    if(front < 24 && front > 12){ // if between 1-2 feet, then go at MEDIUM speed
      // Slow slow slow
        front_speed = SLOW;
      }
    else if(front <12 || right < 8 || left < 8 ){ // if object in front is less than 1 feet, then STOP
        //STAHP
        front_speed = HALT;
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

}

void loop()
{
  updateMotors();
  if (Serial.available() > 0) { 
  // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();

    if (incomingByte == 's') {    // stop
      direction = STOP;
    	
      //Serial.println("Stopped");
    } 
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'w') {    // go forward at slow speed
      direction = FORWARD;
      //Serial.println("Forward 1");
    }
    if (incomingByte == 'a') {    // turn left
    	direction = LEFT;
      //Serial.println("Turning left");
    }
    if (incomingByte == 'd') {    // turn left
    	direction = RIGHT;
      //Serial.println("Turning right");
    }
  }
}
/*
uint32_t x = 0xFFFFFF00; // 32 bits
void loop(){
  Serial.println( x );
  delay(1);
  x++;
}
*/