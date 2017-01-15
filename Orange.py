from Treat import Treat
from Color import *


class Orange(Treat):

    def __init__(self, position, startturn):
        super(Orange, self).__init__(ORANGE, position, startturn, 30)

    def on_contact(self, snake):
        snake.set_reverty(True)

    def get_points(self):
        return 3
