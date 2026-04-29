import pygame
import sys

# Initialize Pygame
pygame.init()

# Sprite sheet dimensions (4 frames × 64px wide each, 64px tall)
SPRITE_SHEET_WIDTH = 256  # 4 × 64
SPRITE_SHEET_HEIGHT = 64
FRAME_SIZE = 64

# Create a surface for the sprite sheet
sprite_sheet = pygame.Surface(size=(SPRITE_SHEET_WIDTH, SPRITE_SHEET_HEIGHT), masks=pygame.SRCALPHA)

# Define colors
BACKGROUND_COLOR = (0, 0, 0, 0)  # Transparent
CHARACTER_COLOR = (255, 165, 0)  # Orange
SHADOW_COLOR = (200, 120, 0)     # Darker orange

def draw_frame_1(x_offset):
    """Standing position - frame 1"""
    # Main body (square)
    pygame.draw.rect(
        sprite_sheet, 
        CHARACTER_COLOR, 
        (x_offset + 22, 22, 20, 20)  # Centered in 64x64 frame
    )
    # Eyes
    pygame.draw.circle(sprite_sheet, (0, 0, 0), (x_offset + 30, 30), 2)
    pygame.draw.circle(sprite_sheet, (0, 0, 0), (x_offset + 38, 30), 2)
    # Shadow
    pygame.draw.ellipse(sprite_sheet, SHADOW_COLOR, (x_offset + 20, 45, 24, 5))

def draw_frame_2(x_offset):
    """Step 1 - frame 2 (tilted right)"""
    # Create a temporary surface for rotation
    temp_surface = pygame.Surface((FRAME_SIZE, FRAME_SIZE), pygame.SRCALPHA)
    
    # Draw character on temporary surface
    pygame.draw.rect(temp_surface, CHARACTER_COLOR, (22, 22, 20, 20))
    pygame.draw.circle(temp_surface, (0, 0, 0), (30, 30), 2)
    pygame.draw.circle(temp_surface, (0, 0, 0), (38, 30), 2)
    pygame.draw.ellipse(temp_surface, SHADOW_COLOR, (20, 45, 24, 5))
    
    # Rotate the surface
    rotated = pygame.transform.rotate(temp_surface, -15)  # Tilt right
    rotated_rect = rotated.get_rect(center=(x_offset + 32, 32))  # Center in frame
    
    # Blit to sprite sheet
    sprite_sheet.blit(rotated, rotated_rect)

def draw_frame_3(x_offset):
    """Step 2 - frame 3 (lifted)"""
    # Main body (square) - shifted up
    pygame.draw.rect(
        sprite_sheet, 
        CHARACTER_COLOR, 
        (x_offset + 22, 18, 20, 20)  # Higher than normal
    )
    # Eyes
    pygame.draw.circle(sprite_sheet, (0, 0, 0), (x_offset + 30, 26), 2)
    pygame.draw.circle(sprite_sheet, (0, 0, 0), (x_offset + 38, 26), 2)
    # Shadow (smaller when lifted)
    pygame.draw.ellipse(sprite_sheet, SHADOW_COLOR, (x_offset + 22, 45, 20, 4))

def draw_frame_4(x_offset):
    """Step 3 - frame 4 (tilted left)"""
    # Create a temporary surface for rotation
    temp_surface = pygame.Surface((FRAME_SIZE, FRAME_SIZE), pygame.SRCALPHA)
    
    # Draw character on temporary surface
    pygame.draw.rect(temp_surface, CHARACTER_COLOR, (22, 22, 20, 20))
    pygame.draw.circle(temp_surface, (0, 0, 0), (30, 30), 2)
    pygame.draw.circle(temp_surface, (0, 0, 0), (38, 30), 2)
    pygame.draw.ellipse(temp_surface, SHADOW_COLOR, (20, 45, 24, 5))
    
    # Rotate the surface
    rotated = pygame.transform.rotate(temp_surface, 15)  # Tilt left
    rotated_rect = rotated.get_rect(center=(x_offset + 32, 32))  # Center in frame
    
    # Blit to sprite sheet
    sprite_sheet.blit(rotated, rotated_rect)

# Draw each frame in the sprite sheet
draw_frame_1(0)       # First frame at x=0
draw_frame_2(64)      # Second frame at x=64
draw_frame_3(128)     # Third frame at x=128
draw_frame_4(192)     # Fourth frame at x=192

# Save the sprite sheet
pygame.image.save(sprite_sheet, "results/sprite_sheet1.png")
print("Sprite sheet created: sprite_sheet.png")

# Clean up
pygame.quit()
sys.exit()
    