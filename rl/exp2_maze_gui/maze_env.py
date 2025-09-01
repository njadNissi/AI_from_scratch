import tkinter as tk
from tkinter import ttk
from typing import Tuple, Dict


class Maze(tk.Tk):
    """2D Maze environment for RL agents (goal = reach 'terminal' cell)."""
    def __init__(
        self,
        maze_size: Tuple[int, int] = (4, 4),  # (rows, cols) of the maze
        cell_size: int = 100,                 # Size of each cell (pixels)
        start_pos: Tuple[int, int] = (0, 0),  # Agent's starting position (row, col)
        terminal_pos: Tuple[int, int] = (3, 3)# Terminal (goal) position (row, col)
    ):
        super().__init__()
        self.title("2D Maze Environment")
        self.resizable(False, False)

        # Maze configuration
        self.n_rows, self.n_cols = maze_size
        self.cell_size = cell_size
        self.start_pos = start_pos
        self.terminal_pos = terminal_pos
        self.current_pos = start_pos  # Track agent's current position

        # Action space: 0=up, 1=right, 2=down, 3=left (4 total actions)
        self.n_actions = 4
        self.action_map: Dict[int, Tuple[int, int]] = {
            0: (-1, 0),  # Up (row-1, col)
            1: (0, 1),   # Right (row, col+1)
            2: (1, 0),   # Down (row+1, col)
            3: (0, -1)   # Left (row, col-1)
        }

        # Create maze GUI
        self._build_maze()

    def _build_maze(self) -> None:
        """Create the maze grid using Tkinter canvas."""
        # Canvas size = (cols * cell_size) x (rows * cell_size)
        self.canvas = tk.Canvas(
            self,
            width=self.n_cols * self.cell_size,
            height=self.n_rows * self.cell_size,
            bg="white"
        )
        self.canvas.pack()

        # Draw grid lines (vertical + horizontal)
        for col in range(1, self.n_cols):
            self.canvas.create_line(
                col * self.cell_size, 0,
                col * self.cell_size, self.n_rows * self.cell_size,
                fill="#CCCCCC"
            )
        for row in range(1, self.n_rows):
            self.canvas.create_line(
                0, row * self.cell_size,
                self.n_cols * self.cell_size, row * self.cell_size,
                fill="#CCCCCC"
            )

        # Draw start position (green circle)
        self._draw_cell(self.start_pos, "green")
        # Draw terminal position (red square)
        self._draw_cell(self.terminal_pos, "red", is_square=True)
        # Draw agent (blue circle, starts at start_pos)
        self.agent = self._draw_cell(self.start_pos, "blue")

    def _draw_cell(
        self,
        pos: Tuple[int, int],
        color: str,
        is_square: bool = False
    ) -> int:
        """Draw a cell (circle/square) at the given (row, col) position."""
        row, col = pos
        # Calculate top-left and bottom-right coordinates of the cell
        x1 = col * self.cell_size + 10  # +10 to leave margin
        y1 = row * self.cell_size + 10
        x2 = (col + 1) * self.cell_size - 10
        y2 = (row + 1) * self.cell_size - 10

        if is_square:
            return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
        else:
            return self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline="")

    def reset(self) -> Tuple[int, int]:
        """Reset agent to start position and return initial state."""
        self.canvas.delete(self.agent)  # Remove old agent
        self.current_pos = self.start_pos
        self.agent = self._draw_cell(self.start_pos, "blue")  # Redraw agent at start
        return self.current_pos  # Return initial state (position)

    def step(self, action: int) -> Tuple[Tuple[int, int], float, bool]:
        """
        Execute action, update agent position, and return (next_state, reward, done).
        
        Args:
            action: Integer representing action (0=up, 1=right, 2=down, 3=left)
        
        Returns:
            next_state: Agent's next position (row, col)
            reward: Reward for the action (-1=normal, 10=reach terminal, -5=hit wall)
            done: True if terminal state is reached, else False
        """
        row, col = self.current_pos
        dr, dc = self.action_map[action]  # Delta row/col from action
        next_row, next_col = row + dr, col + dc

        # Check if next position is within maze bounds (avoid wall hits)
        if 0 <= next_row < self.n_rows and 0 <= next_col < self.n_cols:
            self.current_pos = (next_row, next_col)
            # Check if next position is terminal (goal)
            if self.current_pos == self.terminal_pos:
                reward = 10.0  # Positive reward for reaching goal
                done = True
            else:
                reward = -1.0  # Small negative reward to encourage short paths
                done = False
        else:
            # Hit wall: stay in current position, negative reward
            self.current_pos = (row, col)
            reward = -5.0
            done = False

        # Update agent's position on canvas
        self.canvas.delete(self.agent)
        self.agent = self._draw_cell(self.current_pos, "blue")

        return self.current_pos, reward, done

    def render(self) -> None:
        """Update the GUI to reflect the latest maze state (non-blocking)."""
        self.update_idletasks()  # Refresh GUI without blocking training