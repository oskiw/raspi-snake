from Treat import Treat
from Color import *


class Blueberry(Treat):

    def __init__(self, position, startturn):
        super(Blueberry, self).__init__(BLUE, position, startturn, 30)

    def on_contact(self, snake):
        snake.set_revertx(True)

    def get_points(self):
        return 3
