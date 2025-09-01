import numpy as np
import pandas as pd
import time

# --------------------------
# Hyperparameters (uppercase for constants, clearer comments)
# --------------------------
np.random.seed(2)  # Ensure reproducibility
N_STATES = 6        # 1D world length (states: 0 ~ 4; terminal at "T" = index 5)
ACTIONS = ["left", "right"]  # Available actions
EPSILON = 0.9       # Greedy rate (90% exploit, 10% explore)
ALPHA = 0.1         # Learning rate (updates Q-value step size)
GAMMA = 0.9         # Discount factor (future reward importance)
MAX_EPISODES = 13   # Max training rounds
FRESH_TIME = 0.3    # Delay between each step (for visualization)


def build_q_table(n_states, actions):
    """Create initial Q-table (all zeros) with states as rows, actions as columns."""
    # Fix: Add explicit index name for clarity (states 0 ~ n_states-1)
    q_table = pd.DataFrame(
        np.zeros((n_states, len(actions))),  # Initialize Q-values to 0
        index=range(n_states),               # Rows = states (0 to n_states-1)
        columns=actions                      # Columns = available actions
    )
    return q_table


def choose_action(state, q_table):
    """Select action using epsilon-greedy strategy (explore/exploit)."""
    state_actions = q_table.iloc[state, :]  # Get all Q-values for current state
    
    # Fix 1: Logical error in "all() == 0" → use "any()" to check if state has no valid Q-values
    # Reason: "state_actions.all() == 0" is True ONLY if ALL values are 0 (correct), but "any()" is redundant here.
    # Simplify: Check if all Q-values are 0 (new state) OR random explore.
    if np.random.uniform() > EPSILON or (state_actions == 0).all():
        action_name = np.random.choice(ACTIONS)  # Explore: random action
    else:
        # Fix 2: "argmax()" returns index → map to action name (avoids integer vs string mismatch)
        action_name = state_actions.idxmax()  # Exploit: choose action with max Q-value
    return action_name


def get_env_feedback(current_state, action):
    """Return next state (S_) and reward (R) based on current state (S) and action (A)."""
    if action == "right":  # Move right
        # Terminal condition: current state is 4 (N_STATES-2 = 6-2=4) → next is "terminal"
        if current_state == N_STATES - 2:
            next_state = "terminal"
            reward = 1  # Positive reward for reaching terminal
        else:
            next_state = current_state + 1
            reward = 0  # No reward for normal moves
    else:  # Move left
        reward = 0
        if current_state == 0:  # Hit left wall → stay in place
            next_state = current_state
        else:
            next_state = current_state - 1
    return next_state, reward


def update_env(current_state, episode, step_counter):
    """Visualize the 1D environment (agent = 'o', terminal = 'T', empty = '-')."""
    # Environment structure: e.g., ["-", "-", "-", "-", "-", "T"] (N_STATES=6)
    env_list = ["-"] * (N_STATES - 1) + ["T"]
    
    if current_state == "terminal":
        # End of episode: show stats (no need to print agent)
        interaction = f"Episode {episode + 1}: Total steps = {step_counter}"
        print(f"\r{interaction}", end="")
        time.sleep(2)  # Pause to let user read stats
        print("\r" + " " * len(interaction), end="")  # Clear line for next episode
    else:
        # Show agent's current position
        env_list[current_state] = "o"
        interaction = "".join(env_list)
        print(f"\r{interaction}", end="")
        time.sleep(FRESH_TIME)  # Slow down to visualize movement


def rl():
    """Main Q-learning loop: train agent to learn optimal actions."""
    q_table = build_q_table(N_STATES, ACTIONS)  # Initialize Q-table
    
    for episode in range(MAX_EPISODES):
        step_counter = 0
        current_state = 0  # Start at state 0 (leftmost)
        is_terminated = False  # Flag for episode end
        
        update_env(current_state, episode, step_counter)  # Show initial state
        
        while not is_terminated:
            # 1. Choose action
            action = choose_action(current_state, q_table)
            # 2. Get feedback from environment
            next_state, reward = get_env_feedback(current_state, action)
            # 3. Calculate predicted Q-value (current state-action)
            # Fix 3: Use "loc" (label-based) instead of deprecated "ix"
            q_predict = q_table.loc[current_state, action]
            
            # 4. Calculate target Q-value (Bellman equation)
            if next_state != "terminal":
                # Non-terminal: target = reward + gamma * max(Q of next state)
                q_target = reward + GAMMA * q_table.iloc[next_state, :].max()
            else:
                # Terminal: target = reward (no future steps)
                q_target = reward
                is_terminated = True  # End episode after terminal
            
            # 5. Update Q-table (Bellman update rule)
            q_table.loc[current_state, action] += ALPHA * (q_target - q_predict)
            # 6. Move to next state
            current_state = next_state
            # 7. Update visualization and step counter
            step_counter += 1
            update_env(current_state, episode, step_counter)
    
    return q_table  # Return trained Q-table


if __name__ == "__main__":
    trained_q_table = rl()
    print("\nTrained Q-table:\n")
    print(trained_q_table.round(2))  # Round to 2 decimals for readability