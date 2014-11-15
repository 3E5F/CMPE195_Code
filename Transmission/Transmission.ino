/* 
This code is for putting together the 32-bit message for transmission over serial
*/
char bytes[4];

uint32_t outgoing_message;
void setup(){
	Serial.begin(9600);
	bytes[0] = 0x98;
	bytes[1] = 0x76;
	bytes[2] = 0x54;
	bytes[3] = 0x32;
}

void loop (){
	outgoing_message = 0x00000000;
	outgoing_message |= bytes[0];
	outgoing_message = outgoing_message<<8;
	outgoing_message |= bytes[1];
	outgoing_message = outgoing_message<<8;
	outgoing_message |= bytes[2];
	outgoing_message = outgoing_message<<8;
	outgoing_message |= bytes[3];

	Serial.println(outgoing_message, HEX);
	delay(1000);
}