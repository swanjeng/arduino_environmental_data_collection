#define UNOR4WIFI 1 // comment it if not using Uno R4 WiFi
#include "WiFiS3.h" // change it to your Arduino's WiFi library
#define btn 3 // button pin
#define fileName "LOG3.txt" // the file in SD card
#define CS 10 // CS pin

// if your Arduino doesn't have Serial1, please uncomment the three lines below.
// #include "softwareSerial.h"
// softSerial = SoftwareSerial(rx, tx); // change rx and tx to the pins connected to PMS sensor
// #define PMSserial softSerial
#define PMSserial Serial1 // and comment this line.

#define DHT22_pin A0
#define led 4
#define ssid "YOUR SSID"
#define pass "YOUR PASSWORD"
#define interval 30000 // collection interval (ms)

