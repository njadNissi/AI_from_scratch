from maze_env import Maze
from rl_brain import SarsaTable


def train_sarsa(
    episodes: int = 100,
    learning_rate: float = 0.01,
    reward_decay: float = 0.9,
    e_greedy: float = 0.9
) -> None:
    """Train a SARSA agent on the maze environment."""
    # Initialize environment and agent
    env = Maze()
    rl_agent = SarsaTable(
        actions=list(range(env.n_actions)),  # Actions: [0,1,2,3]
        learning_rate=learning_rate,
        reward_decay=reward_decay,
        e_greedy=e_greedy
    )

    def update() -> None:
        """Inner training loop (called by Tkinter after() to avoid blocking)."""
        for episode in range(episodes):
            # Reset environment and get initial state (convert to string for Q-table)
            observation = env.reset()
            observation_str = str(observation)
            
            # Choose first action based on initial state
            action = rl_agent.choose_action(observation_str)
            
            total_reward = 0  # Track total reward per episode (for debugging)
            step_count = 0    # Track steps per episode (for debugging)

            while True:
                # Render maze (update GUI)
                env.render()
                
                # Execute action and get feedback from environment
                observation_next, reward, done = env.step(action)
                observation_next_str = str(observation_next) if not done else "terminal"
                
                # Choose next action (SARSA needs next action for learning)
                action_next = rl_agent.choose_action(observation_next_str)
                
                # Agent learns from (s, a, r, s', a') transition
                rl_agent.learn(observation_str, action, reward, observation_next_str, action_next)
                
                # Update state, action, and metrics
                observation_str = observation_next_str
                action = action_next
                total_reward += reward
                step_count += 1

                # End episode if terminal state is reached
                if done:
                    print(f"Episode {episode+1:3d} | Steps: {step_count:3d} | Total Reward: {total_reward:5.1f}")
                    break

        # After all episodes: print final Q-table and close environment
        print("\nFinal SARSA Q-Table:")
        print(rl_agent.q_table.round(2))  # Round for readability
        print("\nTraining complete! Closing maze...")
        env.destroy()

    # Start training (delay 100ms to let GUI initialize)
    env.after(100, update)
    env.mainloop()


if __name__ == "__main__":
    train_sarsa(
        episodes=100,
        learning_rate=0.01,
        reward_decay=0.9,
        e_greedy=0.9
    )