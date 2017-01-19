from pygame.locals import *

from raspisnake.color import BLUE
from raspisnake.treats.treat import Treat


class Blueberry(Treat):

    def __init__(self, position, start_turn):
        super(Blueberry, self).__init__(BLUE, position, start_turn, 30)

    def on_contact(self, snake):
        snake.transform_direction = {
            K_DOWN: K_UP,
            K_UP: K_DOWN,
            K_LEFT: K_LEFT,
            K_RIGHT: K_RIGHT
        }

    def get_points(self):
        return 2
