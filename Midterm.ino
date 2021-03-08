/* this is the code to go with python code for part 5 of midterm exam */

// Delcaring all my varaibles and pin i will use in the function

int LedPin8 = 8;
int LedPin9 = 9; 
int LedPin10 = 10; 
int LedPin11 = 11; 
int Button1 = 2;
int Button2 = 3;
int Button3 = 4;
int Button4 = 5;
int Pot1;
int Pot2;
int Pot3;
int Pot4;
int button_val;
int button_val1;
int button_val2;
int button_val3;

/*     Setting up all my pins as inputs and outputs to control various components      */

void setup() 
{
  Serial.begin(9600);
  pinMode(LedPin8, OUTPUT);    //Setting my LED pins as outputs 
  pinMode(LedPin9, OUTPUT);
  pinMode(LedPin10, OUTPUT);
  pinMode(LedPin11, OUTPUT);
  pinMode(Button1, INPUT);    // Setting my Buttos pins as inputs
  pinMode(Button2, INPUT);
  pinMode(Button3, INPUT);
  pinMode(Button4, INPUT);
  
}

/* the main loop that will run all my code and functions */

void loop() 
{
  if (Serial.available()==0)        // Waiting for the serial monitor to recieve information from the program
  {
    String data = Serial.readStringUntil('\n');   // reading the string printed to the serial monitor 
    if (data == "Pin8") // reading and comparing the string in the monitor  
    {
      digitalWrite(LedPin8, HIGH); // if true Toggle Pin8 to turn on for 2 seconds
      delay(2000);                
      digitalWrite(LedPin8, LOW);
      
    }
    else if (data == "Pin9")   //else if the string reads Pin9 to toggle this led on for 2 seconds
    {
      digitalWrite(LedPin9, HIGH);
      delay(2000);
      digitalWrite(LedPin9, LOW);
      
    }
    else if (data == "Pin10") //else if the string reads Pin10 to toggle this led on for 2 seconds
    {
      digitalWrite(LedPin10, HIGH);
      delay(2000);
      digitalWrite(LedPin10, LOW);
      
    }
    else if (data == "Pin11") //else if the string reads Pin11 to toggle this led on for 2 seconds
    {
      digitalWrite(LedPin11, HIGH);
      delay(2000);
      digitalWrite(LedPin11, LOW);
      
    }
    /* This code will run and print to the serial monitor in a specific format.
    This will allow the python program to collect the information and parse it
    apart and store the correct values in the correct location */
    else    // while no if statement is triggered the following code will contiunally loop
    {
      Pot1 = analogRead(A0);       // Storing analog values in variables 
      Pot2 = analogRead(A1);
      Pot3 = analogRead(A2);
      Pot4 = analogRead(A3);
      button_val = digitalRead(Button1);  // storing the value of digital pins in vars
      button_val1 = digitalRead(Button2);
      button_val2 = digitalRead(Button3);
      button_val3 = digitalRead(Button4);
      //all the print function below are seperated but a "," for the python program to read it correctly
      Serial.print(Pot1);        
      Serial.print(",");
      Serial.print(Pot2);
      Serial.print(",");
      Serial.print(Pot3);
      Serial.print(",");
      Serial.print(Pot4);
      Serial.print(",");
      Serial.print(button_val);
      Serial.print(",");
      Serial.print(button_val1);
      Serial.print(",");
      Serial.print(button_val2);
      Serial.print(",");
      // printing the final value as a line so the next set of info in a new line
      Serial.println(button_val3);
      Serial.flush();
    }
    
  }
    
  
}
