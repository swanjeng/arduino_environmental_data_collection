#define UNOR4WIFI 1 // comment it if not using Uno R4 WiFi
#include "WiFiS3.h" // change it to your Arduino's WiFi library
#define btn 3 // button pin
#define fileName "LOG3.txt" // the file in SD card
#define CS 10 // CS pin
#define PMSserial Serial1
#define DHT22_pin A0
#define led 4
#define ssid "YOUR SSID"
#define pass "YOUR PASSWORD"
#define interval 30000 // collection interval
