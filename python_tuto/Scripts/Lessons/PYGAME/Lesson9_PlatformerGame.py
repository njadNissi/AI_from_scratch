import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Platformer")

# Colors
SKY_BLUE = (135, 206, 235)
GROUND_COLOR = (34, 139, 34)
PLAYER_COLOR = (255, 165, 0)
PLATFORM_COLOR = (139, 69, 19)

# Player settings
player_size = 40
player = pygame.Vector2(SCREEN_WIDTH // 2 - player_size // 2, SCREEN_HEIGHT // 2 - player_size // 2)
player_velocity = pygame.Vector2(0, 0)
player_speed = 5
gravity = 0.5
jump_strength = -12
on_ground = False

# Platforms
platforms = [
    pygame.Rect(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40),  # Ground
    pygame.Rect(200, 450, 150, 20),
    pygame.Rect(450, 400, 150, 20),
    pygame.Rect(200, 350, 150, 20),
    pygame.Rect(450, 300, 150, 20),
    pygame.Rect(300, 200, 150, 20)
]

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Jump on spacebar press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                player_velocity.y = jump_strength
                on_ground = False

    # Player movement
    keys = pygame.key.get_pressed()
    player_velocity.x = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed

    # Apply gravity
    player_velocity.y += gravity
    player.y += player_velocity.y
    player.x += player_velocity.x

    # Create player rect for collision
    player_rect = pygame.Rect(player.x, player.y, player_size, player_size)
    
    # Collision detection
    on_ground = False
    for platform in platforms:
        if player_rect.colliderect(platform):
            # Collision from above
            if player_velocity.y > 0:
                player.y = platform.top - player_size
                player_velocity.y = 0
                on_ground = True
            # Collision from below
            elif player_velocity.y < 0:
                player.y = platform.bottom
                player_velocity.y = 0

    # Keep player within screen bounds
    if player.x < 0:
        player.x = 0
    if player.x > SCREEN_WIDTH - player_size:
        player.x = SCREEN_WIDTH - player_size

    # Drawing
    screen.fill(SKY_BLUE)
    
    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(surface=screen, color=PLATFORM_COLOR, rect=platform)
    
    # Draw player
    pygame.draw.rect(surface=screen, color=PLAYER_COLOR, rect=player_rect)

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
    