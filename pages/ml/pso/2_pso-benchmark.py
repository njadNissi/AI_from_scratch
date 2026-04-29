import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import sys

# --- Benchmark Functions (Simplified for brevity) ---
def create_benchmark(function):
    # (Keeping the logic from your notebook)
    if function == "Objective":
        a = (0, 5)
        x, y = np.array(np.meshgrid(np.linspace(0, 5, 100), np.linspace(0, 5, 100)))
        def fx(x, y): return (x - 3.14)**2 + (y - 2.72)**2 + np.sin(3*x + 1.41) + np.sin(4*y - 1.73)
        return fx(x, y), x, y, a, fx
    # ... (Add other functions here as needed)
    return None

# --- PSO Logic ---
def update():
    global V, X, pbest, pbest_obj, gbest, gbest_obj
    r1, r2 = np.random.rand(2)
    V = w * V + c1 * r1 * (pbest - X) + c2 * r2 * (gbest.reshape(-1, 1) - X)
    X = X + V
    obj = fx(X[0], X[1])
    pbest[:, (pbest_obj >= obj)] = X[:, (pbest_obj >= obj)]
    pbest_obj = np.array([pbest_obj, obj]).min(axis=0)
    gbest = pbest[:, pbest_obj.argmin()]
    gbest_obj = pbest_obj.min()

def animate(i):
    update()
    ax.set_title(f'PSO Iteration {i:02d} | Best: {gbest_obj:.4f}')
    pbest_plot.set_offsets(pbest.T)
    p_plot.set_offsets(X.T)
    p_arrow.set_offsets(X.T)
    p_arrow.set_UVC(V[0], V[1])
    gbest_plot.set_offsets(gbest.reshape(1, -1))
    return ax, pbest_plot, p_plot, p_arrow, gbest_plot

if __name__ == "__main__":
    # 1. Setup Environment & Artifacts Path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    artifacts_dir = os.path.join(script_dir, "artifacts")
    os.makedirs(artifacts_dir, exist_ok=True)
    
    # 2. Initialize Parameters
    c1, c2, w = 0.8, 0.8, 0.6
    n_particles = 100
    z, x, y, a, fx = create_benchmark("Objective")
    
    # Global minimum for reference
    x_min, y_min = x.ravel()[z.argmin()], y.ravel()[z.argmin()]

    # Initialize Swarm
    X = np.random.rand(2, n_particles) * 5
    V = np.random.randn(2, n_particles) * 0.1
    pbest = X.copy()
    pbest_obj = fx(X[0], X[1])
    gbest = pbest[:, pbest_obj.argmin()]
    gbest_obj = pbest_obj.min()

    # 3. Setup Plot
    fig, ax = plt.subplots(figsize=(10, 8))
    img = ax.imshow(z, extent=[a[0], a[1], a[0], a[1]], origin='lower', cmap='viridis', alpha=0.5)
    ax.plot([x_min], [y_min], marker='x', markersize=20, color="red", label="Global Optima")
    pbest_plot = ax.scatter(pbest[0], pbest[1], marker='o', color='black', alpha=0.3)
    p_plot = ax.scatter(X[0], X[1], marker='o', color='blue', alpha=0.6)
    p_arrow = ax.quiver(X[0], X[1], V[0], V[1], color='blue', alpha=0.4)
    gbest_plot = ax.scatter([gbest[0]], [gbest[1]], marker='*', s=150, color='yellow', edgecolors='black')
    
    # 4. Generate Animation
    print("🚀 Starting Particle Swarm Optimization...")
    anim = FuncAnimation(fig, animate, frames=200, interval=200, blit=False)
    
    # 5. Save as MP4 into the Artifacts folder
    video_path = os.path.join(artifacts_dir, "pso_optimization.mp4")
    print(f"📹 Saving animation to artifacts...")
    anim.save(video_path, writer='ffmpeg', fps=60)
    
    print(f"✅ Finished!")
    print(f"Final PSO Solution: {gbest_obj:.6f} at {gbest}")
    print(f"Actual Global Minimum: {z.min():.6f}")