#include <SPI.h>
#include <SD.h>
#include "sensorValue.h"
#include "wifi.h"
#include "ledMat.h"
#define btn 3

byte isCollectingData = 0;
long lastDataCollectTime;
int lastButtonState, buttonState;
long lastDebounceTime;
String dataStr = "";

void toggleState(int pin) {
  int reading = digitalRead(pin);
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }
  if ((millis() - lastDebounceTime) > 50) {
    if (reading != buttonState) {
      buttonState = reading;

      if (buttonState == LOW) {
        isCollectingData = (isCollectingData ? 0 : 1);
        if (isCollectingData == 1) {
          matrix.renderBitmap(f1, 8, 12);
          File dataFile = SD.open(fileName, FILE_WRITE);
          dataFile.println("start");
          dataFile.close();
        } else matrix.renderBitmap(f0, 8, 12);
      }
    }
  }

  
  lastButtonState = reading;
}

void setup() {
  Serial.begin(9600);
  delay(1000);
  SD.begin(CS);
  sdState = 1;
  initSensors();
  initWifi();
  matrix.begin();
  matrix.renderBitmap(f0, 8, 12);
  showStateOffHtml();
  pinMode(btn, INPUT_PULLUP);
  lastDataCollectTime = millis();
  lastButtonState = HIGH;
}

void loop() {
  toggleState(btn);
  if (isCollectingData && millis() - lastDataCollectTime >= interval) {
    dataStr = getCurrTime() + " " + dhtdata() + " " + pmsdata() + " " + bmedata();
    File dataFile = SD.open(fileName, FILE_WRITE);
    if (dataFile) {
      dataFile.println(dataStr);
      dataFile.close();
      Serial.println(dataStr);
      clientPrintValues(dataStr);
      sdState = 1;
    } else {
      Serial.println("SD error");
      sdState = 0;
    }
    lastDataCollectTime = millis();
  }
  if (isCollectingData && dataStr != "") clientPrintValues(dataStr);
  if (!isCollectingData) showStateOffHtml();
}
