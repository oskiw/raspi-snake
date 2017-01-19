from pygame.locals import *

from raspisnake.Color import PURPLE
from raspisnake.treats.Treat import Treat


class Plum(Treat):

    def __init__(self, position, start_turn):
        super(Plum, self).__init__(PURPLE, position, start_turn, 10)

    def on_contact(self, snake):
        snake.transform_direction = {
            K_DOWN: K_UP,
            K_UP: K_DOWN,
            K_LEFT: K_LEFT,
            K_RIGHT: K_RIGHT
        }

    def get_points(self):
        return 3
