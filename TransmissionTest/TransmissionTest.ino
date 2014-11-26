/* 
This code is for putting together the 32-bit message for transmission over serial
*/
byte bytes[4];


uint32_t outgoing_message = 0x00000000;
void setup(){
	Serial.begin(9600);
	bytes[0] = 0xC0;
	bytes[1] = 0x00;
	bytes[2] = 0x00;
	bytes[3] = 0x00;
}

void loop (){
	outgoing_message = 0x00000000;
	bytes[0] = 0xC0;
	Serial.write(bytes,4);
	delay(3000);
	
	outgoing_message = 0x00000000;
	bytes[0] = 0xC2;
	//Serial.print(outgoing_message);
	Serial.write(bytes,4);
	delay(3000);

	outgoing_message = 0x00000000;
	bytes[0] = 0xC4;
	//Serial.print(outgoing_message);
	Serial.write(bytes,4);
	delay(3000);
}