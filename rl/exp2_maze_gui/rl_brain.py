import numpy as np
import pandas as pd
from typing import List, Union, Optional


class RL:
    """Base class for Reinforcement Learning agents (Q-Learning/SARSA)."""
    def __init__(
        self,
        action_space: List[int],  # List of available actions (e.g., [0,1,2,3] for up/down/left/right)
        learning_rate: float = 0.01,
        reward_decay: float = 0.9,
        e_greedy: float = 0.9
    ):
        self.actions = action_space  # Action set (e.g., [0,1,2,3])
        self.lr = learning_rate      # Learning rate (α)
        self.gamma = reward_decay    # Discount factor (γ)
        self.epsilon = e_greedy      # Greedy rate (ε)
        # Initialize Q-table (rows=states, columns=actions; states added dynamically)
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)

    def check_state_exist(self, state: str) -> None:
        """Add new state to Q-table if it doesn’t exist (dynamic state handling)."""
        if state not in self.q_table.index:
            # Use pd.concat (replace deprecated append()) to add new state
            new_state_row = pd.DataFrame(
                data=[[0.0] * len(self.actions)],
                index=[state],
                columns=self.q_table.columns
            )
            self.q_table = pd.concat([self.q_table, new_state_row], ignore_index=False)

    def choose_action(self, observation: str) -> int:
        """Choose action via ε-greedy strategy (explore/exploit)."""
        self.check_state_exist(observation)  # Ensure current state is in Q-table
        
        # Exploit (choose best action) with probability ε
        if np.random.rand() < self.epsilon:
            state_actions = self.q_table.loc[observation, :]  # Replace deprecated ix() with loc()
            # Shuffle actions with same Q-value to avoid bias (e.g., always choosing first max)
            state_actions_shuffled = state_actions.sample(frac=1)  # More readable than permutation
            action = state_actions_shuffled.idxmax()  # Get action with max Q-value
        # Explore (random action) with probability 1-ε
        else:
            action = np.random.choice(self.actions)
        
        return action

    def learn(self, *args) -> None:
        """Abstract method for learning (implemented in child classes)."""
        raise NotImplementedError("Learn method must be overridden in child classes!")


class QLearningTable(RL):
    """Off-policy Q-Learning agent (learns optimal policy independently of behavior)."""
    def __init__(
        self,
        actions: List[int],
        learning_rate: float = 0.01,
        reward_decay: float = 0.9,
        e_greedy: float = 0.9
    ):
        # Inherit __init__ from base RL class
        super().__init__(actions, learning_rate, reward_decay, e_greedy)

    def learn(
        self,
        s: str,        # Current state
        a: int,        # Action taken
        r: float,      # Reward received
        s_: str        # Next state
    ) -> None:
        """Update Q-table using Q-Learning update rule: Q(s,a) ← Q(s,a) + α[R + γ·maxQ(s',·) - Q(s,a)]"""
        self.check_state_exist(s_)  # Ensure next state is in Q-table
        
        # Current predicted Q-value
        q_predict = self.q_table.loc[s, a]
        
        # Calculate target Q-value (Bellman equation)
        if s_ != "terminal":
            # Non-terminal: target = reward + discounted max Q-value of next state
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()
        else:
            # Terminal: target = only immediate reward (no future steps)
            q_target = r
        
        # Update Q-value
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)


class SarsaTable(RL):
    """On-policy SARSA agent (learns policy that matches its behavior)."""
    def __init__(
        self,
        actions: List[int],
        learning_rate: float = 0.01,
        reward_decay: float = 0.9,
        e_greedy: float = 0.9
    ):
        # Inherit __init__ from base RL class
        super().__init__(actions, learning_rate, reward_decay, e_greedy)

    def learn(
        self,
        s: str,        # Current state
        a: int,        # Action taken
        r: float,      # Reward received
        s_: str,       # Next state
        a_: int        # Next action to take (key difference from Q-Learning)
    ) -> None:
        """Update Q-table using SARSA update rule: Q(s,a) ← Q(s,a) + α[R + γ·Q(s',a') - Q(s,a)]"""
        self.check_state_exist(s_)  # Ensure next state is in Q-table
        
        # Current predicted Q-value
        q_predict = self.q_table.loc[s, a]
        
        # Calculate target Q-value (Bellman equation)
        if s_ != "terminal":
            # Non-terminal: target = reward + discounted Q-value of (next state, next action)
            q_target = r + self.gamma * self.q_table.loc[s_, a_]
        else:
            # Terminal: target = only immediate reward
            q_target = r
        
        # Update Q-value
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)