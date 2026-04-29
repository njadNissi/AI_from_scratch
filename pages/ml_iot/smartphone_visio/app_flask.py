import json
from flask import Flask, render_template_string, jsonify
from flask_socketio import SocketIO, emit
import folium
from folium import IFrame
import plotly.graph_objects as go
import plotly.io as pio
from datetime import datetime

# ---------------------------
# Flask App Setup
# ---------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# Store live sensor data
live_data = {
    'gps': {'latitude': None, 'longitude': None, 'timestamp': None},
    'gyro': {'x': [], 'y': [], 'z': [], 'timestamps': []},
    'connected': False
}

# ---------------------------
# HTML Templates
# ---------------------------

# 1. Phone Page (Sensor Data Sender)
PHONE_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Phone Sensor Sender</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <style>
        body { font-family: Arial; padding: 20px; max-width: 500px; margin: 0 auto; }
        .status { padding: 10px; border-radius: 5px; margin: 10px 0; }
        .connected { background-color: #d4edda; color: #155724; }
        .disconnected { background-color: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <h1>Phone Sensor Streamer</h1>
    <div id="status" class="status disconnected">Not connected</div>
    <div id="gps">GPS: Waiting...</div>
    <div id="gyro">Gyro: Waiting...</div>

    <script>
        const socket = io.connect('{{ server_url }}');
        
        socket.on('connect', () => {
            document.getElementById('status').className = 'status connected';
            document.getElementById('status').textContent = 'Connected to server';
            
            // GPS Tracking
            if (navigator.geolocation) {
                navigator.geolocation.watchPosition(
                    (position) => {
                        const gpsData = {
                            latitude: position.coords.latitude,
                            longitude: position.coords.longitude,
                            timestamp: new Date().toISOString()
                        };
                        socket.emit('gps_data', gpsData);
                        document.getElementById('gps').textContent = 
                            `GPS: ${gpsData.latitude.toFixed(6)}, ${gpsData.longitude.toFixed(6)}`;
                    },
                    (error) => console.error('GPS error:', error)
                );
            }

            // Gyroscope Tracking
            window.addEventListener('devicemotion', (event) => {
                const gyroData = {
                    x: event.rotationRate.alpha || 0,
                    y: event.rotationRate.beta || 0,
                    z: event.rotationRate.gamma || 0,
                    timestamp: new Date().toISOString()
                };
                socket.emit('gyro_data', gyroData);
                document.getElementById('gyro').textContent = 
                    `Gyro: X: ${gyroData.x.toFixed(2)}, Y: ${gyroData.y.toFixed(2)}, Z: ${gyroData.z.toFixed(2)}`;
            });
        });

        socket.on('disconnect', () => {
            document.getElementById('status').className = 'status disconnected';
            document.getElementById('status').textContent = 'Disconnected';
        });
    </script>
</body>
</html>
"""

# 2. Visualization Dashboard (For Computer)
DASHBOARD_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Sensor Dashboard</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>
        .container { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; padding: 20px; }
        .card { border: 1px solid #ddd; border-radius: 8px; padding: 15px; }
        #map { height: 400px; width: 100%; }
        #gyro-plot { height: 400px; width: 100%; }
        .status { font-weight: bold; margin: 10px 0; }
    </style>
</head>
<body>
    <h1>📱 Smartphone Sensor Dashboard</h1>
    <div class="status" id="connection-status">🔴 Not Connected</div>
    
    <div class="container">
        <div class="card">
            <h2>🌍 GPS Location</h2>
            <div id="map"></div>
        </div>
        <div class="card">
            <h2>🔄 Gyroscope (Rotation Rate)</h2>
            <div id="gyro-plot"></div>
        </div>
    </div>

    <div class="card" style="margin: 20px;">
        <h2>📊 Raw Data</h2>
        <pre id="raw-data"></pre>
    </div>

    <script>
        // Initialize map
        const map = L.map('map').setView([0, 0], 1);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
        let gpsMarker;

        // Connect to WebSocket for real-time updates
        const socket = io.connect('{{ server_url }}');
        
        socket.on('connect', () => {
            document.getElementById('connection-status').textContent = '🟢 Connected';
        });

        // Update GPS map
        socket.on('live_gps', (data) => {
            if (data.latitude && data.longitude) {
                map.setView([data.latitude, data.longitude], 17);
                if (gpsMarker) map.removeLayer(gpsMarker);
                gpsMarker = L.marker([data.latitude, data.longitude]).addTo(map)
                    .bindPopup(`Time: ${data.timestamp}`).openPopup();
            }
        });

        // Update gyroscope plot
        socket.on('live_gyro', (data) => {
            const traceX = { x: data.timestamps, y: data.x, mode: 'lines', name: 'X (α)', line: {color: 'blue'} };
            const traceY = { x: data.timestamps, y: data.y, mode: 'lines', name: 'Y (β)', line: {color: 'red'} };
            const traceZ = { x: data.timestamps, y: data.z, mode: 'lines', name: 'Z (γ)', line: {color: 'green'} };
            
            Plotly.newPlot(
                'gyro-plot',
                [traceX, traceY, traceZ],
                { title: 'Rotation Rate (°/s)', xaxis: {title: 'Time'}, yaxis: {title: 'Rate'} }
            );
        });

        // Update raw data display
        socket.on('live_data', (data) => {
            document.getElementById('raw-data').textContent = JSON.stringify(data, null, 2);
        });

        socket.on('disconnect', () => {
            document.getElementById('connection-status').textContent = '🔴 Disconnected';
        });
    </script>
</body>
</html>
"""

# ---------------------------
# Routes
# ---------------------------
@app.route('/')
def phone_interface():
    """Serve the phone's sensor collection page"""
    server_url = "http://localhost:5000"  # Replace with your server IP
    return render_template_string(PHONE_TEMPLATE, server_url=server_url)

@app.route('/dashboard')
def dashboard():
    """Serve the visualization dashboard for computers"""
    server_url = "http://localhost:5000"
    return render_template_string(DASHBOARD_TEMPLATE, server_url=server_url)

# ---------------------------
# WebSocket Handlers
# ---------------------------
@socketio.on('gps_data')
def handle_gps(data):
    """Receive GPS data from phone and broadcast to dashboard"""
    global live_data
    live_data['gps'] = data
    live_data['connected'] = True
    emit('live_gps', data, broadcast=True)  # Send to all dashboard clients
    emit('live_data', live_data, broadcast=True)

@socketio.on('gyro_data')
def handle_gyro(data):
    """Receive gyro data from phone and broadcast to dashboard"""
    global live_data
    # Keep last 100 samples
    if len(live_data['gyro']['x']) > 100:
        for key in ['x', 'y', 'z', 'timestamps']:
            live_data['gyro'][key].pop(0)
    live_data['gyro']['x'].append(data['x'])
    live_data['gyro']['y'].append(data['y'])
    live_data['gyro']['z'].append(data['z'])
    live_data['gyro']['timestamps'].append(data['timestamp'])
    
    emit('live_gyro', live_data['gyro'], broadcast=True)  # Send to dashboards
    emit('live_data', live_data, broadcast=True)

# ---------------------------
# Run Server
# ---------------------------
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
