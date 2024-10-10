# AI from scratch

This repo is created to give a solid a foundation on AI model Development with machine Learning techniques, Design and Implementation. Above that, It introduces the concept of tinyML and Edge Computing. The idea of leveraging AI predictions for smart IoT devices and varied applications on ebedded systems such as smartphones, microcontrollers, microcomputers, and edge devices. Deploying a model is as important as training one, but MCUs have limited computing resources, thus the need of tinyML and Quantization techniques to fit the model on the hardware.

## Structure:

- ML: this folder introduces Machine Learning Model Development and Deployment on typical computers.
- ML_IoT: this folder introduces different techniques and libraries used to build a model that can run on embedded systems.


### 1. Introduction to Key Concepts

#### 1.1. Artificial Intelligence (AI) and Machine Learning (ML)

AI involves creating systems capable of intelligent behavior, while ML refers to algorithms that allow systems to learn from data and improve performance over time without being explicitly programmed for every task.
    
#### 1.2. Internet of Things (IoT)

IoT refers to the interconnection of physical objects, such as sensors, actuators, and everyday devices, that can collect and exchange data via the internet.
    
#### 1.3. Edge Devices

Edge devices are computing devices located close to the source of data (e.g., sensors, cameras) that process data locally rather than sending it to a centralized cloud. Examples include smartphones, embedded systems, and smart appliances.


#### 1.4. TinyML

TinyML is a subfield of machine learning that focuses on developing machine learning models that can be deployed on low-power and resource-constrained devices, such as microcontrollers and IoT devices.


Examples:

