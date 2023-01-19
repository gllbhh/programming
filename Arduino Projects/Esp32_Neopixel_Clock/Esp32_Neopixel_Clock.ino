/*
  Rui Santos
  Complete project details at https://RandomNerdTutorials.com/esp32-date-time-ntp-client-server-arduino/
  
  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files.
  
  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.
*/

#include <WiFi.h>
#include "time.h"
#include <Adafruit_NeoPixel.h>
#include <EEPROM.h>

const char* ssid     = "WiFi_name";
const char* password = "WiFI_password";

const char* ntpServer = "fi.pool.ntp.org";
const long  gmtOffset_sec = 7200;
const int   daylightOffset_sec = 3600;

char timeHour[3];
char timeMinute[3];
char timeSec[3];

int Hour, Minute, Sec;
byte secondval;
byte minuteval;
byte hourval;

int OnkoBileet; // Tarkistetaan tällä muuttujalla pitääkö kello vai bile-valot olla päällä

#define PIN 27
#define PIXEL 60

Adafruit_NeoPixel pixels = Adafruit_NeoPixel(PIXEL, PIN, NEO_GRB + NEO_KHZ800);

 

void setup(){
  Serial.begin(115200);

  // Connect to Wi-Fi
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected.");
  
  // Init and get the time
  configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
  printLocalTime();

  //disconnect WiFi as it's no longer needed
  WiFi.disconnect(true);
  WiFi.mode(WIFI_OFF);
  
  pixels.begin();
  pixels.show(); 
  pixels.setBrightness(50); 
  OnkoBileet = EEPROM.read(0); 
}

void loop(){
  
    getTime();
    
    secondval = Sec; 
    minuteval = Minute;
    hourval = Hour;
  

    if (hourval > 11) hourval -= 12;
    hourval = (hourval * 60 + minuteval) / 12;
    
    pixels.setPixelColor(hourval, pixels.Color(0, 0, 255));
    pixels.setPixelColor(hourval - 1, pixels.Color(0, 0, 255));
    pixels.setPixelColor(hourval + 1, pixels.Color(0, 0, 255));
    pixels.setPixelColor(minuteval, pixels.Color(0, 255, 0));
    pixels.setPixelColor(secondval, pixels.Color(128, 128, 0));   
    pixels.show();

    pixels.setPixelColor(secondval, pixels.Color(0, 0, 0)); 
    pixels.setPixelColor(minuteval, pixels.Color(0, 0, 0));
    pixels.setPixelColor(hourval, pixels.Color(0, 0, 0));
    pixels.setPixelColor(hourval - 1, pixels.Color(0, 0, 0));
    pixels.setPixelColor(hourval + 1, pixels.Color(0, 0, 0));

    delay(25);
//    }
}

void printLocalTime(){
  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    Serial.println("Failed to obtain time");
    return;
  }
  Serial.println(&timeinfo, "%A, %B %d %Y %H:%M:%S");
  Serial.print("Day of week: ");
  Serial.println(&timeinfo, "%A");
  Serial.print("Month: ");
  Serial.println(&timeinfo, "%B");
  Serial.print("Day of Month: ");
  Serial.println(&timeinfo, "%d");
  Serial.print("Year: ");
  Serial.println(&timeinfo, "%Y");
  Serial.print("Hour: ");
  Serial.println(&timeinfo, "%H");
  Serial.print("Hour (12 hour format): ");
  Serial.println(&timeinfo, "%I");
  Serial.print("Minute: ");
  Serial.println(&timeinfo, "%M");
  Serial.print("Second: ");
  Serial.println(&timeinfo, "%S");
  Serial.println("Time variables");
  strftime(timeHour,3, "%H", &timeinfo);
  strftime(timeMinute,3, "%M", &timeinfo);
  strftime(timeSec,3, "%S", &timeinfo);
  Serial.println(String(timeHour) + ":" + String(timeMinute) + ":" + String(timeSec));
}

void getTime(){
    struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    Serial.println("Failed to obtain time");
    return;
  }
  strftime(timeHour,3, "%H", &timeinfo);
  String HourStr(timeHour);
  Hour = HourStr.toInt();
  strftime(timeMinute,3, "%M", &timeinfo);
  String MinuteStr(timeMinute);
  Minute = MinuteStr.toInt();
  strftime(timeSec,3, "%S", &timeinfo);
  String SecStr(timeSec);
  Sec = SecStr.toInt();
  return;
}
  
void getHour(){
  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    Serial.println("Failed to obtain time");
    return;
  }
  strftime(timeHour,3, "%H", &timeinfo);
  String HourStr(timeHour);
  Hour = HourStr.toInt();
  return;
}

void getMinute(){
  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    Serial.println("Failed to obtain time");
    return;
  }
  strftime(timeMinute,3, "%M", &timeinfo);
  String MinuteStr(timeMinute);
  Minute = MinuteStr.toInt();
  return;
}

void getSec(){
  struct tm timeinfo;
  if(!getLocalTime(&timeinfo)){
    Serial.println("Failed to obtain time");
    return;
  }
  strftime(timeSec,3, "%S", &timeinfo);
  String SecStr(timeSec);
  Sec = SecStr.toInt();
  return;
}
