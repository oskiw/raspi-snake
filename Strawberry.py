from Treat import Treat
from Color import *


class Strawberry(Treat):

    def __init__(self, position, startturn):
        super(Strawberry, self).__init__(RED, position, startturn, 20)

    def on_contact(self, snake):
        snake.set_speed(0.3)

    def get_points(self):
        return 2
