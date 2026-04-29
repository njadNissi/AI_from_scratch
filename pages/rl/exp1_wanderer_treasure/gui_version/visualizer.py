# pygame_visualization.py
# Purpose: Visualize the Q-learning agent (O) moving toward the treasure (T)
# Dependencies: Requires rl_model.py (imports the QLearning class)
import pygame
import sys
from q_learning_core import QLearning  # Import our RL agent

# --------------------------
# 1. Pygame Core Settings (Graphics/Window)
# --------------------------
SCREEN_WIDTH = 800  # Width of the visualization window
SCREEN_HEIGHT = 200  # Height of the window (small for focus on the path)
CELL_SIZE = 100  # Size of each "position" on the path (O moves between these)
FPS = 3  # Frames per second (slower = easier to see left/right choices)

# Color definitions (for clarity: O=blue, T=yellow, path=black)
WHITE = (255, 255, 255)  # Background color
BLUE = (0, 0, 255)       # Wanderer (O) color
YELLOW = (255, 255, 0)   # Treasure (T) color
BLACK = (0, 0, 0)        # Path and text color

# --------------------------
# 2. RL Simulation Settings (Matches the Agent's Logic)
# --------------------------
NUM_STATES = 6  # Total positions (states) for O: 0 (start) → 1 → 2 → 3 → 4 → 5 (treasure)
NUM_ACTIONS = 2  # Actions the agent can take: 0=left, 1=right
EPISODES = 20    # Number of training rounds (enough to let O unlearn left moves)
START_STATE = 0  # O's starting position (leftmost)
TREASURE_STATE = NUM_STATES - 1  # O's goal position (rightmost: state 5)

