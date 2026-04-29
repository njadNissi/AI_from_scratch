import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

# 1. Define the Objective Function: f(x) = x^2 - 4x + 3
def objective_function(x):
    return x**2 - 4*x + 3

def pso_1d_simulation():
    # --- Configuration ---
    script_dir = os.path.dirname(os.path.abspath(__file__))
    artifacts_dir = os.path.join(script_dir, "artifacts")
    os.makedirs(artifacts_dir, exist_ok=True)

    # PSO Hyperparameters
    w = 0.5   # Inertia
    c1 = 1.5  # Cognitive (personal best)
    c2 = 1.5  # Social (global best)
    n_particles = 100
    iterations = 50

    # Initialize Particles
    # Positions x between -5 and 10
    x = np.random.uniform(-5, 10, n_particles)
    v = np.random.uniform(-1, 1, n_particles)
    
    pbest = x.copy()
    pbest_fitness = objective_function(pbest)
    gbest = pbest[np.argmin(pbest_fitness)]
    gbest_fitness = np.min(pbest_fitness)

    # --- Setup Plotting ---
    fig, ax = plt.subplots(figsize=(10, 8))
    x_range = np.linspace(-6, 11, 400)
    y_range = objective_function(x_range)
    
    ax.plot(x_range, y_range, 'b-', label='f(x) = x² - 4x + 3', alpha=0.6)
    ax.axhline(0, color='black', lw=1)
    ax.axvline(2, color='red', linestyle='--', label='Global Minimum (x=2)', alpha=0.5)
    
    # Plot elements to update
    particles_plot, = ax.plot(x, objective_function(x), 'go', label='Particles')
    pbest_plot, = ax.plot(pbest, pbest_fitness, 'y.', alpha=0.5, label='Personal Bests')
    gbest_plot, = ax.plot(gbest, gbest_fitness, 'r*', markersize=15, label='Global Best')
    
    ax.set_title("PSO 1D Optimization")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()

    # --- Animation Logic ---
    def animate(i):
        nonlocal x, v, pbest, pbest_fitness, gbest, gbest_fitness
        
        # PSO Update Rules
        r1, r2 = np.random.rand(), np.random.rand()
        v = w*v + c1*r1*(pbest - x) + c2*r2*(gbest - x)
        x = x + v
        
        fitness = objective_function(x)
        
        # Update Personal Best
        better_mask = fitness < pbest_fitness
        pbest[better_mask] = x[better_mask]
        pbest_fitness[better_mask] = fitness[better_mask]
        
        # Update Global Best
        if np.min(pbest_fitness) < gbest_fitness:
            gbest = pbest[np.argmin(pbest_fitness)]
            gbest_fitness = np.min(pbest_fitness)
            
        # Update Plots
        particles_plot.set_data(x, fitness)
        pbest_plot.set_data(pbest, pbest_fitness)
        gbest_plot.set_data([gbest], [gbest_fitness])
        ax.set_title(f"Iteration {i+1}/{iterations} | Best x: {gbest:.4f}")
        
        return particles_plot, pbest_plot, gbest_plot

    # --- Execution ---
    print(f"🚀 Initializing 1D PSO for {iterations} iterations...")
    ani = animation.FuncAnimation(fig, animate, frames=iterations, interval=200, blit=True)
    
    video_path = os.path.join(artifacts_dir, "pso_1d_run.mp4")
    print(f"📹 Saving animation to: {video_path}")
    
    # Requires ffmpeg
    ani.save(video_path, writer='ffmpeg', fps=60)
    
    plt.close() # Prevents extra window from hanging
    print(f"✅ Simulation Complete. Final Global Best at x = {gbest:.4f}")

if __name__ == "__main__":
    pso_1d_simulation()