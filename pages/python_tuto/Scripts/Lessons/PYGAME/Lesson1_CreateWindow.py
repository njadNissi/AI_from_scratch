# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init() # it initializes the modules and returns their number and the number of failures.
screen = pygame.display.set_mode(size=(1280, 720))
clock = pygame.time.Clock()
running:bool = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("red")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()