# arduino_environmental_data_collection

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

SD 卡模組和 BME280 是 3.3V，PMSA003 是 5V，所有元件共地 (GND)。
