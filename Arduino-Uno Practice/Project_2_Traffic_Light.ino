void setup() {
  
  
  pinMode(4, OUTPUT);
 pinMode(7, OUTPUT);
 pinMode(8, OUTPUT);
  
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  
digitalWrite (4,HIGH );      // It will turn on the led 
delay(1000);
digitalWrite(4,LOW);

digitalWrite (7,HIGH);    // LOW means it will turn of the LED
delay(1000);   
digitalWrite(7,LOW);

digitalWrite (8,HIGH);    // LOW means it will turn of the LED
delay(1000); 

  digitalWrite(8,LOW);
}
