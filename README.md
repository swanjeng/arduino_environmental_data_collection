# arduino_environmental_data_collection

Ever wanna know the temperature, humidity, air quality and air pressure at your surroundings? You can use Arduino and some sensors to do it. Here is an instruction to making this.

## hardware

### parts

1. an Arduino Uno R4 WiFi
2. a PMSA003 particle concentration sensor
3. a DHT22 temperature and humidity sensor
4. an SD card module and a microSD card
5. a BME280 air pressure sensor
6. a pushbutton
7. jumper wires
8. a breadboard

### wiring

Arduino | sensors or modules
------|---------
D0 (RX) | the TX pin of the PMSA003 sensor
D1 (TX) | the RX pin of the PMSA003 sensor
D3 | the pushbutton
CS | the CS pin of the SD card module
MOSI | the MOSI pin of the SD card module
MISO | the MISO pin of the SD card module
SCK | the CLK pin of the SD card module
A0 | the DATA pin of the DHT22 sensor
SDA | the SDA pin of the BME280 sensor
SCL | the SCL pin of the BME280 sensor

The SD card module, the DHT22 sensor and the BME280 sensor are connected to the Arduino's 3.3V pin, and the PMSA003 sensor is connected to the Arduino's 5V pin. All the components are connected to the Arduino's GND.

## software

### Arduino

All the configurations available are in configuration.h. The contents are shown below.

```cpp
#define fileName "LOG3.txt" // the file in SD card
#define ssid "SSID"
#define pass "PASS"
#define interval 30000 // collection interval (ms)
```

Before inserting the micro SD card into the SD card module, make sure that the micro SD card is formatted as FAT32 and that in the root path of the micro SD card, there is a file with the same name as the fileName constant in configuration.h.

After the Arduino IDE has uploaded the program, you can press the button to start collecting temperature, humidity, pm1.0, pm2.5, pm10, and air pressure data to the file in the microSD card.
If the LED matrix doesn't show "ON", just press the button again.

during data collection, you can view the real time data on your web browser.
The Arduino's IP will be shown on Serial Monitor.
If the Arduino is connected to your phone AP, the IP can be seen somewhere in your phone's AP settings. The place varies and depends on your phone's brand.

### Python

After the data collection, you can copy the file in your SD card to the same path as the Python files.

If you don't have an SD card reader, you can use the programs in `sdRead/`. The Arduino sketch should be uploaded before the Python code runs.

The programs will transfer the data in the micro SD card to a file in the path of the Python program, and then the data file in the micro SD card will be cleared for the next data collection.

Before running the Python program, please make sure that the Serial Monitor in Arduino IDE is closed.

```python
ser = serial.Serial("COM3", 115200) # change COM3 to your Arduino's Serial port.
file = "123456789.txt" # specify your file name here
```

Then, it is the data analyzing part.

Please make sure that `matplotlib` and `glob` are installed and the file names are correct.

Different Python programs will visualize the collected data in different ways.
