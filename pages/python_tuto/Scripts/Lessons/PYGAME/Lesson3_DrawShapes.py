import pygame
from pygame.locals import *

size = 640, 320
width, height = size
GREEN = (150, 255, 150)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SerialCom GUI')

run  = True

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		

	pygame.draw.ellipse(screen, RED, (50, 20, 160, 100))
	pygame.draw.ellipse(screen, GREEN, (100, 60, 160, 100))
	pygame.draw.ellipse(screen, BLUE, (150, 100, 160, 100))
	pygame.draw.ellipse(screen, RED, (350, 20, 160, 100), 1)
	pygame.draw.ellipse(screen, GREEN, (400, 60, 160, 100), 4)
	pygame.draw.ellipse(screen, BLUE, (450, 100, 160, 100), 8)
	pygame.display.update()

pygame.quit()