# --------------------------
# 3. Helper Functions (Draw Graphics/Text)
# --------------------------
def draw_environment(screen, wanderer_pos, episode, steps, last_action):
    """
    Draw everything on the screen:
    - Background + path
    - Wanderer (O) and treasure (T)
    - Training info (episode, steps, last action)
    """
    # Clear the screen with white (resets for each frame)
    screen.fill(WHITE)

    # Draw the horizontal path (where O moves) — centered vertically
    path_y = SCREEN_HEIGHT // 2  # Y-coordinate of the path
    pygame.draw.line(
        screen, 
        BLACK, 
        (50, path_y),  # Start of path (left side, 50px from edge)
        (SCREEN_WIDTH - 50, path_y),  # End of path (right side, 50px from edge)
        2  # Line thickness
    )

    # Helper: Convert a "state" (0-5) to an on-screen X-coordinate
    # Ensures O/T are centered in their respective "cells"
    def state_to_x(state):
        return 50 + (state * CELL_SIZE) + (CELL_SIZE // 2)

    # Draw Wanderer (O): Blue circle with "O" text inside
    wanderer_x = state_to_x(wanderer_pos)  # Get X for O's current state
    pygame.draw.circle(screen, BLUE, (wanderer_x, path_y), 30)  # Draw circle
    draw_text(screen, "O", BLACK, wanderer_x, path_y - 10, size=36)  # Add text

    # Draw Treasure (T): Yellow square with "T" text inside
    treasure_x = state_to_x(TREASURE_STATE)  # Get X for T's state (5)
    # Draw square (centered on the path)
    treasure_rect = pygame.Rect(
        treasure_x - 30,  # Left X of square
        path_y - 30,      # Top Y of square
        60, 60            # Width/height of square
    )
    pygame.draw.rect(screen, YELLOW, treasure_rect)
    draw_text(screen, "T", BLACK, treasure_x, path_y - 10, size=36)  # Add text

    # Draw training status (so we can track progress)
    status_text1 = f"Episode: {episode + 1}/{EPISODES} | Steps: {steps}"  # Episode/step count
    status_text2 = f"Last Move: {last_action}"  # Show if O moved left/right
    draw_text(screen, status_text1, BLACK, SCREEN_WIDTH // 2, 30, size=20)  # Top text
    draw_text(screen, status_text2, BLACK, SCREEN_WIDTH // 2, 60, size=20)  # Bottom text

    # Update the display to show the new frame
    pygame.display.flip()

def draw_text(screen, text, color, x, y, size=24):
    """Helper to draw centered text (avoids repeating code for text rendering)"""
    # Create a font object (None = use default font, size = text size)
    font = pygame.font.Font(None, size)
    # Render text to a surface (True = anti-aliased text)
    text_surface = font.render(text, True, color)
    # Center the text on the target (x, y) position
    text_rect = text_surface.get_rect(center=(x, y))
    # Draw the text onto the screen
    screen.blit(text_surface, text_rect)

# --------------------------
# 4. Main Simulation Loop (RL + Visualization)
# --------------------------
def main():
    # Initialize Pygame (required to start the window)
    pygame.init()
    # Create the visualization window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Set window title
    pygame.display.set_caption("RL Wanderer (O) Learns to Find Treasure (T)")
    # Clock to control FPS (ensures consistent speed)
    clock = pygame.time.Clock()

    # Initialize our RL agent (pass settings that match our scenario)
    rl_agent = QLearning(
        num_states=NUM_STATES,  # 6 positions
        num_actions=NUM_ACTIONS  # 2 actions: left/right
    )

    # Run training episodes (each episode = O tries to reach T once)
    for episode in range(EPISODES):
        # Reset state for new episode: O starts at the leftmost position
        current_state = START_STATE
        steps = 0  # Track how many steps O takes this episode (goal: minimize)
        done = False  # Flag to check if O reached T (ends the episode)
        last_action = "Start"  # For visualization (show O's first move)

        # Episode loop: O moves until it reaches T
        while not done:
            # --------------------------
            # Handle Pygame Events (e.g., closing the window)
            # --------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Clean up Pygame and exit if window is closed
                    pygame.quit()
                    sys.exit()

            # --------------------------
            # RL Agent Step 1: Choose Action (Left/Right)
            # --------------------------
            action = rl_agent.choose_action(current_state)
            # Update last_action for visualization (make it human-readable)
            last_action = "Left (←)" if action == 0 else "Right (→)"

            # --------------------------
            # RL Agent Step 2: Execute Action (Move O on Screen)
            # --------------------------
            if action == 0:  # Action = Left
                # Prevent O from moving left of the start (state 0) — invalid move
                next_state = max(current_state - 1, START_STATE)
            else:  # Action = Right
                # Prevent O from moving right of the treasure (state 5) — invalid move
                next_state = min(current_state + 1, TREASURE_STATE)

            # Increment step count (each move = 1 step)
            steps += 1

            # --------------------------
            # RL Agent Step 3: Assign Reward (Teach O "Good/Bad" Moves)
            # --------------------------
            if next_state == TREASURE_STATE:
                # Reward: +20 (big positive reward for reaching T — this is the goal!)
                reward = 20
                done = True  # End the episode (O succeeded)
            elif action == 0:
                # Penalty: -5 (heavily punish left moves — they slow progress)
                reward = -5
            else:
                # Penalty: -1 (small punishment for right moves — encourages speed, not lingering)
                reward = -1

            # --------------------------
            # RL Agent Step 4: Learn from Experience (Update Q-table)
            # --------------------------
            rl_agent.update_q_table(
                current_state=current_state,
                action=action,
                reward=reward,
                next_state=next_state
            )

            # --------------------------
            # Visualization Step: Draw Current State
            # --------------------------
            draw_environment(screen, current_state, episode, steps, last_action)
            # Control speed (wait to match FPS)
            clock.tick(FPS)

            # --------------------------
            # Move to Next State (Prepare for Next Frame)
            # --------------------------
            current_state = next_state

        # Pause for 1 second after each episode (let you see the final step of the episode)
        pygame.time.wait(1000)

    # --------------------------
    # Post-Training: Keep Window Open
    # --------------------------
    while True:
        # Handle window close event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Draw the final state (O at T) with a "done" message
        draw_environment(screen, TREASURE_STATE, EPISODES, steps, "Done (Learned!)")
        clock.tick(FPS)