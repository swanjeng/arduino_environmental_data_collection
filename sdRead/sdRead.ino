#include "SD.h"
#include "SPI.h"

void setup() {
  Serial.begin(9600);
  SD.begin(10);
  while (Serial.available() <= 0);
  byte dummy = Serial.read();
  File f = SD.open("LOG3.txt");
  if (f) {
    while (f.available()) {
      Serial.write(f.read());
    }
  }
  f.close();
  while (Serial.available() <= 0);
  dummy = Serial.read();
  SD.remove("FILENAME.txt"); // change FILENAME to your file name
  File f1 = SD.open("FILENAME.txt", FILE_WRITE); // should be the same as the line above
  f1.close();
  Serial.println("done");
}

void loop() {
}
