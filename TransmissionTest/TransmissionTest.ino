/* 
This code is for putting together the 32-bit message for transmission over serial
*/
char bytes[4];


uint32_t outgoing_message = 0x00000000;
void setup(){
	Serial.begin(9600);
	bytes[0] = 0x40;
	bytes[1] = 0xFF;
	bytes[2] = 0xFF;
	bytes[3] = 0xFF;
}

void loop (){
	outgoing_message = 0x40000000;
	Serial.println(outgoing_message, HEX);

	delay(2000);
	outgoing_message = 0x42000000;
	Serial.println(outgoing_message, HEX);

	delay(2000);
	outgoing_message = 0x44000000;
	Serial.println(outgoing_message, HEX);
	
	delay(2000);
}