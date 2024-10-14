// WIFI
#include <SPI.h>
#include <WiFi.h>
#include <WiFiUdp.h>

int status = WL_IDLE_STATUS;
#include "arduino_secrets.h" 
///////please enter your sensitive data in the Secret tab/arduino_secrets.h
char ssid[] = SECRET_SSID;        // your network SSID (name)
char pass[] = SECRET_PASS;    // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;            // your network key index number (needed only for WEP)

unsigned int localPort = 2390;      // local port to listen on
unsigned int clientPort = 65530;

char packetBuffer[256]; //buffer to hold incoming packet
WiFiUDP Udp;


// Model
#include "IrisClassifier.h"

// IrisClassifier.h creates a irisClassifier object
// that you can use to classify a feature vector
// no setup is required
String features[] = {"Sepal Length", "Sepal Width", "Petal Length", "Petal Width"};
String labels[] = {"Iris Setosa", "Iris Versicolor", "Iris Virginica"};


void setup() {
    //Initialize serial and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // check for the WiFi module:
  if (WiFi.status() == WL_NO_MODULE) {
    Serial.println("Communication with WiFi module failed!");
    // don't continue
    while (true);
  }

  // attempt to connect to WiFi network:
  while (status != WL_CONNECTED) {
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
    status = WiFi.begin(ssid, pass);

    // wait 10 seconds for connection:
    delay(10000);
  }
  Serial.println("Connected to WiFi");
  printWifiStatus();

  Serial.println("\nStarting connection to server...");
  // if you get a connection, report back via serial:
  Udp.begin(localPort);
}

void loop() {

  // if there's data available, read a packet
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    // read the packet into packetBufffer
    int len = Udp.read(packetBuffer, 255);
    if (len > 0) {
      packetBuffer[len] = 0;
    }
    
    IPAddress remoteIp = Udp.remoteIP();
    String input = String(packetBuffer).substring(0, 15);
    String username = String(packetBuffer).substring(16); // can use any char to separate
    username.replace("\n", "");

    Serial.print("Received packet of size ");
    Serial.println(packetSize);
    Serial.print("From " + username + "@" + remoteIp);
    Serial.print(" on port ");
    Serial.println(Udp.remotePort());

    Serial.print("Your Input Data: ");
    Serial.println(packetBuffer);

    // send a reply, to the IP address and port that sent us the packet we received
    Udp.beginPacket(Udp.remoteIP(), clientPort);
    String response = predict_respond(input);
    Serial.print("AI Prediction: ");
    Serial.println(response);
    sendDta("for " + username + ": " + response);
  }
}


void sendDta(String message) {
  // Convert the String to a char array
  const char* charMessage = message.c_str(); 

  // send a reply, to the IP address and port that sent us the packet we received
  Udp.beginPacket(Udp.remoteIP(), clientPort);
  Udp.write(charMessage, strlen(charMessage));
  Udp.endPacket();
  delay(500);
}

void printWifiStatus() {
  // print the SSID of the network you're attached to:
  Serial.print("SSID: ");
  Serial.println(WiFi.SSID());

  // print your board's IP address:
  IPAddress ip = WiFi.localIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  // print the received signal strength:
  long rssi = WiFi.RSSI();
  Serial.print("signal strength (RSSI):");
  Serial.print(rssi);
  Serial.println(" dBm");
}

void predict(float sl, float sw, float pl, float pw){
  float input[4] = {sl, sw, pl, pw};
  int cl = irisClassifier.predict(input);
  for(int i=0; i<3; i++){
    Serial.print(" | ");
    Serial.print(features[i]);
    Serial.print(" : ");
    Serial.print(input[i]);
  }
  Serial.print(" ====> ");
  Serial.println(labels[cl]);
  Serial.println();
}

String predict_respond(String receivedData){
  String d = receivedData; // "5.7,3.6,7.9,6.5":0-15; 16-can be the name
  float inputf[4] = {
    d.substring(0, 3).toFloat(), 
    d.substring(4, 7).toFloat(),
    d.substring(8, 11).toFloat(),
    d.substring(12, 15).toFloat()
    };

  int cl = irisClassifier.predict(inputf);

  return labels[cl];
}