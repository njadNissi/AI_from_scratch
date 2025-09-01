from maze_env import Maze
from rl_brain import QLearningTable


def train_qlearning(
    episodes: int = 100,
    learning_rate: float = 0.01,
    reward_decay: float = 0.9,
    e_greedy: float = 0.9
) -> None:
    """Train an off-policy Q-Learning agent on the 2D Maze environment."""
    # 1. Initialize maze environment and Q-Learning agent
    env = Maze()
    rl_agent = QLearningTable(
        actions=list(range(env.n_actions)),  # Actions: 0=up, 1=right, 2=down, 3=left
        learning_rate=learning_rate,
        reward_decay=reward_decay,
        e_greedy=e_greedy
    )

    def update() -> None:
        """Core training loop (non-blocking via Tkinter after())."""
        for episode in range(episodes):
            # 2. Reset environment for new episode
            observation = env.reset()  # Get initial position (e.g., (0,0))
            observation_str = str(observation)  # Convert to string for Q-table index
            
            # Track metrics for debugging/analysis
            total_reward = 0.0
            step_count = 0

            # 3. Episode loop (run until terminal state)
            while True:
                # 4. Render maze (update GUI to show agent's current position)
                env.render()

                # 5. Agent chooses action (ε-greedy)
                action = rl_agent.choose_action(observation_str)

                # 6. Execute action: get next state, reward, and terminal flag
                observation_next, reward, done = env.step(action)
                # Convert next state to string (use "terminal" if episode ends)
                observation_next_str = str(observation_next) if not done else "terminal"

                # 7. Agent learns (Q-Learning update: no next action needed!)
                rl_agent.learn(
                    s=observation_str,
                    a=action,
                    r=reward,
                    s_=observation_next_str
                )

                # 8. Update state and metrics
                observation_str = observation_next_str
                total_reward += reward
                step_count += 1

                # 9. End episode if terminal state (goal) is reached
                if done:
                    print(f"Episode {episode+1:3d} | Steps: {step_count:3d} | Total Reward: {total_reward:6.1f}")
                    break

        # 10. Post-training: Print results and close environment
        print("\n" + "="*50)
        print("Final Q-Learning Q-Table (rounded to 2 decimals):")
        print(rl_agent.q_table.round(2))
        print("\nTraining complete! Closing maze window...")
        print("="*50)
        env.destroy()

    # 11. Start training (delay 100ms to let Tkinter GUI initialize first)
    env.after(100, update)
    env.mainloop()


# Run training when the file is executed directly
if __name__ == "__main__":
    train_qlearning(
        episodes=100,    # Number of training rounds
        learning_rate=0.01,  # Step size for Q-value updates
        reward_decay=0.9,    # Importance of future rewards
        e_greedy=0.9     # 90% exploit (choose best action), 10% explore (random)
    )