"""Purpose: Defines a Q-learning agent that can choose left/right actions 
    and learn optimal behavior"""
import numpy as np

class QLearning:
    def __init__(self, num_states, num_actions, learning_rate=0.1, discount_factor=0.95, epsilon=0.1):
        """
        Initialize Q-learning parameters
        - num_states: Total positions (e.g., 6 positions for O-----T)
        - num_actions: Possible moves (only 1 here: move right)
        - learning_rate: How much to update Q-values each step
        - discount_factor: Importance of future rewards
        - epsilon: Chance to explore (vs exploit known good actions)
        """
        self.num_states = num_states
        self.num_actions = num_actions
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon

        # Initialize Q-table (states x actions) with small random values
        self.q_table = np.random.uniform(low=-0.1, high=0.1, size=(num_states, num_actions))

    def choose_action(self, current_state):
        """Choose action: explore (random) or exploit (best Q-value)"""
        if np.random.uniform(0, 1) < self.epsilon:
            # Explore: random action (only 1 action here, so always move right)
            return np.random.choice(self.num_actions)
        else:
            # Exploit: choose action with highest Q-value for current state
            return np.argmax(self.q_table[current_state, :])

    def update_q_table(self, current_state, action, reward, next_state):
        """Update Q-value using the Bellman equation"""
        # Current Q-value for (state, action)
        current_q = self.q_table[current_state, action]
        # Maximum Q-value for the next state (future reward)
        max_next_q = np.max(self.q_table[next_state, :])
        # Bellman equation: update Q to reflect new reward
        new_q = current_q + self.lr * (reward + self.gamma * max_next_q - current_q)
        self.q_table[current_state, action] = new_q