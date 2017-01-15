from Treat import Treat
from Color import *


class Lemon(Treat):

    def __init__(self, position, startturn):
        super(Lemon, self).__init__(YELLOW, position, startturn, 10)

    def on_contact(self, snake):
        snake.set_speed(1)

    def get_points(self):
        return 1
