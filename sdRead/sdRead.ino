#include "SD.h"
#include "SPI.h"
#define FILENAME "your file name.txt"

void setup() {
  Serial.begin(115200);
  SD.begin(10);

  // Wait for the Python program to be ready 
  while (Serial.available() <= 0);
  byte dummy = Serial.read();

  // Send the content of the file to the Python program
  File f = SD.open(FILENAME);
  if (f) {
    while (f.available()) {
      Serial.write(f.read());
    }
    Serial.flush();
  }
  Serial.println();
  Serial.println("A"); // EOF signal
  f.close();

  // Wait for the Python program to send "clear file" signal
  while (Serial.available() <= 0);
  dummy = Serial.read();

  // clear the file
  SD.remove(FILENAME);
  File f1 = SD.open(FILENAME, FILE_WRITE);
  f1.close();
  delay(1000);
  Serial.println("done");
}

void loop() {
}
