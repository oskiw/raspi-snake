import pygame
from pygame.locals import *

from random import randint
from time import sleep

from raspisnake.coordinates import Coordinates
from raspisnake.snake import Snake
from raspisnake.board import Board
from raspisnake.treats.treatfactory import TreatFactory


class Game(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_mode((640, 480))
        self._board = Board()
        self._snake = Snake(self._board)

    @property
    def snake(self):
        return self._snake

    def run(self):

        running = True
        paused = False
        points = 0
        turn = 0
        treat = self.get_next_treat(turn)

        while running:
            for event in pygame.event.get():
                print(event)

                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        paused = False if paused else True

                    if not paused:
                        if event.key in [K_DOWN, K_UP, K_RIGHT, K_LEFT]:
                            self._snake.update_direction(event.key)

                if event.type == QUIT:
                    running = self.stop(points)

            if not paused and self._snake.is_moving():
                turn += 1
                next_position = self._snake.get_next_position()
                if next_position == treat.position:
                    points += treat.get_points()
                    self._snake.reset_attributes()
                    treat.on_contact(self._snake)
                    treat = self.get_next_treat(turn)
                else:
                    self._snake.remove_tail()

                if treat.has_expired(turn):
                    self._board.unset_snake_pixel(treat.position)
                    treat = self.get_next_treat(turn)

                if not self._snake.crashed:
                    self._snake.add_head(next_position)

            if self._snake.crashed:
                running = self.stop(points)

            sleep(self._snake.speed)

    def stop(self, points):
        self._board.show_points(points)
        print("Bye - you got " + str(points) + " points")
        return False

    def get_next_treat(self, turn):
        empty_position = []
        for x in range(8):
            for y in range(8):
                p = Coordinates(x, y)
                if not self._snake.is_snake(p):
                    empty_position.append(p)

        position = empty_position[randint(0, len(empty_position) - 1)]
        treat = TreatFactory.get_treat(position, turn)
        self._board.set_pixel(position, treat.color)
        return treat
