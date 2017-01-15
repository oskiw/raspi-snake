import pygame
from pygame.locals import *
from sense_hat import SenseHat
from time import sleep
from random import randint
from Position import Position
from Color import *
from Apple import Apple
from Lemon import Lemon
from Strawberry import Strawberry
from Plum import Plum
from Blueberry import Blueberry
from Orange import Orange

DEFAULT_SPEED = 0.5


class RaspiSnake(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_mode((640, 480))
        self.sense = SenseHat()
        self.speed = DEFAULT_SPEED
        self.sense.clear()
        startingposition = Position(3, 3)
        self.snake = [startingposition]
        self.set_snake_pixel(startingposition)
        self.crash = False
        self.reset_revert()

    def set_snake_pixel(self, position):
        self.set_pixel(position, WHITE)

    def unset_snake_pixel(self, position):
        self.set_pixel(position, BLACK)

    def set_pixel(self, position, color):
        self.sense.set_pixel(position.getx(), position.gety(), color.getr(), color.getg(), color.getb())

    def run(self):

        paused = False
        running = True
        lastdirection = None
        points = 0
        turn = 0
        treat = self.generate_treat(turn)

        while running:
            for event in pygame.event.get():
                print(event)

                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        if paused:
                            paused = False
                        else:
                            paused = True

                    if not paused:
                        if event.key in [K_DOWN, K_UP, K_RIGHT, K_LEFT]:
                            key = event.key
                            if self.reverty:
                                if key == K_DOWN:
                                    key = K_UP
                                elif key == K_UP:
                                    key = K_DOWN
                            if self.revertx:
                                if key == K_LEFT:
                                    key = K_RIGHT
                                elif key == K_RIGHT:
                                    key = K_LEFT
                            if len(self.snake) == 1 or self.get_next_position(key) != self.snake[-2]:
                                lastdirection = key

                if event.type == QUIT:
                    running = False
                    self.stop(points)

            if not paused:
                if lastdirection is not None:
                    turn += 1
                    nextposition = self.get_next_position(lastdirection)
                    if nextposition == treat.get_position():
                        points += treat.get_points()
                        self.speed = DEFAULT_SPEED
                        self.reset_revert()
                        treat.on_contact(self)
                        treat = self.generate_treat(turn)
                    else:
                        self.remove_tail()

                    if treat.has_expired(turn):
                        self.unset_snake_pixel(treat.get_position())
                        treat = self.generate_treat(turn)

                    if not self.crash:
                        self.crash = self.has_crashed(nextposition)

                    if not self.crash:
                        self.add_head(nextposition)

            if self.crash:
                running = False
                self.stop(points)

            sleep(self.speed)

    def set_speed(self, speed):
        self.speed = speed

    def set_crashed(self, crash):
        self.crash = crash

    def reset_revert(self):
        self.revertx = False
        self.reverty = False

    def set_revertx(self, val):
        self.revertx = val

    def set_reverty(self, val):
        self.reverty = val

    def stop(self, points):
        self.sense.clear()
        self.sense.show_message(str(points) + "pts", scroll_speed=0.15, text_colour=WHITE.to_list(),
                                back_colour=BLACK.to_list())
        sleep(1)
        self.sense.clear()
        print("Bye - you got " + str(points) + " points")

    def get_next_position(self, lastdirection):
        lastposition = self.snake[-1]

        if lastdirection == K_DOWN:
            return Position(lastposition.getx(), (lastposition.gety() + 1) % 8)
        if lastdirection == K_UP:
            return Position(lastposition.getx(), (lastposition.gety() - 1) % 8)
        if lastdirection == K_RIGHT:
            return Position((lastposition.getx() + 1) % 8, lastposition.gety())
        if lastdirection == K_LEFT:
            return Position((lastposition.getx() - 1) % 8, lastposition.gety())

        return None

    def has_crashed(self, position):
        for p in self.snake:
            if p == position:
                return True
        return False

    def remove_tail(self):
        self.unset_snake_pixel(self.snake[0])
        self.snake.pop(0)

    def add_head(self, head):
        self.set_snake_pixel(head)
        self.snake.append(head)

    def generate_treat(self, turn):
        emptyposition = []
        for x in range(8):
            for y in range(8):
                p = Position(x, y)
                if not self.has_crashed(p):
                    emptyposition.append(p)

        position = emptyposition[randint(0, len(emptyposition) - 1)]

        t = randint(0, 5)
        if t == 0:
            treat = Apple(position, turn)
        elif t == 1:
            treat = Lemon(position, turn)
        elif t == 2:
            treat = Strawberry(position, turn)
        elif t == 3:
            treat = Blueberry(position, turn)
        elif t == 4:
            treat = Orange(position, turn)
        else:
            treat = Plum(position, turn)

        self.set_pixel(position, treat.get_color())
        return treat


if __name__ == "__main__":
    snake = RaspiSnake()
    snake.run()


