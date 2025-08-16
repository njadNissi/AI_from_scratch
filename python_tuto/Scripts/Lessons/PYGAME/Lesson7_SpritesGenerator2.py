import pygame
import sys
import os  # Added for folder handling

# Initialize Pygame
pygame.init()

# Sprite sheet dimensions (4 frames × 64px wide each, 64px tall)
SPRITE_SHEET_WIDTH = 256  # 4 × 64
SPRITE_SHEET_HEIGHT = 64
FRAME_SIZE = 64

# Create results folder if it doesn't exist
os.makedirs("results", exist_ok=True)

# Create a surface for the sprite sheet with transparency
sprite_sheet = pygame.Surface((SPRITE_SHEET_WIDTH, SPRITE_SHEET_HEIGHT), pygame.SRCALPHA)

# Colors
BLACK = (0, 0, 0)
HEAD_COLOR = (30, 144, 255)  # Dodger blue

def draw_stick_figure_1(x_offset):
    """Frame 1: Standing position"""
    center_x = x_offset + 32  # Horizontal center of frame
    center_y = 32  # Vertical center of frame (fixed)
    
    # Head
    pygame.draw.circle(sprite_sheet, HEAD_COLOR, (center_x, center_y - 12), 8)
    
    # Body
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y - 4), (center_x, center_y + 13), 2)
    
    # Arms (outstretched)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y), (center_x - 12, center_y + 8), 2)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y), (center_x + 12, center_y + 8), 2)
    
    # Legs (slightly apart)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y + 13), (center_x - 8, center_y + 33), 2)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y + 13), (center_x + 8, center_y + 33), 2)

def draw_stick_figure_2(x_offset):
    """Frame 2: Right leg forward, left arm forward"""
    center_x = x_offset + 32
    center_y = 32  # Fixed vertical center
    
    # Head
    pygame.draw.circle(sprite_sheet, HEAD_COLOR, (center_x, center_y - 12), 8)
    
    # Body (slightly tilted)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y - 4), (center_x + 2, center_y + 13), 2)
    
    # Arms (left forward, right back)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y), (center_x - 15, center_y + 3), 2)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y), (center_x + 10, center_y + 10), 2)
    
    # Legs (right forward, left back)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y + 13), (center_x + 10, center_y + 28), 2)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y + 13), (center_x - 8, center_y + 36), 2)

def draw_stick_figure_3(x_offset):
    """Frame 3: One leg up, arms in middle position"""
    center_x = x_offset + 32
    center_y = 32  # Fixed vertical center
    
    # Head
    pygame.draw.circle(sprite_sheet, HEAD_COLOR, (center_x, center_y - 12), 8)
    
    # Body
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y - 4), (center_x, center_y + 13), 2)
    
    # Arms (more centered)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y), (center_x - 10, center_y + 6), 2)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y), (center_x + 10, center_y + 6), 2)
    
    # Legs (one up, one down)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y + 13), (center_x - 5, center_y + 28), 2)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y + 13), (center_x + 8, center_y + 36), 2)

def draw_stick_figure_4(x_offset):
    """Frame 4: Left leg forward, right arm forward"""
    center_x = x_offset + 32
    center_y = 32  # Fixed vertical center
    
    # Head
    pygame.draw.circle(sprite_sheet, HEAD_COLOR, (center_x, center_y - 12), 8)
    
    # Body (slightly tilted)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y - 4), (center_x - 2, center_y + 13), 2)
    
    # Arms (right forward, left back)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y), (center_x - 10, center_y + 10), 2)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y), (center_x + 15, center_y + 3), 2)
    
    # Legs (left forward, right back)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y + 13), (center_x - 10, center_y + 28), 2)
    pygame.draw.line(sprite_sheet, BLACK, (center_x, center_y + 13), (center_x + 8, center_y + 36), 2)

# Draw each frame in the sprite sheet
draw_stick_figure_1(0)    # First frame at x=0
draw_stick_figure_2(64)   # Second frame at x=64
draw_stick_figure_3(128)  # Third frame at x=128
draw_stick_figure_4(192)  # Fourth frame at x=192

# Save the sprite sheet with consistent naming
output_path = "results/sprite_sheet2.png"
pygame.image.save(sprite_sheet, output_path)
print(f"Stick figure sprite sheet created: {output_path}")

# Clean up
pygame.quit()
sys.exit()
    