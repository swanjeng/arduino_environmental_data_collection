#include <SPI.h>
#include <SD.h>
#include "sensorValue.h"
#include "ledMat.h"
#include "wifi.h"
#define btn 3
#define fileName "LOG3.txt"

long interval = 30000;
volatile byte state = 0;
long m;
String dataStr = "";

void ISR() {
  state = (state ? 0 : 1);
  if (state == 1) {
    matrix.renderBitmap(f1, 8, 12);
    File dataFile = SD.open(fileName, FILE_WRITE);
    dataFile.println("start ");
    dataFile.close();
  } else {
    matrix.renderBitmap(f0, 8, 12);
  }
}

void setup() {
  Serial.begin(9600);
  delay(1000);
  SD.begin(10);
  sdState = 1;
  initSensors();
  initWifi();
  matrix.begin();
  matrix.renderBitmap(f0, 8, 12);
  showStateOffHtml();
  pinMode(btn, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(btn), ISR, RISING);
  m = millis();
}

void loop() {
  if (state && millis() - m >= interval) {
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
    m = millis();
  }
  if (state && dataStr != "") clientPrintValues(dataStr);
  if (!state) showStateOffHtml();
}
