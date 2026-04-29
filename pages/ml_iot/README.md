# How It Works

1. GPS Data:
    - Uses navigator.geolocation.watchPosition() (HTML5 Geolocation API) to continuously fetch the phone’s latitude and longitude.
    - Wraps this data in a gpsData object and sends it to the Python backend via socket.emit('gps_data', gpsData).

2. Gyroscope Data:
    - Uses window.addEventListener('devicemotion') (DeviceMotion API) to listen for gyroscope events.
    - Extracts rotation rates around the x, y, and z axes from event.rotationRate.
    - Wraps this data in a gyroData object and sends it to the backend via socket.emit('gyro_data', gyroData).

# How to Use
1. Run the app:
    ```
    python flask_only_app.py
    ```
2. On your phone: Visit http://<your-ip>:5000 to start sending sensor data.
3. On your computer: Visit http://localhost:5000/dashboard to see the live visualizations.