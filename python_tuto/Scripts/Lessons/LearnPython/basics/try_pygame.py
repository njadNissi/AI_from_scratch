#!/usr/bin/python3
import pygame

background_colour = (234, 212, 252)
RED = (255, 0,  0)

# pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Anjie*Pygame')


class Rect:
    rects = []

    def __init__(self, x, y, size):
        self.size = size
        self.x = x
        self.y = y
        self.color = RED
        Rect.rects.append(self)

    def draw(self, surface):
        self.move()
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, self.size, self.size))

    def move(self):
        self.x += 0.01

    @staticmethod
    def draw_all(surface):
        for rect in Rect.rects:
            rect.draw(surface)


def main():

    Rect(10, 10, 50)
    Rect(90, 130, 100)

    running = True
    while running:
        # 1 set BG
        screen.fill(background_colour)

        # 2: draw content
        Rect.draw_all(screen)

        # 3: update screen
        pygame.display.update()

        # 4： check listeners
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


main()
