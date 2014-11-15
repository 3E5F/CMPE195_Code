/*
This code is for parsing a 32-bit uint32_t message into four bytes
and displaying those four bits in hexadecimal format using the print().
*/

unsigned char bytes[4];
uint32_t incoming_message = 0x12345678;

void setup(){
	Serial.begin(9600);
}

void loop(){	
	Serial.println((incoming_message >> 24)& 0xFF);
	Serial.println((incoming_message >> 16)& 0xFF);
	Serial.println((incoming_message >> 8)& 0xFF);
	Serial.println((incoming_message)& 0xFF);
	Serial.println();

// Splitting the message into character bytes
	bytes[0] = (incoming_message >> 24) & 0xFF;
	bytes[1] = (incoming_message >> 16) & 0xFF;
	bytes[2] = (incoming_message >> 8) & 0xFF;
	bytes[3] = (incoming_message >> 0) & 0xFF;

// HEX is a setting for Arduino's print() to display as HEX val
	Serial.println(bytes[0], HEX);	
	Serial.println(bytes[1], HEX);
	Serial.println(bytes[2], HEX);
	Serial.println(bytes[3], HEX);
	Serial.println();

	delay(1000);
}