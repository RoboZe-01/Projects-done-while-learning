



const int my= 5;       // This is a consatant qualifier  
bool myBool=555 ;
char mychar=65;                                           // It is not good practoce to use too many global variable 
bool myBool1=LOW;
int myGlobalVariable=666;     // This is a global variable    // Comparison operator : == , <= ,>= , <,> ,!= 


void setup()
{
float heyFloat=13.26;
char LocalVariable=90;

//Serial.begin(9600); // staring letter of this function is capital 
//Serial.println(myBool);       // used to print value in the variable 
//Serial.println(myBool1);
//Serial.println(mychar+5);
//Serial.println();
//Serial.println("printing in Global variable");
//Serial.println( myGlobalVariable);
//Serial.println("Printing from local variable");
//Serial.println( myGlobalVariable);
//Serial.println( my );
}

void loop (){
  static int xyz=0;
  xyz++;
  Serial.println(xyz);
  delay(100);

}
