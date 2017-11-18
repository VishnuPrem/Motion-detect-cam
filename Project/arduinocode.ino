//Arduino code to receive data through serial communication and control servo
#include<Servo.h>

Servo s;
int pos=135;

void setup()
  { 
    s.attach(9);
    Serial.begin(9600);
    s.write(135);
  
  }

void loop()
  {  
    if(Serial.available())
      { int num=Serial.read();
 
        if (num==49 && pos>89)          
            pos=pos-10;
           
        else if (num==50 && pos<181)          
            pos=pos+10;
            

        s.write(pos);
        delay(15);
  
      }    
  
  }

