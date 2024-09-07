void setup() {
  pinMode(4, OUTPUT);
 pinMode(7, OUTPUT);
 pinMode(8, OUTPUT);
  
  // put your setup code here, to run once:

}

void loop() {
  // put your main code here, to run repeatedly:
  
digitalWrite (7,HIGH );      // It will turn on the led 
delay(1000);
digitalWrite (7,LOW);    // LOW means it will turn of the LED
delay(1000);              // Delay means it will stop for given time 
}
