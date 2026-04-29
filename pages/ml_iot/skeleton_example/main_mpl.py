import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading
import time
import math

# --------------------------
# CONFIG
# --------------------------
NUM_JOINTS = 17
CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (0, 9), (9, 10), (10, 11),
    (0, 12), (12, 13), (13, 14),
    (1, 5), (9, 12)
]

# --------------------------
# REALISTIC DATA GENERATOR
# --------------------------
class RealisticSkeletonGenerator:
    def __init__(self):
        self.time = 0.0
        self.base_pose = np.array([
            [0, 300],     # 0: Torso
            [-40, 260],   # 1: R Shoulder
            [-80, 220],   # 2: R Elbow
            [-120, 180],  # 3: R Wrist
            [-140, 160],  # 4: R Hand
            [40, 260],    # 5: L Shoulder
            [80, 220],    # 6: L Elbow
            [120, 180],   # 7: L Wrist
            [140, 160],   # 8: L Hand
            [-30, 200],   # 9: R Hip
            [-30, 100],   #10: R Knee
            [-30, 0],     #11: R Foot
            [30, 200],    #12: L Hip
            [30, 100],    #13: L Knee
            [30, 0],      #14: L Foot
            [0, 340],     #15: Neck
            [0, 380]      #16: Head
        ], dtype=np.float32)

    def get_realistic_joints(self):
        self.time += 0.05
        t = self.time
        body_sway = 15 * math.sin(t * 0.8)
        arm_swing = 25 * math.sin(t * 1.2)
        leg_sway = 8 * math.sin(t * 0.6)
        
        pose = self.base_pose.copy()
        pose[:, 0] += body_sway
        pose[1:5, 1] += arm_swing
        pose[5:9, 1] -= arm_swing
        pose[9:11, 0] += leg_sway
        pose[12:14, 0] -= leg_sway
        pose += np.random.normal(0, 1.5, pose.shape)
        return pose

    def get_serial_string(self):
        joints = self.get_realistic_joints()
        return ','.join([f'{x:.2f},{y:.2f}' for x, y in joints])

# --------------------------
# GLOBAL DATA
# --------------------------
joint_data = np.zeros((NUM_JOINTS, 2))
data_lock = threading.Lock()
running = True

# --------------------------
# SIMULATED SERIAL READER
# --------------------------
def read_serial():
    global joint_data, running
    gen = RealisticSkeletonGenerator()
    print("✅ Simulated realistic skeleton running (no hardware needed)")
    
    while running:
        try:
            line = gen.get_serial_string()
            values = list(map(float, line.split(',')))
            if len(values) == NUM_JOINTS * 2:
                with data_lock:
                    joint_data = np.array(values).reshape(NUM_JOINTS, 2)
            time.sleep(0.03)
        except:
            continue

# --------------------------
# MATPLOTLIB ANIMATION
# --------------------------
fig, ax = plt.subplots(figsize=(6, 8))
ax.set_xlim(-200, 200)
ax.set_ylim(-50, 450)
ax.set_aspect('equal')
ax.grid(True, alpha=0.3)
ax.set_title("Real-Time Human Skeleton (Simulated Data)", fontsize=12)

lines = []
for _ in CONNECTIONS:
    line, = ax.plot([], [], 'r-', linewidth=3)
    lines.append(line)
joint_scatter = ax.scatter([], [], c='blue', s=60)

def update(frame):
    with data_lock:
        data = joint_data.copy()
    for i, (s, e) in enumerate(CONNECTIONS):
        lines[i].set_data([data[s,0], data[e,0]], [data[s,1], data[e,1]])
    joint_scatter.set_offsets(data)
    return lines + [joint_scatter]

# --------------------------
# START
# --------------------------
serial_thread = threading.Thread(target=read_serial, daemon=True)
serial_thread.start()

ani = FuncAnimation(fig, update, interval=30, blit=True)
plt.show()

running = False
serial_thread.join()