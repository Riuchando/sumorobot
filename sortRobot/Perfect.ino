#include <Servo.h> //Includes the Servo library
#include <Pixy.h>  //Includes the Pixy library 
#include <SPI.h>   //Includes the SPI library

Servo myservo; //Creates a servo object
Pixy pixy;     //Creates a pixy object 

int x;
const int stepper = 40;  //Creates the stepper variable and assigns to pin 40 on the Arduino
const int dir = 41;      //Creates the direction variable on the NEMA 23 and assigns it to pin 41 on the Arduino
const int rate = 4500;   //Creates the rate variable and assigns it the stepper motor speed
const int wait = 500;    //Creates the wait variable and assigns it the wait time between direction changes on the NEMA 23
const int angle1 = 637;  //Creates the angle1 variable and assigns it the angle between home position and the first sorting hole (in steps)
const int angle2 = 837;  //Creates the angle2 variable and assigns it the angle between home position and the second sorting hole (in steps)
const int angle3 = 1037; //Creates the angle3 variable and assigns it the angle between home position and the third sorting hole (in steps)
const int angle4 = 1237; //Creates the angle4 variable and assigns it the angle between home position and the fourth sorting hole (in steps)
const int angle5 = 1437; //Creates the angle5 variable and assigns it the angle between home position and the fifth sorting hole (in steps)
const int angle6 = 1637; //Creates the angle5 variable and assigns it the angle between home position and the sixth sorting hole (in steps)

boolean rot = HIGH;      //Creates the rot variable and assigns it  high for the NEMA 23

int linEnable = 30;      //Creates the linEnable variable and assigns it to pin 30 of the Arduino
int linMotor1 = 31;      //Creates the linMotor1 variable and assigns it to pin 31 of the Arduino
int linMotor2 = 32;      //Creates the linMotor2 variable and assigns it to pin 32 of the Arduino
boolean linDir = HIGH;   //Creates the linDir variable and assigns it high for the linear actuator
int linWait = 8000;      //Creates the linWait variable and assigns it the wait time for the linear actuator

int grab = 180;          //Creates the grab variable and assigns it to the open rotation angle of the servo
int drop = 0;            //Creates the drop variable and assigns it to the closed rotation angle of the servo

const int elevator = 35;
const int elevator_dir = 36;
int block_height = 35.32;
int radius = 13;
int lin_revolution = 2*3.1415*radius*2;
//also this int division you ass, this will always be 0
//int steps_per_block = block_height / lin_revolution * 180;
//JESUS CHRIST THIS THING GESTS STUCK, it rquires about 400
int steps_per_block = 400 ;
int prev; // this is the previous block from the pixy camera
int curr; // this is the current one

void setup() {                     
pinMode(stepper,OUTPUT);       //Declares stepper as an output 
pinMode(dir,OUTPUT);           //Declares dir as an output

pinMode(elevator, OUTPUT);
pinMode(elevator_dir, OUTPUT);

pinMode(linEnable, OUTPUT);    //Declares linEnable as an output
pinMode(linMotor1, OUTPUT);    //Declares linMotor1 as an output
pinMode(linMotor2, OUTPUT);    //Declares linMotor2 as an output
digitalWrite(linEnable, HIGH); //Declares linEnable as an output

Serial.begin(9600); //starts up serial monitor
myservo.attach(3);            //Attaches myservo to pin 3 on the Arduino
pixy.init();                   //Initializes Pixy camera
prev=getBlockSig();
}


void loop() {
  //delay(10000);
//   elevate(1000);
  //red(1);     //Calls the red() function
  /*
  red(1);     //Calls the red() function
  blue(1);    //Calls the blue() function
  green(1);   //Calls the green() function
  orange(1);  //Calls the orange() function
  purple(1);  //Calls the purple() function
  discard(1); //Calls the discard() function
  */
  //could simplify this to a busy wait, but I dunno
  
//  Serial.println(curr);
  gripper(1000);
  //gripper(0);
}
void pixyDrop(){
  curr=getBlockSig();
  //not sure if this is needed
 /*
  while(curr== prev){
    curr=getBlockSig();
  }
  */
  
  if(curr== 2){
      red(1);     //Calls the red() function
          Serial.println("RED");
  }
  else if( curr == 1){
      blue(1);    //Calls the blue() function
          Serial.println("BLUE");
  }
  else if(curr == 4 ){
      green(1);   //Calls the green() function
          Serial.println("GREEN");
  }
  
  /*else{
      //Mdiscard(1); //Calls the discard() function
          Serial.println("DISCARD");
  }*/
  
  
  
}
//input:Pixy is a global variable object
//this should get an image from the pixy, then determine it's color
//there should only be one object at a time
int getBlockSig(){
  //busy wait until blocks are detected, deprecated
 // while (!pixy.getBlocks());
  char buf[32]; 
  uint16_t blocks=pixy.getBlocks();
  if(blocks){
    
    for (int j=0; j<blocks; j++)
      {
        /*
        sprintf(buf, "  block %d: ", j);
        Serial.print(buf); 
        pixy.blocks[j].print();
        */
        //because the pixy hasn't been trained well, I think it SHOULD be about this size
        // I think I fixed this, by clearing the signatures
        if( pixy.blocks[j].height >50 && pixy.blocks[j].width >50){
            return pixy.blocks[j].signature;          
        }
      }
  }
   //should only detect one block
   return 0; // this is an error message, make sure if you are maintaining this that you take care of this properly

}


