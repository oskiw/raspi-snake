from unittest import TestCase
from pygame.locals import *

from raspisnake.snake import Snake
from raspisnake.board import Board
from raspisnake.coordinates import Coordinates


class TestSnake(TestCase):

    def setUp(self):
        self.board = Board()
        self.snake = Snake(self.board)

    def tearDown(self):
        self.board.clear()

    def test_update_direction_initial(self):
        for key in [K_DOWN, K_UP, K_LEFT, K_RIGHT]:
            self.snake.update_direction(key)
            self.assertEquals(self.snake._direction, key)

    def test_update_direction_after_transformation(self):
        self.snake.transform_direction = {
            K_DOWN: K_LEFT,
            K_UP: K_DOWN,
            K_LEFT: K_UP,
            K_RIGHT: K_RIGHT
        }
        self.snake.update_direction(K_DOWN)
        self.assertEquals(self.snake._direction, K_LEFT)
        self.snake.update_direction(K_LEFT)
        self.assertEquals(self.snake._direction, K_UP)

    def test_update_direction_not_allowed(self):
        self.snake.update_direction(K_LEFT)
        self.assertEquals(self.snake._direction, K_LEFT)
        self.snake.update_direction(K_RIGHT)
        self.assertEquals(self.snake._direction, K_RIGHT)
        self.snake.add_head(Coordinates(4, 3))
        self.snake.update_direction(K_LEFT)
        self.assertEquals(self.snake._direction, K_RIGHT)

    def test_add_head(self):
        head = Coordinates(3, 4)
        self.snake.add_head(head)
        self.assertEquals(head, self.snake.head())
        head = Coordinates(2, 4)
        self.snake.add_head(head)
        self.assertEquals(head, self.snake.head())
        head = Coordinates(2, 3)
        self.snake.add_head(head)
        self.assertEquals(head, self.snake.head())
        not_head = Coordinates(3, 3)
        self.snake.add_head(not_head)
        self.assertEquals(head, self.snake.head())
        self.assertEquals(self.snake.crashed, True)
