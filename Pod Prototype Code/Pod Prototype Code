/*
  Wireless Testing - Remote Control
  As user inputs commands into terminal -> xBee, c-controller (containing this code) will
  receive the commands, which are WASD and transmit relative hex values to the m-controller
*/

#include <Wire.h>
int incomingByte;      // a variable to read incoming serial data into
int ID;

enum DIRECTION{
  FORWARD = 'w',
  LEFT = 'a',
  RIGHT = 'd',
  STOP = 's',
};

enum FRONTSPEED{
  SLOW = 0x11,
  FAST = 0x13,
  HALT = 0x00,
};

const int frontSensor = 7; // front sensor
const int leftSensor = 5; // left sensor
const int rightSensor = 3; // right sensor

long pulseFront, pulseLeft, pulseRight;
long front, left, right;  //used for output to serial - converted to inches



void setup()
{
  Serial.begin(9600);
  Wire.begin();
  pinMode(frontSensor, INPUT);
  pinMode(leftSensor, INPUT);
  pinMode(rightSensor, INPUT);
}

FRONTSPEED front_speed;
DIRECTION direction;

void checkSensors(){
  front = (pulseIn(frontSensor, HIGH))/146;
  if (direction == FORWARD){  
    if(front < 24 && front > 12){ // if between 1-2 feet, then go at MEDIUM speed
      // Slow slow slow
        front_speed = SLOW;
      }

    else if(front <12){ // if object in front is less than 1 feet, then STOP
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
}

void loop()
{
  checkSensors();
  if (Serial.available() > 0) { 
  // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();

    if (incomingByte == 's') {    // stop
      direction = STOP;
    	Wire.beginTransmission(4);
    	Wire.write(0x00);
    	Wire.endTransmission();
      //Serial.println("Stopped");
    } 
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'w') {    // go forward at slow speed
      direction = FORWARD;
    	Wire.beginTransmission(4);
    	Wire.write(front_speed);
    	Wire.endTransmission();
      //Serial.println("Forward 1");
    }
    if (incomingByte == 'e') {    // go forward at faster speed
    	Wire.beginTransmission(4);
    	Wire.write(0x13);
    	Wire.endTransmission();
      //Serial.println("Forward 2");
    }
    if (incomingByte == 'a') {    // turn left
    	direction = LEFT;
      Wire.beginTransmission(4);
    	Wire.write(0x14);
    	Wire.endTransmission();
      //Serial.println("Turning left");
    }
    if (incomingByte == 'd') {    // turn left
    	direction = RIGHT;
      Wire.beginTransmission(4);
    	Wire.write(0x15);
    	Wire.endTransmission();
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