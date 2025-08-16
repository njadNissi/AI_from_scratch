import math
import pygame as pg

pg.init()

FPS = 40  # frames per second setting
fpsClock = pg.time.Clock()
TEXT_SIZE = 15
SPEED = 5

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WIDTH = 760
HEIGHT = 720
Screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('Ulam Spiral')


def isPrime(number):
    if number <= 1:
        return False
    if number > 1:
        # A composite number must have a factor <= to the sqrt of that number. Otherwise, the number is prime.
        for i in range(2, int(math.sqrt(number))):
            if number % i == 0:
                return False
    return True


prevPoint = (WIDTH / 2, HEIGHT / 2)


def draw(string, coordx, coordy, fontSize, showOnlyPrime):  # Function to set text
    # delay printing
    pg.time.wait(SPEED)
    pg.display.update()

    font = pg.font.Font(None, fontSize)
    text = font.render(string, True, WHITE)
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)

    if isPrime(int(string)) == True:
        # Width properties defines about draw when value = 1 or fill when value = radius
        pg.draw.circle(Screen, RED, (coordx - 1, coordy - 1),
                       TEXT_SIZE/2, TEXT_SIZE, True, True, True, True)
        Screen.blit(text, textRect)

    if showOnlyPrime == False:
        pg.draw.circle(Screen, BLUE, (coordx - 1, coordy - 1),
                       TEXT_SIZE/2, int(1), True, True, True, True)
        Screen.blit(text, textRect)

    # show links
    global prevPoint
    pg.draw.line(Screen, RED, prevPoint, (coordx, coordy), 1)
    prevPoint = (coordx, coordy)


def apply_turn(key, x, y, textSize):
    if key == 0:
        return (x + textSize, y)
    elif key == 1:
        return (x, y - textSize)
    elif key == 2:
        return (x - textSize, y)
    else:  # key = 3
        return (x, y + textSize)


def draw_ulam_spiral(limitNum):

    x, y = WIDTH / 2, HEIGHT / 2 + TEXT_SIZE
    step = 1  # starting number
    stepSize = 1.5 * TEXT_SIZE  # pixels for blank space between two numbers
    numOfSteps = 1  # the initial number of steps is 1 for 1 and 2, then two for 3-4-5 and 6-7-8. etc
    state = 0
    # every time we turn, to know when to increase the number of steps before turn.
    turnCounter = 0
    while step <= limitNum + 1:
        # print the current step
        draw(str(step), x, y, TEXT_SIZE, True)

        # get the position of the next step
        x, y = apply_turn(state, x, y, stepSize)

        if step % numOfSteps == 0:  # check wether I need to turn.
            state = (state + 1) % 4  # get the right direction of turn.
            turnCounter += 1  # mention that I turned.

            if turnCounter % 2 == 0:  # every same number of steps should run twice.
                # if I already turned twice with the same number of steps, increment it by 1.
                numOfSteps += 1

        # go for next step.
        step += 1


if __name__ == "__main__":

    RUNNING = True
    while RUNNING:

        # display content
        Screen.fill(BLACK)
        draw_ulam_spiral(1000)

        # update graphics
        # pg.display.update()
        # fpsClock.tick_busy_loop(FPS)
        pg.time.wait(1000)
        pg.display.flip()

    # check program execution condition
        for event in pg.event.get():
            if event.type == pg.QUIT:
                RUNNING = False
    pg.quit()  # when RUNNING == False, while stops and falls here.
