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


void setup() 
{
  Serial.begin(9600);
  pinMode(LedPin8, OUTPUT);
  pinMode(LedPin9, OUTPUT);
  pinMode(LedPin10, OUTPUT);
  pinMode(LedPin11, OUTPUT);
  pinMode(Button1, INPUT);
  pinMode(Button2, INPUT);
  pinMode(Button3, INPUT);
  pinMode(Button4, INPUT);
  
}

void loop() 
{
  if (Serial.available()==0)
  {
    String data = Serial.readStringUntil('\n');
    if (data == "Pin8") // Toggle Pin8 to turn on
    {
      digitalWrite(LedPin8, HIGH);
      delay(2000);
      digitalWrite(LedPin8, LOW);
      
    }
    else if (data == "Pin9") 
    {
      digitalWrite(LedPin9, HIGH);
      delay(2000);
      digitalWrite(LedPin9, LOW);
      
    }
    else if (data == "Pin10") 
    {
      digitalWrite(LedPin10, HIGH);
      delay(2000);
      digitalWrite(LedPin10, LOW);
      
    }
    else if (data == "Pin11") 
    {
      digitalWrite(LedPin11, HIGH);
      delay(2000);
      digitalWrite(LedPin11, LOW);
      
    }
    else
    {
      Pot1 = analogRead(A0);
      Pot2 = analogRead(A1);
      Pot3 = analogRead(A2);
      Pot4 = analogRead(A3);
      button_val = digitalRead(Button1);
      button_val1 = digitalRead(Button2);
      button_val2 = digitalRead(Button3);
      button_val3 = digitalRead(Button4);
      digitalRead(Button2);
      digitalRead(Button3);
      digitalRead(Button4);
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
      Serial.println(button_val3);
      Serial.flush();
    }
    
  }
    
  
}
