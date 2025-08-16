import pygame as pg
import graph
import inputter

WIDTH = 800
window = pg.display.set_mode((WIDTH, WIDTH - 100))
pg.display.set_caption("A* Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class NodeView:
    diameter = 10

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        pg.draw.circle(window, self.color, (self.x, self.y), NodeView.diameter)


if __name__ == '__main__':
    run = True
    while run:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                run = False

            if event.type == pg.KEYDOWN:  # key n => new node
                if event.key == pg.K_n:
                    node_label = inputter.getTextInput(
                        'Enter the vertex label:')
                    print(node_label)
    pg.quit()
