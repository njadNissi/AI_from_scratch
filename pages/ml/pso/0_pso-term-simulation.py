import numpy as np
import time
import os

# --------------------------
# PSO Parameters
# --------------------------
SWARM_SIZE = 1000        # Number of particles
DIMENSIONS = 2         # 2D problem
ITERATIONS = 100        # Number of iterations
BOUNDS = [(-5, 5), (-5, 5)]  # Search space bounds

# PSO hyperparameters
W = 0.5         # Inertia weight
C1 = 1.5        # Cognitive coefficient (personal influence)
C2 = 1.5        # Social coefficient (swarm influence)

# Function to minimize (Rosenbrock function - has a narrow valley)
def objective_function(x):
    x1, x2 = x
    return (1 - x1)**2 + 100 * (x2 - x1**2)** 2

# --------------------------
# PSO Initialization
# --------------------------
class Particle:
    def __init__(self):
        # Random initial position within bounds
        self.position = np.array([
            np.random.uniform(BOUNDS[0][0], BOUNDS[0][1]),
            np.random.uniform(BOUNDS[1][0], BOUNDS[1][1])
        ])
        
        # Random initial velocity
        self.velocity = np.array([
            np.random.uniform(-1, 1),
            np.random.uniform(-1, 1)
        ])
        
        # Personal best initialization
        self.pbest_position = self.position.copy()
        self.pbest_value = objective_function(self.position)

# Initialize swarm
swarm = [Particle() for _ in range(SWARM_SIZE)]

# Global best initialization
global_best = min(swarm, key=lambda p: p.pbest_value)
gbest_position = global_best.pbest_position.copy()
gbest_value = global_best.pbest_value

# --------------------------
# Terminal Visualization Helpers
# --------------------------
GRID_SIZE = 75  # Size of the terminal grid (20x20 characters)

def scale_to_grid(value, dim):
    """Scale a coordinate to grid position (0 to GRID_SIZE-1)"""
    min_val, max_val = BOUNDS[dim]
    return int(((value - min_val) / (max_val - min_val)) * (GRID_SIZE - 1))

def clear_terminal():
    """Clear the terminal (works on Windows and Unix)"""
    os.system('cls' if os.name == 'nt' else 'clear')

# --------------------------
# PSO Main Loop with Animation
# --------------------------
for iter in range(ITERATIONS):
    # Update each particle
    for particle in swarm:
        # 1. Update velocity
        r1, r2 = np.random.rand(), np.random.rand()  # Random coefficients
        
        cognitive_term = C1 * r1 * (particle.pbest_position - particle.position)
        social_term = C2 * r2 * (gbest_position - particle.position)
        particle.velocity = W * particle.velocity + cognitive_term + social_term
        
        # 2. Update position
        particle.position += particle.velocity
        
        # 3. Keep position within bounds
        for i in range(DIMENSIONS):
            particle.position[i] = np.clip(
                particle.position[i], 
                BOUNDS[i][0], 
                BOUNDS[i][1]
            )
        
        # 4. Update personal best
        current_value = objective_function(particle.position)
        if current_value < particle.pbest_value:
            particle.pbest_value = current_value
            particle.pbest_position = particle.position.copy()
    
    # Update global best
    current_best = min(swarm, key=lambda p: p.pbest_value)
    if current_best.pbest_value < gbest_value:
        gbest_value = current_best.pbest_value
        gbest_position = current_best.pbest_position.copy()
    
    # --------------------------
    # Draw terminal animation
    # --------------------------
    clear_terminal()
    
    # Print status
    print(f"PSO Animation - Iteration {iter+1}/{ITERATIONS}")
    print(f"Global Best Value: {gbest_value:.4f}")
    print(f"Global Best Position: ({gbest_position[0]:.2f}, {gbest_position[1]:.2f})")
    print("-" * (GRID_SIZE + 2))
    
    # Create empty grid
    grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    # Mark particles on grid
    for i, particle in enumerate(swarm):
        x = scale_to_grid(particle.position[0], 0)
        y = scale_to_grid(particle.position[1], 1)
        grid[y][x] = str(i % 10)  # Use 0-9 for particle IDs
    
    # Mark global best on grid
    gx = scale_to_grid(gbest_position[0], 0)
    gy = scale_to_grid(gbest_position[1], 1)
    grid[gy][gx] = 'G'  # 'G' for global best
    
    # Draw grid
    for row in grid:
        print(f"|{''.join(row)}|")
    print("-" * (GRID_SIZE + 2))
    
    # Pause for animation effect
    time.sleep(0.3)

print("\nOptimization complete!")
print(f"Final Global Best: Position = ({gbest_position[0]:.4f}, {gbest_position[1]:.4f}), Value = {gbest_value:.6f}")