void stepMotor(int angle, boolean Dir) {  //Creates the two variable stepMotor function for controlling the NEMA 23
  digitalWrite(dir,Dir);                  //Writes high or low to the dir pin to determin direction of rotation
  for(x = 0; x < angle; x++) {            //Iterative loop for stepping to the angle specified by the angle variable
    digitalWrite(stepper,HIGH);           //Writes high to stepper pin
    delayMicroseconds(rate);              //Delays for the time specified by rate (in microseconds)
    digitalWrite(stepper,LOW);            //Writes low to the stepper in
    delayMicroseconds(rate);              //Delays for the time specified by rate (in microseconds)
  } 
  delay(wait);                            //Delays for the time specified by wait (in milliseconds)
}

void motorDir(boolean t) {                //Creates the single variable motorDir function for switching direction of the linear actuator
  digitalWrite(linMotor1, t);             //Writes high or low based on the input variable t to the linMotor1 pin
  digitalWrite(linMotor2, !t);            //Writes the oppossite value of input variable t to the linMotor2 pin
  delay(linWait);                         //Delays for the time specified by linWait (in milliseconds)
}

void elevate(int p) {
  digitalWrite(elevator_dir, HIGH);
    for(x = 0; x < p; x++) {      
    Serial.println(x);      
    digitalWrite(elevator,HIGH);           
    delayMicroseconds(rate);              
    digitalWrite(elevator,LOW);            
    delayMicroseconds(rate);              
}
}

void gripper(int state) {                 //Creates the single variable gripper function for opening and closing the end effector
  myservo.write(state);                   //Writes the input variable state to the servo pin
  delay(1000);                            //Delays for 1000 milliseconds
}

void red(boolean a) {                              //Creates the red function for extending, gripping and rotating to the first sorting hole
  Serial.println("RED");
  gripper(drop);
  motorDir(linDir);
  gripper(grab);
  stepMotor(angle1,rot);
  gripper(drop);
  motorDir(!linDir);
  elevate(steps_per_block);
  stepMotor(angle1,!rot);
  
}

void blue(boolean b) {                              //Creates the blue function for extending, gripping and rotating to the second sorting hole
  Serial.println("BLUE");
  gripper(drop);
  motorDir(linDir);
  gripper(grab);
  stepMotor(angle2,rot);
  gripper(drop);
  motorDir(!linDir);
  elevate(steps_per_block);
  stepMotor(angle2,!rot);
}

void green(boolean c) {      //Creates the green function for extending, gripping and rotating to the third sorting hole
  Serial.println("GREEN");
  gripper(drop);
  motorDir(linDir);
  gripper(grab);
  stepMotor(angle3,rot);
  gripper(drop);
  motorDir(!linDir);
  elevate(steps_per_block);
  stepMotor(angle3,!rot);
}

void orange(boolean d) {                           //Creates the orange function for extending, gripping and rotating to the fourth sorting hole
  gripper(drop);
  motorDir(linDir);
  gripper(grab);
  stepMotor(angle4,rot);
  gripper(drop);
  motorDir(!linDir);
  elevate(steps_per_block);
  stepMotor(angle4,!rot);
}

void purple(boolean e) {                            //Creates the red function for extending, gripping and rotating to the fifth sorting hole
  Serial.println("PURPLE");
  gripper(drop);
  motorDir(linDir);
  gripper(grab);
  stepMotor(angle5,rot);

  gripper(drop);
  motorDir(!linDir);
  elevate(steps_per_block);
  stepMotor(angle5,!rot);
}

void discard(boolean f) {                            
    Serial.println("DISCARD");
  gripper(drop);
  motorDir(linDir);
  gripper(grab);
  stepMotor(angle6,rot);
  gripper(drop);
  motorDir(!linDir);
  elevate(steps_per_block);
  stepMotor(angle6,!rot);
}
