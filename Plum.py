from Treat import Treat
from Color import *


class Plum(Treat):

    def __init__(self, position, startturn):
        super(Plum, self).__init__(PURPLE, position, startturn, 10)

    def on_contact(self, snake):
        snake.set_crashed(True)

    def get_points(self):
        return 0
