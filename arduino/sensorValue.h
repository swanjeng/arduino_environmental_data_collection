#include <PMS.h>
#include <DHT.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include "configuration.h"

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme;
DHT dht(DHT22_pin, DHT22); 
PMS pms(PMSserial);
PMS::DATA data;

void initSensors() {
  PMSserial.begin(9600);
  dht.begin();
  bme.begin(0x76, &Wire);
  pms.passiveMode();
  pms.wakeUp();
}

String dhtdata() {
  delay(10);
  float t = dht.readTemperature();
  delay(10);
  float h = dht.readHumidity();
  return String(t) + " " + String(h);
}

String pmsdata() {
  String str = "";
  pms.requestRead();
  if (pms.readUntil(data)) {
    str += String(data.PM_AE_UG_1_0);
    str += " ";
    str += String(data.PM_AE_UG_2_5);
    str += " ";
    str += String(data.PM_AE_UG_10_0);
  } else str = "error error error";
  return str;
}

String bmedata() {
  return String(bme.readPressure() / 100.0);
}