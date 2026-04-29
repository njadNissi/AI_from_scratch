# STEPS TO FOLLOW TO RUN THE IRIS FLOWERS CLASSIFICATION DEMO PROJECT



### Step1: Train the model

    python 0_iris_mode_train.py

### Step2: Prepare Your Microcontroller (I used Arduino, .ino files)

**1. Open the folder named `IrisClassification-MCU-ino`**

**2. You can test any of the 2 sketches:**

Compile and Upload the sketch to your board (arduino, or similar). the example tests predicting a type of Iris flower(`Setosa`, `Versicolor`, `Virginica`) based on its four properties(`Sepal Length`, `Sepal Width`, `Petal Length`, `Petal Width`).

**1. use `0_IrisClassificationSimple` sketch for a local testing, you can type your Input values directly in the code.**

**2. use `IrisClassificationWifi` sketch for wi-fi based testing. for this edit the `arduino_secrets.h` file to set your wifi SSID and PassWord.**

- Run:

```python serialread.py -p <SERIAL PORT> -br <BUAD-RATE>```

in the `command line `(cmd for windows) or `terminal` for (mac and linux). it helps you see requests sent to the arduino via UDP over WiFi and the results of predictions made by the model.
- Serial Port: on windows it looks like `COM<number>`, on UNIX(linux or MAC) `/dev/ttyUSB<number>` or `/dev/ttyACM<number>`

- BAUD-RATE: the code is set to `9600`, you can change it to other values like `115200` if needed.

- To send requests to your arduino over wifi, you need either to download a network UDP Utilities apps on your phone. you can try installing `UDP Terminal` or `UDP Sender/Receiver` or similar apps.

![alt text](/results/IrisClassifier.png)