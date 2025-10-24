# arduino_environmental_data_collection

Ever wanna know the temperature, humidity, air quality and air pressure at your surroundings? You can use Arduino and some sensors to do it. Here is an instruction to making this.

## hardware

### parts

1. Any Arduino boards that can connect to the Internet
2. a PMSA003 particle concentration sensor
3. a DHT22 temperature and humidity sensor
4. an SD card module and a microSD card
5. a BME280 air pressure sensor
6. a pushbutton
7. an LED or, if using Uno R4 WiFi, built-in LED matrix
8. a 1k ohms resistor if using an LED
9. jumper wires
10. a breadboard

### wiring

Arduino | sensors or modules
------|---------
D0 (RX) for hardware serial or D6 for software serial | the TX pin of the PMSA003 sensor
D1 (TX) for hardware serial or D7 for software serial | the RX pin of the PMSA003 sensor
D3 | the pushbutton
D4 | LED (if not Uno R4 WiFi)
CS | the CS pin of the SD card module
MOSI | the MOSI pin of the SD card module
MISO | the MISO pin of the SD card module
SCK | the CLK pin of the SD card module
A0 | the DATA pin of the DHT22 sensor
SDA | the SDA pin of the BME280 sensor
SCL | the SCL pin of the BME280 sensor

The SD card module and the BME280 sensor are connected to the Arduino's 3.3V pin, and the PMSA003 sensor is connected to the Arduino's 5V pin. All the components are connected to GND.

## software

### Arduino

All the configurations available are in configuration.h. The contents are shown below.

```cpp
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
#define ssid "SSID"
#define pass "PASSWORD"
#define interval 30000 // collection interval
```

After uploading, press the button to start collecting temperature, humidity, pm1.0, pm2.5, pm10, and air pressure data to the file in the microSD card.
If the LED matrix doesn't show "ON" or the LED doesn't light up, just press the button again.

during data collection, you can view the real time data on your web browser.
The Arduino's IP will be shown on Serial Monitor.
If the Arduino is connected to your phone AP, the IP can be seen somewhere in your phone's AP settings. The place varies and depends on your phone's brand.

### Python

After the data collection, you can copy the file in your SD card to the same path as the Python file.

Please make sure that matplotlib is installed.

The Python program will visualize the data collected.
