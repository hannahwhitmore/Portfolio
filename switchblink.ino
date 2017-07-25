int [] outputs = [0,1,2]
void setup() {
  pinMode(0, OUTPUT);
  pinMode(1, OUTPUT);
  pinMode(2, OUTPUT);
}

void loop() {
  digitalWrite(0, HIGH);
  delay(100);
  digitalWrite(0, LOW);
  delay(100);
  digitalWrite(1, HIGH);
  delay(100);
  digitalWrite(1, LOW);
  delay(100);
  digitalWrite(2, HIGH);
  delay(100);
  digitalWrite(2, LOW);
  delay(100);

}
