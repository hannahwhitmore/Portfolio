int red = 13;
int yellow = 12;
int green = 9;

void setup() {
pinMode(red, OUTPUT);
pinMode(yellow, OUTPUT);
pinMode(green, OUTPUT);
}

void loop() {
changeLights();
delay(500);

}
void changeLights(){
  digitalWrite(green, LOW);
  digitalWrite(yellow, HIGH);
  digitalWrite(red, LOW);
  delay(500);

  digitalWrite(yellow, LOW);
  digitalWrite(red, HIGH);
  digitalWrite(green, LOW);
  delay(500);


  digitalWrite(yellow, LOW);
  digitalWrite(red, LOW);
  digitalWrite(green, HIGH);
  delay(500);
  
}



