from pygame.locals import *

from raspisnake.color import PURPLE
from raspisnake.treats.treat import Treat


class Plum(Treat):

    def __init__(self, position, start_turn):
        super(Plum, self).__init__(PURPLE, position, start_turn, 10)

    def on_contact(self, snake):
        snake.transform_direction = {
            K_DOWN: K_DOWN,
            K_UP: K_UP,
            K_LEFT: K_RIGHT,
            K_RIGHT: K_LEFT
        }

    def get_points(self):
        return 3
