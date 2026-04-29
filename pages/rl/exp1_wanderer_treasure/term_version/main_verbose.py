import numpy as np
import pandas as pd
import time

# --------------------------
# Hyperparameters
# --------------------------
np.random.seed(2)  # Reproducibility
N_STATES = 6        # 1D world (states: 0 ~ 4; terminal = "T" at index 5)
ACTIONS = ["left", "right"]  # Available actions
EPSILON = 0.9       # 90% exploit, 10% explore
ALPHA = 0.1         # Learning rate
GAMMA = 0.9         # Discount factor for future rewards
MAX_EPISODES = 13   # Total training episodes
FRESH_TIME = 0.3    # Delay for visualization


def build_q_table(n_states, actions):
    """Initialize Q-table (rows = states, columns = actions) with zeros."""
    q_table = pd.DataFrame(
        np.zeros((n_states, len(actions))),
        index=range(n_states),  # Label rows with state numbers (0~5)
        columns=actions
    )
    return q_table


def choose_action(state, q_table):
    """Epsilon-greedy action selection."""
    state_actions = q_table.iloc[state, :]
    
    # Explore (random) if: 10% chance, or state has no learned values yet
    if np.random.uniform() > EPSILON or (state_actions == 0).all():
        action = np.random.choice(ACTIONS)
    # Exploit (max Q-value) otherwise
    else:
        action = state_actions.idxmax()  # Returns action name (not index)
    return action


def get_env_feedback(current_state, action):
    """Return next state (S_) and reward (R) based on current action."""
    if action == "right":
        # Reach terminal if current state is 4 (N_STATES-2 = 6-2=4)
        if current_state == N_STATES - 2:
            next_state = "terminal"
            reward = 1  # Positive reward for success
        else:
            next_state = current_state + 1
            reward = 0
    else:  # Move left
        reward = 0
        if current_state == 0:  # Hit left wall → stay in place
            next_state = current_state
        else:
            next_state = current_state - 1
    return next_state, reward


def update_env(current_state, episode, step_counter):
    """Visualize the 1D environment (agent = 'o', terminal = 'T')."""
    env_list = ["-"] * (N_STATES - 1) + ["T"]  # e.g., ["-", "-", "-", "-", "-", "T"]
    
    if current_state == "terminal":
        # Show episode stats and clear line after pause
        stats = f"Episode {episode + 1} (Epoch {episode + 1}): Steps = {step_counter}"
        print(f"\r{stats}", end="")
        time.sleep(2)
        print("\r" + " " * len(stats), end="")  # Clear for next episode
    else:
        # Show agent's position
        env_list[current_state] = "o"
        print(f"\r{''.join(env_list)}", end="")
        time.sleep(FRESH_TIME)


def rl():
    """Main Q-learning loop with episode-by-episode Q-table snapshots."""
    q_table = build_q_table(N_STATES, ACTIONS)
    print("=== Starting Q-Learning Training ===")
    print(f"Initial Q-table (all zeros):\n{q_table.round(2)}\n")  # Show initial state

    for episode in range(MAX_EPISODES):
        step_counter = 0
        current_state = 0  # Start at leftmost state (0)
        is_terminated = False

        update_env(current_state, episode, step_counter)  # Visualize start

        while not is_terminated:
            # 1. Choose action
            action = choose_action(current_state, q_table)
            # 2. Get environment feedback
            next_state, reward = get_env_feedback(current_state, action)
            # 3. Calculate predicted Q-value
            q_predict = q_table.loc[current_state, action]
            # 4. Calculate target Q-value (Bellman equation)
            if next_state != "terminal":
                q_target = reward + GAMMA * q_table.iloc[next_state, :].max()
            else:
                q_target = reward
                is_terminated = True  # End episode
            
            # 5. Update Q-table (Bellman update rule)
            q_table.loc[current_state, action] += ALPHA * (q_target - q_predict)
            # 6. Move to next state and update steps
            current_state = next_state
            step_counter += 1
            update_env(current_state, episode, step_counter)  # Update visualization

        # --------------------------
        # New: Show Q-table after each episode
        # --------------------------
        print(f"\n--- After Episode {episode + 1} (Epoch {episode + 1}) ---")
        print(f"Total steps taken: {step_counter}")
        print(f"Q-table snapshot:\n{q_table.round(2)}\n")  # Round for readability

    return q_table


if __name__ == "__main__":
    trained_q_table = rl()
    # Final summary
    print("=== Training Complete ===")
    print(f"Final Trained Q-table (optimal policy):\n{trained_q_table.round(2)}")
    # Highlight optimal actions (max Q-value per state)
    optimal_actions = trained_q_table.idxmax(axis=1)
    print(f"\nOptimal actions per state:\n{optimal_actions}")