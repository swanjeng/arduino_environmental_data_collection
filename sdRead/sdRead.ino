#include "SD.h"
#include "SPI.h"

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  SD.begin(10);
  while (Serial.available() <= 0);
  byte dummy = Serial.read();
  File f = SD.open("LOG3.txt");
  if (f) {
    while (f.available()) {
      Serial.write(f.read());
    }
    Serial.flush();
  }
  Serial.println();
  Serial.println("A");
  f.close();
  while (Serial.available() <= 0);
  dummy = Serial.read();
  SD.remove("LOG3.txt");
  File f1 = SD.open("LOG3.txt", FILE_WRITE);
  f1.close();
  delay(1000);
  Serial.println("done");
}

void loop() {
  // put your main code here, to run repeatedly:
  
}
