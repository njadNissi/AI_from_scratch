import pygame
from pygame.locals import *
import serial
import time


ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1.0)

time.sleep(3)
ser.reset_input_buffer()
print('SERIAL COMMUNICATION READY!')

size = 640, 320
width, height = size
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (150, 255, 150)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('SerialCom GUI')
font = pygame.font.Font('freesansbold.ttf', 350)

run  = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	screen.fill(BLACK)
	
	cc = str(ser.readline())
	btn_code = cc[2:][:-5]
	text = font.render(btn_code, True, BLUE, GREEN)
	textRect = text.get_rect()
	textRect.center = (size[0] // 2, size[1] // 2)
	screen.blit(text, textRect)

	pygame.display.update()

pygame.quit()
