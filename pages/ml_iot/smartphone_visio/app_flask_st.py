import json
from flask import Flask, render_template_string
from flask_socketio import SocketIO, emit
import streamlit as st
from streamlit.runtime.scriptrunner import add_script_run_ctx
import threading
import folium
from streamlit_folium import st_folium
import plotly.graph_objects as go
from datetime import datetime

# ---------------------------
# Flask Server (Data Receiver)
# ---------------------------
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

# Store live data
live_data = {
    'gps': {'latitude': None, 'longitude': None, 'timestamp': None},
    'gyro': {'x': [], 'y': [], 'z': [], 'timestamps': []},
    'connected': False
}

# HTML page for smartphone to send data
PHONE_HTML = """
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
            
            // Request GPS
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

            // Request Gyroscope
            window.addEventListener('devicemotion', (event) => {
                const gyroData = {
                    x: event.rotationRate.alpha || 0,  // Rotation around z-axis
                    y: event.rotationRate.beta || 0,   // Rotation around x-axis
                    z: event.rotationRate.gamma || 0,  // Rotation around y-axis
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

@app.route('/')
def phone_interface():
    # Replace with your server's IP (e.g., "http://192.168.1.100:5000" for local network)
    # server_url = "http://localhost:5000"
    server_url = "http://192.168.45.90:5000"
    return render_template_string(PHONE_HTML, server_url=server_url)

@socketio.on('gps_data')
def handle_gps(data):
    global live_data
    live_data['gps'] = data
    live_data['connected'] = True

@socketio.on('gyro_data')
def handle_gyro(data):
    global live_data
    # Keep last 100 gyro samples for smooth plotting
    if len(live_data['gyro']['x']) > 100:
        live_data['gyro']['x'].pop(0)
        live_data['gyro']['y'].pop(0)
        live_data['gyro']['z'].pop(0)
        live_data['gyro']['timestamps'].pop(0)
    live_data['gyro']['x'].append(data['x'])
    live_data['gyro']['y'].append(data['y'])
    live_data['gyro']['z'].append(data['z'])
    live_data['gyro']['timestamps'].append(data['timestamp'])

# ---------------------------
# Streamlit Visualization
# ---------------------------
def run_streamlit():
    st.set_page_config(page_title="Phone Sensor Visualizer", layout="wide")
    st.title("📱 Smartphone Sensor Tracker")

    # Initialize plots
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌍 GPS Location")
        map_placeholder = st.empty()

    with col2:
        st.subheader("🔄 Gyroscope (Rotation Rate)")
        gyro_placeholder = st.empty()

    st.subheader("📊 Live Data")
    data_placeholder = st.empty()

    # Update UI in real-time
    while True:
        # Update connection status
        status = "🟢 Connected" if live_data['connected'] else "🔴 Not Connected"
        st.sidebar.markdown(f"**Connection Status**: {status}")

        # Update GPS map
        with col1:
            if live_data['gps']['latitude']:
                m = folium.Map(
                    location=[live_data['gps']['latitude'], live_data['gps']['longitude']],
                    zoom_start=17,
                    tiles="CartoDB positron"
                )
                folium.Marker(
                    [live_data['gps']['latitude'], live_data['gps']['longitude']],
                    popup=f"Time: {live_data['gps']['timestamp']}"
                ).add_to(m)
                map_placeholder.empty()
                with map_placeholder:
                    st_folium(m, width=700, height=400)
            else:
                map_placeholder.text("Waiting for GPS data...")

        # Update gyroscope plot
        with col2:
            if live_data['gyro']['timestamps']:
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=live_data['gyro']['timestamps'],
                    y=live_data['gyro']['x'],
                    mode='lines', name='X (α)', line=dict(color='royalblue')
                ))
                fig.add_trace(go.Scatter(
                    x=live_data['gyro']['timestamps'],
                    y=live_data['gyro']['y'],
                    mode='lines', name='Y (β)', line=dict(color='firebrick')
                ))
                fig.add_trace(go.Scatter(
                    x=live_data['gyro']['timestamps'],
                    y=live_data['gyro']['z'],
                    mode='lines', name='Z (γ)', line=dict(color='green')
                ))
                fig.update_layout(
                    height=400,
                    xaxis_title="Time",
                    yaxis_title="Rotation Rate (°/s)",
                    margin=dict(l=20, r=20, t=20, b=20)
                )
                gyro_placeholder.empty()
                with gyro_placeholder:
                    st.plotly_chart(fig, use_container_width=True)
            else:
                gyro_placeholder.text("Waiting for gyroscope data...")

        # Update raw data display
        data_placeholder.json(live_data, expanded=False)

        # Small delay to reduce CPU usage
        st.session_state.get('stop_flag', False)
        if st.session_state.get('stop_flag', False):
            break
        st.experimental_rerun()  # Refresh UI


# ---------------------------
# Run Both Servers Concurrently
# ---------------------------
if __name__ == '__main__':
    # Start Flask server in a thread
    flask_thread = threading.Thread(
        target=lambda: socketio.run(app, host='0.0.0.0', port=5000, debug=False)
    )
    flask_thread.daemon = True
    flask_thread.start()

    # Run Streamlit app
    run_streamlit()