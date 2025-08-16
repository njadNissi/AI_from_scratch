import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Animation")

# Colors
BACKGROUND_COLOR = (50, 50, 50)

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_path, frame_width, frame_height, frame_count):
        super().__init__()
        
        # Load and process sprite sheet
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert_alpha()
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.frame_count = frame_count
        self.frames = []
        
        # Extract frames from sprite sheet
        for i in range(frame_count):
            frame_rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = self.sprite_sheet.subsurface(frame_rect)
            self.frames.append(frame)
        
        # Animation settings
        self.current_frame = 0
        self.animation_speed = 0.15
        self.animation_timer = 0
        
        # Set initial image
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    
    def update(self, dt):
        # Update animation
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.current_frame = (self.current_frame + 1) % self.frame_count
            self.image = self.frames[self.current_frame]
            self.animation_timer = 0

# Create sprite group
all_sprites = pygame.sprite.Group()

# Note: You'll need a sprite sheet image file for this to work
# Create animated sprite (replace with your own sprite sheet)
# For testing, you can create a simple sprite sheet with 4 frames, 64x64 each
try:
    player = AnimatedSprite(
        "results/sprite_sheet2.png",  # Replace with your sprite sheet path
        64,  # Frame width
        64,  # Frame height
        4    # Number of frames
    )
    all_sprites.add(player)
except FileNotFoundError:
    print("Error: Sprite sheet not found! Please create a sprite_sheet.png file.")
    pygame.quit()
    sys.exit()

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(60) / 1000.0  # Delta time in seconds
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update sprites
    all_sprites.update(dt)
    
    # Drawing
    screen.fill(BACKGROUND_COLOR)
    all_sprites.draw(screen)
    
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
    