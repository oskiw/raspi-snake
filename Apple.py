from Treat import Treat
from Color import *


class Apple(Treat):

    def __init__(self, position, startturn):
        super(Apple, self).__init__(GREEN, position, startturn, 30)

    def on_contact(self, snake):
        return

    def get_points(self):
        return 1
