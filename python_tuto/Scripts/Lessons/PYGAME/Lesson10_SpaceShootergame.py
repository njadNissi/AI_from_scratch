import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter")

# Colorsa: R G B
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player_x = SCREEN_WIDTH // 2 - player_size // 2
player_y = SCREEN_HEIGHT - player_size - 10
player_speed = 7

# Laser settings
laser_size = (5, 20)
laser_speed = 10
lasers = []

# Enemy settings
enemy_size = 40
enemy_speed = 3
enemies = []
enemy_spawn_rate = 50  # Lower = more frequent spawns
spawn_counter = 0

# Game variables
score = 0
font = pygame.font.SysFont(None, 36)

def draw_player():
    """Draw the player ship"""
    # Main body
    pygame.draw.polygon(screen, BLUE, [
        (player_x + player_size//2, player_y),
        (player_x, player_y + player_size),
        (player_x + player_size, player_y + player_size)
    ])
    # Cockpit
    pygame.draw.circle(screen, WHITE, 
                      (player_x + player_size//2, player_y + player_size//2), 
                      8)

def shoot_laser():
    """Create a new laser at player's position"""
    laser_x = player_x + player_size//2 - laser_size[0]//2
    laser_y = player_y
    lasers.append(pygame.Rect(laser_x, laser_y, laser_size[0], laser_size[1]))

def update_lasers():
    """Move lasers and remove those that go off-screen"""
    for laser in lasers[:]:
        laser.y -= laser_speed
        if laser.y < 0:
            lasers.remove(laser)

def draw_lasers():
    """Draw all active lasers"""
    for laser in lasers:
        pygame.draw.rect(screen, GREEN, laser)

def spawn_enemy():
    """Spawn a new enemy at random x position"""
    enemy_x = random.randint(0, SCREEN_WIDTH - enemy_size)
    enemy_y = random.randint(-100, -enemy_size)  # Spawn off-screen top
    enemies.append(pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size))

def update_enemies():
    """Move enemies and remove those that go off-screen"""
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > SCREEN_HEIGHT:
            enemies.remove(enemy)

def draw_enemies():
    """Draw all active enemies"""
    for enemy in enemies:
        # Draw enemy as a square with a cross
        pygame.draw.rect(screen, RED, enemy)
        pygame.draw.line(screen, BLACK, 
                        (enemy.x, enemy.y), 
                        (enemy.x + enemy_size, enemy.y + enemy_size), 
                        2)
        pygame.draw.line(screen, BLACK, 
                        (enemy.x + enemy_size, enemy.y), 
                        (enemy.x, enemy.y + enemy_size), 
                        2)

def check_collisions():
    """Check for collisions between lasers and enemies"""
    global score
    for laser in lasers[:]:
        for enemy in enemies[:]:
            if laser.colliderect(enemy):
                lasers.remove(laser)
                enemies.remove(enemy)
                score += 10  # Increase score for each enemy hit

def draw_score():
    """Draw the current score on screen"""
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot_laser()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_size:
        player_x += player_speed

    # Spawn enemies
    spawn_counter += 1
    if spawn_counter >= enemy_spawn_rate:
        spawn_enemy()
        spawn_counter = 0
        # Increase difficulty over time
        if enemy_spawn_rate > 10:
            enemy_spawn_rate -= 0.1

    # Update game objects
    update_lasers()
    update_enemies()
    check_collisions()

    # Drawing
    screen.fill(BLACK)
    draw_player()
    draw_lasers()
    draw_enemies()
    draw_score()

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
    