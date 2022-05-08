#include <Wire.h>
#include <LCD.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd (0x27, 2, 1, 0, 4, 5, 6, 7);

int DIR_1 = 50;
int DIR_2 = 51;
int option;
#define PIN_BUTTON A0

void setup() {
  
  Serial.begin(9600);
  pinMode(DIR_1, OUTPUT);
  pinMode(DIR_2, OUTPUT);

  lcd.setBacklightPin(3,POSITIVE);
  lcd.setBacklight(HIGH);
  lcd.begin(16, 2);
  lcd.clear();
  
}

void loop() {
  
  int Value_Button;
  Value_Button = analogRead(PIN_BUTTON);
  delay(1000);
  Serial.println(Value_Button);
  
  lcd.clear();
  lcd.setCursor(2, 0);
  lcd.print("Please Press");
  lcd.setCursor(3, 1);
  lcd.print("The Button");
  
  if(Serial.available() > 0)
  option = Serial.read();
  {
    if (option == 'M' and option != 'O' and option != 'C')
    {
       lcd.clear();
       lcd.setCursor(1, 0);
       lcd.print("Please Look at");
       lcd.setCursor(3, 1);
       lcd.print("The Camera");
       delay(2700);
    }
    if(option == 'O')
    {
      lcd.clear();
      lcd.setCursor(5, 0);
      lcd.print("WELCOME");
      for (int i = 0; i<3; i++)
      {
        digitalWrite(DIR_1, HIGH);
        delay(270); 
      }
      digitalWrite(DIR_1, LOW);
      digitalWrite(DIR_2, LOW);
      
      delay(3000);
      lcd.clear();
      lcd.setCursor(5, 0);
      lcd.print("CAUTION");

      for (int i = 0; i<4; i++)
      {
        digitalWrite(DIR_2, HIGH);
        delay(400); 
      }
      digitalWrite(DIR_1, LOW);
      digitalWrite(DIR_2, LOW);
      option = 'S';
            
    }
    if(option == 'C')
    {
      for(int i = 0; i<5; i++)
      {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("PLEASE  PUT YOUR");
        lcd.setCursor(6, 1);
        lcd.print("MASK");
        delay(500);
      }
      option = 'S';
    }
  }
}