![Picture1](https://github.com/user-attachments/assets/a44434f8-d575-413b-aec3-c1d25c94144a)

![Picture2](https://github.com/user-attachments/assets/03a9693e-347d-479c-bef7-5564a55e6322)

![Picture3](https://github.com/user-attachments/assets/f680733f-6b32-4376-ac45-f4966a5dd574)


### 2. The Role of Machine Learning in Edge, IoT, and TinyML

Machine learning models are key to making edge and IoT devices "smart." By embedding ML models into these devices, they can make decisions, predict outcomes, and automate processes in real time, without relying on constant connectivity to cloud systems.

|Concept | Description|
|--------|------------|
|Edge AI|Running AI/ML algorithms directly on edge devices to process data locally without relying on cloud-based computing.|
|On-Device Inference	|Once trained, a machine learning model is deployed on an edge device for making predictions based on new input data.|
|On-Device Learning|	The process of training or updating machine learning models on the device itself. This is especially |important for personalization and adaptation over time.|
|Federated Learning|	A method for training ML models where multiple devices collaborate to train a model without sharing raw data, improving data privacy and security.|

### 3. Machine Learning Techniques for Edge and IoT Devices

#### 3.1. Common Machine Learning Algorithms for Edge and IoT

|ML Algorithm|	Description|	Use Cases|
|------------|-------------|-------------|
|Linear Regression|	A simple algorithm to predict continuous outcomes based on linear relationships.|	Predicting temperature, power consumption, etc.|
|Decision Trees	|A tree-like model for decision-making based on features. Lightweight and efficient.|	Fault detection, predictive maintenance.|
|k-Nearest Neighbors (k-NN)|	A classification algorithm that assigns a class to new data based on the closest data points.|	Gesture recognition, health monitoring.|
|Convolutional Neural Networks (CNNs)|	Primarily used for image processing and computer vision tasks.|	Object detection, image classification on IoT cameras.|
|Recurrent Neural Networks (RNNs)|	Designed for sequence data and time series analysis.|	Predicting sensor readings, activity recognition.|

#### 3.2. TinyML-Specific Algorithms

TinyML optimizes algorithms for constrained environments:

- Quantization: Reduces the precision of the numbers used in ML models to reduce model size and computational requirements.
- Pruning: Removes unnecessary neurons or weights from a neural network to reduce its size and improve efficiency.
- Distillation: Involves training a small "student" model to mimic the behavior of a larger "teacher" model to reduce model complexity while maintaining performance.

### 4. Key Components of an IoT and Edge AI System

To understand how AI techniques are used in IoT and Edge devices, it's essential to know the components of the system:
|Component|	Description|
|---------|------------|
|Sensors/Actuators|	Hardware components that collect real-world data (e.g., temperature, motion) or perform actions based on ||decisions (e.g., turning on a motor).|
|Edge Device/Node|	A device that processes sensor data using embedded ML models, performing actions locally.|
|Gateway|	Connects the edge devices to a broader network, such as the internet, and may also perform pre-processing of data before sending it to the cloud.|
|Cloud Backend|	A centralized system for deeper analytics, longer-term storage, and coordination of multiple edge devices.|
|Machine Learning Model	A pre-trained model deployed to an edge device to infer predictions based on real-time data.|

### 5. Edge AI vs. Cloud AI
|Aspect|	Edge AI|	Cloud AI|
|------|-----------|------------|
|Latency|	Low, as data is processed locally.|	Higher, as data must travel to/from the cloud.|
|Bandwidth Usage|	Minimal, since not all data is sent to the cloud.|	High, as large amounts of data are uploaded.|
|Privacy|	Data is processed locally, improving privacy.|	Sensitive data may need to be sent to the cloud.|
|Computational Power|	Limited by the device's hardware (microcontroller, embedded systems).|	Powerful cloud servers are used for |complex tasks.|
|Energy Consumption	Efficient, optimized for low-power environments.|	High energy consumption due to large-scale infrastructure.|
|Scalability|	Limited to the device's processing capacity.|	Can scale horizontally with cloud resources.|


### 6. Use Cases of Machine Learning in IoT and Edge Devices

#### 6.1. Smart Homes

- Voice Assistants (Edge AI): Devices like Alexa and Google Home use ML to recognize voice commands and perform actions (e.g., turning off lights).
- Energy Management (IoT): Smart meters use ML to predict energy consumption and optimize usage, reducing costs.

#### 6.2. Industrial IoT (IIoT)

- Predictive Maintenance: Machine learning models analyze data from sensors on industrial equipment to predict when machines are likely to fail, allowing for timely repairs.
- Fault Detection: Edge devices can monitor machine performance in real time, flagging abnormalities in sensor data that indicate a malfunction.

#### 6.3. Healthcare and Wearables

- Activity Recognition (TinyML): Wearable devices, such as smartwatches, use ML models to track movements, heart rate, and other health metrics to provide insights into the user’s health.
- Remote Monitoring (IoT): Continuous monitoring of patients’ vital signs, with alerts triggered by ML models in case of anomalies.

#### 6.4. Agriculture

- Smart Irrigation: IoT devices with embedded ML models can predict the optimal watering times based on weather conditions, soil moisture levels, and crop types, improving water efficiency.
- Crop Monitoring: Drones equipped with cameras and sensors use ML models to analyze crop health and detect diseases early.

### 7. Optimizing Machine Learning Models for Edge Devices (TinyML)

Running machine learning models on resource-constrained devices (TinyML) requires optimization techniques to reduce memory, computation, and energy requirements.

#### 7.1. Model Compression Techniques
|Technique|	Description|
|---------|------------|
|Model Quantization|	Reduces the precision of weights and activations, typically from 32-bit to 8-bit, saving memory and computation power.|
|Model Pruning|	Removes less important weights or neurons from the model, reducing its size and complexity.|
|Knowledge Distillation|	Trains a small, lightweight "student" model using the predictions of a larger "teacher" model.|

#### 7.2. Popular Frameworks for TinyML
|Framework|	Description|
|TensorFlow Lite|	A lightweight version of TensorFlow for mobile and embedded devices, with optimizations for TinyML.|
|AIfES (AI for Embedded Systems)|	A lightweight AI framework designed for microcontrollers, perfect for running TinyML models on small devices.|
|Edge Impulse|	A platform for developing and deploying machine learning models for IoT and edge devices.|

### 8. Challenges in Implementing Machine Learning on Edge and IoT Devices
Challenge	Description
Limited Computational Power	Edge devices and IoT nodes often have limited processing capabilities, making complex ML models challenging to deploy.
Memory Constraints	Embedded devices typically have very limited memory, so ML models need to be compact and efficient.
Energy Efficiency	Many IoT devices are battery-powered, requiring ML algorithms that consume minimal power.
Real-Time Processing	Many applications require real-time decision-making, putting pressure on the ML algorithms to be both fast and accurate.
Data Privacy	Processing sensitive data on IoT devices brings security concerns, especially if models involve personal or confidential information.



-------------------------------------------------------------------------------------------------------------------------
### Contacts

njadnissi@gmail.com
35507497566@qq.com
202352620015@nuist.edu.cn
https://www.linkedin.com/in/njadnissi/
https://www.kaggle.com/njadnissi
