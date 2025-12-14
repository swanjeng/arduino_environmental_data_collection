#include <SPI.h>
#include <SD.h>
#include "sensorValue.h"
#include "wifi.h"
#include "ledMat.h"
#define btn 3

byte is_collecting_data = 0;
long last_data_collect_time;
int last_btn_state, btn_state;
long last_debounce_time;
String dataStr = "";

void toggle_state(int pin) {
  int reading = digitalRead(pin);
  if (reading != last_btn_state) {
    last_debounce_time = millis();
  }
  if ((millis() - last_debounce_time) > 50) {
    if (reading != btn_state) {
      btn_state = reading;

      if (btn_state == LOW) {
        is_collecting_data = (is_collecting_data ? 0 : 1);
      }
    }
  }

  if (is_collecting_data == 1) {
    matrix.renderBitmap(f1, 8, 12);
    File dataFile = SD.open(fileName, FILE_WRITE);
    dataFile.println("start");
    dataFile.close();
  } else matrix.renderBitmap(f0, 8, 12);

  last_btn_state = reading;
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
  last_data_collect_time = millis();
  last_btn_state = HIGH;
}

void loop() {
  toggle_state(btn);
  if (is_collecting_data && millis() - last_data_collect_time >= interval) {
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
    last_data_collect_time = millis();
  }
  if (is_collecting_data && dataStr != "") clientPrintValues(dataStr);
  if (!is_collecting_data) showStateOffHtml();
}
