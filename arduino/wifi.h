#include <NTPClient.h>
#include <WiFiUdp.h>
#include "RTC.h"
#include "configuration.h"

WiFiServer server(80);
int status = WL_IDLE_STATUS;
WiFiUDP Udp;
NTPClient timeClient(Udp);
int sdState;

void initWifi() {
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid, pass);
    delay(10000);
  }
  IPAddress ip = WiFi.localIP();
  Serial.println(ip);
  server.begin();
  timeClient.begin();
}

String getCurrTime() {
  timeClient.update();
  if (!timeClient.update()) timeClient.forceUpdate();
  auto timeZoneOffsetHours = 8;
  auto unixTime = timeClient.getEpochTime() + (timeZoneOffsetHours * 3600);
  RTCTime currentTime = RTCTime(unixTime);
  String str = String(currentTime.getYear()) + "." 
             + String(Month2int(currentTime.getMonth())) + "."
             + currentTime.getDayOfMonth() + " "
             + currentTime.getHour() + ":"
             + currentTime.getMinutes() + ":"
             + currentTime.getSeconds();
  
  return str;
}

void clientPrintValues(String dataStr) {
  int firstSpace = dataStr.indexOf(' ');
  String date = dataStr.substring(0, firstSpace);
  int secSpace = dataStr.indexOf(' ', firstSpace + 1);
  String t = dataStr.substring(firstSpace + 1, secSpace);
  int thrSpace = dataStr.indexOf(' ', secSpace + 1);
  String temp = dataStr.substring(secSpace + 1, thrSpace);
  int forSpace = dataStr.indexOf(' ', thrSpace + 1);
  String h = dataStr.substring(thrSpace + 1, forSpace);
  int fifSpace = dataStr.indexOf(' ', forSpace + 1);
  String pm1 = dataStr.substring(forSpace + 1, fifSpace);
  int sixSpace = dataStr.indexOf(' ', fifSpace + 1);
  String pm25 = dataStr.substring(fifSpace + 1, sixSpace);
  int sevSpace = dataStr.indexOf(' ', sixSpace + 1);
  String pm10 = dataStr.substring(sixSpace + 1, sevSpace);
  String pre = dataStr.substring(sevSpace + 1);

  WiFiClient client = server.available();
  if (client) {
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        if (c == '\n' && currentLineIsBlank) {
          // send a standard HTTP response header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");  // the connection will be closed after completion of the response
          client.println("Refresh: 10");  // refresh the page automatically every 10 sec
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<html>");
          
          client.println("<head></head>");
          client.println("<body>");
          
          client.println("<h2>SD card state: " + String(sdState ? "ok" : "error") + "</h2>");
          client.println("<h2>time: " + t + "</h2>");
          client.println("<h2>temperature: " + temp + " C</h2>");
          client.println("<h2>humidity: " + h + " %</h2>");
          client.println("<h2>PM1.0: " + pm1 + " ug / m3</h2>");
          client.println("<h2>PM2.5: " + pm25 + " ug / m3</h2>");
          client.println("<h2>PM10: " + pm10 + " ug / m3</h2>");
          client.println("<h2>pressure: " + pre + " hPa</h2>");
          
          client.println("</body></html>");
          break;
        }
        if (c == '\n') {
          // you're starting a new line
          currentLineIsBlank = true;
        } else if (c != '\r') {
          // you've gotten a character on the current line
          currentLineIsBlank = false;
        }
      }
    }
    // give the web browser time to receive the data
    delay(1);

    // close the connection:
    client.stop();
  }
}

void showStateOffHtml() {
  WiFiClient client = server.available();
  if (client) {
    boolean currentLineIsBlank = true;
    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        if (c == '\n' && currentLineIsBlank) {
          // send a standard HTTP response header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");  // the connection will be closed after completion of the response
          client.println("Refresh: 10");  // refresh the page automatically every 10 sec
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<html>");
          
          client.println("<head></head>");
          client.println("<body>");
          
          client.println("<h2>state: off</h2>");
          
          client.println("</body></html>");
          break;
        }
        if (c == '\n') {
          // you're starting a new line
          currentLineIsBlank = true;
        } else if (c != '\r') {
          // you've gotten a character on the current line
          currentLineIsBlank = false;
        }
      }
    }
    // give the web browser time to receive the data
    delay(1);

    // close the connection:
    client.stop();
  }
}